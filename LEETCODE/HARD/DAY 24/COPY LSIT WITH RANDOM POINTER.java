class RandomListNode {
    int label;
    RandomListNode next, random;
    RandomListNode(int x) { this.label = x; }
}

public class Solution {
    public RandomListNode copyRandomList(RandomListNode head) {
        if (head == null) return null;

        // Step 1: Clone each node and insert it next to original
        RandomListNode p = head;
        while (p != null) {
            RandomListNode copy = new RandomListNode(p.label);
            copy.next = p.next;
            p.next = copy;
            p = copy.next;
        }

        // Step 2: Assign random pointers for the copy
        p = head;
        while (p != null) {
            if (p.random != null) {
                p.next.random = p.random.next;
            }
            p = p.next.next;
        }

        // Step 3: Separate original and copied list
        p = head;
        RandomListNode headCopy = head.next;
        while (p != null) {
            RandomListNode copy = p.next;
            p.next = copy.next;
            copy.next = (p.next != null) ? p.next.next : null;
            p = p.next;
        }

        return headCopy;
    }
}
