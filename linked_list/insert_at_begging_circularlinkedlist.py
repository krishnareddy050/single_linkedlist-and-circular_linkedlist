class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def circular(head,x):
    temp = Node(x)
    if head == None:
        temp.next = temp
        return temp
    curr = head
    while curr.next != head:
        curr = curr.next

    curr.next = temp
    temp.next = head
    return temp
    
    




def printCircular(head):
    if head == None:
        return
    print(head.data, end=" ")
    curr = head.next
    while curr != head:
        print(curr.data, end=" ")
        curr = curr.next

    print() 


    
    
    
    
    
    

   
    





head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = head




head=circular(head,25)   

printCircular(head)   


