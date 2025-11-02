
ad = input("Adınızı girin: ")
soyad = input("Soyadınızı girin: ")
print("Tam adınız:", ad, soyad)


sayi1 = int(input("Birinci sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))
print("Toplam:", sayi1 + sayi2)
print("Fark:", sayi1 - sayi2)
print("Çarpım:", sayi1 * sayi2)


yas = int(input("Yaşınızı girin: "))
print("18 yaşından büyük mü?:", yas > 18)


kisa = int(input("Kısa kenarı girin: "))
uzun = int(input("Uzun kenarı girin: "))
print("Alan:", kisa * uzun)
print("Çevre:", 2 * (kisa + uzun))


sayi = int(input("Bir sayı girin: "))
print("Pozitif mi?:", sayi > 0)


kelime = input("Bir kelime girin: ")
print("İlk 3 harf:", kelime[0:3])
print("Son 2 harf:", kelime[-2:])


sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))
print("Ortalama:", (sayi1 + sayi2) / 2)


sayi2 = int(input("İkinci sayıyı girin: "))
print("Her ikisi de çift mi?:", sayi1 % 2 == 0 and sayi2 % 2 == 0)


metin = input("Bir metin girin: ")
print("Uzunluk:", len(metin))
print("Büyük harf hali:", metin.upper())


yaricap = float(input("Yarıçapı girin: "))
pi = 3.14
print("Dairenin alanı:", pi * (yaricap ** 2))


sayi1 = int(input("Birinci sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))
print("Eşit mi?:", sayi1 == sayi2)
print("Birinci sayı ikinci sayıdan büyük mü?:", sayi1 > sayi2)


sayi = int(input("Bir sayı girin: "))
print("Hem 3’e hem 5’e tam bölünüyor mu?:", sayi % 3 == 0 and sayi % 5 == 0)

