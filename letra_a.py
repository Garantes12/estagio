def contar_letra_a(str):
    # Converte a string para minúsculas e conta a quantidade de 'a'
    count = str.lower().count('a')
    return count

# Recebe a string do usuário
palavra = input("Informe uma palavra: ")

# Verifica a quantidade de vezes que a letra 'a' aparece na string
count = contar_letra_a(palavra)

if count > 0:
    print(f"A letra 'a' aparece {count} vezes na palavra.")
else:
    print("A letra 'a' não aparece na palavra.")
