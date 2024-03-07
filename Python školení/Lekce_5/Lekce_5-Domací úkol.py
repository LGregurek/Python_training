my_list = [1, 2, 3, "čtyři", "pět", "šest", 7, 8]
print ("můj seznam", my_list)

my_list.append(9)
print ("append - 9", my_list)

my_list.insert(4,4)
print ("insert - 4,4", my_list)

my_list.remove("čtyři")
my_list.remove("pět")
my_list.remove("šest")
print ("remove - texty", my_list)

my_list.sort()
print ("sort", my_list)

popped_element = my_list.pop()
print ("popped_element - ", popped_element)
print ("my_list -", my_list)
my_list.append(popped_element)
print ("pop-back", my_list)

my_tuple = (1, 2, 1, 3, 2, 4, 5, 6, 2, 3, 5)

print ("*******************************")
print ("my_tuple", my_tuple)

count = my_tuple.count(2)
print ("count (2)", count)

index = my_tuple.index(5)
print ("index (5)", index)

print ("-------------------------------")
my_set1 = {2, 4, 6, 8, 10,}
my_set2 = {4, 8, 12, 16, 20, 24}
print ("my set1 -", my_set1)
print ("my set2 -", my_set2)

my_set1.add(12)
print ("add", my_set1)

intersection_set = my_set1.intersection(my_set2)
print ("intersection =", intersection_set)

union_set = my_set1.union(my_set2)
print ("union", union_set)

print("<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")

my_string = "jedna, dva, tri, ctyri, pet, sest, sedm, osm, devet, deset"
print("my string - ", my_string)

print ("split - ", my_string.split(","))

print ("upper - ", my_string.upper())

print ("replace - ", my_string.replace("pet","padesat"))


