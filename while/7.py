# encontramos o maior divisor comum
a = 84
b = 36

while b != 0:
    resto = a % b
    
    a = b
    b = resto
print(f"MDC {a}")