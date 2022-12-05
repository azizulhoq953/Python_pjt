
fname = input("Enter file name: ")

num_words = 0

with open(fname, 'r') as f:
 
    count = f.read().count('.')
    f.close()
    
print("Number of dot:")
print(count)