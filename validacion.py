import re
from datetime import date
import datetime
from datetime import datetime

RegEx = "(^([0-9][0-9]|19[0-9][0-9]|20[0-9][0-9])(\.|-|)([1-9]|0[1-9]|1[0-2])(\.|-|)([1-9]|0[1-9]|1[0-9]|2[0-9]|3[0-1])$)"
hoy = date.today()

def validar_fecha():

    fecha = input("\nfecha:")
    try:
        fecha_datetime = datetime.strptime(fecha, "%Y-%m-%d")
        fecha_date = fecha_datetime.date()
    except:
        pass

    while re.match(RegEx, fecha) == None or len(fecha) != 10 or fecha_date >= hoy:
        print("\nIngrese una fecha válida...")
        fecha = input("fecha:")
        try:
            fecha_datetime = datetime.strptime(fecha, "%Y-%m-%d")
            fecha_date = fecha_datetime.date()
        except:
            pass

    print("\nFecha guardada...")

    return fecha

def validar_temporalidad(inicio, fin):
    inicio_datetime = datetime.strptime(inicio, "%Y-%m-%d")
    inicio_date = inicio_datetime.date()

    fin_datetime = datetime.strptime(fin, "%Y-%m-%d")
    fin_date = fin_datetime.date()

    if inicio_date > fin_date:
        return True
    else:
        return False



