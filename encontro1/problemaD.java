
package encontro1;

import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class problemaD{
    public static void main(String[] args){
        Scanner teclado = new Scanner(System.in); 
        List<Integer>AtividadeCansativa = new ArrayList<>();
        List<Integer>AtividadeRevigorante = new ArrayList<>();
       
    // primeira linha da entrada
       int disposicao=teclado.nextInt(); // disposição de willian
       int Ncansativas=teclado.nextInt(); // numero de atividade cansativas
       int Nrevigorante=teclado.nextInt(); // numero de atividades revigorante
    
    // 
       for (int i=0; i<Ncansativas;i++){
            int cansativa = teclado.nextInt();     // le o consumo de cada uma das atividades cansativas
            AtividadeCansativa.add(cansativa);    // adiciona o esse consumo em uma lista
       }
       for (int i=0; i<Nrevigorante;i++){
            int revigorante = teclado.nextInt(); // le a quanto cada atividade fornece de energia
            AtividadeRevigorante.add(revigorante); // adiciona as energia ganhas 
       }
      
       int contador=0; // contar o numero de atividade
       
       while(!AtividadeRevigorante.isEmpty()){ // percorre as atividades enquanto ainda existirem atividades revigorantes 
        
            if(!AtividadeCansativa.isEmpty()){ // verifica se a lista de atividades cansativas não esta vazia
                if(disposicao>=AtividadeCansativa.get(0)){ // verifica se tem disposicao para realizar a primeira atividadeda lista
                    disposicao = disposicao - AtividadeCansativa.get(0); 
                    AtividadeCansativa.remove(0); //remove a atividade realizada da lista
                    contador++; 
                }
            }
            if((!AtividadeRevigorante.isEmpty())){//verifica se a lista de atividades revigorante não esta vazia
                    disposicao = disposicao + AtividadeRevigorante.get(0);
                    AtividadeRevigorante.remove(0);//remove a atividade da lista
                    contador++;
            }
          
       }
        System.out.println("---------------");
        System.out.println(contador);
        teclado.close();
    }
}