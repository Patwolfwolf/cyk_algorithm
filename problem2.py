def cykRec(G, w, i, j):
    set = []
    if i == j:
        for r in G:
            if r.endswith(w[i]) and r[0] not in set:
                set.append(r[0])
    else:
        for k in range(i, j):
            for a in cykRec(G, w, i, k):
                for b in cykRec(G, w, k+1, j):
                    for r in G:
                        if r.endswith(a+b) and r[0] not in set:
                            set.append(r[0])
    return set


def cykRecMain(G, S, w):
    v = cykRec(G, w, 0, len(w) - 1)
    print w, v
    if S in v:
        print "T"
        return True
    else:
        print "F"
        return False


#main
G = ["S->AB", "S->BC", "A->AB", "A->a", "B->CC", "B->b", "C->AB", "C->a"]

s1 = "baaba"
s2 = "abbba"
s3 = "aababaababaababaaba"
s4 = "abaaababaaabbaaba"

cykRecMain(G, "S", s1)
cykRecMain(G, "S", s2)
cykRecMain(G, "S", s3)
cykRecMain(G, "S", s4)
