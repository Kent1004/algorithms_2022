"""
Задание 4.

Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
4) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.

Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.

Приложение должно давать ответы на эти вопросы
 и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, применить словарь.

Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""

users = { 1 : ['Mikky' , '234rddsd' , 'Active'],
          2 : ['Jimmy' , '21e12321e' , 'No'],
          3 : ['Stephan' , 'dsd3d' , 'Active']
}

#Вариант 1 сложность #O(N)
def check_status (username):
    for val in users.values(): # O(N)+ O(N)
        if username == val[0]: #O(1)
            if val[2] == 'Active': #O(1)
                return "Проверка пройдена" #O(1)
            else: #O(1)
                return "Аккаунт не активирован" #O(1)

print (check_status("Jimmy"))
print (check_status("Mikky"))


#Вариант 2 сложность #O(N^2)
def check_status2 (username):
    for val in users.values(): # O(N)+ O(N)
        for v in val: # O(N)
            if v == username and val[2] == 'Active': #O(1) + O(1)
               return "Проверка пройдена" #O(1)
            else:
               return "Аккаунт не активирован" #O(1)

print (check_status2("Jimmy"))
print (check_status2("Mikky"))