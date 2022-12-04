fname = input("Enter file:")
if len(fname) < 1 : fname = "mbox-short.txt"
handle = open(fname)
dic = dict()
for lin in handle:
    if "From:" in lin:
        continue
    if "From" in lin:
        w = lin.split()
        hour = w[5].split(":")[0]
        dic[hour] = dic.get(hour,0)+1
fal =sorted([(v,k) for k,v in dic.items()],reverse=True)
lst =list()
for a,b in fal:
    lst.append([b,a])
for a,b in sorted(lst):
    print(a,b)
