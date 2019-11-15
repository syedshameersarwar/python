class Stack(object):
    def __init__(self):
        self.items = []
    def is_empty(self):
        return self.items==[]
    def push(self,value):
        self.items.append(value)
    def pop(self):
        if self.size()==0:
            return None
        return self.items.pop()
    def peek(self):
        if self.size()==0:
            return None
        return self.items[-1]
    def size(self):
        return len(self.items)
    def __str__(self):
        exp = "["
        for i in range(self.size()):
            if i==self.size()-1:
                exp +=str(self.items[i]) + "]"
            else:
                exp +=str(self.items[i])+ ","  #patch for idle otherwise this expression is enough 
        return exp
        

def precedence(operator):
    if operator == '+' or operator == '-':
        return 1
    elif operator == '/' or operator == '*':
        return 2
    elif operator == '^':
        return 3
    else:
        return 0


def isoperator(operator):
    if operator == '+' or operator == '-' or operator == '/' \
       or operator == '*' or operator == '^' :
           return True
    return False


def infixtopostfix(infix):
    s = Stack()
    postfix = ""
    s.push("(")
    infix += ")"
    for char in infix:
        if char.isdigit() or char.isalpha():
            postfix+= char
        elif char == "(":
            s.push(char)
        elif isoperator(char):
            while precedence(char)<=precedence(s.peek()):
                postfix += str(s.pop())
            s.push(char)
        elif char == ")":
            while s.peek()!= "(":
                postfix += str(s.pop())
            s.pop()
    if s.is_empty():
        return postfix


def infixtoprefix(infix):
    infix_reverse = infix[::-1]       #reverse postfix expression
    for i in range(len(infix_reverse)):   #replace ( with ), and ) with (
        if infix_reverse[i] == '(':
            infix_reverse = infix_reverse[:i] + ')' + infix_reverse[i+1:]
        elif infix_reverse[i] == ')':
            infix_reverse = infix_reverse[:i] + '(' + infix_reverse[i+1:]
    postfix = infixtopostfix(infix_reverse) #convert to postfix
    prefix = postfix[::-1]  #reverse postfix to get prefix
    return prefix


def eval_postfix(postfix):
    s = Stack()
    postfix += ")"
    for char in postfix:
        if char.isdigit():
            s.push(char)
        elif isoperator(char):
            A = s.pop()
            B = s.pop()
            s.push(eval(str(B)+char+str(A)))
    result = s.pop()
    return result

print(infixtoprefix("(a-b/c)*(a/k-l)"))  #test for prefix
print(infixtopostfix("( A + B ) * ( C + D )")) #test for postfix
print(eval_postfix("7 8 + 3 2 + /")) #test for postfix evaluation
    
