'''
@Author: XxPayánStyleS2xX
@Theme: Pruebas unitarias con unittest
'''

import unittest

def es_par(x):
	return 1 if x%2 == 0 else 0
	
def duplicar(x):
	return x*2

class Pruebas(unittest.TestCase):
	def test_es_par(self):
		self.assertEqual(es_par(35), False) #Prueba la función es_par()
		self.assertEqual(es_par(28), True) #Prueba la función es_par()
	
	def test_duplicar(self):
		self.assertEqual(duplicar(10), 20) #Prueba la función duplicar()
		self.assertEqual(duplicar('Ab'), 'AbAb') #Prueba la función duplicar()
####
if __name__ == "__main__":
	unittest.main()