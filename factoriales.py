'''
@Author: XxPayánStyleS2xX
@Theme: Factoriales desde 1 hasta n
'''
def fact(num):
	if num < 2:
		return 1

	return num * fact(num-1)

def main():
	num = int(input("Numero a tratar en secuencia: "))
	for _ in range(1,num+1):
		print("El factorial de {0} es: {1}".format(_,fact(_)))

if __name__ == '__main__':
	main()
	print("\n\t XxPayanStyleS2xX\n")