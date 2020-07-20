''' Términos de la serie armónica
	@Author: XxPayánStyleS2xX	'''

def main():
	N = int(input("Ingrese Limite: ")) 	#Entrada del usuario
	if N < 1 or N > 10:	#Condición de entrada
		print("Error! Fuera del limite!!") 	#Si N > 10 imprime el error
		return	#Sale de la función y termina el programa

	Sum, term = 0, 0	#Variables locales
	while Sum <= N:		#Bucle del proceso de operaciones mientras la sumatoria sea menor a la entrada del usuario
		term += 1	#Aumenta en 1 con cada iteración
		Sum += 1/term 	#Realiza la sumatoria de 1 sobre el termino actual

	print("El numero de terminos es: {}".format(term))	#Imprime la cantidad de términos total
	print("La suma es {:.2f}".format(Sum))  #Imprime la sumatoria de la serie armónica con 2 decimales

if __name__ == '__main__':	#Condición del programa principal
	main()	#Función principal
	print("\n Autor: XxPayanStyleS2xX")