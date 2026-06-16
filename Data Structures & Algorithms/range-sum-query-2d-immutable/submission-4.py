class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        self.prefix_sum_matrix = [[0]* len(self.matrix[x]) for x in range(len(self.matrix))]
        self.calc_prefixsum_matrix(self.matrix)
        
    def calc_prefixsum_matrix (self,matrix : List[List[int]]):
        self.prefix_sum_matrix[0][0] = self.matrix[0][0]
        matrix_length = len(self.matrix)

        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                top = self.prefix_sum_matrix[i-1][j] if i > 0 else 0
                left = self.prefix_sum_matrix[i][j-1] if j > 0 else 0
                diag = self.prefix_sum_matrix[i-1][j-1] if i > 0 and j > 0 else 0
                self.prefix_sum_matrix[i][j] = matrix[i][j] + top + left - diag



    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        
        total = self.prefix_sum_matrix[row2][col2]
        top = self.prefix_sum_matrix[row1-1][col2] if row1 > 0 else 0
        left = self.prefix_sum_matrix[row2][col1-1] if col1 > 0 else 0
        diag = self.prefix_sum_matrix[row1-1][col1-1] if row1 > 0 and col1 > 0 else 0
        return total - top - left + diag

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)