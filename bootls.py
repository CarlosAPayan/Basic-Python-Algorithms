'''
@Author: XxPayánStyleS2xX
@Theme: Bootles types
'''

def main():
	typeA, typeB = -1,-1
	sumA, sumB = 0,0
	while typeA < 0 or typeB < 0:
		typeA = int(input('Botellas de menos de 1 litro: '))
		typeB = int(input('Botellas de mas de 1 litro: '))

	for _ in range(typeA):
		sumA += 0.1

	for _ in range(typeB):
		sumB += 0.25

	print("Total recaudado por botellas tipo A: {0:.2f}".format(sumA))
	print("Total recaudado por botellas tipo B: {0:.2f}".format(sumB))

if __name__ == '__main__':
	main()
	print("\nXxPayanStyleS2xX\n")