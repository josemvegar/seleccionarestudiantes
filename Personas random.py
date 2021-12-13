import random
estudiantes = ["Norlie Rojas", "Jose Vega", "Wuilmer Pulgar", "Ashly", "Cesar", "Diego Tineo", "Enrique Salazar" ,"Estefano Ramos", "Hector Salazar", "Jose Agreda", "Jose Angel", "Jose Diaz", "Maria Veronica", "Mauricio"]

## Imprime 2 estudiantes de la lista
resp=random.choice(estudiantes)
print (resp)
estudiantes.remove(resp)
print (random.choice(estudiantes))