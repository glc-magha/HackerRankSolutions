"""A set is an unordered collection of elements without duplicate entries.
When printed, iterated or converted into a sequence, its elements will appear in an arbitrary order.
Example
>>> print set()
set([])

>>> print set('HackerRank')
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])

>>> print set([1,2,1,2,3,4,5,6,0,9,12,22,3])
set([0, 1, 2, 3, 4, 5, 6, 9, 12, 22])

>>> print set((1,2,3,4,5,5))
set([1, 2, 3, 4, 5])

>>> print set(set(['H','a','c','k','e','r','r','a','n','k']))
set(['a', 'c', 'r', 'e', 'H', 'k', 'n'])

>>> print set({'Hacker' : 'DOSHI', 'Rank' : 616 })
set(['Hacker', 'Rank'])

>>> print set(enumerate(['H','a','c','k','e','r','r','a','n','k']))
set([(6, 'r'), (7, 'a'), (3, 'k'), (4, 'e'), (5, 'r'), (9, 'k'), (2, 'c'), (0, 'H'), (1, 'a'), (8, 'n')])
Basically, sets are used for membership testing and eliminating duplicate entries.
Task
Now, let's use our knowledge of sets and help Mickey.
Ms. Gabriel Williams is a botany professor at District College
One day, she asked her student Mickey to compute the average
of all the plants with distinct heights in her greenhouse.
Formula used:
Function Description
Complete the average function in the editor below.
average has the following parameters:
int arr: an array of integers
Returns
float: the resulting float value rounded to 3 places after the decimal
Input Format
The first line contains the integer, , the size of .
The second line contains the  space-separated integers, .
Constraints
Sample Input
STDIN                                       Function
-----                                       --------
10                                          arr[] size N = 10
161 182 161 154 176 170 167 171 170 174     arr = [161, 181, ..., 174]
Sample Output

169.375
Explanation

Here, set is the set containing the distinct heights.
Using the sum() and len() functions, we can compute the average.
Language
Pypy 3
More
1234
def average(array):
    # your code goes here

if __name__ == '__main__':
Line: 1 Col: 1

Test against custom input
Blog
#----------------------------------------------------
Bir küme, yinelenen girdileri olmayan sıralanmamış bir öğe koleksiyonudur.
Yazdırıldığında, yinelendiğinde veya bir diziye dönüştürüldüğünde,
öğeleri keyfi bir sırada görünecektir.
Örnek
>>> print set()
set([])
>>> print set('HackerRank')
set(['a', 'c', 'e', ​​'H', 'k', 'n', 'r', 'R'])

>>> print set([1,2,1,2,3,4,5,6,0,9,12,22,3])
set([0, 1, 2, 3, 4, 5, 6, 9, 12, 22])

>>> print set((1,2,3,4,5,5))
set([1, 2, 3, 4, 5])

>>> print set(set(['H','a','c','k','e','r','r','a','n','k']))
set(['a', 'c', 'r', 'e', ​​'H', 'k', 'n'])

>>> print set({'Hacker' : 'DOSHI', 'Rank' : 616 })
set(['Hacker', 'Rank'])

>>> print set(enumerate(['H','a','c','k','e','r','r','a','n','k']))
set([(6, 'r'), (7, 'a'), (3, 'k'), (4, 'e'), (5, 'r'), (9, 'k'), (2, 'c'), (0, 'H'), (1, 'a'), (8, 'n')])
Temel olarak, kümeler üyelik testi ve yinelenen girişleri ortadan kaldırmak için kullanılır.
Görev
Şimdi, kümeler hakkındaki bilgimizi kullanalım ve Mickey'e yardım edelim.
Bayan Gabriel Williams, District College'da botanik profesörüdür. Bir gün, öğrencisi Mickey'den serasındaki farklı boylardaki tüm bitkilerin ortalamasını hesaplamasını istedi.
Kullanılan formül:
İşlev Açıklaması
Aşağıdaki düzenleyicide ortalama işlevini tamamlayın.
average aşağıdaki parametrelere sahiptir:
int arr: tamsayı dizisi
Döndürür
float: ondalıktan sonra 3 basamağa yuvarlanan sonuçtaki float değeri
Giriş Biçimi
İlk satır tamsayıyı, , boyutunu içerir.
İkinci satır boşlukla ayrılmış tamsayıları, içerir.
Kısıtlamalar
Örnek Giriş
STDIN İşlevi
----- --------
10 arr[] size N = 10
161 182 161 154 176 170 167 171 170 174 arr = [161, 181, ..., 174]
Örnek Çıktı

169.375
Açıklama

Burada, küme farklı yükseklikleri içeren kümedir.
sum() ve len() işlevlerini kullanarak ortalamayı hesaplayabiliriz.

Dil
Pypy 3
Daha Fazla
1234
def average(array):
# kodunuz buraya gelir

if __name__ == '__main__':
Line: 1 Col: 1
#------------------------------------------------------------------
def average(array):
    # Convert list to set to eliminate duplicates
    distinct_heights = set(array)
    # Calculate average of unique heights
    return round(sum(distinct_heights) / len(distinct_heights), 3)

if __name__ == '__main__':
    n = int(input())  # Read the size of the array
    arr = list(map(int, input().split()))  # Read the list of integers
    result = average(arr)
    print(result)
"""