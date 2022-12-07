
def count_mutations (filename):

    data = open('rosalind_hamm.txt', "r")

    dataset = data.read().splitlines()

    firststring = dataset[0]

    secondstring = dataset[1]

    count = 0
    for i in range(len(firststring)):
        if firststring[i] != secondstring[i]:
            count +=1

    return count



filename = "rosalind_hamm.txt"
print (count_mutations (filename))