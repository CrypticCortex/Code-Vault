import java.util.LinkedList;

public class insertlinkl {
    //make a linked list 
    LinkedList<String> list = new LinkedList<String>();
    //add elements to the linked list
    public void add(String s) {
        list.add(s);
    }
    //a method to insert data at a particular index
    public void insert(String s, int index) {
    //a method without using inbuilt method
        LinkedList<String> temp = new LinkedList<String>();
        for (int i = 0; i < index; i++) {
            temp.add(list.get(i));
        }
        temp.add(s);
        for (int i = index; i < list.size(); i++) {
            temp.add(list.get(i));
        }
        list = temp;
    }
    public static void main(String[] args) {
        insertlinkl obj = new insertlinkl();
        obj.add("a");
        obj.add("b");
        obj.add("c");
        obj.add("d");
        obj.add("e");
        obj.add("f");
        obj.add("g");
        obj.add("h");
        obj.add("i");
        obj.add("j");
        obj.add("k");
        obj.add("l");
        obj.add("m");
        obj.add("n");
        obj.add("o");
        obj.add("p");
        obj.add("q");
        obj.add("r");
        obj.add("s");
        obj.add("t");
        obj.add("u");
        obj.add("v");
        obj.add("w");
        obj.add("x");
        obj.add("y");
        obj.add("z");
        obj.insert("z", 5);
        System.out.println(obj.list);
    }
}
