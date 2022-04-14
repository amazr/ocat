class Seq:
    def __init__ (self, id, statements):
        self.id = id
        self.statements = statements

    def __repr__ (self):
        return  f"{type(self).__name__}({self.id}, {self.statements})"
        
class Declare:
    def __init__ (self, type, assignment):
        self.type = type
        self.assignment = assignment
    
    def __repr__ (self):
        return f"{type(self).__name__}({self.type}, {self.assignment})"

class Assign:
    def __init__ (self, name, expr):
        self.name = name
        self.expr = expr

    def __repr__ (self):
        return f"{type(self).__name__}({self.name}, {self.expr})"

class Name:
    def __init__ (self, name):
        self.name = name
    
    def __repr__ (self):
        return f"{type(self).__name__}({self.name})"

class Number:
    def __init__ (self, value):
        self.value = value
    
    def __repr__ (self):
        return f"{type(self).__name__}({self.value})"

class Type:
    def __init__ (self, type):
        self.type = type
    def __repr__ (self):
        return f"{type(self).__name__}({self.type})"

class BinOp:
    def __init__ (self, left, right):
        self.left = left
        self.right = right
    
    def __repr__ (self):
        return f"{type(self).__name__}({self.left}, {self.right})"

class Add (BinOp):
    pass

class Sub (BinOp):
    pass

class Mult (BinOp):
    pass

class Div (BinOp):
    pass

class UnaryOp:
    def __init__ (self, node):
        self.node = node
    
    def __repr__ (self):
        return f"{type(self).__name__}({self.node})"

class UnarySub (UnaryOp):
    pass

class BitwiseNot (UnaryOp):
    pass

class Callable:
    def __init__ (self, name, args):
        self.name = name
        self.args = args

    def __repr__ (self):
        return  f"{type(self).__name__}({self.name}, {self.args})"

class Function (Callable):
    pass

class Procedure (Callable):
    pass