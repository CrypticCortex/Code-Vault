package LeetCode;

public class PalindromNumber {
    class Solution {
        public boolean isPalindrome(int x) {
            if (x < 0) {
                return false;
            }
            int original = x;
            int reversed = 0;
            while (x > 0) {
                int digit = x%10;
                reversed = reversed * 10 + digit;
                x/=10;
            }
            return original == reversed;
        }
    }
    public static void main(String[] args) {
        PalindromNumber pn = new PalindromNumber();
        Solution sol = pn.new Solution();
        System.out.println(sol.isPalindrome(121));
        System.out.println(sol.isPalindrome(-121));
        System.out.println(sol.isPalindrome(10));
    }    
}
