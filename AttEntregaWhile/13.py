a = int(input("digite um numero: "))
b = int(input("digite um numero: "))

while b != 0:
    resto = a % b
    
    a = b
    b = resto
print(f"MDC {a}")