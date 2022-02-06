from cmath import sqrt
from spot import Spot

class Heuristics:
    TYPES = ["manhattan","euclidean", "diagonal"]

    def __init__(self, type: str) -> None:
        if type not in Heuristics.TYPES:
            self.name = "manhattan"
        else:
            self.name = type

    def manhattan(x1,x2,y1,y2):
        return abs(x1 - x2) + abs(y1 - y2)
    
    def euclidean(x1,x2,y1,y2):
        distance = sqrt((x1 - x2)**2 + (y1 - y2)**2).real
        return distance
    
    def diagonal(x1,x2,y1,y2):
        dx = abs(x1 - x2)
        dy = abs(y1 - y2)
        return abs(dx - dy) + min(dx,dy) * sqrt(2).real
    
    def compute_distance(self, p1: Spot, p2: Spot):
        x1, y1 = p1.get_pos()
        x2, y2 = p2.get_pos()
        
        if self.name == "manhattan ":
            return Heuristics.manhattan(x1,x2,y1,y2)
        
        if self.name == "euclidean":
            print("euclidean")
            return Heuristics.euclidean(x1,x2,y1,y2)
        
        else:
            return Heuristics.diagonal(x1,x2,y1,y2)
