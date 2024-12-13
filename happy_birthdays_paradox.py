


#парадокс дней рождений на python
import datetime,random
def create_birthday(birthday_num):
    birthdays =[]
    for i in range(birthday_num):
        start_of_year =datetime.date(2001,1,1)
        random_day =datetime.timedelta(random.randint(0,364))
        birthday =start_of_year + random_day
        birthdays.append(birthday)  ######
    return birthdays
def get_match(birthdays):
    if len(birthdays) ==len(set(birthdays)):
        return None
    for a,birthdayA,in enumerate(birthdays):
        for b,birthdayB,in enumerate(birthdays[a +1 :]):
            if birthdayA ==birthdayB:
                return birthdayA
print("Парадокс дня рождения показывает нам, что в группе из неопределенного человек вероятность того, что у двоих из них совпадут дни рождения, на удивление велика.Эта программа выполняет моделирование методом Монте-Карло (то есть повторяет случайные симуляции), чтобы исследовать эту концепцию")
month =("Январь","Февраль","Март","Aпрель","Май","Июнь","Июль","Август","Сентябрь","Октябрь","Ноябрь","Декабрь")


while True:
    print("Сколько дней рождений я сгенерирую?Ответ за тобой (масимум 100)")
    generating =input(">>>>>>")
    if generating.isdecimal() and (0 < int(generating) <=100):
        numBDAYS =int(generating)
        break
print()
print("здесь",numBDAYS,"дней рождений")
birthdays = create_birthday(numBDAYS,)
for i,birthday in enumerate(birthdays):
    if i !=0:
        print(",",end="")
    month_name =month[birthday.month -1]
    date_text ="{} {}".format(month_name,birthday.day)
    print(date_text,end="")
print()
print()
match =get_match(birthdays)
print("В этой симуляции,",end ="")
if match !=None:
    month_name =month[match.month -1]
    date_text ="{} {}".format(month_name,match.day)
    print("у нескольких человек день рождения в:",date_text)
else:
    print("совпадающих дней рождения не существует :(")
print()
print("Генерирую",numBDAYS,"случайных дней рождений 100,000 раз......")
input("Нажмите клавишу ENTER,чтобы продолжить")
print("Давайте пробежимся по еще 100,000 симуляций :)")
sim_match =0
for i in range(100_000):
    if i % 10_000 ==0:
        print(i,'Симуляции выполняються.......')
    birthdays =create_birthday(numBDAYS)
    if get_match(birthdays) !=None:
        sim_match =sim_match +1
print("100,000 симуляций смоделировано :)")
probability =round(sim_match / 100_000 * 100,2)
print("из 100 000 симуляций",numBDAYS," человек был")
print("совпадающий день рождения в этой группе",sim_match,"раз.это означает, что")
print("этих",numBDAYS,"у людей есть",probability, "% шанс")
print("отметить одинаковый день рождения в своей группе")
print("это и есть вероятность этого больше, чем вы могли бы подумать :)")



