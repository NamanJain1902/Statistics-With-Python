# Using Statistics module
import statistics
from statistics import mode

def modeVal(List):
  return mode(List)


# Naive Approach
def maxOcc(List):
  counter = 0
  num = List[0]

  for i in range(len(List)):
    curr_frequency = List.count(List[i])
    if(curr_frequency > counter):
      counter = curr_frequency
      num = List[i]
  return num

# Pythonic Naive Approach
def setMax(List):
  return max(set(List), key=List.count)

# Using Counter
from collections import Counter

def most_frequent(List):
  occurence_count = Counter(List)
  return occurence_count.most_common()[0][1]
# # # # # # # # # # # # #

# Using Dictionaries in python
def maxDict(List): 
	dict = {} 
	count, itm = 0, '' 
	for item in reversed(List): 
		dict[item] = dict.get(item, 0) + 1
		if dict[item] >= count : 
			count, itm = dict[item], item 
	return(itm)

List = [2,1.2,1,2,3,1,4,2]

print(maxDict(List))
print(most_frequent(List))
print(setMax(List))
print(maxOcc(List))
print(modeVal(List))


