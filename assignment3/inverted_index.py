import MapReduce
import sys

# Part 1
mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[0]
    value = record[1]
    words = value.split()
    for w in words:
      mr.emit_intermediate(w, value)

# Part 3
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    #total = 0
    #for v in list_of_values:
      #total += v
    mr.emit((key, list(set(list_of_values))))

# Part 4
inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)

'''
def locateWords(strlist):
d = {}
for i, substr in enumerate(strlist):
    for word in substr.split()
        if word not in d:
            d[word] = [i]
        else:
            d[word].append(i)
return d
'''
