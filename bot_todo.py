import random
import telebot


random_tasks = ['работать', 'пройтись', 'петь']

help = """\
Доступные команды:
/help - справка
/add - добавить задачу
/print - показать список задач
/random - добавить случайную задачу
"""

print('Bot starting...')

TOKEN = '1832624548:AAE2EQyu357qCs_m71sYFQqExq3OH3HLrCc'

bot = telebot.TeleBot(TOKEN)

task_list = {}



def add_task(date, task):
  if date in task_list:
    task_list[date].append(task)
  else:
    task_list[date] = [task]


@bot.message_handler(commands=['help', 'HELP'])
def show_help(message):
  bot.send_message(message.chat.id, help)


@bot.message_handler(commands=['random'])
def random_task(message):
  date = message.text.split(' ')[1]
  task = random.choice(random_tasks)
  add_task(date, task)
  bot.send_message(message.chat.id, f'Случайная задача {task} добавлена на {date}')

@bot.message_handler(commands=['print'])
def print_task(message):
  date = message.text.split(' ')[1]
  if date in task_list:
    text = f'Tasks for {date}:\n'
    for t_do in task_list[date]:
      text = text + f'\n— {t_do.title()}'
    bot.send_message(message.chat.id, text)
  else:
    bot.send_message(message.chat.id, f'У вас нет задач на {date}.')

@bot.message_handler(commands=['add'], content_type=['text'])
def add(message):
  splitter = message.text.split(' ', maxsplit=2)
  date = splitter[1]
  task = splitter[2]
  add_task(date, task)
  bot.send_message(message.chat.id, f'Задача {task} добавлена на {date}.')


bot.polling(none_stop=True)