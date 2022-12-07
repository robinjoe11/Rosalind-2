def liverabbits(months,k):
    F1 = 1
    F2 = 1
    for i in range(months-2):
        F3 = F1*k+F2
        F1 = F2
        F2 = F3
    return F3


with open('rosalind_fib.txt','r') as file:
    content = file.read()
n,k = content.split(' ')
print(liverabbits(int(n),int(k)))