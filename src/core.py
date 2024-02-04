import functools
import inspect



class Cons:
    __match_args__ = ("head", "rest")
    def __init__(self, value, other):
        self.value = value
        self.other = other
        if not isinstance(self.other, Linked):
            raise TypeError("Not of Linked type")  
class Empty: 
    pass 

Linked = Cons | Empty


def head(lst): 
    if isinstance(lst, Linked):
        if isinstance(lst, Cons):
            return lst.value
        else: 
            ## adding templating here
            raise TypeError("lst is empty") 
    else:
        raise TypeError("Not of the linked type")
    
def tail(lst): 
    if isinstance(lst, Linked):
        if isinstance(lst, Cons):
            return lst.other
        else: 
            ## adding templating here
            raise TypeError("lst is empty") 
    else:
        raise TypeError("Not of the linked type")


## need to use match_args for pattern, matching I can probably use this as real pattern mattern a la FP
def map(func, linked):
    if isinstance(linked, Linked):
        match linked: 
            case Cons(head, rest): 
                return Cons(func(head), map(func, rest))
            case Empty(): 
                return Empty()
    else:
        raise TypeError("Not a Linked type")

### this is for code introspection stuff
def is_lambda_function(func):
    return (
        inspect.isfunction(func)
        and func.__name__ == '<lambda>'
        and func.__code__.co_argcount > 0
        and func.__code__.co_filename == '<string>'
    )


## adding arithmetic function primitives to s.py 
def add(*args):
    return sum(args) 


def mul(*args): 
    return functools.reduce(lambda x, y: x * y, args)



## the crux of what is happening
class S:
    def __init__(self, func, *args):
        self.func = func
        self.args = args

    def __call__(self):
        evaluated_args = [arg() if isinstance(arg, S) else arg for arg in self.args]
        #lambdas = [arg() for arg in self.args if is_lambda_function(arg)]
        return self.func(*evaluated_args)

# Example usage:
    

result = S(mul, S(add, 2, 2, 3), 5)()
print(result)  # Output: 20

#new_result = S(mul, lambda x: x, 2)()$

#print(new_result) 

lst_example = Cons(3, Empty())

print(lst_example)
print(head(lst_example))
print(isinstance(lst_example))
