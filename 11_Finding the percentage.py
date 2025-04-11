"""he provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.
Example
The query_name is 'beta'. beta's average score is .
Input Format
The first line contains the integer , the number of students' records. The next  lines contain the names and marks obtained by a student, each value separated by a space. The final line contains query_name, the name of a student to query.
Constraints
Output Format
Print one line: The average of the marks obtained by the particular student correct to 2 decimal places.
Sample Input 0
3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika
56.00


Sağlanan kod parçası, öğrencilerin listesi için name:[marks] anahtar/değer çiftlerini içeren bir sözlükte okunacaktır. Sağlanan öğrenci adı için not dizisinin ortalamasını, ondalık noktadan sonra 2 basamak gösterecek şekilde yazdırın.
Örnek
Query_name 'beta'dır. beta'nın ortalama puanı .
Giriş Biçimi
İlk satır tam sayıyı, öğrencilerin kayıt sayısını içerir. Sonraki satırlar bir öğrencinin aldığı adları ve notları içerir, her değer bir boşlukla ayrılır. Son satır query_name, sorgulanacak öğrencinin adını içerir.
Kısıtlamalar
Çıktı Biçimi
Bir satır yazdırın: Belirli öğrencinin aldığı notların 2 ondalık basamağa kadar ortalaması.

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    query_scores = student_marks[query_name]
    average = sum(query_scores) / len(query_scores)
    print("{:.2f}".format(average))
"""