"""Task

Given a year, determine whether it is a leap year. If it is a leap year,
return the Boolean True, otherwise return False.

Note that the code stub provided reads from STDIN and passes arguments to
the is_leap function. It is only necessary to complete the is_leap function.

Input Format
Read , the year to test.
Constraints
Output Format
The function must return a Boolean value (True/False). Output is handled by the provided code stub.
Sample Input 0
1990
Sample Output 0
False
Explanation 0
1990 is not a multiple of 4 hence it's not a leap year.
#.......................................................
Bir yıl verildiğinde, bunun artık yıl olup olmadığını belirleyin. Artık yıl ise,
Boolean True değerini döndürün, aksi takdirde False değerini döndürün.
Sağlanan kod parçasının STDIN('den okuduğunu ve is_leap işlevine argümanlar ilettiğini unutmayın.'
 Sadece is_leap işlevini tamamlamak gerekir.)

Giriş Biçimi
Okuma, test edilecek yıl.
Kısıtlamalar
Çıktı Biçimi
İşlev bir Boolean değeri (True/False) döndürmelidir. Çıktı, sağlanan kod parçası tarafından işlenir.
Örnek Giriş 0
1990
Örnek Çıktı 0
Yanlış
Açıklama 0
1990, 4'ün katı değildir, dolayısıyla artık yıl değildir.


def is_leap(year):
    return (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)

    leap = False

    # Write your logic here

    return leap


year = int(input())
print(is_leap(year))
"""