def cykMemo(G, w, i, j, T):
    if T[i, j]:
        return T[i, j]
    elif i == j:
        for r in G:
            if r.endswith(w[i]) and r[0] not in T[i, j]:
                T[i, j].append(r[0])
    else:
        for k in range(i, j):
            for a in cykMemo(G, w, i, k, T):
                for b in cykMemo(G, w, k+1, j, T):
                    for r in G:
                        if r.endswith(a+b) and r[0] not in T[i, j]:
                            T[i, j].append(r[0])
    return T[i, j]


def cykMemoMain(G, S, w):
    dict = {}
    for x in range(0, len(w)):
        for y in range(x, len(w)):
            dict[x,y] = []
    v = cykMemo(G, w, 0, len(w) - 1, dict)
    print w, v
    if S in v:
        print "T"
        return True
    else:
        print "F"
        return False


# main
G = ["S->AB", "S->BC", "A->AB", "A->a", "B->CC", "B->b", "C->AB", "C->a"]

s1 = "baaba"
s2 = "abbba"
s3 = "aababaababaababaaba"
s4 = "abaaababaaabbaaba"

cykMemoMain(G, "S", s1)
cykMemoMain(G, "S", s2)
cykMemoMain(G, "S", s3)
cykMemoMain(G, "S", s4)
