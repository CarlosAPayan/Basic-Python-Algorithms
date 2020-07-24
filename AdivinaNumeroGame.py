import sys
from random import randint

	#Función que permite los límites entre los que se va a encontrar el número
def limites():
	inf = int(input("Escoja limite inferior: ")) #Entrada del usuario
	sup = int(input("Escoja limite superior: "))

	return inf,sup 	#Regresa la tupla de valores

def main():
	gameOver = False
	nameUser = ''
	oports = 0 #Número de intentos del usuario
		#No puede haber un nombre vacío
	while nameUser == '':
		nameUser = input("Nombre de usuario: ")

	inf,sup = limites()	#Cacha los límites
	num = randint(inf,sup) #Genera num aleatorio entre los límites dados
	while not gameOver:
		try:
			n = int(input("Ingrese numero: ")) # Entrada del usuario, intento de acertar
			if n < num:
				print("Tsss!... Quedaste corto") # Si el intento es más pequeño que num
				oports += 1 #Aumenta el contador de intentos
			elif n > num:
				print("Ups!... Te pasaste") # Si el intento es más grande que num
				oports += 1 #Aumenta el contador de intentos
			else:
				print("\n¡Adivinaste! " + nameUser + " - tras: {0} intentos".format(oports)) #Si el usuario ingresa el número correcto
				gameOver = True #El juego termina
		except:
			print("Ingrese valores correctos!") # Si la entrada no es un número

if __name__ == '__main__':
	print("| ----------- Juego Adivina el Numero ------------ |")
	print("\t\t Bienvenido\n")
	main()
	print("\n\t\tXxPayanStyleS2xX")