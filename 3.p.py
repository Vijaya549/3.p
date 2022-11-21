n = int(input()) # Taking input number
n-=1 # As we are staring from 1 so -1 is taken in n
elo = ['0','1','2','5','6','8','9'] # List of numbers whose inverse is also number
l =[]
s = ""
for item in elo:
  s+=item #0125689
# Function for permutaions which will find nth possible number
def elon(s):
    length = 7 # Lentgth of elo list
    mylist = []
    for i in range(1, length+1):
        for j in range(length-i+1):
            mylist.append(s[j:j+i]) # adding all the elements possible into mylist
    return mylist # List which contains all numbers i.e. permutaions

w = elon(s)[n] # Nth possible number
# Function to revrse our number w
def reverse(w):
    str = ""
    for i in w:
        str = i + str
    return str
if n<7: # For n less than 7 we will simply return the value at index n of list elo
  print(elo[n])
else:
  print(int(reverse(w))) # Printing output
