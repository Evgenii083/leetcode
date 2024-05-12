import os
import timeit
import psutil


# Напишите программу, которая считывает текст из файла (в файле может быть больше одной строки) и выводит самое частое слово в этом тексте и через пробел то, сколько раз оно встретилось. 
# Если таких слов несколько, вывести лексикографически первое (можно использовать оператор < для строк).
# В качестве ответа укажите вывод программы, а не саму программу.

# Слова, написанные в разных регистрах, считаются одинаковыми.

# Sample Input:
# abc a bCd bC AbC BC BCD bcd ABC
# Sample Output:
# abc 3



# Формируем путь к файлу, который будет корректно работать на любой ОС
file_path = os.path.join('C:', os.sep,'Users', 'evgenijrybalkin', 'Downloads', 'dataset_3363_3-6.txt')

with open(file_path, 'r') as file:
    lines = []
    for line in file:
        line = line.lower().strip()
        lines.append(line)
    
one_line = ''.join(lines).split()

result = {}
for word in one_line:
    count = one_line.count(word)
    result[word]= count
    
max_value = max(result.values())
final_list = {}

for key,value in result.items():
    if value == max_value:
        final_list[key] = value
 
 
answer = next(iter(final_list.items()))
 

print(f"{answer[0]} {answer[1]}")
time =timeit.timeit('"-".join(str(n) for n in range(100))', number=10000)
time = round(time,4)

process = psutil.Process(os.getpid())

print(f"Время : {time} сек.")
print (f"Используемая память : {process.memory_info().rss / 1024 ** 2}")
    