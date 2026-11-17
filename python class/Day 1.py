# indexing matlab kisi bhi element ki position us variable mai nikalna 
# ye hamesha 0 se start hota hai.  

# Example: 

s= "Computer"
print(s.index("o")) # Output: 1

# Syntax: print(string_variable.index("search element"))

# ye case sesitive hai agar tere string mai c upper case mai hai or tune lower mai dala toh voh
# value error dega.


# Negative Indexing: 

# Back of the string -1 se start hoti hai 

# Slicing Mtlab katna and [] bracket use hote hai. 
# Slicing keval string mai use hoti hai

s="computer"
print(s[0:4]) # Output: comp

# Syntax: Variable[start:stop+1:step]
# end value mai jaha tak chaiye usme +1 kar dena.
b="computer is bad"
print(b[0:11]) # computer is
print(b[0:11:3]) # cpei

# Step: element skip karne ke liye hota hai jaise 3 dala toh voh har teesre element ko uthayega

# Example Question:

p= "Python is a funny language"
print(p[0:11:3]) 
print(p[::]) # Puri string lega ye
print(p[::2]) # ye puri string lega har 2-2 ke gap pe 
print(p[4:8:1])
print(p[7:11:2])

# Concatination: do ya do se jyda string ko ek sath jodna

s="tanmay"
p="Mittal"
print(s+" "+p) # " " ye do string ke beech mai string dega

# replication: multiplication

s="tanmay"
print(s*3) 

# Membership Operator: in and not in

s="Raghav"
print("s" not in s)


# rstrip(), lstrip(), strip()

#rstrip(): remove spaces from right
#lstrip(): remove spaces from left
#strip(): remove spaces from both left and right.

s=" TanmayMittal         "
print(s)
print(s.strip()) # remove all the spaces from left and right. 

# index and find mai koi diff nhi hai index mai error dega and find mai -1 return karega no error

# count: find the total number of times the words comes in string:

p="Python is a good language, python is good , python is bad"
print(p.count("python"))

