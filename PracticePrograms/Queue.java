import java.util.LinkedList;

//amking queue with linked lists
/**
 * Queue
 */
public class Queue {

    private LinkedList<Integer> queue;

    public Queue() {
        queue = new LinkedList<Integer>();
    }

    public void enqueue(int value) {
        queue.add(value);
    }

    public int dequeue() {
        return queue.remove(0);
    }

    public int peek() {
        return queue.get(0);
    }

    public boolean isEmpty() {
        return queue.isEmpty();
    }

    public int size() {
        return queue.size();
    }

    public void print() {
        System.out.println(queue);
    }
    public void reverse(){
        int size = queue.size();
        for(int i = 0; i < size/2; i++){
            int temp = queue.get(i);
            queue.set(i, queue.get(size-i-1));
            queue.set(size-i-1, temp);
        }
    }
    public static void main(String[] args) {
        Queue q = new Queue();
        q.enqueue(1);
        q.enqueue(2);
        q.enqueue(3);
        q.enqueue(4);
        q.enqueue(5);
        q.print();
        q.reverse();
        q.print();
    }
}