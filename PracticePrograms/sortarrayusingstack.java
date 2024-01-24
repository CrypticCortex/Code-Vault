/**
 * sortarrayusingstack
 */
public class sortarrayusingstack {  

    static final int MAX = 100;
    int top;
    int a[] = new int[MAX]; // Maximum size of Stack

    boolean isEmpty() {
        return (top < 0);
    }

    sortarrayusingstack() {
        top = -1;
    }

    boolean push(int x) {
        if (top >= (MAX - 1)) {
            System.out.println("Stack Overflow");
            return false;
        } else {
            a[++top] = x;
            //System.out.println(x + " pushed into stack");
            return true;
        }
    }

    int pop() {
        if (top < 0) {
            System.out.println("Stack Underflow");
            return 0;
        } else {
            int x = a[top--];
            return x;
        }
    }

    int peek() {
        if (top < 0) {
            System.out.println("Stack Underflow");
            return 0;
        } else {
            int x = a[top];
            return x;
        }
    }

    void print() {
        for (int i = top; i > -1; i--) {
            System.out.print(" " + a[i]);
        }
    }
    //sort the stack in descending order
    void sortdes() {
        int temp;
        for (int i = 0; i < top; i++) {
            for (int j = i + 1; j <= top; j++) {
                if (a[i] < a[j]) {
                    temp = a[i];
                    a[i] = a[j];
                    a[j] = temp;
                }
            }
        }
    }

    void sortasc() {
        int temp;
        for (int i = 0; i < top; i++) {
            for (int j = i + 1; j <= top; j++) {
                if (a[i] > a[j]) {
                    temp = a[i];
                    a[i] = a[j];
                    a[j] = temp;
                }
            }
        }
    }
    //sortting the stack using temp stack
    void sort() {
        sortarrayusingstack temp = new sortarrayusingstack();
        int x;
        while (!isEmpty()) {
            x = pop();
            while (!temp.isEmpty() && temp.peek() >= x) {
                push(temp.pop()); //
            }
            temp.push(x);
        }
        while (!temp.isEmpty()) {
            push(temp.pop());
        }
    }
    public static void main(String[] args) {
        sortarrayusingstack s = new sortarrayusingstack();
        s.push(5);
        s.push(1);
        s.push(4);
        s.push(45);
        s.print();
        System.out.println("\n");
        s.sort();
        s.print();
    }
}