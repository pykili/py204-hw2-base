# Задача №7

**Подзадача 1.**
Дан список `l`. Преобразуйте "иногда двумерный" список в одномерный. 
Например,
`l=[1, [2, 3], [4, 5], 6]`
должен превратиться в `[1,2,3,4,5,6]`.  

Пользуйтесь тем, что в питоне можно спросить `type(my_variable)`.
```
a = 2
print(type(a) == int)  # напишет тру
```

```
a = [2]
print(type(a) == list)  # напишет тру
```

**Подзадача 2.**
Преобразуйте "многомерный" список в одномерный
Многомерность неограничена -- каждый элемент может быть сколь угодно вложенным.
Напрмиер, преобразуйте `l=[1,[2,3],[4,[5,[6]]]]` в `[1, 2, 3, 4, 5, 6]`.
Не пользуйтесь рекурсиями.

Это задача про то, чтобы пока ваш список не стал простым (без вложенных), раз за разом его упрощать, избавляясь хот от какой-то имеющейся вложенности

### Код, с которого можно начать
в файле `solution_7.py`

