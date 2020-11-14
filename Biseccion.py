'''
@Author: Payán Rosales Carlos A.
@Métodos Numéricos: Método de Bisección
'''
import numpy as np
import math as m


def bisection(a,b,f_x): #Método de bisección
	nI,	start = 0, True
	T = 0.0000000001
	f_a, f_b = f_x(a), f_x(b)
	while start:
		nI += 1
		p = a + ((b - a)/2)
		#print(p)
		f_p = f_x(p)
		if f_a*f_p > 0:
			a = p
			f_a = f_p
		else:
			b = p
			f_b = f_p
		if f_p == 0:
			print("Raíz encontrada: {} en {} Iteraciones".format(p, nI))
			start = False
		if abs((b - a)/2) < T or nI > 1000:
			print("Aproximación encontrada: {} en {} Iteraciones".format(p, nI))
			print("f(p): ",f_p)
			start = False


if __name__ == '__main__':
	f_x1 = lambda x: x**3 + 4*x**2 - 10
	a1,b1 = 1,2

	f_x2 = lambda x: x**3 - 10*x**2 + 5
	a2,b2 = 0.6,0.8

	f_x3 = lambda x: m.tan(x)
	a3,b3 = 0,20

	print("\nPrimera funcion")
	bisection(a1, b1, f_x1)
	print("\n\nSegunda funcion")
	bisection(a2, b2, f_x2)
	print("\n\nTercera funcion")
	bisection(a3, b3, f_x3)
