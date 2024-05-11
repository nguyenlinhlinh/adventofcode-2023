f= open("5/input.txt", "r")
sources = [int(i) for i in f.readline().split()[1:]]
mapping = {}
def mapSources():
    for i in range(len(sources)):
        source = sources[i]
        mapped = None
        for k, v in mapping.items():
            (dest, mapRange) = v
            if k <= source and source <= k + mapRange :
                diff = source - k
                mapped = dest + diff
                break
        if mapped == None:
            mapped = source
        sources[i] = mapped
    
for line in f:
    if line[0] == "\n":
        mapSources()
    elif not line[0].isdigit():
        mapping = {}
    else:
        [destination, source, mapRange] =  line.split()
        mapping[int(source)] = (int(destination), int(mapRange))

mapSources()
print(min(sources))
# Solution 825516882