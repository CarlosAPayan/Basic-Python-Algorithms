'''
@Author: XxPayánStyleS2xX
@Theme: Nums aleatorios y comparaciones
@Description: Programa que simula el lanzamiento de dos dados e imprime cuantas veces los dados obtienen el mismo valor
'''
from random import randint
import sys

def tiroDados():
	mism = 0
	try:
		n = int(input("Numero de lanzamientos: "))
		for _ in range(n):
			d1,d2 = randint(1,6),randint(1,6)
			if d1 == d2:
				print("D1: {0} y D2: {1}".format(d1,d2))
				mism += 1
		print("Total de tiros iguales D1 y D2: {0}".format(mism))
		return
	except ValueError as e:
		print("¡Error! - Intente de nuevo", file = sys.stderr)
		return

if __name__ == '__main__':
	out = False
	while not out:
		tiroDados()
		print("\nXxPayanStyleS2xX\n")
		cond = input("¿Desea salir? (S/N): ")
		if cond in ('S', 's'):
			out = True