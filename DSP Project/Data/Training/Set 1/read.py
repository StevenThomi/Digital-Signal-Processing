def readFile(file):
    data = []

    infile = open(file,"r")
    s = infile.read()

    numbers = [eval(x) for x in s.split()]
    for number in numbers:
        data.append(number)

    infile.close() # Close the file
    return data

music_nv_1_freq = readFile('P1_4.txt')
print(music_nv_1_freq)
