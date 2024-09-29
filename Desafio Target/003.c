#include <stdio.h>

int main() {
    int INDICE = 12, SOMA = 0, K = 1;

    while (K < INDICE) {
        K = K + 1;  // Incrementa K
        SOMA = SOMA + K;  // Adiciona K à SOMA
    }

    printf("%d\n", SOMA);  // Imprime o valor de SOMA
    return 0;
}

// O resultado vai ser 77 
