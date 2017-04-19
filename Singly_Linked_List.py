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

    def  remove_list_first_element(self):
        n = self.head
        if n is None:
            return
        else:

            self.head=n.next

        return self


    def remove_list(self,key):
        n= self.head
        if n is None:
            return

        while n.next:
            if (n.data==key):
                break
            prev=n
            n=n.next
        #print "previous",prev.next
        #print "next", n.next
        prev.next=n.next
        #print "n",n
        n = None


    def RemoveNode(self, index):
        prev = None
        node = self.head
        i = 0

        while (node.next != None) and (i < index):
            prev = node
            node = node.next
            i += 1

        if prev == None:
            node.next =self.head
        else:
            prev.next = node.next #this line



    def nth_element(self,key):
        n=self.head
        position =0
        while n.next:
            if n.data == key:
                return position
            n =n.next
            position+=1

        return position



    def detect_loop(self):
        first_pointer =self.head
        second_pointer =self.head

        while(first_pointer.next  and first_pointer  and second_pointer):
                first_pointer = first_pointer.next.next
                second_pointer = second_pointer.next
                if (first_pointer == second_pointer):

                    return True




    def search_list_element(self,data):

        n= self.head
        position =0
        while n.next:
            if n.data == data:
                return position
            n = n.next
            position+=1

        return position

    def delete_duplicate_element_sorted_list(self):
        p1 = self.head
        while (p1.next):
            if (p1.data == p1.next.data):
                p1.next =p1.next.next
            else:
                p1 = p1.next

        return self.head






    def sort_list(self):
        pass



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

k.append(10)

k.append(30)


k.append(40)

k.append(105)



#k.printList()
#print "size",k.list_size()

#print "middle number is ",k.middle_number()


#k.RemoveNode(2)
#k.remove_list_last_element()
#k.printList()
#k.delete_duplicate_element_sorted_list()
#k.delete_duplicate_element_sorted_list()
#k.printList()

k.remove_list(40)
k.printList()


#print k.nth_element(15)
#k.head.next.next.next = k.head
#print k.detect_loop()

#print k.detect_loop()
#k.reverse_list()
#print k.printList()


