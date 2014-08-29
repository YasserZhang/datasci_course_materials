import MapReduce
import sys

# Part 1
mr = MapReduce.MapReduce()

# Part 2
def mapper(record):
    # key: document identifier
    # value: document contents
    key = record[1]
    #value = record
    #words = value.split()
    mr.emit_intermediate(key, record)

# Part 3
def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    #total = 0
    #for v in list_of_values:
      #total += v
    #mr.emit((key, list(set(list_of_values))))
    a=[]
    b=[]
    for l in list_of_values:
      if l[0] == "order":
        a.append(l)
      else:
        b.append(l)
    for m in a:
      for n in b:
        x=m+n
        mr.emit(x)

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
