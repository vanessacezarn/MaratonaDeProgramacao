
import java.util.Scanner;

public class problemaA {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);

        int grau = teclado.nextInt();
        int k = teclado.nextInt();

        int coef = grau+1;

        int [] t = new int [coef];
        int [] p = new int [coef];
        int [] q = new int [coef];

        // le os coeficientes de t(x)
        for(int i=0; i<coef;i++){
            t[i]=teclado.nextInt();
        }
        // le os coeficientes de p(x)
        for(int i=0; i<coef;i++){
            p[i] = teclado.nextInt();
        }

        int termoIN = 0;

        for(int i=0;i<coef;i++){
            if(i==0){
                // termo independente = q[0]
                q[0] = q[0]+ t[i] + p[i];
            }else if(i>0){
                // i indica a potencia de x ; se i =2 então t[i]x²

                /*System.out.print(" + "+t[i]+"(x+"+k+")^"+i);
                System.out.print(" + "+p[i]+"(x-"+k+")^"+i);*/

                q[0] = q[0]+ (t[i]*k) + (p[i]*(-1)*k);
                //q[i] = t[i] + p[i]; 

            }
            
            if(q[i]<0){
                q[i] = 998244353 + q[i];
            }
        }
        
        for(int i= 0; i<coef;i++){
            System.out.println("Coeficiente de grau "+i+" = "+q[i]);
        }
        teclado.close();
    }
}
