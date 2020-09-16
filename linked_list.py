class Node:
    def __init__(self,content):
        self.content=content
        self.next=None

class list:
    def __init__(self):
        self.head=None

    def printl(self):
        tempo=self.head
        while(tempo):
            print(tempo.content)
            tempo=tempo.next    
    

    def add_front(self):
        print("Enter data to be inserted")
        content=input()
        new_node=Node(content)
        if self.head==None:
            self.head=new_node
            return self.head
        
        else:
            new_node.next=self.head
            self.head=new_node
            return self.head
    

    def add_back(self):
        print("Enter data to be inserted")
        content=input()
        new_node=Node(content)
        if self.head==None:
            self.head=new_node
            return self.head

        else:
            tempo=header.head
            while(tempo.next!=None):
                tempo=tempo.next
            tempo.next=new_node
            return self.head

    def delete_front(self):
        if self.head==None: 
            print("List is already empty")
            return header
        else:
            tempo=self.head
            self.head=self.head.next
            tempo=None
            print("Deleted Successfully")
            return self.head

    def delete_back(self):
        if self.head==None:
            print("Nothing to delete") 
            return header
        else:
            tempo=self.head
            pre=None
            while(tempo.next==None):
                pre=tempo
                tempo=tempo.next
            pre.next=None
            tempo=None
            print("Deleted Successfully")
            return self.head    



if __name__=="__main__":

    header=list()
    
    header=header.delete_back()
    header=header.delete_front()