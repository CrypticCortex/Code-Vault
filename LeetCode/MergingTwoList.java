package LeetCode;

import java.util.List;

public class MergingTwoList {

    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        ListNode dummy = new ListNode(-1); // Create a dummy node to simplify insertion
        ListNode current = dummy;

        if (list1 == null) {
            return list2;
        }
        if (list2 == null) {
            return list1;
        }
        while(list1 != null && list2 !=null){
            if(list1.val < list2.val){
                current.next = list1;
                list1 = list1.next;
            }
            else{
                current.next = list2;
                list2 = list2.next;
            }
            if(list1 != null){
                current.next = list1;
            }
            if(list2 != null){
                current.next = list2;
            }

        }
        return dummy.next;
    }

    public static void main(String[] args) {
        MergingTwoList mtl = new MergingTwoList();
        ListNode list1 = mtl.new ListNode(1);
        
    }
    public class ListNode {
     int val;
     ListNode next;
     ListNode() {}
     ListNode(int val) { this.val = val; }
     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 }
 
}
