class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next
class LinkedList:
    def __init__(self):
        self.head = None
    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node
    def print_list(self):
        if self.head == None:
            print("Linked list is empty")
            return
        itr = self.head
        liststr = ""
        while itr:
            liststr += str(itr.data) + "--->"
            itr = itr.next
        print(liststr)
    def insert_at_end(self, data):
        if self.head == None:
            self.head = Node(data, None)
            return
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
    def length(self):
        itr = self.head
        count = 0
        while itr:
            count +=1
            itr = itr.next
        return count
    def remove(self, index=None):
        if index == None:
            index = self.length() - 1
        if index < 0 or index > self.length():
            raise Exception("invalid index")
        if index == 0:
            self.head = self.head.next
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count +=1
    def insert_at(self, index, data):
        if index < 0 or index > self.length():
            raise Exception("invalid index")
        if index == 0:
            self.insert_at_beginning(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1
    def at(self, index):
        if index < 0 or index > self.length():
            raise Exception("invalid index")
        itr = self.head
        count = 0
        while itr:
            if count == index - 1:
                return itr.next.data
            itr = itr.next
            count += 1
    def get_ele(self, f1=None, f2=None):
        if f1 == None:
            f1 = 0
        if f2 == None:
            f2 = self.length()
        if f1 < 0 or f1 > self.length():
            raise Exception("first index is not valid")
        if f2 < 0 or f2 > self.length():
            raise Exception("second index is not valid")
        itr = self.head
        count = 0
        ele = []
        while itr:
            if count == f2:
                ele.append(itr.data)
                break
            if count >= f1:
                ele.append(itr.data)
            itr = itr.next
            count += 1
        return ele
    def replace(self, index=None, data=None):
        if index == None:
            index = 0
        if index < 0 or index > self.length():
            raise Exception("invalid index")
        itr = self.head
        count = 0
        while itr:
            if count == index:
                itr.data = data
            itr = itr.next
            count += 1
    def insert_after(self, ins_af, data):
        count = 0
        itr = self.head
        while itr:
            if ins_af == itr.data:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1
    def count_of(self, data):
        count = 0
        dcount = 0
        itr = self.head
        while itr:
            if itr.data == data:
                dcount += 1
            itr = itr.next
            count += 1
        return dcount
if __name__ == "__main__":
    llist = LinkedList()
    # llist.insert_at_beginning(7)
    # llist.insert_at_beginning(5)
    # llist.insert_at_end(6)
    llist.insert_values(["orange", "black", "white", "gold", "silver", "green"])
    # llist.insert_at(3, "programming")
    # print(llist.length())
    # print(llist.at(3))
    # llist.remove()
    llist.replace(3, "platinum")
    llist.insert_after("gold", "red")
    print(llist.count_of("green"))
    llist.print_list()
