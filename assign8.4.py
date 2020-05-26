fh=open('mbox-short.txt')
for line in fh:
    line=line.rstrip()
    print('Line:',line)
    wd=line.split()
    print('words:',wd)
    if len(wd)<3:
        continue
    if wd[0]!='From':
        continue
    print(wd[2])
