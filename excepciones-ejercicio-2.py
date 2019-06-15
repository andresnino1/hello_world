def divide():

	try:

		op1=(float(input("ingresa numero uno: ")))
		op2=(float(input("ingresa numero dos: ")))
		print("la division es: "+ str(op1/op2))

	except:
		print("error general")

	# except ValueError:
	# 	print("valor introducido erroneo")

	#except ZeroDivisionError:
	 #	print("no se puede dividir por cero")

	



	print("calculo finalizado")

divide()
