'''
    A simple implementation of a stack data structure
'''
class stack(object):
   
    def __init__(self) -> None:
        self.stk = []

    def size(self):
        return len(self.stk)

    def stk_push(self, item):
        self.stk.append(item)

    def stk_pop(self):
        return self.stk.pop(-1)            
        
    def stk_top(self):
        return self.stk[-1]

    def print_stack(self):
        print("Stack:")
        for i in range (len(self.stk)):
            print(self.stk[-1-i])


class queue(object):
   
    def __init__(self) -> None:
        self.q = []

    def size(self):
        return len(self.q)

    def q_enque(self, item):
        self.q.append(item)

    def q_deque(self):
        return self.q.pop(0)            
        
    def q_front(self):
        return self.q[0]

    def print_q(self):
        print("Queue:")
        for i in range (len(self.q)):
            print(self.q[i], end = " ... ")
        print("")


myQ = queue()            

myQ.q_enque(1)
myQ.q_enque(2)
myQ.q_enque(3)
myQ.q_enque(4)
myQ.q_enque(5)
myQ.q_enque(6)

myQ.print_q()
print("front: ",myQ.q_front())
print("Dequed: ",myQ.q_deque())
print("Dequed: ",myQ.q_deque())
myQ.print_q()
