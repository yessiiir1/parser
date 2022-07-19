import pymorphy2
import re

'''morph = pymorphy2.MorphAnalyzer
def normal_str(input_str):
    word_list = input_str.split()
    res = []
    for word in word_list :
        p = morph.parse(word)[0]
        res.append(p.normal_form)
        return ' '.join(res)
m = input('enter something :')
normal_str(m)'''


print("Здравствуйте! О чем вы хотите напомнить?")
str = input('enter something :')
string =str.split()
print(string)
Month = {

    1: "января",
    2: "февраля",
    3: "марта",
    4: "апреля",
    5: "мая",
    6: "июня",
    7: "июля",
    8: "августа",
    9: "сентября",
    10: "октября",
    11: "ноября",
    12: "декабря"
}
Day = {
    1: "понедельник",
    2: "вторник",
    3: "среда",
    4: "четверг",
    5: "пятница",
    6: "суббота",
    7: "воскресенье",
}
if Month in string:
    print()




