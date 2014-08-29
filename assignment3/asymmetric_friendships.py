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
    #words = value.split()
    #for w in words:
    mr.emit_intermediate(key,value)
    #mr.emit_intermediate(value,key)

# Part 3

def reducer(key, list_of_values):
    # key: word
    # value: list of occurrence counts
    #total = 0
    #for v in list_of_values:
      #total += v
    for value in list_of_values:
      if value not in mr.intermediate.keys():
      	mr.emit((key,value))
        mr.emit((value,key))
      else:
        if key not in mr.intermediate[value]:
      	  mr.emit((key,value))
          mr.emit((value,key))

# Part 4

inputdata = open(sys.argv[1])
mr.execute(inputdata, mapper, reducer)
#print mr.intermediate
