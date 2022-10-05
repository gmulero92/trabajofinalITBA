import requests
import sqlite3
import validacion
from datetime import date

def actualizar_datos():
   
    #######  PEDIDO DE DATOS  #######
    fechas_ok = True

    ticker = input("\nIntroduzca el ticker a analizar:").upper()

    while fechas_ok == True:
        print(f"\nIngrese una fecha de inicio anterior a {date.today()} con el siguiente formato AAAA-MM-DD:")
        inicio = validacion.validar_fecha()
        
        print(f"\nIngrese una fecha de fin anterior a {date.today()} con el siguiente formato AAAA-MM-DD:")
        fin = validacion.validar_fecha()

        if validacion.validar_temporalidad(inicio, fin):
            print("\nLa fecha de inicio no puede ser posterior a la fecha de fin, vuelva a intentarlo.")
        else:
            fechas_ok = False

    #  CONEXION A LA API  #

    try:
        print("\nSolicitando información al servidor...")
        ticker_get = requests.get(f"https://api.polygon.io/v2/aggs/ticker/{ticker}/range/1/day/{inicio}/{fin}?adjusted=true&sort=asc&limit=120&apiKey=SpWc8kFZ8V2WfHrgfSWyOvztfC9tAxmO")
        obj_ticker = ticker_get.json()
    except:
        print("No es posible conectarse al servidor, intente más tarde...")    

    #  GUARDADO EN LA BASE DE DATOS  #

    if obj_ticker['resultsCount'] != 0:

        try:
            con = sqlite3.connect('tickers.db')
            cursor = con.cursor()
        except:
            print("No es posible conectarse con la base de datos...")

        cursor.execute(f'''INSERT INTO resumen (ticker, fecha_inicio, fecha_fin, ultimo) VALUES ("{ticker}", "{inicio}", "{fin}", "1");''')
        con.commit()

        obtener_id = cursor.execute('''SELECT (id) FROM resumen WHERE ultimo = 1;''').fetchone()[0]

        for x in range(len(obj_ticker['results'])):
            cierre = obj_ticker['results'][x]['c']
            dia_habil = x + 1

            cursor.execute(f'''INSERT INTO resultados VALUES ("{obtener_id}", "{dia_habil}", "{cierre}");''')
            con.commit()

        cursor.execute(f'''UPDATE resumen SET ultimo = 0 WHERE id = {obtener_id};''')
        con.commit()
        con.close()

        print(f"\nDatos almacenados correctamente.")

    else:
        print("\nNo se obtuvieron datos del servidor, esto puede deberse a:\n \
                * El nombre del ticker es inexistente o se encuentra mal escrito.\n \
                * Los datos solicitados corresponden a dias no hábiles o feriados donde no hubo registros de los mismos.")