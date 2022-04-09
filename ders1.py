#python ve vscode yükleme

# int
# float
# string
# bool
# Strings

print("Hello World!")
isim = "Ahmet"
yas = "70"
print("Yıllar önce Ahmet adında bir adam vardı.")
print("70 yaşlarındaydı.")
print("Ahmet kendi adını gerçekten seviyordu.")
print("Fakat 70 yaşında olmayı hiç sevmiyordu.")


print("Merhaba \n Dünya!")
metin = "Merhaba Dünya!"
print(metin + " nasılsın")
print(metin.lower())


print(metin.upper())
print(metin.isupper())
print(metin.islower())
print(len(metin))
print(metin[0])
print(metin.index("D"))
print(metin.replace("Merhaba", "Nasılsın"))

print(input("Bir değer giriniz: "))
 
import random

user_action = input("Seçiminiz (Taş, Kağıt, Makas): ")
possible_actions = ["Taş", "Kağıt", "Makas"]
computer_action = random.choice(possible_actions)
print("Senin seçimin: " + user_action + "\nBilgisayarın seçimi: " + computer_action + "")