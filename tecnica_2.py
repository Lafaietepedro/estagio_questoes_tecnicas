def fibonacci(n):
    sequencia_fib = [0, 1]  # Inicializa a sequência com os dois primeiros números
    
    while sequencia_fib[-1] < n:
        valor_seguinte = sequencia_fib[-1] + sequencia_fib[-2]  # Calcula o próximo valor
        sequencia_fib.append(valor_seguinte)  # Adiciona o valor à sequência
    
    return sequencia_fib

def verifica_fib(n):
    #Verifica se um número pertence à sequência de Fibonacci.

    sequencia_fib = fibonacci(n)  # Gera a sequência de Fibonacci até n
    
    if n in sequencia_fib:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} não pertence à sequência de Fibonacci."
    
# Programa principal
numero = int(input("Informe um número: "))  # Solicita um número ao usuário
resultado = verifica_fib(numero)  # Verifica se o número pertence à sequência
print(resultado)  # Exibe o resultado