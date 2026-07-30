compra = float(input("qual o valor da sua compra: "))
desconto1 = compra - 0.20
desconto2 = compra - 0.10

if compra >= 500 :
    print(f"o valor da sua compra foi {compra} e o desconto é de {desconto1}")
    
elif imc < 25:
    print("saudavel")
elif imc < 30:
    print("cuidado em")
        
else:
    print("pare de comer")   