
"""Task
Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of .
Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.
Input Format
The first line contains an integer, , denoting the number of elements in the tuple.
The second line contains  space-separated integers describing the elements in tuple .
Output Format
Print the result of .
Sample Input 0
2
1 2
Görev
Bir tam sayı, , ve giriş olarak boşluklarla ayrılmış tam sayılar verildiğinde, bu tam sayılardan oluşan bir (tuple ,
oluşturun. Ardından, 'nin sonucunu hesaplayın ve yazdırın.)
Not: hash(), __builtins__ modülündeki işlevlerden biridir, bu nedenle içe aktarılması gerekmez.
Giriş Biçimi
İlk satır, tuple'daki öğe sayısını belirten bir tam sayı, içerir.
İkinci satır, tuple'daki öğeleri tanımlayan boşluklarla ayrılmış tam sayılar içerir.

n = int(input())
integer_list = map(int, input().split())
t = tuple(integer_list)
print(hash(t))

"""
