with open('rosalind_lcsm.txt','r') as file:
    s = file.read()
    s = s.split(">")[1:]
    
for i in range(len(s)):
    s[i] = s[i].replace("\n", '')
    while s[i][0] not in "ACGT":
        s[i] = s[i][1:]


index = s.index(min(s, key=len))

motif = 'A'
shortest = s[index]


for i in range(len(shortest)):
    n = 0
    present = True
    while present:
           
        for each in s:
            if shortest[i:i+n] not in each or n>1000:
                present = False
                break
        if present:
            motif = max(shortest[i:i+n], motif, key=len)
        n += 1


print (motif)