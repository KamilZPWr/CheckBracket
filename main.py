class Stack:
    def __init__(self):
        self.items=[]

    def isEmpty(self):
        return len(self.items)==0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

def parChcecker(fileAddress):

    file = open(fileAddress)
    try:
        kodHTML = file.read()
    finally:
        file.close()

    s = Stack()
    index = 0
    balanced = True

    while (index<len(kodHTML)):
        sign = kodHTML[index]
        if (sign == "{" or sign == "[" or sign == "<" or sign == "("):
                s.push(sign)
        elif (sign == "}" or sign == "]" or sign == ">" or sign == ")"):
            a=s.pop()
            a=ord(a)
            n_sign = ord(sign)

            if (n_sign-a==2 or n_sign-a==1):
                balanced = True
            else:
                balanced = False
        index=index+1

    if balanced==s.isEmpty()==True:
        return True
    else:
        return False

print(parChcecker('html_file'))
            
        
               
       
