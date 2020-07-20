'''
@Theme: Encuentra una subcadena en una cadena más grande
@Author XxPayánStyleS2xX'''

def bruteMatch(n,m):
	for i in range(0,len(n)-len(m)+1): #len() saca la longitud de las cadenas
		if n[i:len(m)+i]==m: #Si encuentra la subcadena imprime la posición inicial
			print(i)
			return
	print("No encontrada")


# # # # # # # # # # # #

if __name__ == '__main__':
	cadA = input('Subcadena: ') #Entrada de la primera Cadena
	cadB = input('Cadena padre: ')	#Entrada de la segunda Cadena
	bruteMatch(cadB, cadA)
	print("XxPayanStyleS2xX")