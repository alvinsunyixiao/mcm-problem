appendix = open('appendix','r')
newAppendix = file('small-appendix','w+')
raw_lines = appendix.readlines()
for line in raw_lines:
    a = line
    index = -1
    encounter = False
    count = 0
    while index<len(a)-1:
        index += 1
        if a[index]=='.':
            encounter = True
            continue
        if a[index]==',' or a[index]=='/' or a[index]=='\n':
            encounter = False
            count = 0
            continue
        if encounter:
            count += 1
        if count>=4:
            j = 1
            while a[index+j] != ',' and a[index+j] != '\n' and a[index+j] != '/':
                j += 1
            a = a[0:index+1]+a[index+j:]
            count = 0
    newAppendix.write(a)