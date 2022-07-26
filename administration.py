import vk_api
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType

# Функция вызывающая клавиатуру языки программирования для курсов
def language(user_id):
	keyboard = VkKeyboard(one_time=False)
	keyboard.add_button('C', color=VkKeyboardColor.PRIMARY)
	keyboard.add_button('C#', color=VkKeyboardColor.PRIMARY)
	keyboard.add_button('C++', color=VkKeyboardColor.PRIMARY)
	keyboard.add_line()
	keyboard.add_button('Python', color=VkKeyboardColor.PRIMARY)
	keyboard.add_button('java', color=VkKeyboardColor.PRIMARY)
	keyboard.add_line()
	keyboard.add_button('HTML и CSS', color=VkKeyboardColor.PRIMARY)
	keyboard.add_line()
	keyboard.add_button('Назад к направлениям', color=VkKeyboardColor.NEGATIVE)
	
	message = "Какой язык тебя интересует?"

	write_msg(user_id, message, keyboard)

# Функция вызывающее клавиатуру Меню (Самая первая вкладка)
def menu(user_id):
	keyboard = VkKeyboard(one_time=False)
	keyboard.add_button('Курсы', color=VkKeyboardColor.PRIMARY)
	keyboard.add_button('Форумы', color=VkKeyboardColor.PRIMARY)
	keyboard.add_line()
	keyboard.add_button('Конкурсы', color=VkKeyboardColor.PRIMARY)	
	keyboard.add_button('Гранты', color=VkKeyboardColor.PRIMARY)
	keyboard.add_line()
	keyboard.add_button('Стажировки', color=VkKeyboardColor.PRIMARY)
	keyboard.add_line()
	keyboard.add_button('Тех. поддержка', color=VkKeyboardColor.PRIMARY)

	message = "Выбери что тебя интересует 👇"

	write_msg(user_id, message, keyboard)

# Функция вызывающее направление курсов
def infa(user_id, message):
    keyboard = VkKeyboard(one_time=False)
    keyboard.add_button('Программирование', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Дизайн', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Менеджмент', color=VkKeyboardColor.PRIMARY)
    keyboard.add_line()
    keyboard.add_button('Назад', color=VkKeyboardColor.NEGATIVE)

    write_msg(user_id, message, keyboard)

# Функция, которая выводит текст который в неё передаётсяя
def write_msg(user_id, message, keyboard=None):
	# Если передали список кнопок выводим сообщение вместе с клавиатурой
	if keyboard != None:
		vk.method("messages.send",{'user_id': user_id, 'message': message, 'keyboard': keyboard.get_keyboard(), 'random_id': 0})
	# Если не передали список кнопок выводим просто текст 
	else:
		vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': 0})

#Функция для считывания сообщения от пользователя
def input_msg():
	for event in longpoll.listen():
		if event.type == VkEventType.MESSAGE_NEW:
			if event.to_me:
				rtrn = event.text
				break
		return rtrn

def adm(request, user_id):
	# Неизменяемое стартовое сообщение
	start_message = """Привет \nЯ чат-бот Светик! Я расскажу тебе обо всех образовательных программах, а также форумах, грантах и конкурсах нашей страны.
	\n\nВы вошли под аккаунтом Администратора"""		

	match request:
		case "Привет":
			write_msg(user_id, start_message)
			menu(user_id)

		case "Начать":
			write_msg(user_id, start_message)
			menu(user_id)
						
		case "Форумы":
			keyboard = VkKeyboard(one_time=False)
			keyboard.add_button('Назад', color=VkKeyboardColor.NEGATIVE)
			keyboard.add_line()
			keyboard.add_button('Изменить Форумы', color=VkKeyboardColor.NEGATIVE)
							
			file = open('forum.txt', encoding='utf-8')
						
			message = file.read()
							
			write_msg(user_id, message, keyboard)

			file.close()

		case "Гранты":
			keyboard = VkKeyboard(one_time=False)
			keyboard.add_button('Назад', color=VkKeyboardColor.NEGATIVE)
			keyboard.add_line()
			keyboard.add_button('Изменить Гранты', color=VkKeyboardColor.NEGATIVE)
							
			file = open('grants.txt', encoding='utf-8')
			message = file.read()
							
			write_msg(user_id, message, keyboard)

			file.close()

		case "Стажировки":
			keyboard = VkKeyboard(one_time=False)
			keyboard.add_button('Назад', color=VkKeyboardColor.NEGATIVE)
			keyboard.add_line()
			keyboard.add_button('Изменить Стажировки', color=VkKeyboardColor.NEGATIVE)
							
			file = open('internships.txt', encoding='utf-8')
			message = file.read()
							
			write_msg(user_id, message, keyboard)

			file.close()

		case "Тех. поддержка":
			keyboard = VkKeyboard(one_time=False)
			keyboard.add_button('Назад', color=VkKeyboardColor.NEGATIVE)

			message = "Вы можете предложить нам новые идеи, рекомендации по развитию нашего бота, недочёты во время его использования. \nДля этого перейдите, пожалуйста, в обсуждение:\nhttps://vk.com/topic-214145803_48910633"

			write_msg(user_id, message, keyboard)

		case "Конкурсы":
			keyboard = VkKeyboard(one_time=False)
			keyboard.add_button('Назад', color=VkKeyboardColor.NEGATIVE)
							
			file = open('contests.txt', encoding='utf-8')
			message = file.read()
							
			write_msg(user_id, message, keyboard)

			file.close()

		case "Курсы":
			message = "Здесь ты можешь узнать про 👇"
			infa(user_id, message)

		case "Менеджмент": 
			keyboard = VkKeyboard(one_time=False)
			keyboard.add_button('Назад к направлениям', color=VkKeyboardColor.NEGATIVE)
			keyboard.add_line()
			keyboard.add_button('Изменить Менеджмент', color=VkKeyboardColor.NEGATIVE)

			file = open('Management.txt', encoding='utf-8')
			message = file.read()

			write_msg(user_id, message, keyboard)

			file.close()

		case "Дизайн":
			keyboard = VkKeyboard(one_time=False)
			keyboard.add_button('Назад к направлениям', color=VkKeyboardColor.NEGATIVE)
			keyboard.add_line()
			keyboard.add_button('Изменить Дизайн', color=VkKeyboardColor.NEGATIVE)

			file = open('Desing.txt', encoding='utf-8')
			message = file.read()

			write_msg(user_id, message, keyboard)

			file.close()

		case "Программирование":
			language(user_id)

		case "Python":
			keyboard = VkKeyboard(one_time=False)
			keyboard.add_button('Назад к языкам', color=VkKeyboardColor.NEGATIVE)
			keyboard.add_line()
			keyboard.add_button('Изменить Python', color=VkKeyboardColor.NEGATIVE)

			file = open('Python.txt', encoding='utf-8')
			message = file.read()

			write_msg(user_id, message)

			file.close()
							
		case "C++":
			keyboard = VkKeyboard(one_time=False)
			keyboard.add_button('Назад к языкам', color=VkKeyboardColor.NEGATIVE)
			keyboard.add_line()
			keyboard.add_button('Изменить С++', color=VkKeyboardColor.NEGATIVE)

			file = open('C++.txt', encoding='utf-8')
			message = file.read()

			write_msg(user_id, message, keyboard)

			file.close()

		case "java":
			keyboard = VkKeyboard(one_time=False)
			keyboard.add_button('Назад к языкам', color=VkKeyboardColor.NEGATIVE)
			keyboard.add_line()
			keyboard.add_button('Изменить java', color=VkKeyboardColor.NEGATIVE)

			file = open('java.txt', encoding='utf-8')
			message = file.read()

			write_msg(user_id, message, keyboard)

			file.close()

		case "C":
			keyboard = VkKeyboard(one_time=False)
			keyboard.add_button('Назад к языкам', color=VkKeyboardColor.NEGATIVE)
			keyboard.add_line()
			keyboard.add_button('Изменить С', color=VkKeyboardColor.NEGATIVE)

			file = open('C.txt', encoding='utf-8')
			message = file.read()

			write_msg(user_id, message, keyboard)

			file.close()

		case "C#":
			keyboard = VkKeyboard(one_time=False)
			keyboard.add_button('Назад к языкам', color=VkKeyboardColor.NEGATIVE)
			keyboard.add_line()
			keyboard.add_button('Изменить С#', color=VkKeyboardColor.NEGATIVE)
							
			message = "Пока что нет информации, но это временно"
							
			write_msg(user_id, message, keyboard)

		case "HTML и CSS":
			keyboard = VkKeyboard(one_time=False)
			keyboard.add_button('Назад к языкам', color=VkKeyboardColor.NEGATIVE)
			keyboard.add_line()
			keyboard.add_button('Изменить HTML и CSS', color=VkKeyboardColor.NEGATIVE)

			file = open('HTML_CSS.txt', encoding='utf-8')
			message = file.read()

			write_msg(user_id, message, keyboard)

			file.close()
						
		case "Назад к языкам":
			language(user_id)

		case "Назад к направлениям":
			message = "Какое направление тебя интересует?"
			infa(user_id, message)

		case "Назад":
			menu(user_id)

		case "Изменить Python":
			message = 'Эта функция временно не работает'

			write_msg(user_id, message)

		case "Изменить С++":
			message = 'Эта функция временно не работает'

			write_msg(user_id, message)

		case "Изменить java":
			message = 'Эта функция временно не работает'

			write_msg(user_id, message)
		
		case "Изменить С":
			message = 'Эта функция временно не работает'

			write_msg(user_id, message)
		
		case "Изменить С#":
			message = 'Эта функция временно не работает'

			write_msg(user_id, message)
		
		case "Изменить HTML и CSS":
			message = 'Эта функция временно не работает'

			write_msg(user_id, message)

		case "Изменить Дизайн":
			message = 'Эта функция временно не работает'

			write_msg(user_id, message)

		case "Изменить Менеджмент":
			message = 'Эта функция временно не работает'

			write_msg(user_id, message)

		case "Изменить Конкурсы":
			message = 'Эта функция временно не работает'

			write_msg(user_id, message)
		
		case "Изменить Форумы":
			message = 'Эта функция временно не работает'

			write_msg(user_id, message)

		case "Изменить Гранты":
			message = 'Эта функция временно не работает'

			write_msg(user_id, message)



# API-ключ созданный ранее
token = "vk1.a.tNB73Y7VJDG5aZASqDSRnjH08B4yF_dGcVlCtozJAbBTKNzz6AwFEsfiG_y9ovTaNhgNxi-4Rj0AXmzeHPlolqPcjdI0T278xW-XUxVHhDZGu4SWOMaUbNzTaGMe_0UypDbauAqXHKZl4TxAeA7tpHGtWu1co0tahtoDndKfDED0TfnFNoegLzaDNALf1xSa"
# Авторизовываемся как сообщество
vk = vk_api.VkApi(token=token) 
# Работа с сообщениями
longpoll = VkLongPoll(vk_api.VkApi(token=token))