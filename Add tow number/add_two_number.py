# -*- coding: utf-8 -*-

# Build my own armory: build a single link.

class ListNode(object):
    def __init__(self, val, next):
        super(ListNode, self).__init__()
        self.val = val
        self.next = next



def buildLink(numbers=[]):
    """
    :rtype: ListNode
    """
    prev = None

    for i in reversed(numbers):
        current = ListNode(i, prev)
        prev = current

    # return the head node.
    return current


def travelList(number_link):
    pivot = number_link

    while pivot is not None:
        print(pivot.val)
        pivot = pivot.next


def add_two_number_links(link1, link2):
    """
    :type link1: ListNode
    :type link2: ListNode
    :rtype: ListNode
    """
    p1, p2 = link1, link2
    carry = 0
    result = []
    while p1 is not None and p2 is not None:
        t = p1.val + p2.val + carry
        carry = t / 10
        t = t % 10
        result.append(t)

    return buildLink(result)


__all__ = [
    'buildLink'
]


if __name__ == '__main__':
    l = buildLink([2,4,3])
    travelList(l)
