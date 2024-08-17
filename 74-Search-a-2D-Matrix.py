class Solution(object):
    def searchMatrix(self, matrix, target):
        \\\
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        \\\
        L,R= 0, len(matrix)-1
        while L<=R:
            mid= (L+R)//2
            if matrix[mid][-1]<target:
                L=L+1
            elif matrix[mid][-1]>target:
                R=R-1
            else:
                return True

        L1,R1=0, len(matrix[0])-1
        while L1<=R1:
            midrow= (L1+R1)//2
            if matrix[mid][midrow]<target:
                L1=L1+1
            elif matrix[mid][midrow]>target:
                R1=R1-1
            else:
                return True
        return False
