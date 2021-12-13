## Integrantes:
# José Manuel Vega R. 27.000.723
# Norlie Rojas. 26.707.950
import random
estudiantes = ["Norlie Rojas", "Jose Vega", "Wuilmer Pulgar", "Ashly", "Cesar", "Diego Tineo", "Enrique Salazar" ,"Estefano Ramos", "Hector Salazar", "Jose Agreda", "Jose Angel", "Jose Diaz", "Maria Veronica", "Mauricio"]
fin = 'n'
## Imprime 2 estudiantes de la lista
while (fin == 'n' or fin=='N'):
    resp=random.choice(estudiantes)
    print (resp)
    estudiantes.remove(resp)
    print (random.choice(estudiantes))
    print("¿Salir? S/N")
    fin = input()
    while (fin!='n' and fin!='N' and fin!='s' and fin!='S'):
        print("Ingrese una opción correcta. S/N")
        fin = input()