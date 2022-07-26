import vk_api
from vk_api.utils import get_random_id
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
from vk_api.longpoll import VkLongPoll, VkEventType
from polzovatel import polz
from administration import adm


# API-ключ созданный ранее
token = ""
# Авторизовываемся как сообщество
vk = vk_api.VkApi(token=token) 
# Работа с сообщениями
longpoll = VkLongPoll(vk_api.VkApi(token=token))

# Неизменяемое стартовое сообщение
start_message = "Привет \nЯ чат-бот Светик! Я расскажу тебе обо всех образовательных программах, а также форумах, грантах и конкурсах нашей страны."""


for event in longpoll.listen(): # Основной цикл

	if event.type == VkEventType.MESSAGE_NEW: # Если пришло новое сообщение    
		if event.to_me:  # Если оно имеет метку для меня (то есть бота)

			request = event.text # Сообщение от пользователя   
			user_id = event.user_id # id пользователя
			
			# Здесь будут храниться id всех Админов
			id_admin = open('forum.txt', encoding='utf-8')


			# Проверка на то является ли пользователь Администратором
			if user_id in id_admin:
				polz(request, user_id)
			
			else:
				adm(request, user_id)