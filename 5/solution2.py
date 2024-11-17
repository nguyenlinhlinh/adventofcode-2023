f= open("5/input.txt", "r")


ranges = [int(i) for i in f.readline().split()[1:]]
sources = []

# Create source ranges
for i in range(0, len(ranges), 2):
    start = ranges[i]
    end = start + ranges[i + 1]
    sources.append((start, end))

def mapSources(sources):
    newSources = []
    for i in range(0, len(sources)):
        (s, e) = sources[i]
        toMap = [(s, e)]
        mapped = False
        for (s, d) in mapping:
            if len(toMap) == 0:
                break

            (start, end) = toMap.pop()
            (startSource, endSource) = s
            (startDestination, endDestination) = d
            # Source range |-------|
            # Range          |---|
            if startSource <= start and end <= endSource :
                diff = startDestination - startSource
                if(start + diff <= end + diff):
                    if(end == endSource):
                        newSources.append((start + diff, (end - 1) + diff))
                        toMap.append((endSource, endSource))
                    else:
                        newSources.append((start + diff, (end - 1) + diff))
                mapped = True
            # Source range |-------|
            # Range       |---------|  
            elif startSource >= start and end >= endSource:
                if start <= startSource -1:
                    toMap.append((start, startSource -1))
                if end >= endSource:
                    toMap.append((endSource, end))
                newSources.append((startDestination, endDestination -1))
                mapped = True
            # Source range      |-------|
            # Range       |---------|  
            elif startSource >= start and end <= endSource and startSource <= end:
                if start <= max(startSource -1, 0):
                    toMap.append((start, max(startSource -1, 0)))
                diff = startDestination - startSource
                if startDestination <= end + diff:
                    newSources.append((startDestination, end + diff))
                mapped = True
            # Source range |-------|
            # Range           |---------|  
            elif startSource <= start and end >= endSource and start < endSource:
                if endSource <= end:
                    toMap.append((endSource, end))
                diff = startDestination - startSource
                if start + diff <= endDestination:
                    newSources.append((start + diff, endDestination))
                mapped = True
            if mapped == False:
                toMap.append((start, end))
            mapped == False
            toMap.sort()
            

        if len(toMap) > 0:
            for i in toMap:
                newSources.append(i)

    newSources.sort(key=sortSources)
    return newSources
                



f.readline()
def sortToMap(value):
    return value[0]
def sort(value):
    return value[0][0]

def sortSources(value):
    return value[0]

mapping = []

for line in f:
    if line[0] == "\n":
        mapping.sort(reverse=False, key=sort)
        sources = mapSources(sources)
    elif not line[0].isdigit():
        mapping = []
    else:
        [destination, source, mapRange] =  [int(i) for i in line.split()]
        # (source range) - (destination range)
        mapping.append(((source, source + mapRange), (destination, mapRange + destination)))


mapping.sort(reverse=False, key=sort)
sources = mapSources(sources)

print("lowest location", sources[0][0])
# Solution 136096660