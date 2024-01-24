class stack {
    static final int MAX = 1000;
    int top;
    String a[] = new String[MAX]; // Maximum size of Stack

    boolean isEmpty() {
        return (top < 0);
    }

    stack() {
        top = -1;
    }

    boolean push(String x) {
        if (top >= (MAX - 1)) {
            System.out.println("Stack Overflow");
            return false;
        } else {
            a[++top] = x;
            //System.out.println(x + " pushed into stack");
            return true;
        }
    }

    String pop() {
        if (top < 0) {
            System.out.println("Stack Underflow");
            return "0";
        } else {
            String x = a[top--];
            return x;
        }
    }

    String peek() {
        if (top < 0) {
            System.out.println("Stack Underflow");
            return "0";
        } else {
            String x = a[top];
            return x;
        }
    }

    void print() {
        for (int i = top; i > -1; i--) {
            System.out.print(" " + a[i]);
        }
    }
    public static void main(String[] args) {
        stack s = new stack();
        s.push("urmom+1");
        s.push("urmom");
        s.print();
        //reversing the string
        String x = s.pop();
        String y = s.pop();
        s.push(x);
        s.push(y);
        s.print();

    }
}