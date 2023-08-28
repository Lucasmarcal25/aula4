
def IMC(peso,altura):
    return (peso/altura ** 2)

peso=int(input("Digite seu peso: "))  
altura=float(input("Digite sua altura:")) 

resultado=IMC(peso,altura)
print(resultado)

if resultado <18.5: 
    print("Baixo Peso")
elif resultado <= 24.99 :
     print("Normal")
elif resultado  <= 29.99: 
    print("Sobrepeso")
elif resultado < 35 : 
    print("Obseidade")
else:
    print("Obseidade Extrema")
