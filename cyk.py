# CS301 Assignment 8
# CYK Alogorithm, Dynamic Programming Version
# Ruiwen Fu
# April.1st 2017

#cyk alogorithm
def cykDP(G, S, w):
    dict = {}
    for x in range(0, len(w)):
        for y in range(x, len(w)):
            dict[x,y] = []
    # initialization steps
    i = 0
    for s in w:
        for r in G:
            if s in r[2:] and r[0] not in dict[i, i]:
                dict[i, i].append(r[0])
        i += 1
    # substring of length >= 1
    i = 0
    for l in range(1, len(w)):
        for i in range(0, len(w) - l):
            j = i + l
            for k in range(i, j):
                for a in dict[i, k]:
                    for b in dict[k+1, j]:
                        for r in G:
                            if a+b in r[2:] and r[0] not in dict[i, j]:
                                dict[i, j].append(r[0])
    if S in dict[0, len(w)-1]:
        print "T"
        return True
    else:
        print "F"
        return False

#cyk Recursive
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
    if S in v:
        print "T"
        return True
    else:
        print "F"
        return False


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


#cyk memoization
def cykMemoMain(G, S, w):
    dict = {}
    for x in range(0, len(w)):
        for y in range(x, len(w)):
            dict[x,y] = []
    v = cykMemo(G, w, 0, len(w) - 1, dict)
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
print "Result from cyk algorithm"
cykDP(G, "S", s1)
cykDP(G, "S", s2)
cykDP(G, "S", s3)
cykDP(G, "S", s4)
print "Result from cyk Recursive"
cykRecMain(G, "S", s1)
cykRecMain(G, "S", s2)
cykRecMain(G, "S", s3)
cykRecMain(G, "S", s4)
print "Result from cyk memoization"
cykMemoMain(G, "S", s1)
cykMemoMain(G, "S", s2)
cykMemoMain(G, "S", s3)
cykMemoMain(G, "S", s4)


