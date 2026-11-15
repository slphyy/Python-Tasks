def raiz(N, A, E):
    if ((A**2 - N) < E):
        return A
    else:
        return print(f"{N}: {((A**2) + N) / (2*A)}")   

raiz(9, 4, 0.01)
