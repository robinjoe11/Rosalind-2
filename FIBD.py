
def mortalfibonacci(n,k):
    s = [0]*(k+1)
    s[0] = 1

    for i in range(1,n):
        s[1:k+1] = s[0:k]
        s[0] = sum(s[2:])
     
    return sum(s[:-1])

print (mortalfibonacci(96,18))