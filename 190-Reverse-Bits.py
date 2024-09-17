class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        a=0
        for i in range(32):
            if (n>>i)&1==1:
                a+=(2**(31-i))
        return a
        