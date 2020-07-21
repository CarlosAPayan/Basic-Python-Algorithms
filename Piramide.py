'''
@Theme: Altura de una pirámide con bloques
@Author: XxPayánStyleS2xX
'''

def main():
	n = int(input('Num de bloques: '))	#Entrada del usuario "n" = número de bloques
	p = 0	#Control de la altura
	for i in range(n):	#Ciclo que recorre desde 1 hasta n
		p += i 	#Sumatoria 0+1+2+3+...+n

		if p == n: 	#Si p es igual a n Se puede construir perfectamente una pirámide de altura p
			print('Altura: {0}\n'.format(i)) #Salida a consola
			return
		elif p > n:
			print("No se puede construir\n") #La Sumatoria es mayor a n por lo tanto no existe una piramide de n bloques
			return




if __name__ == '__main__':
	process = True
	while process == True: #bucle principal
		main()
		option = input('¿Otra vez?: (S) o (N): \n') #Opción de continuar
		if option in ('N', 'n'):
			process = False

	print("XxPayanStyleS2xX")