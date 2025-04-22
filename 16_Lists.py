Consider a list (list = []). You can perform the following commands:
insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of
commands where each command will be of the  types listed above.
Iterate through each command in order and perform the corresponding operation on your list.

Example
: Append  to the list, .
: Append  to the list, .
: Insert  at index , .
: Print the array.
Output:
[1, 3, 2]
Input Format
The first line contains an integer, , denoting the number of commands.
Each line  of the  subsequent lines contains one of the commands described above.
Constraints
The elements added to the list must be integers.
Output Format
For each command of type print, print the list on a new line.
Sample Input 0
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
Sample Output 0
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
#---------------------------------------------------------------
Bir liste düşünün (liste = []). Aşağıdaki komutları gerçekleştirebilirsiniz:
insert i e: . konumuna tam sayı ekle.
print: Listeyi yazdır.
remove e: . tam sayısının ilk örneğini sil.
append e: Listenin sonuna tam sayı ekle.
sorting: Listeyi sırala.
pop: Listeden son öğeyi çıkar.
reverse: Listeyi ters çevir.
Listenizi başlatın ve her komutun yukarıda listelenen türlerden olacağı komut satırlarının değerini okuyun.
Her komutu sırayla yineleyin ve listenizde karşılık gelen işlemi gerçekleştirin.
Örnek
: Listeye ekle, .
: Listeye ekle, .
: . dizinine ekle, .
: Diziyi yazdır.
Çıktı:
[1, 3, 2]
Giriş Biçimi
İlk satır, komut sayısını belirten bir tam sayı, içerir.
Sonraki satırların her satırı yukarıda açıklanan komutlardan birini içerir.
Kısıtlamalar
Listeye eklenen öğeler tam sayı olmalıdır.
Çıktı Biçimi
Yazdırma türündeki her komut için listeyi yeni bir satıra yazdır.
Örnek Giriş 0
12
ekle 0 5
ekle 1 10
ekle 0 6
yazdır
kaldır 6
ekle 9
ekle 1
sırala
yazdır
pop
ters
yazdır
Örnek Çıktı 0

[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
İlk satır: Komut sayısını belirler.
Sonraki satırlar: Yapılacak işlemleri belirtir. Örneğin:
insert i e: Listenin i indeksine e değerini ekler.
print: Listenin anlık halini yazdırır.
remove e: Listedeki e değerinin ilk görünümünü siler.
append e: Listenin sonuna e değerini ekler.
sort: Listeyi küçükten büyüğe sıralar.
pop: Listenin son elemanını siler.
reverse: Listeyi ters çevirir.
#------------------------------------------------------------------------------
