#
from src.coin import Coin

class Experiment:
    
    def p_2_heads(self, cnt =100_000):
        results = []
        c = Coin()
        for i in range(cnt):      
            results.append((c.flip(),c.flip()))  
        return (results.count(('H','H')) / cnt)
        

    def p_pattern(self, patt, cnt =100_000):
        flip_cnt = len(patt)
        t_patt = list(patt)
        #print(t_patt)
        results = []
        c = Coin()
        for i in range(cnt):
            flips = [] 
            for i in range(flip_cnt):
                flips.append(c.flip()) 
            results.append(flips)
        return (results.count(t_patt) / cnt)
       