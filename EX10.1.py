dic_address = dict()
lst = list()
fname = input('Enter file name ')
fname = open(fname)


for line in fname:
    words = line.split()
    if len(words) < 2 or words[0] == 'From':
        continue
    if words[1] not in dic_address:
        dic_address[words[1]] = 1
    else:
        dic_address[words[1]] += 1

for key, val in list(dic_address.items()):
    lst.append((val, key))
    lst.sort(reverse = True)
for count, email in lst[:1]:
    print(key,val)

