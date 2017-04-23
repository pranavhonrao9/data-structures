class Node:
    # Constructor to create a new node
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


# Class to create a Doubly Linked List
class DoublyLinkedList:
    # Constructor for empty Doubly Linked List
    def __init__(self):
        self.head = None

    # Given a reference to the head of a list and an
    # integer,inserts a new node on the front of list
    def push(self, data):


        new_node = Node(data)

        if self.head is None:
            self.head=new_node


        self.head.prev=new_node

        new_node.next=self.head

        self.head=new_node



        # 1. Allocates node
        # 2. Put the data in it

        '''
        new_node = Node(new_data)

        # 3. Make next of new node as head and
        # previous as None (already None)
        new_node.next = self.head

        # 4. change prev of head node to new_node
        if self.head is not None:
            self.head.prev = new_node

        # 5. move the head to point to the new node
        self.head = new_node
        '''

    # Given a node as prev_node, insert a new node after
    # the given node
    def insertAfter(self, prev_node, new_data):

        # 1. Check if the given prev_node is None
        if prev_node is None:
            print 'thats not fair'
            return
        new_node = Node(new_data)

        new_node.next= prev_node.next

        prev_node.next=new_node

        new_node.prev=prev_node

        if new_node.next is not None:
            new_node.next.prev=new_node

    def delete_node(self,dele):


        if self.head is None or dele is None:
            return

        if self.head == dele:
            self.head =dele.next

        if dele.next is not None:
            dele.prev.next =dele.next

        if dele.prev is not None:
            dele.next.prev = dele.prev


    def append(self, new_data):


        new_node = Node(new_data)
        new_node.next = None
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return


        last = self.head
        while (last.next is not None):
            last = last.next


        last.next = new_node


        new_node.prev = last

        return


    def printList(self, node):

        print "\nTraversal in forward direction"
        while (node is not None):
            print " %d" % (node.data),
            last = node
            node = node.next

        print "\nTraversal in reverse direction"
        #while (last is not None):
         #   print " %d" % (last.data),
          #  last = last.prev



    def  adjcent_number(self,node1,node2):
        n=self.head

        if n is None:
            return
        elif n.data ==node1:
            if n.next.data==node2 :
                return True
            else:
                return False
        else:
            while n.next !=None:
                if n.data == node1 and n.next.data == node2:
                    tmp= (n.data + n.next.data)/2
                    extra = Node(tmp)
                    n.prev.next=extra
                    extra.next = n.next.next
                    extra.prev = n.prev
                    n=extra







                    return

                else:
                    n = n.next






llist = DoublyLinkedList()


llist.append(6)


llist.push(17)


llist.push(1)


llist.append(4)


llist.insertAfter(llist.head.next, 18)

print "Created DLL is: ",
llist.printList(llist.head)
print llist.adjcent_number(17,18)

llist.printList(llist.head)


