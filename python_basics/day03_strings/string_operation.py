# Indexing
s="python"
print("First Character:",s[0])
print("Last Character:",s[-1])

# Slicing
# a)Used to access a range of characters.
# b)Syntex:string[start:end]   Note: Here end is excluded

#  P    Y   T   H   O   N
#  0    1   2   3   4   5

print(s[1:4])  # print 1 to 3 because 4 is excluded
print(s[:2])   # pring 0 to 1
print(s[3:])    # print 3 to last



# in keyword in python string
sentence = "Python is Powerfull"
keyword = "Python"

if keyword in sentence:
    print(f"{keyword} keyword included in sentence")
else:
    print(f"{keyword} is not included in sentence")
    
# Different Operations on String
str="python is a good language"
chars="python"
count=3
print("\n\nCapital:",str.capitalize())
print("Lower:",str.lower())
print("Upper:",str.upper())
print("Title:",str.title())
print("strip(chars):",str.strip(chars))    #ython is a good language
print("replace:",str.replace("python", "java", count))
print("is-digit:",str.isdigit())
print("is-numeric:",str.isnumeric())
print("is-lower:",str.islower())
print("is-upper:",str.isupper())