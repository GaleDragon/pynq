import itertools

class Pynq (object):
    def select(self, fn):
        return [fn(x) for x in self]
        
    def group(self, fn):
        # [k for k, g in groupby('AAAABBBCCDAABBB')] --> A B C D A B
        # [list(g) for k, g in groupby('AAAABBBCCD')] --> AAAA BBB CC D
        # { g1 : (), g2 : () }
        ret = {}
        for x in self:
            r = fn(x)
            if r not in ret.keys():
                ret[r] = [x]
            else:
                ret[r].append(x)
        return ret
    
    def aggregate(self, fn):
        pass
    
    def sum(self, fn):
        s = 0
        for x in self:
            s += fn(x)
        return s
    
    def average(self, fn):
        pass
        
class List (list, Pynq):
    def __init__(self, *args, **kwargs):
        if isinstance(args[0], list):
            for a in args[0]:
                self.append(a)