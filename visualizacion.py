import sqlite3
import matplotlib as mpl
import matplotlib.pyplot as plt

def mostrar_resumen():

    try:
        con = sqlite3.connect('tickers.db')
        cursor = con.cursor()
        resumen = cursor.execute('''SELECT id, ticker, fecha_inicio, fecha_fin FROM resumen;''').fetchall()

        print("\nLos períodos guardados en la base de datos son los siguiente:")

        for x in range (len(resumen)):
            print(f"{x+1}. {resumen[x][1]} - {resumen[x][2]} <-> {resumen[x][3]}")

    except:
        print("No es posible conectarse con la base de datos...")
    finally:
        con.close()

def mostrar_grafico():

    ticker_grafico = input("\nIngrese el ticker a graficar:").upper()

    try:
        con = sqlite3.connect('tickers.db')
        cursor = con.cursor()
        periodos_ticker = cursor.execute(f'''SELECT id, ticker, fecha_inicio, fecha_fin FROM resumen WHERE ticker = "{ticker_grafico}";''').fetchall()
    except:
        print("No es posible conectarse con la base de datos...")

    if len(periodos_ticker) != 0:

        print("\nLos períodos guardados para el ticker seleccionado son los siguientes:")

        for x in range(len(periodos_ticker)):
            print(f"\nID: {periodos_ticker[x][0]} - {periodos_ticker[x][1]} - {periodos_ticker[x][2]} <-> {periodos_ticker[x][3]}")
        
        id_valido = True

        while (id_valido):

            periodo_seleccion = input("\nIngrese el ID del período a graficar:")

            for x in range(len(periodos_ticker)):
                if periodo_seleccion == str(periodos_ticker[x][0]):
                    id_valido = False

        dias_habiles = cursor.execute(f'''SELECT dia_habil FROM resultados WHERE id = {periodo_seleccion};''').fetchall()
        cierre = cursor.execute(f'''SELECT cierre FROM resultados WHERE id = {periodo_seleccion};''').fetchall()

        fig, ax = plt.subplots()
        ax.plot(dias_habiles, cierre)
        ax.set_xlabel('DIAS HABILES')
        ax.set_ylabel('CIERRE (U$S)')
        ax.set_title(f"CIERRES DEL DIA PARA '{periodos_ticker[0][1]}' EN EL PERIODO {periodos_ticker[0][2]} A {periodos_ticker[0][3]}")
        plt.show()

        con.close()

    else:
        print("\nNo existen registros para el ticker solicitado.")
