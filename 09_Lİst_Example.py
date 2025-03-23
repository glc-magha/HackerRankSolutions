"""Let('s learn about list comprehensions! '
    'You are given three integers  and  representing the dimensions of a cuboid along with an integer .'
    ' Print a list of all possible coordinates given by  on a 3D grid where the sum of  is not equal to .'
    ' Here, . Please use list comprehensions rather than multiple loops, '
    'as a learning exercise.Each variable  and  will have values of  or .'
    ' All permutations of lists in the form .)
Remove all arrays that sum to  to leave only the valid permutations.

Liste kavrayışlarını öğrenelim! Üç tam sayı ve bir küboidin boyutlarını ve
bir tam sayıyı temsil eden bir sayı verildi. Toplamının 'e eşit olmadığı 3 boyutlu
 bir ızgarada verilen tüm olası koordinatların bir listesini yazdırın. Burada, .
  Öğrenme egzersizi olarak, lütfen birden fazla döngü yerine liste kavrayışlarını kullanın.
   Her değişken ve veya değerlerine sahip olacaktır. Listelerin biçimindeki tüm permütasyonları.
Yalnızca geçerli permütasyonları bırakmak için toplamı olan tüm dizileri kaldırın

# Read input values
x = int(input())
y = int(input())
z = int(input())
n = int(input())

# Generate the 3D grid with list comprehension
coordinates = [[i, j, k] for i in range(x + 1)
                        for j in range(y + 1)
                        for k in range(z + 1)
                        if (i + j + k) != n]

# Print the valid coordinates
print(coordinates)

#...............................................
# Girdi değerlerini oku
x = int(input())
y = int(input())
z = int(input())
n = int(input())

# Liste üreteci kullanarak 3D koordinatları oluştur
coordinates = [[i, j, k] for i in range(x + 1)
                        for j in range(y + 1)
                        for k in range(z + 1)
                        if (i + j + k) != n]

# Geçerli koordinatları yazdır
print(coordinates)
"""
