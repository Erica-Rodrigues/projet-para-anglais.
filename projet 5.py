A = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
L = list(str.lower("Fhfl hvw xqh sduwlh gx whawh, iéolflwdwlrqv."))
i = 0
d = 1
nt = ""
while d < len(A):
    while i < len(L):
        if L[i] in A:
            nl = A.index(L[i]) - d
            nt += A[nl]
        else :
            nt += L[i]
        i = i + 1
    input(nt)
    i = 0
    d = d + 1
    nt = ""

