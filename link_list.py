# 单向链表
# 2019.10.10


# 结点类
class Node:
    def __init__(self, elem):
        self.elem = elem
        self.next = None


# 单链表
class Single_Linklist:
    def __init__(self, node=None):
        # 头节点定义为私有变量
        self._head = node

    def is_empty(self):
        # 判断链表是否为空
        if self._head is None:
            return True
        else:
            return False

    def length(self):
        # 返回链表的长度
        # cur游标，用来移动遍历节点
        # count用来计数
        cur = self._head
        count = 0
        while cur != None:
            count += 1
            cur = cur.next
        return count

    def travel(self):
        # 遍历输出整个链表
        cur = self._head
        while cur != None:
            print(cur.elem, end=' ')
            cur = cur.next
        print()

    def add(self, item):
        # 头部添加一个节点
        node = Node(item)
        if self._head == None:
            self._head = node
        else:
            node.next = self._head
            self._head = node

    def append(self, item):
        # 尾部添加一个节点
        node = Node(item)
        # 若链表为空，直接将该节点作为链表的第一个元素
        if self._head == None:
            self._head = node
        else:
            cur = self._head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def insert(self, pos, item):
        # 在指定位置pos添加节点
        # 若指定位置pos为第一个元素之前，则执行头部插入
        if pos <= 0:
            self.add(item)
        # 若指定位置超过链表尾部，则执行尾部插入
        elif pos >= self.length():
            self.append(item)
        else:
            pre = self._head
            count = 0
            node = Node(item)
            while count < (pos-1):
                count += 1
                pre = pre.next

            node.next = pre.next
            pre.next = node

    def remove(self, item):
        # 删除某一个节点
        # 若链表为空，则直接返回
        if self.is_empty():
            return
        pre = None
        cur = self._head

        while cur != None:
            # 若没有找到元素，继续按链表后移节点
            if cur.elem != item:
                pre = cur
                cur = cur.next
            else:
                # 若要删除的点为头节点
                if cur == self._head:
                    self._head = cur.next
                else:
                    if cur == self._head:
                        self._head = cur.next
                        break
                    else:
                        pre.next = cur.next
                        break

    def search(self, item):
        # 查找节点是否存在
        cur = self._head
        while cur != None:
            if cur.elem == item:
                return True
            else:
                cur = cur.next
        return False


if __name__ == '__main__':
    sing_obj = Single_Linklist()
    print(sing_obj.is_empty())
    print(sing_obj.length())
    sing_obj.append(1)
    sing_obj.append(2)
    sing_obj.append(3)
    sing_obj.append(4)
    sing_obj.travel()
    sing_obj.add(-1)
    sing_obj.travel()
    sing_obj.insert(2, 9)
    sing_obj.travel()
    print(sing_obj.search(3))
    sing_obj.remove(2)
    sing_obj.travel()














