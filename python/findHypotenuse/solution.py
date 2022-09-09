from typing import List
from math import sqrt

class Hypotenuse:
    def findHypotenuse(self, hickA: List[int], hickB: List[int]) -> List[int]:
        hypot = []
        result = 0.0
        if not hickA or not hickB:
            return []
        if len(hickA) == len(hickB):
            for a in range(0, len(hickA)):
                for b in range(0, len(hickB)):
                    if a == b:
                        result=(hickA[a]*hickA[a])+(hickB[b]*hickB[b])
                        hypot.append(sqrt(result))
        else:
            return []
        return hypot

                
