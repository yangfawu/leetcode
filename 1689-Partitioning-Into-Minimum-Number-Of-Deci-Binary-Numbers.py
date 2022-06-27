class Solution:
    def minPartitions(self, n: str) -> int:
        # for 1 digit, its value determine the # of 1s you need
        
        # for k digits, you can solve each digit independently
        # AND then merge them into a deci-binary numbers
        # (MEANS you can represent any # with a set of DB #s)
        
        # you should never need more than 10 DB #s
        # the max in fact is the biggest digit value
        # we can always use 0 as a digit in a DB # when we don't need a 1
        
        best = 0
        for c in n:
            best = max(best, int(c))
        return best
