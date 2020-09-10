#isEven function

def isEven(a):
    if a % 2 == 0:
        return True
    return False

print(isEven(2))
print(isEven(5))


#Warmup-1 > missing_char

def missing_char(str, n):
  
  newStr = ""
  newStr = str[0:n] + str[ n+1 : len(str)]
  return newStr

