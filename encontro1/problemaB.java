package encontro1;

import java.util.Scanner;

public class problemaB{
    public static void main(String[] args){
        Scanner teclado = new Scanner(System.in);
        int quantiaBrinquedos = teclado.nextInt();
        int alturaCarlito = teclado.nextInt();
        int contador=0;

        for(int i=0;i<quantiaBrinquedos;i++){
            int alturaBrinquedo = teclado.nextInt();
            if(alturaBrinquedo>alturaCarlito){
                contador++;
            }
        }
        System.out.println("--------------");
        System.out.println(contador);
        teclado.close();
    }
}
