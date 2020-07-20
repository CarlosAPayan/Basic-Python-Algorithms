#Serie Fibonacci
# @ Author: XxPayánStyleS2xX

suma = 0 # Variable global para llevar la sumatoria de la serie Fibonacci

	#Función que hace todo el proceso
def fibo():
	global suma #Se aclara que la variable suma se ocupa como global y no local
	a,b = 0,1
	num = int(input("Ingresa limite de la serie Fibbonacci: ")) #Entrada del usuario

	while num > 0: # bucle de proceso en la sucesión
		print(a, end = ' ') #Imprime en cada iteración el valor de la serie
		a,b = b, a+b 	#Se hace la sucesión
		suma += a 	#Se hace la sumatoria
		num -= 1 	#Decrementa el numero de iteraciones a ejecutar

if __name__ == '__main__':	#Inicia el proceso principal
	fibo()	#Llama a la función para su ejecución
	print('\n Suma : ' + str(suma))	#Imprime el reultado de la sumatoria
	print("Autor: XxPayanStyleS2xX")