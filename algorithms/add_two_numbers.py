"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    def __eq__(self, other):
        return self.val == other.val

    @classmethod
    def fromlist(cls, *vals):
        if vals:
            head = cls(vals[0])

            curr = head
            for val in vals[1:]:
                node = cls(val)
                curr.next = node
                curr = node

            return head


def add_two_numbers_brute_force(l1, l2):  # O(n)
    def get_num_from_linked_list(l):  # O(n)
        mag = 1
        n = 0
        while l:
            n += mag * l.val
            mag *= 10
            l = l.next
        return n

    def get_linked_list_from_num(n):  # O(n)
        curr = head = ListNode(n % 10)
        n //= 10

        while n:
            node = ListNode(n % 10)
            curr.next = node
            curr = node
            n //= 10

        return head

    n1 = get_num_from_linked_list(l1)
    n2 = get_num_from_linked_list(l2)
    return get_linked_list_from_num(n1 + n2)


def add_two_numbers_optimized(l1, l2):  # O(n)
    dummy_head = curr = ListNode(0)
    carry = 0
    while l1 or l2:
        x = l1.val if l1 else 0
        y = l2.val if l2 else 0
        s = carry + x + y
        carry = s // 10
        curr.next = ListNode(s % 10)
        curr = curr.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None
    if carry:
        curr.next = ListNode(carry)
    return dummy_head.next


if __name__ == '__main__':
    assert add_two_numbers_brute_force(
        ListNode.fromlist(2, 4, 3),
        ListNode.fromlist(5, 6, 4)
    ) == ListNode.fromlist(7, 0, 8)

    assert add_two_numbers_optimized(
        ListNode.fromlist(2, 4, 3),
        ListNode.fromlist(5, 6, 4)
    ) == ListNode.fromlist(7, 0, 8)
