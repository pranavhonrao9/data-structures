class Node(object):
    def __init__(self,data):
        self.data =data
        self.next =None

    def __str__(self):
        return str(self.data)

class LinkedList(object):
    def __init__(self):
        self.head = None
        #self.size =0

    def append(self,data):
        if not self.head:
            n = Node(data)
            self.head = n
            return
        else:
            n = self.head
            while n.next!=None:
                n=n.next

            newnode =Node(data)
            n.next=newnode

            return


    def printList(self):
        n = self.head
        while n:
            print str(n),"->"
            n = n.next

    def list_size(self):
        n =self.head
        size1=1
        while n.next:
            n=n.next
            size1 += 1
        return size1

    def reverse_list(self):
        current =self.head
        prev =None
        while current != None:
            next=current.next
            current.next=prev
            prev =current
            current =next
        self.head =prev
        return

    def  remove_list(self,position):
        pass


    def detect_loop(self):
        first_pointer =self.head
        second_pointer =self.head

        while(first_pointer.next  and first_pointer  and second_pointer):
                first_pointer = first_pointer.next.next
                second_pointer = second_pointer.next
                if (first_pointer == second_pointer):

                    return True






    def search_list(self,data):

        n=self.head

        while n:
            if n.data == data:
                return True
            n = n.next

        return False


    def middle_number(self):
        fast_pointer =self.head
        slow_poninter=self.head

        if (self.head!=None):
            while (fast_pointer !=None and fast_pointer.next !=None):
                fast_pointer=fast_pointer.next.next
                slow_poninter=slow_poninter.next
            return slow_poninter.data


k = LinkedList()

k.append(20)
k.append(4)
k.append(15)



k.printList()
#print "size",k.list_size()

#print "middle number is ",k.middle_number()



k.head.next.next.next = k.head
print k.detect_loop()

#print k.detect_loop()
#k.reverse_list()
#print k.printList()


