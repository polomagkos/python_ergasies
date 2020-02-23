while True:
  try:
    num = int(input("Παρακαλώ δώστε έναν φυσικό αριθμό: "))  ##dexetai enan arithmo
    while num < 0: ##eksasfalizei oti o arithmos einai fisikos
      print("Ο αριθμός πρέπει να είναι φυσικός! Δοκιμάστε ξανά.") 
      num = int(input("Παρακαλώ δώστε έναν φυσικό αριθμό: ")) 
    else:  
      break
  except ValueError:
    print("Ο αριθμός πρέπει να είναι ακέραιος! Δοκιμάστε ξανά.") ##eksasfalizei oti o arithmos einai int



num = (num * 3) + 1 ##pollaplasiazetai epi 3 kai sti sunexeia prostithetai 1

def sum_digits(x):
  s = 0
  while x:
    s += x % 10
    x //= 10
  return s ##prosthetei ta psifia

while sum_digits(num) >= 10:
  num = (sum_digits(num) * 3) + 1 
  def sum_digits(x):
    s = 0
    while x:
      s += x % 10
      x //= 10
    return s ##me afto to while o telikos arithmos einai sigoura monopsifios

else:
  print(sum_digits(num)) ##prostithontai ta psifia tou arithmou pou prokiptei
