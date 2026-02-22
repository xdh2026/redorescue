class node:
    def __init__(self,value):
        self.value = value
        self.next = None

values = []
class linkedlist:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self,value):
        n = node(value)
        if self.head is None:
            self.head = n
            self.tail = n
        else:

            self.tail.next = n
            self.tail = n
        
    def display(self):
        current = self.head
        #values = []
        while current :
            values.append(str(current.value))
            current = current.next
        print("-->".join(values))

my_list = linkedlist()
def main_insert():
    #print("11")
    
    #my_list = linkedlist()
    my_list.add(21)
    my_list.add(32)
    my_list.add(51)
    my_list.add(77)
    my_list.display()
    #return values
    
if __name__== "__main__":
    #values = []
    main_insert()
    print(my_list) #print the object

       
