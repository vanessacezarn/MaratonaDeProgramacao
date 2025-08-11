#include <stdio.h>
#define MAX 10000000

int main() {
    int n;
    scanf("%d", &n);

    float sequencia[MAX];
    for (int i = 0; i < n; i++) {
        scanf("%f", &sequencia[i]);
    }

    int somaAtual = 0, maiorSoma = sequencia[0];

    for (int i = 0; i < n; i++) {
        somaAtual += sequencia[i];

        if (somaAtual > maiorSoma) {
            maiorSoma = somaAtual;
        }

        if (somaAtual < 0) {
            somaAtual = 0;
        }
        printf("%d",somaAtual)
    }

    printf("%d", maiorSoma);
    return 0;
}