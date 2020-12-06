import math
nums = ""
nvals = ""

for x in range (1, 1000):
  num = 6*x + 1
  num2 = math.sqrt(num)
  if num2.is_integer():
    nums+= " " + str(num)
    nvals+= " " + str(x)
    
print(nums + "\n")
print(nvals + "\n\n")


numList = nums.split()
numList2 = nvals.split()

strNumslol = ""

for y in range (0, len(numList2) - 2):
  othernum = int(numList2[y + 1]) - int(numList2[y])
  strNumslol += " " + str(othernum)
  
print(strNumslol)