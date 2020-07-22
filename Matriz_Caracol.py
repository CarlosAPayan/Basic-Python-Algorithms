'''
@Author: XxPayánStyleS2xX
@Theme: Matríz de Caracol
'''

def Caracol(n):
	mat = [[0]*n for _ in range(n)]	#Crea una matriz de nxn llena de 0's
	dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]
	x, y, z = 0, -1, 1

	#Rellena matriz
	for i in range(n+n-1):
		for j in range((n+n-i)//2):
			x += dx[i%4]
			y += dy[i%4]
			mat[x][y] = z
			z += 1

	return mat

def showMat(tam):
	print(' ')
	#Imprime la matriz devuelta por la función Caracol
	for _ in Caracol(tam): print(*_)

def main():
	size = int(input('N: ')) #Entrada del usuario
	showMat(size)

if __name__ == '__main__':
	process = True
	while process == True:
		main()
		option = input('¿Otra vez?: (S) o (N): \n')
		if option in ('N', 'n'):
			process = False

	print("XxPayanStyleS2xX")