


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        num1 = num2 = 0
        for i in range(len(l1)):
            num1 += l1[i] * 10 ** i
        for i in range(len(l2)):
            num2 += l2[i] * 10 ** i
        num =  list(str(num1 + num2))
        list1 = list(map(int, num))
        list1.reverse()
        print(list1)

#.reverse()
test = Solution()
test.addTwoNumbers([2, 4, 3], [5, 6, 4])