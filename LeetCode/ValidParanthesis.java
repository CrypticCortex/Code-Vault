package LeetCode;

import java.util.Stack;

class ValidParanthesis {
    public boolean isValid(String s) {
        Stack<Character> stack = new Stack<>();
        
        for (char ch : s.toCharArray()) {
            if (ch == '(' || ch == '{' || ch == '[') {
                stack.push(ch);
            } else {
                if (stack.isEmpty()) {
                    return false; // No corresponding opening bracket
                }
                
                char openBracket = stack.pop();
                if ((ch == ')' && openBracket != '(') ||
                    (ch == '}' && openBracket != '{') ||
                    (ch == ']' && openBracket != '[')) {
                    return false; // Mismatched brackets
                }
            }
        }
        
        return stack.isEmpty(); // All brackets should be matched and popped
    }
    public static void main(String[] args) {
        ValidParanthesis vp = new ValidParanthesis();
        System.out.println(vp.isValid("()"));
        System.out.println(vp.isValid("()[]{}"));
        System.out.println(vp.isValid("(]"));
        System.out.println(vp.isValid("([)]"));
        System.out.println(vp.isValid("{[]}"));
    }
}

