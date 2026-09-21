class Solution:
    def removeNthFromEnd(self, head, n):
        length = 0
        temp = head

        while temp:
            length += 1
            temp = temp.next

        if n == length:
            return head.next

        temp = head

        for i in range(length - n - 1):
            temp = temp.next

        temp.next = temp.next.next

        return head