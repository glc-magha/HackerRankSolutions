"""The included code stub will read an integer, , from STDIN.
Without using any string methods, try to print the following:
Note that "" represents the consecutive values in between.
Example
Print the string .

Input Format
The first line contains an integer .
Constraints
Output Format
Print the list of integers from  through  as a string, without spaces.
Sample Input 0
3
Sample Output 0
123
#-----------------------------------------------------------------
Kullanıcıdan bir tam sayı (n) alacaksın,
ve sonra 1'den n'e kadar olan tüm sayıları yan yana (boşluksuz) yazdıracaksın.
Dahil edilen kod parçası, STDIN'den bir tam sayı, , okuyacaktır.
Herhangi bir dize yöntemi kullanmadan, aşağıdakileri yazdırmayı deneyin:
""'nin aradaki ardışık değerleri temsil ettiğini unutmayın.
Örnek
Dizeyi yazdırın.
Giriş Biçimi
İlk satır bir tam sayı içerir.
Kısıtlamalar
Çıktı Biçimi
Tam sayıların listesini, boşluklar olmadan bir dize olarak yazdırın.
Örnek Giriş 0
3
Örnek Çıktı 0
123

if __name__ == '__main__':
    n = int(input())
    for i in range(1, n+1):
        print(i, end='')"""