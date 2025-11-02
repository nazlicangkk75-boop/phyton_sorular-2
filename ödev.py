1. Kullanıcıdan adını ve soyadını ayrı ayrı alıp, tam adını ekrana yazdıran program.
•	ad = input("Adınızı girin: ")
soyad = input("Soyadınızı girin: ")
print("Tam adınız:", ad, soyad)
2. İki sayının toplamını, farkını ve çarpımını hesaplayan program.
•	sayi1 = int(input("Birinci sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))
print("Toplam:", sayi1 + sayi2)
print("Fark:", sayi1 - sayi2)
print("Çarpım:", sayi1 * sayi2)
3. Kullanıcının yaşını alıp, 18 yaşından büyük olup olmadığını True/False olarak gösteren program.
•	yas = int(input("Yaşınızı girin: "))
print("18 yaşından büyük mü?:", yas > 18)
4. Dikdörtgenin alanını ve çevresini hesaplayan program.
•	kisa = int(input("Kısa kenarı girin: "))
uzun = int(input("Uzun kenarı girin: "))
print("Alan:", kisa * uzun)
print("Çevre:", 2 * (kisa + uzun))
5. Girilen bir sayının pozitif olup olmadığını kontrol eden program.
•	sayi = int(input("Bir sayı girin: "))
print("Pozitif mi?:", sayi > 0)
6. Kullanıcıdan bir kelime alıp, kelimenin ilk 3 harfini ve son 2 harfini yazdıran program.
•	kelime = input("Bir kelime girin: ")
print("İlk 3 harf:", kelime[0:3])
print("Son 2 harf:", kelime[-2:])
7. İki sayının ortalamasını hesaplayıp, sonucu ondalıklı sayı olarak gösteren program.
•	sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))
print("Ortalama:", (sayi1 + sayi2) / 2)
8. Kullanıcının girdiği iki sayının her ikisinin de çift sayı olup olmadığını kontrol eden program.
•	sayi1 = int(input("Birinci sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))
print("Her ikisi de çift mi?:", sayi1 % 2 == 0 and sayi2 % 2 == 0)
9. Girilen bir metnin uzunluğunu ve büyük harfe çevrilmiş halini ekrana yazdıran program.
•	metin = input("Bir metin girin: ")
print("Uzunluk:", len(metin))
print("Büyük harf hali:", metin.upper())
10. Dairenin alanını hesaplayan program (pi = 3.14 kabul edin).
•	yaricap = float(input("Yarıçapı girin: "))
pi = 3.14
print("Dairenin alanı:", pi * (yaricap ** 2))
11. İki sayının eşit olup olmadığını ve birincinin ikinciden büyük olup olmadığını gösteren program.
•	sayi1 = int(input("Birinci sayıyı girin: "))
sayi2 = int(input("İkinci sayıyı girin: "))
print("Eşit mi?:", sayi1 == sayi2)
print("Birinci sayı ikinci sayıdan büyük mü?:", sayi1 > sayi2)
12. Bir sayının hem 3’e hem de 5’e tam bölünüp bölünmediğini kontrol eden program.
•	sayi = int(input("Bir sayı girin: "))
print("Hem 3’e hem 5’e tam bölünüyor mu?:", sayi % 3 == 0 and sayi % 5 == 0)
