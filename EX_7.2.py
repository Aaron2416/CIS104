fname = input("Enter file name:")
try:
    if fname == "na na boo boo":
        print("NA NA BOO BOO TO YOU - You have been punk'd!")
        quit()

        fh = open(fname)
except FileNotFoundError:
    print("File not found")
    quit()
fh = open(fname)
count = 0
total = 0
for line in fh:
    if line.startswith("X-DSPAM-Confidence:"):
            count = count + 1
    for line in fh:
        if line.startswith("X-DSPAM-Confidence:"):
            line = float(line[21:])
            total = line + total
            average = total / count
print("Average spam confidence:",average)
