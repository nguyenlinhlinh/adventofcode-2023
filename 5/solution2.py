# Map source ranges to destination ranges
# There is for kind of range matching as commented below
# It map the range that match with the source range. Create new ranges to map for ranges that are outside of matching range
# Sources and toMap are in always sorted to ease the matching
# The tricky thing about this is to realize that it can only be matched until end of source range - 1
def mapSources(sources, mapping):
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
            diff = startDestination - startSource
            # Source range        |-------|
            # To map range          |---|
            if startSource <= start and end <= endSource :
                if(start + diff <= end + diff):
                    if(end == endSource):
                        newSources.append((start + diff, (end - 1) + diff))
                        toMap.append((endSource, endSource))
                    else:
                        newSources.append((start + diff, end + diff))
                mapped = True
            # Source range         |-------|
            # To map range       |------------|  
            elif startSource >= start and end >= endSource:
                if start <= startSource -1:
                    toMap.append((start, startSource -1))
                if end >= endSource:
                    toMap.append((endSource, end))
                newSources.append((startDestination, endDestination -1))
                mapped = True
            # Source range              |-------|
            # To map range         |---------|  
            elif startSource >= start and end <= endSource and startSource <= end:
                if start <= max(startSource -1, 0):
                    toMap.append((start, max(startSource -1, 0)))
                if startDestination <= end + diff:
                    newSources.append((startDestination, end + diff))
                mapped = True
            # Source range      |-------|
            # To map range          |---------|  
            elif startSource <= start and end >= endSource and start < endSource:
                if endSource <= end:
                    toMap.append((endSource, end))
                if start + diff <= endDestination:
                    newSources.append((start + diff, endDestination))
                mapped = True

            if mapped == False:
                toMap.append((start, end))
            mapped == False
            toMap.sort()
            
        # Left over that can't match
        if len(toMap) > 0:
            for i in toMap:
                newSources.append(i)

    newSources.sort(key=sortSources)
    return newSources
                
def sortToMap(value):
    return value[0]
def sortMapping(value):
    return value[0][0]

def sortSources(value):
    return value[0]

def findLowestLocation():
    f= open("5/input.txt", "r")
    ranges = [int(i) for i in f.readline().split()[1:]]
    sources = []
    mapping = []

    # Create source ranges
    for i in range(0, len(ranges), 2):
        start = ranges[i]
        end = start + ranges[i + 1]
        sources.append((start, end))

    f.readline()

    for line in f:
        if line[0] == "\n":
            mapping.sort(reverse=False, key=sortMapping)
            sources = mapSources(sources, mapping)

        elif not line[0].isdigit():
            mapping = []
        else:
            [destination, source, mapRange] =  [int(i) for i in line.split()]
            # (source range) - (destination range)
            mapping.append(((source, source + mapRange), (destination, mapRange + destination)))

    mapping.sort(reverse=False, key=sortMapping)
    sources = mapSources(sources, mapping)
    return sources[0][0]

print("Lowest location", findLowestLocation())
# Solution 136096660