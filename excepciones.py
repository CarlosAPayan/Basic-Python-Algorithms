'''
@Author: XxPayánStyleS2xX
@Theme: Excepciones
'''
import sys	# Importación del módulo para instrucciones de sistema

try:
	#Intenta convertir la entrada del usuario a número entero
	num1 = int(input("Introduzca numero: ")) # Entrada del sistema con cast int
	print("Conversion exitosa!! int = ", str(num1)) #Impresión si la conversión se realiza con éxito
except ValueError as e:
	print("Conversion imposible", file = sys.stderr) #Si no puede realizar la conversión imprime un msj
finally: #Finalmente si se realiza la conversión con éxito o no, se sale de la ejecución
	print("XxPayanStyleS2xX")
	sys.exit() #Salida con el llamado al sistema
