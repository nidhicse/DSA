# Complete the printLinkedList function below.

#
# For your reference:
#
# SinglyLinkedListNode:
#     int data
#     SinglyLinkedListNode next
#
#
def printLinkedList(head):
    ptr=head
    while(ptr!=None):
        print(ptr.data)
        ptr=ptr.next
        
        
        
