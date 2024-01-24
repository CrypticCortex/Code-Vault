import java.util.Random;
import java.util.Scanner;

/**
 * RockPaperScissor
 */
public class RockPaperScissor {

    public static final String ROCK = """
                ROCK
                _________
            ___|     ____)
                    (______)
                    (_______)
                    (______)
            ____,__(____)

            """;

    public static final String PAPER = """
                PAPER
                ________
            ___'    ____)____
                      _______)
                     _________)
                    _________)
            ______,_______)
            """;

    public static final String SCISSOR = """
                SCISSOR
                _________
            ____'      ____)____
                          _______)
                       ____________)
                       (_____)
            ______,____(___)
            """;

    public static void main(String[] args) {
        System.out.println("""
                Enter Your Choice
                 Rock
                 Paper
                 Scissor \n""");
        String userchoice = getuserchoice();
        String compChoice = getcompChoice();
        if (userchoice == compChoice) {
            System.out.println("It's a tie !");
        } else if (userchoice == ROCK && compChoice == SCISSOR) {
            System.out.println("YOU Won");
        } else if (userchoice == SCISSOR && compChoice == ROCK) {
            System.out.println("Comp Won");
        } else if (userchoice == PAPER && compChoice == SCISSOR) {
            System.out.println("Comp Won");
        } else if (userchoice == SCISSOR && compChoice == PAPER) {
            System.out.println("You Won");
        } else if (userchoice == PAPER && compChoice == ROCK) {
            System.out.println("You Won");
        } else if (userchoice == ROCK && compChoice == PAPER) {
            System.out.println("Comp Won");
        }
    }

    public static String getcompChoice() {
        String compChoice;
        Random random = new Random();
        int input = random.nextInt(3) + 1;
        if (input == 1)
            compChoice = ROCK;
        else if (input == 2)
            compChoice = PAPER;
        else
            compChoice = SCISSOR;

        System.out.println("Computer move is: " + compChoice);
        System.out.println();
        return compChoice;
    }

    public static String getuserchoice() {
        Scanner in = new Scanner(System.in);
        String input = in.next();
        String userchoice = input.toUpperCase();
        System.out.println("Player move is: " + userchoice);
        return userchoice;
    }
}
