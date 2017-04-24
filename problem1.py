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
    print dict[0, len(w)-1]
    if S in dict[0, len(w)-1]:
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

cykDP(G, "S", s1)
cykDP(G, "S", s2)
cykDP(G, "S", s3)
cykDP(G, "S", s4)


