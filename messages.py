hello = 'Добрый день, {name}\n'
start = 'Все доступные функции используются в определенных чатах, не обижайся'
help = start
error = 'Ошибка'
joke_another_type = 'Только gif и картинки'
wait = '⏳ Надо немного подождать'
limit_advice_is_over = 'К сожалению, только {limit} советов в день. До завтра!'
limit_joke_is_over = 'К сожалению, только {limit} шуток в день на весь чат. До завтра!'
only_private = 'Ошибка, напишите мне в личные сообщения что бы пользоваться командой'
only_one_vote = 'Голосовать только один раз 😡'
delete_template = '''\
{text}

<i>Сообщение будет удалено через {time} секунд</i>'''
advice_template = '''\
{name}, {advice}

<i>Получить совет</i> /advice'''
not_for_self = 'Только не себя 😶'
not_for_me = 'Только не меня'
like_select = '''\
{user} предлагает похвалить {likes}

Да - {yes}{list_yes}

Нет - {no}{list_no}

Давайте проголосуем
<i>Голосование завершится через {time} минуты</i>'''
dislike_select = '''\
{user} предлагает поругать {likes}

Да - {yes}{list_yes}

Нет - {no}{list_no}

Давайте проголосуем
<i>Голосование завершится через {time} минуты</i>'''
like_result_yes = '''\
{likes} - Молодец! Добра в карму насыпали!

Да - {yes}{list_yes}

Нет - {no}{list_no}'''
dislike_result_yes = '''\
{likes}, подумай над своим поведением...

Да - {yes}{list_yes}

Нет - {no}{list_no}'''
like_result_no = '''\
{likes} - Не такой уж и достойный, в следующий раз

Да - {yes}{list_yes}

Нет - {no}{list_no}'''
dislike_result_no = '''\
{likes}, сегодня простили, но завтра новый день

Да - {yes}{list_yes}

Нет - {no}{list_no}'''
like = '''\
{name} - молодец!
Добавим в карму добра!'''
dislike = '{name}, ну как так то? Ну сколько можно?'
new_chat = '''\
Рад приветсвовать всех в чате <b>{name}</b>

Нас тут <b>{count}</b>

Давайте знакомиться и все дружно нажмём {command}'''
karma = '''\
Вот такая ситуация в чате <b>{name}</b>
{text}'''
like_keyboard = '{name}, кого будем хвалить?'
dislike_keyboard = '{name}, кто себя плохо вёл?'
only_admin = 'Только администратор'
not_for_you = 'Это не ваше голосование'
admin_not_me = 'Кто, кто, но только не я'
admin_not_admin = 'Кто, кто, но только не главный админ'
new_admin = 'А у нас новый админ - {name}'
delete_admin = 'Ну значит за дело - {name}'
bye = 'Прощай {name}'
admin_list = '''\
Список админов
{text}'''
user_list = '''\
Список пользователей
{text}'''
chat_list = '''\
Ваша карма в чатах:
{text}
'''
user_chat_list = '''\
<b>{name}</b>
{text}'''
user_karma = '{name} <b>{karma}</b>'
super_admin_commands = '''\
Ты главный админ и можешь добавлять бота в другие чаты и использовать команды:
/admin - Назначить админа, просто сделай reply сообщения пользователя, которого хочешь сделать админом, отправив команду /admin@{username}
/admins - Посмотреть всех админов
/users - Посмотреть всех пользователей во всех чатах
/admin_delete - Разжаловать админа, просто сделай reply сообщения пользователя, которого хочешь разжаловать, отправив команду /admin_delete@{username}'''
admin_commands = '''\
Ты админ и можешь добавлять бота в другие чаты и использовать команды:
/admin - Назначить админа, просто сделай reply сообщения пользователя, которого хочешь сделать админом, отправив команду /admin@{username}
/admin_delete - Разжаловать админа, просто сделай reply сообщения пользователя, которого хочешь разжаловать, отправив команду /admin_delete@{username}'''
random_like = 'Вот хорошо сказал, держи лайк!'
random_dislike = 'Сначала думаешь, потом говоришь, сегодня дизлайк, друг...'


MESSAGES = {
        'hello': hello,
        'start': start,
        'help': help,
        'error': error,
        'like': like,
        'dislike': dislike,
        'new_chat': new_chat,
        'karma': karma,
        'like_keyboard': like_keyboard,
        'only_admin': only_admin,
        'dislike_keyboard': dislike_keyboard,
        'admin_not_me': admin_not_me,
        'new_admin': new_admin,
        'admin_not_admin': admin_not_admin,
        'delete_admin': delete_admin,
        'admin_list': admin_list,
        'bye': bye,
        'user_list': user_list,
        'user_chat_list': user_chat_list,
        'user_karma': user_karma,
        'super_admin_commands': super_admin_commands,
        'admin_commands': admin_commands,
        'chat_list': chat_list,
        'joke_another_type': joke_another_type,
        'wait': wait,
        'delete_template': delete_template,
        'limit_advice_is_over': limit_advice_is_over,
        'limit_joke_is_over': limit_joke_is_over,
        'advice_template': advice_template,
        'only_private': only_private,
        'not_for_you': not_for_you,
        'like_select': like_select,
        'only_one_vote': only_one_vote,
        'like_result_yes': like_result_yes,
        'like_result_no': like_result_no,
        'dislike_select': dislike_select,
        'dislike_result_yes': dislike_result_yes,
        'dislike_result_no': dislike_result_no,
        'not_for_self': not_for_self,
        'not_for_me': not_for_me,
        'random_like': random_like,
        'random_dislike': random_dislike,

}







