x=float(input("Digite um número racional: "))
n=int(input("Quantas casas decimais: "))
if 2>n>0:
	print(f"Número arredondado: {round(x, n)} ")
elif n==0:
	print(f"Número arredondado: {int(round(x, n))}")
elif n>=2:
	k=n-2
	print(f"Número arredondado: {float(x)}", end="")
	for k in range (0,k+1):
		print("0", end="")