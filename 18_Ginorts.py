
#Küçük harfler (a-z),Büyük harfler (A-Z) ,Rakamlar (0-9)
k = input()

print(''.join(sorted(k, key=lambda x: (
    x.isdigit(),                     # Harfler önce, rakamlar sonra
    x.isdigit() and int(x) % 2 == 1, # Tek rakamlar önce (True olanlar sona geçmesin diye burada '== 1')
    x.isupper(),                     # Küçük harfler önce
    x.lower()                        # Alfabetik sıralama
))))

