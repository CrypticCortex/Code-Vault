/**
 * finder
 */
public class finder {

    public static void commonsub() {
        //given 2 strings find the common substrings
        String s1 = "atgct";
        String s2 = "agct";
        int count = 0;
        //find character not common
        for (int i = 0; i < s1.length(); i++) {
            for (int j = 0; j < s2.length(); j++) {
                if (s1.charAt(i) !=s2.charAt(j)) {
                    System.out.println("Character not common: " + s1.charAt(i));
                    count++;
                }
            }
        }
    }

    public static void main(String[] args) {
        commonsub();
    }
}