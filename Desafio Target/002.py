user = input("Escreva um texto ou palavra: ") # Entrada do usuário

# Variável para armazenar o texto em letras minúsculas
minus = user.lower()

# Variável para contar a quantidade de vezes que a letra "a" aparece
contador = minus.count('a')

# Verifica se a letra "a" está presente no texto
if "a" in minus:
    print(f"A letra a está presente no texto {user} e aparece {contador} vezes.")
else:
    print(f"A letra a não está presente no texto {user}.")
