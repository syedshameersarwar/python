def check_precedence(v1,v2):
    precedence=['-','+','/','*','^']
    for i in range(len(precedence)):
        if precedence[i] is v1:
            count1=i
        if precedence[i] is v2:
            count2=i
    if count1 > count2:
        return True
    else:
        return False
class stack:
    def __init__(self):
        self.stlist=[]
        self.top=-1
    def push(self,data):
        self.stlist.append(data)
        self.top+=1
    def pop(self):
        self.top-=1
        item=self.stlist.pop()
        return item
    def peak(self):
        return self.stlist[self.top]
    def empty(self):
        count=0
        for y in self.stlist:
            count+=1
        if count is 0:
            return True
        else:
            return False
    def display(self):
        for i in self.stlist:
            print(i,end=' ')
        print()
class infix_to_postfix:
    def __init__(self,expression="0"):
        self.exp=expression
        self.operator=stack()
        self.operand=stack()
    def check_exp(self):
        lenofexp=len(self.exp)
        for i in self.exp:
            lenofexp-=1
            res=i.isalpha()
            if i is '(':
                continue
            elif res is True:
                self.operand.push(i)
            elif res is False and i is not '(' and i is not ')':
                if self.operator.empty() is True:
                    self.operator.push(i)
                elif self.operator.empty() is False:
                    if check_precedence(i,self.operator.stlist[self.operator.top]):
                        self.operator.push(i)
                    else:
                        while self.operator.empty() is False:
                            self.operand.push(self.operator.pop())
                        self.operator.push(i)
            elif i is ')':
                if self.operator.empty() is False:
                    self.operand.push(self.operator.pop())
        if self.operator.empty() is False and lenofexp is 0:
            while self.operator.empty() is False:
                self.operand.push(self.operator.pop())
    def print_exp(self):
        print("Infix : ",self.exp)
        print("Postfix: ",end=' ')
        for x in self.operand.stlist:
            print(x,end='')
        print()
#expression=input("Enter the expression: ")
expression=("A+(B*C -(D/E^F)*G)*H)")
intopost=infix_to_postfix(expression)
intopost.check_exp()
intopost.print_exp()
