class Calculator():
    def __init__(self,first,second,operation):
        self.first = first
        self.second = second
        self.operation = operation

    def calc(self):
        if (self.operation == '+'):
            return(self.first + self.second)
        if (self.operation == '-'):
            return(self.first - self.second)
        if (self.operation == '*'):
            return(self.first * self.second)
        if self.second == 0 and self.operation == '/':
            return("на ноль делить нельзя")
        elif (self.operation == '/'):
            return(self.first / self.second)


