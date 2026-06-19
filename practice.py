class node():
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.previous = None

class linked_list():
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        new_node.next = self.head
        self.head = new_node


    def delete(self):
        self.head.next = self.head
        #while cur.next != None:
        #    cur = cur.next
        #cur.next = cur

    def get_first_element(self):
        return self.head
            
        

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
my_list.append(4)
my_list.append(7)
my_list.display()
my_list.delete()
my_list.display()

####append works 






