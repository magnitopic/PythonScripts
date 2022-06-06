""" 
	Generar 12 números aleatorios entre 0 y 100 y calcular su media.
	Generar otros 12 números aleatorios entre 0 y 100 y calcular su media.
	Mostrar en pantalla las dos listas
	Finalmente muestre en pantalla las medias de ambas series y diga cuál de las dos ha resultado mayor.
"""
import random; [print(*(num1 := [random.randint(0,100) for i in range(12)])),[print(*(num2 := [random.randint(0,100) for i in range(12)]))] ,print(f"Media lista 1: {(med1 := sum(num1)/len(num1))}"), print(f"Media lista 2: {(med2 := sum(num2)/len(num2))}"), print(*[f"La {'primera' if med1>med2 else 'segunda'} lista es mayor" if med1!=med2 else "Las dos medias son iguales"])]