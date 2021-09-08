# Matrix 클래스를 생성합니다.
# 2*2크기라고 가정합니다.
# 두 행렬을 더하고 빼는 함수를 구현합니다.

class Matrix:

    # Matrix class 생성자
    # 2D array에 값을 할당해줍니다.
    def __init__(self, a, b, c, d):
        A = [[0, 0], [0, 0]]
        self.A = [[a, b], [c, d]]

    def __str__(self):
        result = ""
        for i in range(len(self.A)):
            result += str(self.A[0][i]) + " "
        result += "\n"
        for i in range(len(self.A)):
            result += str(self.A[1][i]) + " "
        return result

    # 연산자 오버로딩!!!
    # 1. 덧셈
    def __add__(self, other):
        result = Matrix(0, 0, 0, 0)
        for i in range(len(self.A)):
            for j in range(len(self.A[0])):
                result.A[i][j] = self.A[i][j]+other.A[i][j]
        return result
    
    # 2. 뺄셈
    def __sub__(self, other):
        result = Matrix(0, 0, 0, 0)
        for i in range(len(self.A)):
            for j in range(len(self.A[0])):
                result.A[i][j] = self.A[i][j]-other.A[i][j]
        return result


if(__name__ == "__main__"):
    A = Matrix(1, 2, 3, 4)
    B = Matrix(5, 6, 7, 8)


    C = A+B
    D = A-B

    print(C)
    print("-------------------")
    print(D)
