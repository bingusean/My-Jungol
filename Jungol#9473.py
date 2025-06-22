def func(A, B, C, D, E, F, G, H, I, J):
    L = [A, B, C, D, E, F, G, H, I, J]
    return abs(A) + abs(B) + abs(C) + abs(D) + abs(E) + abs(F) + abs(G) + abs(H) + abs(I) + abs(J)
K, L, M, N, O, P, Q, R, S, T = map(int, input().split())
print(func(K, L, M, N, O, P, Q, R, S, T))