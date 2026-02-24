`DataFrame` — это таблица с именованными столбцами и индексами строк. Создать `DataFrame` можно из словаря списков:

```Python
students_marks_dict = { "student": ["Студент_1", "Студент_2", "Студент_3"], "math": [5, 3, 4], 
"physics": [4, 5, 5] } students = pd.DataFrame(students_marks_dict) 
print(students) # Вывод программы # student math physics # 0 Студент_1 5 4 # 1 Студент_2 3 5 # 2 Студент_3 4 5
```