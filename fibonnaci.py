""""
1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre 
será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), 
escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e 
retorne uma mensagem avisando se o número informado pertence ou não a sequência.

"""
def is_fibonacci(n):
    # Inicializa os dois primeiros números da sequência
    a, b = 0, 1
    # Gera a sequência até o valor maior ou igual ao número informado
    while b < n:
        a, b = b, a + b
    # Verifica se o número informado é igual a algum número da sequência gerada
    return b == n or n == 0

# Recebe o número do usuário
numero = int(input("Informe um número: "))

# Verifica se o número pertence à sequência de Fibonacci
if is_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonacci.")
