import java.util.*;

class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}

public class MergeKLists {
    public ListNode mergeKLists(List<ListNode> lists) {
        if (lists == null || lists.isEmpty()) return null;

        Queue<ListNode> heap = new PriorityQueue<>(lists.size(), (a, b) -> a.val - b.val);

        for (ListNode node : lists) {
            if (node != null) heap.add(node);
        }

        ListNode dummy = new ListNode(0);
        ListNode curr = dummy;

        while (!heap.isEmpty()) {
            ListNode node = heap.poll();
            curr.next = node;
            curr = curr.next;

            if (node.next != null) {
                heap.add(node.next);
            }
        }
        return dummy.next;
    }
}
