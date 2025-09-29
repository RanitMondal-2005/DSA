# basic queue _ list implementation
class Queue:
    def __init__(self):
        self.l=[]
        
    def enqueue(self,num): # PUSH
        self.l.append(num)
    def dequeue(self): # DELETE
        if len(self.l)==0:
            return -1 # no element
        return self.l.pop(0)
    def get_front(self):
        if len(self.l)==0:
            return -1 # no element
        return self.l[0]
    def get_rear(self):
        if len(self.l)==0:
            return -1 # no element
        return self.l[-1]
    def length(self):
        x=len(self.l)
        return x
    def display(self):
        if len(self.l)==0:
            return-1
        print(self.l)
if __name__=="__main__":
    q1 = Queue()
    q1.enqueue(2)
    q1.enqueue(5)
    q1.enqueue(7)
    q1.display()       # [2, 5, 7]
    print(q1.dequeue()) # 2
    q1.display()       # [5, 7]
    print(q1.get_front()) # 5
    print(q1.get_rear())  # 7
    print(q1.length())    # 2