import java.util.Random;

/**
 * rand
 */
public class rand {

    //making random numbers without using Math.random()
    public static int randoms(){
        Random rand = new Random();
        int randomNum2 = rand.nextInt(100);
        return randomNum2;
    }
    /**
     * Innerrand
     */
    public static class Innerrand {
    
        //calling rand class and making random numbers
        public static void main(String[] args) {
            int randomNum = randoms();
            System.out.println(randomNum);
        }
   }
}