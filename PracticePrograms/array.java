public class array {
    public static void main(String[] args) {
        //make longest array and have random numbers in it
        int[] arr = new int[100000000];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = (int) (Math.random() * 100000000);
        }
        
        System.out.println(arr[5]);

    }
}
