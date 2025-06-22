def f(A, B):
    L = [abs(A), abs(B)]
    if max(L) == abs(A):
        return A
    elif max(L) == abs(B):
        return B
def u(C, D):
    M = [abs(C), abs(D)]
    if min(M) == abs(C):
        return C
    elif min(M) == abs(D):
        return D
I1, I2 = list(map(int, input().split()))
J1, J2 = list(map(float, input().split()))
print(f(I1, I2))
print(u(J1, J2))