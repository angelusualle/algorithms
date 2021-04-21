class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

# O(N) time O(1) space
def reverse_k_group(head, k):
        if k == 1:
            return head
        len_list = 1
        it = head
        while it.next != None:
            it = it.next
            len_list += 1
        cnt = 0
        orig_head = head
        next_ = head
        prev = None
        global_cnt = 0
        link = None
        tmp_head = None
        i_n = None
        while True:
            if cnt < k:

                tmp = next_.next
                if prev is not None:
                    i_n.next = tmp
                    next_.next = prev
                if prev == head:
                    head = next_
                prev = next_
                next_ = tmp
                tmp_head = prev
                cnt += 1
                global_cnt += 1
                if i_n is None:
                    i_n = prev
            else:
                if link is not None:
                    link.next = tmp_head
                    link = i_n
                else:
                    link = orig_head
                prev=None
                cnt = 0
                i_n = None
                if len_list - global_cnt < k:
                    break
        return head