class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # map units -> # of boxes
        tally = {}
        for b, u in boxTypes:
            if u in tally:
                tally[u]+= b
            else:
                tally[u] = b
        
        # sort units from least to greatest
        units = list(tally.keys())
        units.sort()
        
        # we ultimately want to use boxes with the BIGGEST units first
        total = 0
        while len(units) > 0:
            # get biggest unit and box count
            u = units.pop()
            b = tally[u]
            
            # calculate the # of boxes that can be stored
            used = min(truckSize, b)
            if used < 1:
                # if noboxes were used -> no capacity left
                break
            
            # decrease capacity and increase units
            truckSize-= used
            total+= used*u
                
        return total
        
