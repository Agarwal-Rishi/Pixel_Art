class node():
    def __init__(self, data=None):
        self.data = data
        self.next = None

class linked_list():
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = new_node

    def delete(self):
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = cur

    def get_last_element(self):
        cur = self.head       
        while cur.next != None:
            cur = cur.next
        return cur
            
        

    def display(self):
        cur = self.head
        print(cur.data)
        while cur.next != None:
            print(cur.next.data)
            cur = cur.next
            
    def contains(self, data):
        cur = self.head
        while cur.next != None:
            cur = cur.next
            if data == cur:
                return True
            else:
                return False
            
            

my_list = linked_list()
my_list.append(2)
my_list.append(3)
my_list.append(4)
my_list.display()
if my_list.contains(3):
    print("6")





