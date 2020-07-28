'''
@Author: XxPayánStyleS2xX
@Theme: Nums aleatorios y comparaciones
@Description: Programa que simula un juego de azar con el lanzamiento de 1 dado con pérdidas y ganancias 
'''
from random import randint
import sys, time

def game(p):
	opc = [("0",0), ("Sigue jugando", 0), ("Pierde 2 Pesos", -2), ("Gana 10 pesos", 10), ("Pierde 4 pesos", -4), ("Pierde 5 pesos", -5), ("Gana 1 peso",1)]
	gOver = False
	try:
		n = int(input("Numero de lanzamientos: "))
		aux = n
		while not gOver:
			if n < 1:
				print("\nFelicidades! Lograste tirar {0} veces".format(aux))
				if p > 10:
					print("Tuviste ganancias, tu saldo es de: {0} pesos".format(p))
				else:
					print("Tuviste perdidas :(, tu saldo es de {0} pesos".format(p))
				gOver = True

			elif p < 1:
				print("\n\t¡Game Over!")
				print("Lo sentimos, te quedaste sin dinero! :(")
				gOver = not gOver

			else:
				d = randint(1,6)
				print(opc[d][0])
				p += opc[d][1]
				n -= 1
				time.sleep(1)

		return 1
	except ValueError as e:
		print("Error! - Ingresa valores correctos")
		return 0


if __name__ == '__main__':
	play = True
	while play:
		p = 10
		print("------- Bienvenido ------\n")
		print("Inicialmente tienes: {0} pesos".format(p))
		print("\t¡A jugar!\n")
		time.sleep(1)
		if game(p):
			op = input("Seguir jugando: (S), Salir: (N): ")
		else:
			op = input("Jugar: (s), Salir: (n): ")

		if op in ('N', 'n'):
			play = not play

	print("\n\tXxPayanStyleS2xX")