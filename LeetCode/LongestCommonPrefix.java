package LeetCode;

import java.util.Arrays;

public class LongestCommonPrefix {
    class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs == null || strs.length == 0) {
            return "";
        }
        
        Arrays.sort(strs);
        String s1 = strs[0];
        String s2 = strs[strs.length - 1];
        int idx = 0;
        int minLength = Math.min(s1.length(), s2.length()); // Optimize by using the shorter length
        
        while (idx < minLength && s1.charAt(idx) == s2.charAt(idx)) {
            idx++;
        }
        
        return s1.substring(0, idx);
    }
}

    public static void main(String[] args) {
        LongestCommonPrefix lcp = new LongestCommonPrefix();
        Solution sol = lcp.new Solution();
        String[] strs = {"flower", "flow", "flight"};
        System.out.println(sol.longestCommonPrefix(strs));
    }
}
