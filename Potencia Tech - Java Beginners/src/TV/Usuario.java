package DIO;

public class Usuario{
    
    public static void main(String[] args) throws Exception {

        SmartTv smartTv = new SmartTv();
        
        // inicial 

        System.out.println("A TV está ligada? " + smartTv.ligada);
        System.out.println("O canal atual é: " + smartTv.canal);
        System.out.println("O volume atual é "+ smartTv.volume);


        //ligar/desligar TV 

        smartTv.ligar();
        System.out.println("Novo Status> A TV está ligada?" + smartTv.ligada);

        smartTv.desligar();
        System.out.println("Novo Status> A TV está ligada?" + smartTv.ligada);
    
        smartTv.ligar();
        System.out.println("Novo Status> A TV está ligada?" + smartTv.ligada);

        //diminuir/aumentar volume
        
        smartTv.diminuirVolume();
        System.out.println("O volume atual é "+ smartTv.volume);

        smartTv.diminuirVolume();
        smartTv.volume--;
        System.out.println("diminuindo o volume para: " + smartTv.volume);
        

        //trocar de canal

        smartTv.mudarCanal(13);
         System.out.println("O canal atual é: " + smartTv.canal);
    
    }
}