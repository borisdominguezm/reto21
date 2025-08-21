import datetime

def validar_fecha(texto):
    try:
        datetime.date.fromisoformat(texto)
        return True
    except ValueError:
        return False
    

print(validar_fecha("2000-14-02")) 
print(validar_fecha("02-11-2000"))  
print(validar_fecha("14-02-2025"))
print(validar_fecha("hola"))
print(validar_fecha("2025-11-03"))       