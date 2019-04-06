import heapq


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def mergeKLists(lists):
    head = tail = ListNode(None)
    heap = []
    cntr = 0  # Unique counter to make sure we don't get a TypeError comparing ListNodes
    for l in lists:
        if l:
            heapq.heappush(heap, (l.val, cntr, l))
            cntr += 1
    while heap:
        _, _, l = heapq.heappop(heap)
        while l and (not heap or l.val <= heap[0][0]):
            tail.next = l
            tail = l
            l = l.next
        if l and heap:
            heapq.heappush(heap, (l.val, cntr, l))
            cntr += 1
    return head.next


def make_testcase(lists_of_nums):
    linked_lists = []
    for list_of_nums in lists_of_nums:
        if list_of_nums:
            head = curr = ListNode(list_of_nums[0])
            for n in list_of_nums[1:]:
                curr.next = ListNode(n)
                curr = curr.next
            linked_lists.append(head)
    return linked_lists


def print_linked_list(node):
    if node:
        print(node.val, end=' ')
        print_linked_list(node.next)
    else:
        print('')


if __name__ == '__main__':
    print_linked_list(mergeKLists(make_testcase([
        [1,4,5],
        [1,3,4],
        [2,6]
    ])))