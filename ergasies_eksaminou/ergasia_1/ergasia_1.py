with open('keimeno.txt', 'r') as file: ##diabazei to keimeno apo to eksoteriko arxeio
    lekseis = file.read().replace('linesep', '').replace(',', '').replace('-', '').replace('_', '').replace('!', '').replace('.', '').replace('?', '').replace(';', '').replace('<', '').replace('>', '').replace('/', '').replace('|', '').replace('[', '').replace(']', '').replace('{', '').replace('}', '').replace('+', '').replace('#', '').replace('^', '').replace('&', '').replace('"', '').replace('*', '').replace('=', '').replace('  ', '') ##bazei olo to keimeno se mia grammi kai bgazei ta simbola
lekseis = lekseis.split() ##metatrepei string se list 
lista = sorted(lekseis, key=len, reverse=True) ##bazei tis lekseis apo tin megaliteri stin mikroteri
##me ton sigkekrimeno tropo kleinei to arxeio

fon = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U', 'α', 'ε', 'η', 'ι', 'ο', 'υ', 'ω', 'Α', 'Ε', 'Η', 'Ι', 'Ο', 'Υ', 'Ω', 'ά', 'έ', 'ή', 'ί', 'ό', 'ύ', 'ώ', 'Ά', 'Έ', 'Ή', 'Ί', 'Ό', 'Ύ', 'Ώ', '¨ϊ', 'ϋ', 'ΐ', 'ΰ', 'Ϊ', 'Ϋ', '΅Ι', '΅Υ') ##epilegw ta fonienta

leksi1 = lista [0][::-1] ##h megaliteri leski grafetai anapoda
for x in leksi1:
  if x in fon:
    leksi1 = leksi1.replace(x, "") ##afairountai ta fonienta
print ("Η πρώτη λέξη είναι --> %s" % (leksi1,))
leksi2 = lista [1][::-1] ##h amesos epomeni kok
for y in leksi2:
  if y in fon:
    leksi2 = leksi2.replace(y, "")
print ("Η δεύτερη λέξη ειναι --> %s" % (leksi2,))
leksi3 = lista [2][::-1] 
for z in leksi3:
  if z in fon:
    leksi3 = leksi3.replace(z, "")
print("Η τρίτη λέξη έιναι --> %s" % (leksi3,))
leksi4 = lista [3][::-1]
for w in leksi4:
  if w in fon:
    leksi4 = leksi4.replace(w, "")
print("Η τέταρτη λέξη είναι --> %s" % (leksi4,))
leksi5 = lista[4][::-1]
for c in leksi5:
  if c in fon:
    leksi5 = leksi5.replace(c, "")
print("Η πέμπτη λέξη είναι --> %s" % (leksi5,))
