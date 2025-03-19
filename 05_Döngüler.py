"""Task
The provided code stub reads an integer, ,
 from STDIN. For all non-negative integers ,
print .
Exampl
The list of non-negative integers that are less than  is .
Print the square of each number on a separate line.
Görev
Sağlanan kod parçası, STDIN'den bir tam sayı, , okur.
Tüm negatif olmayan tam sayılar için, yazdırın.
Örnek
'den küçük olan negatif olmayan tam sayıların listesi.
Her sayının karesini ayrı bir satıra yazdırın."""

# Read an integer from input
n = int(input().strip())

# Loop through all non-negative integers less than n
for i in range(n):
    print(i ** 2)  # Print the square of each number
#done