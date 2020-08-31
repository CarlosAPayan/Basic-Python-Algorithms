'''
@Author: XxPayánStyleS2xX
@Theme: Áreas
'''

def area(base, altura):
	acre = 43560 #feet o pies
	areaF = base * altura
	return areaF/acre

if __name__ == '__main__':
	bas, alt = 0,0
	while bas < 1 and alt < 1:
		bas = int(input('Base: '))
		alt = int(input('Altura: '))
	
	print("Area de la habitacion: {} acres".format(area(bas, alt)))
	print("\nXxPayanStyleS2xX\n")