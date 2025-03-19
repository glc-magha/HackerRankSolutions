"""Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
Input Format
A single line containing a positive integer, .
Constraints
Output Format
Print Weird if the number is weird. Otherwise, print Not Weird.
Görev
Bir tam sayı verildiğinde, aşağıdaki koşullu eylemleri gerçekleştirin:
Tek sayıysa, Garip yazdır
Çift sayıysa ve dahil aralığındaysa, Garip Değil yazdır
Çift sayıysa ve dahil aralığındaysa, Garip yazdır
Çift sayıysa ve büyükse, Garip Değil yazdır
Giriş Biçimi

Pozitif bir tam sayı içeren tek bir satır,
.Sayı garipse Garip yazdır. Aksi takdirde Garip Değil yazdır."""
n = int(input().strip())

if n % 2 == 1:  # Check if n is odd
    print("Weird")
elif 2 <= n <= 5:  # Check if n is even and in range 2 to 5
    print("Not Weird")
elif 6 <= n <= 20:  # Check if n is even and in range 6 to 20
    print("Weird")
else:  # Check if n is even and greater than 20
    print("Not Weird")


