package LeetCode;
import java.util.HashMap;
import java.util.Map;

public class RomantoInteger {
    

class Solution {
    public int romanToInt(String s) {
        Map<Character, Integer> romanToInteger = new HashMap<>();
        romanToInteger.put('I', 1);
        romanToInteger.put('V', 5);
        romanToInteger.put('X', 10);
        romanToInteger.put('L', 50);
        romanToInteger.put('C', 100);
        romanToInteger.put('D', 500);
        romanToInteger.put('M', 1000);
        
        int result = 0;
        for (int i = 0; i < s.length(); i++) {
            if (i < s.length() - 1 && romanToInteger.get(s.charAt(i)) < romanToInteger.get(s.charAt(i + 1))) { // checks if left is less than right so that we can subtract
                result += romanToInteger.get(s.charAt(i + 1)) - romanToInteger.get(s.charAt(i));
                i++; 
            } else {
                result += romanToInteger.get(s.charAt(i));
            }
        }
        return result;
    }
}
    public static void main(String[] args) {
        RomantoInteger ri = new RomantoInteger();
        Solution sol = ri.new Solution();
        System.out.println(sol.romanToInt("III"));
        System.out.println(sol.romanToInt("IV"));
        System.out.println(sol.romanToInt("IX"));
        System.out.println(sol.romanToInt("LVIII"));
        System.out.println(sol.romanToInt("MCMXCIV"));
    }
}
