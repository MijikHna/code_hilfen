# 1 - Python loops

# 2 - The while loops
secret = "password"
pw=""
while pw != secret:
    pw = input("What is the secret word: ")

# 3 - The for loops
animals = ("bear", "bunny", "dog")
for pet in animals:
    print(pet)
for pet in range(5):
    print(pet)
# 4 - Additional controls
#continue, break, !! else !!
secret = "password"
pw=""
auth = False
count = 0
max_attemt = 5
while pw != secret:
    count += 1
    if count > max_attemt:
        break
    pw = input("What is the secret word: {} ".format(count))
else:
    auth = True
print("Authorized " if auth else "Calling the FBI ...")
 
