while True:
  try:
    card = input("Παρακαλώ εισάγετε τον αριθμό της πιστοτικής σας κάρτας.") ##o xristis bazei ton arithmo ths kartas
    if len(card) != 16:
      print("Ο αριθμός της κάρτας πρέπει να έχει 16 ψηφία!") ##eksasfalizoume pws o arithmos einai 16psifios
    else:
      card = int(card) ##eksasfalizoume pws einai arithmos
      break
  except ValueError:
        print("Ο αριθμός της κάρτας πρέπει να περιέχει μόνο αριθμούς. Προσπαθήστε ξανά.") ##tha bgei an balei grammata

def luhn_checksum(card_number):
    def digits_of(n):
        return [int(d) for d in str(n)]
    digits = digits_of(card_number)
    odd_digits = digits[-1::-2]
    even_digits = digits[-2::-2]
    checksum = 0
    checksum += sum(odd_digits)
    for d in even_digits:
        checksum += sum(digits_of(d*2))
    return checksum % 10

def is_luhn_valid(card_number):
    return luhn_checksum(card_number) == 0



print(is_luhn_valid(card))
