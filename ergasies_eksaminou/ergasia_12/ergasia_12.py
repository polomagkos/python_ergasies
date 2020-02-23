from datetime import datetime, time, timedelta ##xrisimopoiw thn bibliothiki datetime
now = datetime.now() ##h hmerominia tou ypologisti

while True:
  try:
    date1 = str(input("Παρακαλώ δώστε μια ημερομηνία της μορφής ΗΗ/ΜΜ/ΕΕΕΕ:")) ##eisagei o xrhsths thn hmeromhnia pou thelei
    val_date = datetime.strptime(date1, "%d/%m/%Y") ##to / exei megali simasia etsi eksasfalizoume pws einai ths swsths morfhs
    break
  except ValueError:
    print("Καταχωρήσατε λάθος τύπο ημερομηνίας! Παρακαλώ προσπαθήστε ξανά.") ##se periptwsh pou exei kanei lathos bgainei eidopoihsh


date2 = datetime.strptime(date1, '%d/%m/%Y') ##xrisimopoioume to date2 gia na einai sthn idia morfi me to now kai na ginei h afairesi

def date_diff_sec(dt2, dt1):
  timedelta = dt2 - dt1
  return timedelta.days * 24 * 3600 +timedelta.seconds

def date_diff (seconds):
  minutes, seconds = divmod(seconds, 60)
  hours, minutes = divmod (minutes,60)
  days, hours = divmod(hours, 24)
  return (days, hours, seconds) ##afta tha mas emfanisei

print("Η ημερομηνία που δώσατε απέχει από την τωρινή ημερομηνία: %d ημέρες, %d ώρες, %d δευτερόλεπτα." % date_diff(date_diff_sec(date2, now)))


def leap_year(year):
  return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0) ##pote ena etos einai disekto

meres = {1 : 31, 2 : 28, 3 : 31, 4 : 30, 5 : 31, 6 : 30, 7 : 31, 8 : 31, 9 : 30, 10 : 31, 11 : 30, 12 : 31} ##ginetai antistoixisi imerwn stous mines

date3 = date2.month ##krataw mono ton mina
date4 = date2.year ##krataw mono ton xrono

def minas_xronos(month, year):
  if leap_year(year) and month == 2:
    print("Επίσης ο μήνας της ημερομηνίας που επιλέξατε έχει τόσες ημέρες: 29")
  else:
    print("Ο μήνας που επιλέξατε έχει τόσες ημέρες:", meres[month])

minas_xronos(date3, date4)
