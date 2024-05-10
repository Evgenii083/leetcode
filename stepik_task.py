import os


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
one_line = sorted(one_line)

result = {}

for word in one_line:
    count = one_line.count(word)
    result[word]= count
    
sorted_result = dict(sorted(result.items(),key=lambda item:item[1],reverse=True)) 

max_value = max(sorted_result.values())
final_list = {}

for key,value in sorted_result.items():
    if value == max_value:
        final_list[key] = value
 
final_list = dict(sorted(final_list.items()))       
answer = next(iter(final_list.items()))
 

print(f"{answer[0]} {answer[1]}")
    