#Fibonacci using class with an interator

import time
class fiboneitor():

    def __init__(self, maxnumb):
        self.maxnumb = maxnumb
    
    def __iter__(self):
        self.n1 = 0
        self.n2 = 1
        self.counter = 0
        return self
    
    def __next__(self):
        if self.counter == 0 :
            self.counter += 1 
            return self.n1
        elif self.counter == 1 :
            self.counter += 1 
            return self.n2
        else:
            if self.counter < self.maxnumb:
                self.aux = self.n1 + self.n2
                self.n1 , self.n2 = self.n2 , self.aux
                self.counter = self.aux
                return self.aux
            else:
                raise StopIteration
if __name__ == '__main__':
    fiboneador= fiboneitor(150)
    for elements in fiboneador:
        print(elements)
        time.sleep(0.5)

