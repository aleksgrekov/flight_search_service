Техническое задание «Сервис поиска авиабилетов»
Что нужно сделать
Необходимо создать сервис поиска авиабилетов в виде консольного приложения.

Основные функции приложения:

создание нового рейса;
вывод информации обо всех рейсах;
вывод информации о конкретном рейсе.

Изображение: главное меню — внешний вид и UI. Здесь и далее — скриншоты с сайта  replit.com



Создание нового рейса
Приложение принимает на вход:

Номер рейса в формате XXXX. При вводе проверьте, что поле содержит четыре символа. Пользователь может ввести данные в любом регистре, выводятся данные в верхнем регистре.
Дату вылета в формате ДД/ММ/ГГГГ. При вводе проверьте, что поле содержит десять символов.
Время вылета в формате ЧЧ:ММ. При вводе проверьте, что поле содержит пять символов.
Время перелёта в формате ЧЧ.ММ. При вводе проверьте, что поле содержит неотрицательное двузначное число и может принимать дробные числа.
Код ИАТА аэропорта вылета в формате XXX. При вводе проверьте, что поле содержит три символа. Пользователь может ввести данные в любом регистре, выводятся данные в верхнем регистре.
Код ИАТА аэропорта прилёта в формате XXX. При вводе проверьте, что поле содержит три символа. Пользователь может ввести данные в любом регистре, выводятся данные в верхнем регистре.
Стоимость авиабилета. Проверьте, что поле содержит неотрицательное число и может принимать дробные числа, например 5000,50.
Приложение возвращает сообщение с результатом: «Информация о рейсе добавлена».


Создание нового рейса



Вывод информации обо всех рейсах
Приложение выводит сведения по всем сохранённым рейсам.

Информация выводится через пробел в последовательности: номер рейса, дата вылета, время перелёта, код аэропорта вылета, код аэропорта прилёта, стоимость билета.

Если нет сохранённых рейсов, выводится сообщение: «Информация о рейсах отсутствует».


Вывод информации обо всех рейсах


Информация о рейсах отсутствует



Вывод информации о конкретном рейсе
Приложение принимает на вход номер рейса.

Возвращает в ответ данные по конкретному рейсу.

Информация выводится через пробел в последовательности: номер рейса, дата вылета, время перелёта, код аэропорта вылета, код аэропорта прилёта, стоимость билета.


Вывод информации о конкретном рейсе


Информация о конкретном рейсе не найдена



Требования к коду
Из встроенных функций нужно использовать только ввод (input) и вывод (print).

Преобразование типов выполнять только на вводе (some_variable = int(input("Enter some number")).

Нельзя использовать методы строк и прочие встроенные методы Python. Работа должна выполняться строго в рамках пройденного материала (модули 1–13).

Вложенные однотипные циклы недопустимы:

for ...:

    for ...:
Вложенные разнотипные циклы допустимы для проверки пользовательского ввода только в основной функции. Уровней вложенности должно быть не больше двух:

for ...:

    while ...:
В условиях должно быть не более двух уровней вложенности:

if ...:

    if ...:
Функция должна возвращать не более одного однотипного значения или не возвращать ничего:

def some_function():

    if ...:

        return 1

    return 0
Каждая отдельно взятая функция должна выполнять только одно действие:

def cubes(number):

    cube = number ** 3

        return cube
Нельзя использовать global.

Код должен соответствовать РЕР 8.
