import time

start_time = time.time()

f = open('names_1.txt', 'r')
names_1 = f.read().split("\n")  # List containing 10000 names
f.close()

f = open('names_2.txt', 'r')
names_2 = f.read().split("\n")  # List containing 10000 names
f.close()

duplicates = []
# i could have used a binary search but
# i used intersection since this is a large data set
# by just using intersection the code runs under
# intersection here means its comparing
#  whats common in set name1 and name 2
#  0.0035, 0.013, 0.0038 etc
duplicates = set(names_1).intersection(names_2)

end_time = time.time()
print (f"{len(duplicates)} duplicates:\n\n{', '.join(duplicates)}\n\n")
print (f"runtime: {end_time - start_time} seconds")

