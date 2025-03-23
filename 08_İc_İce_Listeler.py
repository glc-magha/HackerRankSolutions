"""Given the names and grades for each student in a class of  students,
store them in a nested list and print the name(s) of any student(s) having the second lowest grade.

Note: If there are multiple students with the second lowest grade,
order their names alphabetically and print each name on a new line.
Example
The ordered list of scores is , so the second lowest score is .
There are two students with that score: .
Ordered alphabetically, the names are printed as:

The first line contains an integer, , the number of students.
The  subsequent lines describe each student over  lines.
- The first line contains a student's name.
- The second line contains their grade.
There will always be one or more students having the second lowest grade.
Output Format
Print the name(s) of any student(s) having the second lowest grade in.
If there are multiple students,
order their names alphabetically and print each one on a new line.
There are  students in this class whose names and grades are assembled to build the following list:

python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

The lowest grade of  belongs to Tina.
The second lowest grade of  belongs to both Harry and Berry,
so we order their names alphabetically and print each name on a new line.


Bir sınıftaki her öğrencinin adı ve notu verildiğinde,
bunları iç içe geçmiş bir listede saklayın ve ikinci en düşük nota sahip
olan herhangi bir öğrencinin adını/adlarını yazdırın.
Not: İkinci en düşük nota sahip birden fazla öğrenci varsa,
adlarını alfabetik olarak sıralayın ve her bir adı yeni bir satıra yazdırın.
Örnek
Sıralı puan listesi 'dir, dolayısıyla ikinci en düşük puan 'dir.
Bu puana sahip iki öğrenci vardır: .
Alfabetik olarak sıralandığında, adlar şu şekilde yazdırılır:

İlk satır bir tam sayı, , öğrenci sayısını içerir.
Daha sonraki satırlar her bir öğrenciyi satırlar halinde açıklar.
- İlk satır bir öğrencinin adını içerir.
- İkinci satır notunu içerir.
Her zaman ikinci en düşük nota sahip bir veya daha fazla öğrenci olacaktır.
Çıktı Biçimi
İkinci en düşük nota sahip herhangi bir öğrencinin adını/adlarını yazdırın. Birden fazla öğrenci varsa, adlarını alfabetik olarak sıralayın ve her birini yeni bir satıra yazdırın.
Bu sınıfta isimleri ve notları bir araya getirilerek aşağıdaki liste oluşturulmuş öğrenciler var:
python students = [['Harry', 37.21], ['Berry', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]
En düşük not Tina'ya ait. İkinci en düşük not ise hem Harry'ye hem de Berry'ye ait, bu yüzden isimlerini alfabetik olarak sıralıyoruz ve her ismi yeni bir satıra yazıyoruz.

# Step 1: Read input data
n = int(input())  # Number of students
students = []  # Nested list to store [name, grade] pairs

# Step 2: Store student names and grades in a list
for _ in range(n):
    name = input()  # Read student's name
    grade = float(input())  # Read student's grade
    students.append([name, grade])  # Store as a list inside students list

# Step 3: Find the second lowest grade
grades = sorted(set([grade for name, grade in students]))  # Unique sorted grades
second_lowest = grades[1]  # Second lowest grade

# Step 4: Get names of students with second lowest grade
second_lowest_students = [name for name, grade in students if grade == second_lowest]

# Step 5: Sort names alphabetically and print them
for name in sorted(second_lowest_students):
    print(name)
#..........................................................
# 1. Adım: Kullanıcıdan giriş verisini al
n = int(input())  # Öğrenci sayısını oku
students = []  # Öğrenci bilgilerini saklamak için iç içe liste

# 2. Adım: Öğrenci isim ve notlarını listeye ekle
for _ in range(n):
    name = input()  # Öğrenci ismini oku
    grade = float(input())  # Öğrenci notunu oku
    students.append([name, grade])  # Listeye ekle

# 3. Adım: İkinci en düşük notu bul
grades = sorted(set([grade for name, grade in students]))  # Notları sıralı ve benzersiz liste yap
second_lowest = grades[1]  # İkinci en düşük notu al

# 4. Adım: Bu nota sahip öğrencileri seç
second_lowest_students = [name for name, grade in students if grade == second_lowest]

# 5. Adım: İsimleri alfabetik sıraya koy ve yazdır
for name in sorted(second_lowest_students):
    print(name)
"""



