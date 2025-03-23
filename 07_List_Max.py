"""Given the participants(' score sheet for your University Sports Day, '
                'you are required to find the runner-up score.'
                ' You are given  scores. Store them in a list and find the score of the runner-up.)

Input Format
The first line contains . The second line contains an array   of  integers each separated by a space.
Given list is . The maximum score is , second maximum is . Hence, we print  as the runner-up score.
Dahil edilen kod parçası, STDIN'den bir tam sayı, okunmayacaktır.
Herhangi bir dize yöntemi kullanmadan, aşağıdakileri yazdırmayı değiştirme:
""'nin aradaki ardışık değerlerini temsil etmeyi unutmayın.
Örnek
Diziyi yazdırın.
Giriş Formatı
İlk satır bir tam sayı içerir.
Verilen liste şu şekildedir. Maksimum puan , ikinci maksimum ise dir. Bu nedenle ikincilik puanı olarak yazdırıyoruz.

n = int(input())  # Read the number of participants
scores = list(map(int, input().split()))  # Convert input into a list of integers

max_score = max(scores)  # Find the highest score
while max_score in scores:
    scores.remove(max_score)  # Remove all occurrences of the highest score

runner_up = max(scores)  # Find the next highest score (runner-up)
print(runner_up)  # Print the runner-up score

#.......................................................................
n = int(input())  # Katılımcı sayısını oku
scores = list(map(int, input().split()))  # Puanları listeye çevir

max_score = max(scores)  # En yüksek skoru bul
while max_score in scores:
    scores.remove(max_score)  # En yüksek skoru listeden kaldır

runner_up = max(scores)  # Kalan listede en yüksek olanı bul
print(runner_up)  # Runner-up skorunu yazdır
"""