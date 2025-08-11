#include <stdio.h>

int main(){
    int n;
    scanf("%i",&n);

    int sequencia[n];
    for(int i=0 ; i<n; i++){
        scanf("%i",&sequencia[i]);
    }


    int soma=0, maiorSoma=0;
    for(int i=0; i<n; i++){
        for(int k=n; k>i; k--){
            for(int j=i; j<k; j++){
                soma += sequencia[j];

            }
            if(soma > maiorSoma){
                maiorSoma = soma;
            }
            soma=0;
        }
    }

    printf("%d",maiorSoma);

    return 0;
}