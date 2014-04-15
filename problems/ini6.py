input = open('input_filename', 'r')
words = input.readline().split()
dict = {}
for word in words:
    if word in dict:
        dict[word] = dict[word] + 1
    else:
        dict[word] = 1
for key, value in dict.iteritems():
    print key + ' ' + str(value)
input.close()