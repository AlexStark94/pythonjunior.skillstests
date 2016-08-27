import sys

def test():
    vowels = ['a','A','á','e','E','é','i','I','í','o','O','ó','u','U','ú']
    file = open(str(sys.argv[1]),'r')
    line = file.readline().strip('\n')
    cont = 0
    vocal = False
    with3consonants = []
    while (line != ''):
        for i in range(len(line)):
            for j in range(len(vowels)):
                if line[i] == vowels[j]:
                    vocal = True
            if not vocal:
                cont+=1
            else:
                vocal = False
        if (cont >= 3):
            with3consonants.append(line)
        cont = 0
        line = file.readline().strip('\n')
    file.close()
    print(with3consonants)

test()
