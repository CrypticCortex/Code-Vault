import java.io.BufferedReader;
import java.io.FileReader;

/**
 * securerandom
 */
public class securerandom {

    public static void reader() {
        //read a fasta file
        try {
            BufferedReader br = new BufferedReader(new FileReader("/home/naylak15/Documents/tempfolder made by prop/JAAS_GrTE_14332.fasta"));
            String line = br.readLine();
            while (line != null) {
                //System.out.println(line);
                line = br.readLine();
            }
            br.close();
        } catch (Exception e) {
            System.out.println("Error: " + e);
        }
    }
    public static void finder() {
        //find whether string tggccaggat is present in the file
        try {
            BufferedReader br = new BufferedReader(new FileReader("/home/naylak15/Documents/tempfolder made by prop/JAAS_GrTE_14332.fasta"));
            String line = br.readLine();
            while (line != null) {
                if (line.contains("atgct")) {
                    System.out.println("atgct is present in the file");
                }
                else{
                    System.out.println("atgct is not present in the file");
                }
                line = br.readLine();
            }
            br.close();
        } catch (Exception e) {
            System.out.println("Error: " + e);
        }
    }
    public static void main(String[] args) {
        //call reader and finder methods
        reader();
        finder();

    }
}