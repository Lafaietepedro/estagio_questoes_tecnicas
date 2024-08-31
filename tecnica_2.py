def fibonacci(n):
    sequencia_fib = [0, 1]
    
    while sequencia_fib[-1] < n:
        valor_seguinte = sequencia_fib[-1] + sequencia_fib[-2]
        sequencia_fib.append(valor_seguinte)
    
    return sequencia_fib

def verifica_fib(n):
    sequencia_fib = fibonacci(n)
    
    if n in sequencia_fib:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} não pertence à sequência de Fibonacci."
    
numero = int(input("Informe um número: "))
resultado = verifica_fib(numero)
print(resultado)