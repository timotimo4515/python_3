#A Function Enabled Calculater
def start(count):
  i = 0
  a = 0
  b = 1
  while(i < count):
    sum = a + b
    print(str(sum))
    a = b
    b = sum
    i += 1
    
#The activater of the function
start(10)
