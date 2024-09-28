# Descobrindo a lógica 

#a)1,3,5,7,__ <- 9

#A lógica em si é de número ímpares

num_impar = []

for i in range(15):
    if i%2 == 1:
        num_impar.append(i)

print(num_impar)

#b) 2,4,8,16,32,64,__ <- 128

#A lógica é pegar o valor e multiplicar por 2 pelo resultado anterior

lista_mult = []

a = 2

while a < 200:
    lista_mult.append(a)
    a *=2

print(lista_mult)


#c) 0,1,4,9,16,25,36,___ <- 49

#A lógica por trás dessa sequência é representada pelos quadrados perfeitos dos números inteiros não negativos

square_list = []


def square(n):
    for i in range(11):
        n = i**2
        square_list.append(n)
    print(square_list)
    
square(0)

#d) 4,16,36,64,___ <- 100

#Segue a mesma lógica que a letra c, porém com um diferencial! O número base começa com 2 e continua adicionando mais 2 a base até chegar a um determinado número

square_list2 = []

a = 2

while True:
    for i in range(a,11):
        if i%2 == 0:
            i *= a
            a += 2
            square_list2.append(i)           
    break
print(square_list2)

#e)1,1,2,3,5,8,___ <- 13

#A lógica vem da sequência de Fibonacci

def fibonacci(n):
    sequence = []
    a, b = 0, 1  # Começando com 0 e 1
    for _ in range(n):
        sequence.append(a)
        a, b = b, a + b  # Atualizando os valores
    return sequence

n = 10  # Número de termos desejados
fibonacci_sequence = fibonacci(n)
print(fibonacci_sequence)

#f)2,10,12,16,17,18,19,___ <- 200

#Devo admitir que demorei para entender (haha). A lógica é, todos o números começam com a letra D.