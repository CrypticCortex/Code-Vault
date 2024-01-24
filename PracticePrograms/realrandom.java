public class realrandom {
    //find whether 1001,3,999 are present in the array consecutively
    public static void main(String[] args) {
        //making array and assigning random numbers
        int[] arr = new int[10000000];
        for (int i = 0; i < arr.length; i++) {
            arr[i] = (int) (Math.random() * 10000000);
        }

        arr[5] = 1001;
        arr[6] = 3;
        arr[7] = 999;
        //finding whether 1001,3,999 are present in the array consecutively
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == 1001 && arr[i + 1] == 3 && arr[i + 2] == 999) {
                //print the array index where 1001,3,999 are present
                System.out.println("1001 is present at index " + i + " \n and 3 is present at index " + (i + 1) + "\n and 999 is present at index " + (i + 2));
            }
        }
    }
    
}
