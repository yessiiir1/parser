import re
import datetime
from datetime import timedelta, datetime

text = "Сходить      покушать   на    неделе в 13:13"


def inst(word):
	ob = re.sub(r'\s+|_|\*', ' ', word)
	return ob


m = ['января', 'февраля', 'марта', 'апреля', 'мая', 'июня', 'июля', 'августа', 'сентября', 'октября', 'ноября', 'декабря'] #month
d = ['дня', 'день', 'дней'] #day
k = ['минут', 'минуты', 'часа', 'часов', 'число'] #key
mi = ['минут', 'минуты', 'минуту'] #minutes
h = ['часа', 'часов', 'час'] #hours
tk = ['через', 'Через', 'каждые', 'Каждые', 'каждое', 'Каждое', 'каждый', 'Каждый', 'каждую' , 'Каждую', 'в', 'В', 'к', 'К'] #time_key
dw = ['понедельник', 'вторник', 'среду', 'четверг', 'пятницу', 'субботу' ,'воскресенье'] #days_of_week
ch = ['через'] #cherez
c = ['через', 'завтра', 'утром', 'на', 'по'] #check

smth = ['неделе', 'году', 'год', 'неделю', 'месяце', 'месяц']

now = datetime.now()

def Date(thing):
	day = now.day
	month = now.month
	mins = ''
	hours = ''
	minutes = ''
	obs = ''
	time = ''
	year = now.year
	text = thing.split()
	try:
		for word in text:

			# проверка дней недель
			if word in dw:
				day = word
				for i in range(len(dw)):
					if day == day[i]:
						day = datetime.weekday(day)



			# проверка дней и месяцов
			try:
				if word.isdigit() and text[text.index(word) + 1] in m:
					# print(thing)
					day = str(word)
					for i in range(len(m)):
						if text[text.index(word) + 1] == m[i]:
							month = i + 1


			except Exception as ex:
				print(ex)
			#все связанное с через
			if word in ch:
				#час
				if text[text.index(word) + 1] in h:
					print(text[text.index(word) + 1])
					mins = now + timedelta(hours=1)
					print(mins)
					mins = mins.time()
					print(mins)
					hours = mins.hour
					minutes = mins.minute
					if now.time() > mins:
						day = now + timedelta(days=1)
						day = day.day
						print(day)

				#  2 дня(10 дней)
				if text[text.index(word) + 2] in d:
					day = now + timedelta(days=int(text[text.index(word) + 1]))
					print(day)
					day = day.day
					print(day)
					mins = '12:00'

				#22 минуты
				if text[text.index(word) + 2] in mi:
					a = now + timedelta(minutes=int(text[text.index(word) + 1]))
					a = a.time()
					hours = a.hour
					minutes = a.minute
					mins = str(hours) + ':' + str(minutes)
					if now.time() > a:
						day = now + timedelta(days=1)
						day = day.day
						print(day)

				#2 часа
				if text[text.index(word) + 2] in h:  # and text[text.index(item) + 3].isdigit() == False:
					mins = now + timedelta(hours=int(text[text.index(word) + 1]))
					mins = mins.time()
					hours = mins.hour
					minutes = mins.minute
					mins = str(hours) + ':' + str(minutes)

				#2 часа 30 минут
				if text[text.index(word) + 2] in h and text[text.index(word) + 3].isdigit():
					mins = now + timedelta(hours=int(text[text.index(word) + 1]),
										   minutes=int(text[text.index(word) + 3]))
					mins = mins.time()
					hours = mins.hour
					minutes = mins.minute
					mins = str(hours) + ':' + str(minutes)

			if 'утром' in word:
				print(1)
				mins = '09:00'

			if 'днем' in word:
				print(1)
				mins = '13:00'

			if 'вечером' in word:
				print(1)
				mins = '18:00'

			if 'завтра' in word:
				day = now.today() + timedelta(days=1)
				day = day.day
				mins = '12:00'

			# год
			if word.isdigit() and (2000 <= int(word)):
				year = word

			# время записывается в mins
			if ':' in word:
				mins = word
				time = datetime.strptime(mins, '%H:%M')

				if ((time.time() <= now.time()) and (day == now.day)):
					day = now.today() + timedelta(days=1)
					day = day.day


	except Exception as ex:
		print(ex)
	print(day, month, year, mins)
	return [day, month, year, mins, obs]


def Time(word):
	try:
		for object in word.split(' '):

			try:
				if object in tk or object.isdigit() or (
						object in ch and word.split()[word.split().index(object) + 1] in smth):
					time_case = ' '.join(word.split()[word.split().index(object):])
					info = Date(time_case)
					state = 'SUCCESS'

					try:
						data = {'STATUS': state,
								'DATE': {
									'year': info[2],
									'month': info[1],
									'day': info[0],
									'time': {
										'hours': info[3].split(':')[0],
										'minutes': info[3].split(':')[1]
									},
									'Доп.сведения': info[-1]},
								'текст': ' '.join(word.split()[:word.split().index(object)])
								}
					except:

						data = {'STATUS': state,
								'DATE': {
									'year': info[2],
									'month': info[1],
									'day': info[0],
									'time': {
										'hours': '',
										'minutes': ''
									},
									'Доп.сведения': info[-1]},
								'текст': ' '.join(word.split()[:word.split().index(object)])
								}

					return data

			except Exception as ex:
				print(ex)
				state = 'ERROR'
				data = {'STATUS': state}
				return data

	except:
		pass


text_0 = "позвонить через час"
text_1 = "Проснуться, улыбнуться, почистить зубы и помыться в 07:13"
text_2 = "Съездить на дачу 17 мая в 16:15"
text_3 = 'Подписать служебку у начальника 13 декабря 2021 года в 16:15'
text_4 = "Убраться в квартире через 90 минут"
text_5 = "Позвонить друзьям через 3 часа"
text_6 = "Приготовить покушать на 2-3 дня 3 сентября 2022 года в 06:01"
text_7 = "Перевод локального компьютера в режим гибернации завтра"
text_8 = "Выключить 13 декабря в 20:17"
text_9 = "Перевод локального компьютера в режим гибернации через 2 дня"
text_10 = 'Служебку подписать на питон 12 ноября утром'
text_11 = 'Служебку подписать на питон в четверг в 20:17'
text_12 = 'Служебку подписать на питон в среду'
text_13 = 'Служебку в отдел кадров в среду в 13:13'
text_14 = "В понедельник уроки"
text_15 = 'Поскольку все записи имеют один и тот же шаблон, внести данные, которые хотите извлечь из пары скобок 13 декабря 2022 года в 16:15'

text_16 = "Напомни про гречку через 14 минут"
text_17 = "Через 50 минут таймер установаить. дерзай"
text_18 = "Основы Python в четверг 15:00 3 сентября 2022 года"
text_19 = " Основы Python в четверг 15:00 в среду 15:00 "
text_22 = "Сходить покушать на неделе в 13:13"
text_23 = "del_qustion_answer*как дела?*норма, как сам?"
text_24 = "Сходить покушать на неделе"
text_25 = "В следующем месяце Подписать служебку "
text_26 = "\d\de23 2\3 3r3556"
text_27 = "Подписать служебку по выходным"
text_28 = "Сходить в сауну каждое 28 число"
text_29 = "Подписать служебку по выходным в 20:19"
text_30 = "поздравить с др маму через год в 20:18"
text_31 = "поздравить с др маму через час"
text_32 = "тренировка каждый час в 20:19"
text_33 = "Подписать служебку 23 февраля"
text_34 = "Тренировка каждый понедельник"
text_35 = "Тренировка каждый год"

for item in list(range(0, 36)):
	try:
		print('-------------------')
		text = inst(globals()[f'text_{item}'])
		print(Time(text))
		print(globals()[f'text_{item}'].strip())
	except:
		pass


