//finding data in the linked list
class finding{
    //find the number given by user in linked list
    public class Node{
        int data;
        Node next;
        Node(int d){
            data = d;
            next = null;
        }
    }
    Node head = null;
    Node tail = null;
    public void add(int d){
        Node newNode = new Node(d);
        if(head == null){
            head = newNode;
            tail = newNode;
        }
        else{
            tail.next = newNode;
            tail = newNode;
        }
    }
    public void print(){
        Node temp = head;
        while(temp != null){
            System.out.print(temp.data + " ");
            temp = temp.next;
        }
    }
    public void find(int d){
        Node temp = head;
        while(temp != null){
            if(temp.data == d){
                System.out.println("Found");
                //print where the data is found
                System.out.println("Data found at: " + temp.data);
                return;
            }
            temp = temp.next;
        }
        System.out.println("Not Found");
    }
    public static void main(String[] args){
        finding obj = new finding();
        obj.add(1);
        obj.add(2);
        obj.add(3);
        obj.add(4);
        obj.add(5);
        obj.add(6);
        obj.add(7);
        obj.add(8);
        obj.add(9);
        obj.add(10);
        obj.print();
        System.out.println();
        obj.find(5);
    }
}