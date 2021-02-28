import json
import math

f = open("airlines.csv","r")
dict = {}
skipline =   True
max_count = 0
min_count = math.inf
#print(min_count)
max_name = ""
min_name = ""

for i in f:
    if skipline:
        skipline = False
        continue
    lis = i.split('"')
    d = lis[1]
    if d not in dict:
        dict[d] = 1
    else:
        dict[d] += 1

final_ans = json.dumps(dict, indent = "")

for i in dict:
#   print(max_count)
#   print(min_count)
    if (dict[i] > max_count):
        max_count = dict[i]
        max_name = i
    elif (dict[i] < min_count):
        min_count = dict[i]
        min_name = i

print(final_ans)
print(max_name, max_count)
print(min_name, min_count)
