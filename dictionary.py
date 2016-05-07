name = raw_input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
lis = list()
for line in handle:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    for word in words:
        lis.append(word)

counts = dict()
for word in lis:
    counts[word] = counts.get(word,0) + 1
bigcount = None
bigword = None
for word,count in counts.items():
    if '@' not in word: continue
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
print bigword, bigcount