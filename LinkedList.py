
#the basic node of the linked list data structure
class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next

#the linked list data structure
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_begining(self,data):          #insert data in the begining of linked list
        node = Node(data, self.head)
        self.head = node

    def print(self):                            #print the data in the begining of linked list
        if self.head is None:
            print("Linked List is Empty")
            return
        
        itr = self.head
        lstr = ''

        while itr:
            lstr += str(itr.data) + '---->'
            itr = itr.next

        print(lstr)  

    def insert_at_end(self,data):               #insert data in the end of linked list
        if self.head is None:
            self.head = Node(data, None)
            return
        
        itr = self.head
        while itr.next:
            itr = itr.next

        itr.next = Node(data, None) 

    def insert_values_at_end(self, data_lst):   #insert several data at th same timein the end of linked list
        for data in data_lst:
            self.insert_at_end(data)  

    def insert_values_at_begin(self, data_lst): #insert several data at th same time in the begin of linked list
        for data in data_lst:
            self.insert_at_begining(data) 

    def get_len(self):                          #get the length of linked list
        count = 0
        itr = self.head
        while itr:
            count = count + 1
            itr = itr.next
        return count                 

    def remove_at(self, index):                 #remove data from certain place
        count = 0
        itr = self.head

        if index < 0 or index > self.get_len():
            raise Exception ("This is invalid index")
        
        if index == 0:
            self.head = self.head.next
            return
        
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1
            
    def insert_at(self, index, data):           #add data in certain place
        count = 0
        itr = self.head

        if index < 0 or index > self.get_len():
            raise Exception ("This is invalid index")

        if index == 0:
            self.insert_at_begining(data)
            return
        
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):   #add data in after data
        if self.head is None:
            return

        if self.head.data == data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break

            itr = itr.next

    def remove_by_value(self, data):                            #remove data in after data
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

                         


node_1 = LinkedList()
data_1 = [28,27,25,26]
data_2 = [28,27,25,26]

node_1.insert_at_end('Ali')
node_1.insert_at_end('Amin')
node_1.insert_at_end('Mahmoud')

node_1.insert_values_at_end(data_1)
node_1.insert_values_at_begin(data_2)



print(f"\nThe length of the linkedlist = {node_1.get_len()} elements")
node_1.print()

node_1.insert_at(1,'Mohammed')
print(f"\nThe length of the linkedlist = {node_1.get_len()} elements after adding this new element")
node_1.print()

node_1.insert_at(0,'hassan')
print(f"\nThe length of the linkedlist = {node_1.get_len()} elements after adding this new element")
node_1.print()

node_1.insert_after_value('hassan', 'Zain')
print(f"\nThe length of the linkedlist = {node_1.get_len()} elements after adding this new element")
node_1.print()

node_1.remove_by_value('Amin')
print(f"\nThe length of the linkedlist = {node_1.get_len()} elements after removing this new element")
node_1.print()

"""
node_1.insert_at(5,'hassan')
print(node_1.get_len())
node_1.print()

node_1.remove_by_value('hassan')
print(node_1.get_len())
node_1.print()

node_1.remove_by_value('Ali')
print(node_1.get_len())
node_1.print()

node_1.remove_by_value('hassan')
print(node_1.get_len())
node_1.print()



    


        
