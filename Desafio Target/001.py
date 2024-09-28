# Variáveis iniciais da sequência de Fibonacci
a, b = 0, 1  # 'a' começa em 0 e 'b' começa em 1, representando os dois primeiros números da sequência
seq_fibonnaci = []  # Lista para armazenar os valores gerados da sequência de Fibonacci

# Entrada do usuário: número de termos da sequência de Fibonacci a ser gerada
n = int(input("Digite o número de termos da sequência de Fibonacci que deseja gerar: "))

# Exibe o início da sequência para o número de termos escolhido
print(f"A sequência de Fibonacci para o valor {n} é:")

# Loop para gerar e exibir a sequência de Fibonacci até o n-ésimo termo
for i in range(n):  # Itera até n (exclusivo), gerando exatamente 'n' termos
    print(a, end=' ')  # Imprime o valor atual de 'a' sem quebra de linha
    seq_fibonnaci.append(a)  # Armazena o valor atual de 'a' na lista 'seq_fibonnaci'
    a, b = b, a + b  # Atualiza 'a' e 'b' para o próximo número da sequência (a = b, b = a+b)

# Verifica se o valor 'n' está presente na sequência gerada
if n in seq_fibonnaci:
    print(f"\nO valor {n} está na sequência de Fibonacci!\n")
else:
    print(f"\nO valor {n} não está na sequência de Fibonacci!\n")
