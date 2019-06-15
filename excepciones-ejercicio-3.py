#programa que evalua la edad

# def evaluaedad(edad):
	

# 	if edad<20:
# 		return "eres muy joven"
# 	elif edad<40:
# 		return "eres maduro"
# 	elif edad<65:
# 		return "eres maduro"
# 	elif edad<100:
# 		return "cuidate.. "

# print (evaluaedad(100))

import math

def calcularaiz(num1):

	if num1<0:
		raise ValueError ("el numero no puede ser negativo")
	else:
		return math.sqrt(num1)


op1=float(input("ingresa numero 1: "))

try:
	print(calcularaiz(op1))
except ValueError as ErrorDeNumeroNegativo :
	print (ErrorDeNumeroNegativo)

print ("termina")

