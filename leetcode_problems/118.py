
class Solution:
    def generate(self, numRows):
        '''
        matrix = Prepare a matrix of numRows * numRows

        then iterate for each row
            then iterate each col
                fill it using the (col-1 row-1) + (row-1, col)

        print(matrix)
        '''
        if numRows != 0:
            numRows = numRows+1
            matrix = [[0 for _ in range(numRows)] for _ in range(numRows)]

            for i in range(1, numRows):
                for j in range(1, numRows):
                    if i == j:
                        matrix[i][j] = 1
                    else:
                        matrix[i][j] = matrix[i-1][j-1] + matrix[i-1][j]
            matrix = [[i for i in X if i != 0] for X in matrix]
            return [ele for ele in matrix if ele != []]
        else:
            return [0]

s = Solution()
print(s.generate(0))
