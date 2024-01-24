
public class CircularQueue<T> {
    private T[] queue;
    private int front;
    private int rear;
    private int size;
    private int maxSize;

    public CircularQueue(int maxSize) {
        this.maxSize = maxSize;
        this.queue = (T[]) new Object[maxSize];
        this.front = 0;
        this.rear = 0;
        this.size = 0;
    }

    public void enqueue(T value) {
        if (size == maxSize) {
            System.out.println("Queue is full");
            return;
        }
        queue[rear] = value;
        rear = (rear + 1) % maxSize;
        size++;
    }

    public T dequeue() {
        if (size == 0) {
            System.out.println("Queue is empty");
            return null;
        }
        T value = queue[front];
        front = (front + 1) % maxSize;
        size--;
        return value;
    }

    public T peek() {
        if (size == 0) {
            System.out.println("Queue is empty");
            return null;
        }
        return queue[front];
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public int size() {
        return size;
    }

    public void print() {
        for (int i = front; i < front + size; i++) {
            System.out.print(queue[i % maxSize] + " ");
        }
        System.out.println();
    }
    public static void main(String[] args) {
        CircularQueue<Integer> queue = new CircularQueue<>(5);
        queue.enqueue(1);
        queue.enqueue(2);
        queue.enqueue(3);
        queue.enqueue(4);
        queue.enqueue(5);
        queue.print();
        
    }
}
