'''
@Author: XxPayánStyleS2xX
@Theme: Serie de Taylor de e^x
'''

def factorial(n):
	if n <= 1:
		return n

	return n * factorial(n-1)

def Taylor():
	n = int(input("Grado de la serie: "))
	x = int(input("Define el x: "))
	eX = 1
	i = 1 
	while i <= n:
		eX += (x**i)/factorial(i)
		i+=1

	return eX

if __name__ == '__main__':
	print("La sumatoria de la serie de Tylor es: ", str(Taylor()))
	print("\nXxPayanStyleS2xX\n")