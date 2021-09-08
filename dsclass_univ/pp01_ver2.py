class Matrix:

    def __init__(self,a,b,c,d):
       self.a=a
       self.b=b
       self.c=c
       self.d=d

    def __add__(self,B):
          
        return Matrix(self.a+B.a,self.b+B.b,self.c+B.c,self.d+B.d)

    def __sub__(self,B):
        return Matrix(self.a-B.a,self.b-B.b,self.c-B.c,self.d-B.d)

    def __str__(self):
        return str(self.a)+' '+str(self.b)+'\n'+str(self.c)+' '+str(self.d)

if __name__ == "__main__":
    A = Matrix(1, 2, 3, 4)
    B = Matrix(5, 6, 7, 8)
    C = A+B
    D = A-B
    print(C)
    print(D)
    
