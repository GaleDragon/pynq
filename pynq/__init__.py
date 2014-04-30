import itertools

class Pynq (object):
    def _convert(self, x):
        if isinstance(x, list):
            return List(x)
        elif isinstance(x, dict):
            return Group(x)
        elif isinstance(x, str):
            return String(x)
        else:
            return x
    
    def select(self, fn):
        l = List([fn( self._convert(x) ) for x in self])
        return l
        
    def group(self, fn):
        # [k for k, g in groupby('AAAABBBCCDAABBB')] --> A B C D A B
        # [list(g) for k, g in groupby('AAAABBBCCD')] --> AAAA BBB CC D
        # { g1 : (), g2 : () }
        ret = Group()
        for x in self:
            r = fn( self._convert(x) )
            if r not in ret.keys():
                ret[r] = List([ self._convert(x) ])
            else:
                ret[r].append( self._convert(x) )
        return ret
    
    def aggregate(self, fn):
        pass
    
    def sum(self, fn):
        s = 0
        for x in self:
            s += fn(x)
        return s
    
    def average(self, fn):
        s = sum( self._convert([ fn(x) for x in self ]) )
        return s / len(self)
        
    def __getattr__(self, name):
        self = self._convert(self)
        super.__getattr__(name)
        
class List (list, Pynq):
    def __init__(self, *args, **kwargs):
        if len(args) == 0:
            pass
        elif isinstance(args[0], list):
            for a in args[0]:
                self.append(a)
                
class Group (dict, Pynq):
    def __init__(self, *args, **kwargs):
        if len(args) == 0:
            pass
        elif isinstance(args[0], dict):
            for a in args[0]:
                self[args[0]] = args[0][a]
                
class String (str, Pynq):
    def __init__(self, *args, **kwargs):
        if len(args) == 0:
            pass
        elif isinstance(args[0], str):
            for a in args[0]:
                self += a
                
                
                
                
                
                