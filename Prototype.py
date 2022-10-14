
from abc import ABCMeta, abstractstaticmethod
import copy

class IPrototype(metaclass=ABCMeta):
    """Interface para o metodo clone"""
    @abstractstaticmethod
    def clone():
        """"""

class ConcreteClass1(IPrototype):

    def __init__(self, i=0, s="", l=[], d={}):
        self.i = i
        self.s = s
        self.l = l
        self.d = d

    def clone(self):
        return type(self)(
            self.i,
            self.s,
            self.l.copy(),
            self.d.copy())

    def __str__(self):
        return f"{id(self)}\ti={self.i}\ts={self.s}\tl={self.l}\td={self.d}"


class ConcreteClass2(IPrototype):

    def __init__(self, i=0, s="", l=[], d={}):
        self.i = i
        self.s = s
        self.l = l
        self.d = d

    def clone(self):
        return type(self)(
            self.i,
            self.s,
            copy.deepcopy(self.l),
            copy.deepcopy(self.d))

    def __str__(self):
        return f"{id(self)}\ti={self.i}\ts={self.s}\tl={self.l}\td={self.d}"

if __name__ == '__main__':
    objeto1 = ConcreteClass2(1, "objeto1", [1,2,3], {"a":1 , "b":2, "c":3})
    print(objeto1)
    objeto2 = objeto1.clone()
    print(objeto2)