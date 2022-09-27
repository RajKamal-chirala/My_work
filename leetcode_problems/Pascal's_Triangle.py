class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n = numRows
        
        output = []
        
        if n == 1:
            output.append([1])
        elif n == 2:
            output.append([1])
            output.append([1,1])
        else:
            output.append([1])
            output.append([1,1])
            i = 1
            while i < n-1:
                sum = 0
                res = []
                res.append(1)
                l = len(output[i])
                for j in range(l):
                    if j == l-1:
                        res.append(1)
                    else:
                        sum = output[i][j] + output[i][j+1]
                        res.append(sum)
                output.append(res)
                i+=1
        return output