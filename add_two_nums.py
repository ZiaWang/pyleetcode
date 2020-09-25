# -*- coding: utf-8 -*-

"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
    输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
    输出：7 -> 0 -> 8
    原因：342 + 465 = 807

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/add-two-numbers

"""


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    #@profile
    def add_two_numbers(self, l1, l2):
        """
        Args:
            l1: ListNode，链表的第一个节点
            l2: ListNode，另一个链表的第一个节点
        Return:
            返回ListNode，是结果链表的第一个节点
        """

        num_ret = self.get_num_from_node(l1) + self.get_num_from_node(l2)
        return self.create_listNode_from_num(num_ret)

    #@profile
    def create_listNode_from_num(self, num):
        nodes = [ListNode(int(val)) for val in reversed(str(num))]

        pre_node = None
        for node in nodes:
            if pre_node:
                pre_node.next = node
            pre_node = node

        return nodes[0]

    #@profile
    def get_num_from_node(self, l):
        num_s = "%s" % l.val

        next_l = l
        while next_l.next:
            next_l = next_l.next
            num_s = str(next_l.val) + num_s

        return int(num_s)


#@profile
def test():
    obj = Solution()

    # 321
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)

    assert obj.get_num_from_node(l1) == 321

    l2 = ListNode(3)
    l2.next = ListNode(4)
    l2.next.next = ListNode(5)

    assert obj.get_num_from_node(l2) == 543

    # 864
    ret = obj.add_two_numbers(l1, l2)
    assert ret.val == 4
    assert ret.next.val == 6
    assert ret.next.next.val == 8


if __name__ == '__main__':
    test()


