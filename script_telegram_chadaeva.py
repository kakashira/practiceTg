#Разработать скрипт на пайтон с использованием библиотеки telethon для парсинга открытых ру чатов (5 штук разных, между собой чтобы они у вас не пересекались). 
# Задача: получить по 1000 последних постов из каждого канала и сохранить все вместе в файле формата json. 

#Пошагово:
#1) Импортировать зависимости telethon, json
#2) Получить TelegramClient через telethon
#3) Написать в массив список тг каналов
#4) В цикле по этому массиву получать через telethon сообщения каналов и накапливать их в отдельном списке
#5) Сохранить результат в файл с помощью json.dump

#Вторая часть задания: 
#Формат файла теперь будет такой: [{ "index": цифра, "text": текст}, {}, {}, {}].
#Проанализировать как выглядят посты с пророссийским содержанием и доработать программу, чтобы она по каким-либо признакам разделяла пророссийские и нейтральные посты, помечая index этого предложения как 1 - если пророссийское и 0 если нейтральное



import json
from telethon.sync import TelegramClient

import pymorphy3

# Вставляем api_id и api_hash
api_id = 28957893
api_hash = 'ab1ea375ed637f05abc4e1a7f3016280'
 
client = TelegramClient('session_4', api_id, api_hash, system_version='4.16.30-vxCUSTOM')
client.start()

morph = pymorphy3.MorphAnalyzer()

channels = ['https://t.me/kadyrov_95chat', 'https://t.me/specchatZ', 'https://t.me/ags_chat123', 'https://t.me/vswarvs', 'https://t.me/ru2chnews']
array = []
rusWords = ['хохлы', 'хохлуши', 'свиноботы', 'укры', 'укропы', 'хлопчик' 'российские патриоты', 'российские защитники', 'киевский режим', 'укроботы', 'ВСУчки', 'ВСУшники' ]
# ukrWords = ['рашисты', 'русня','россосия', 'рассея', 'российские террористы', 'оккупанты', 'оккупированные', 'оккупация', 'украинские защитники']

normalizedWords = [morph.parse(word)[0].normal_form for word in rusWords]

for channel in channels:
    for m in client.iter_messages(channel,limit=1000):
        if(m.text is not None) and ('реклама' not in m.text) and (len(m.text) != 0) and any(word in m.text for word in normalizedWords):    
            array.append({"index": 1, "text":m.text})
        else:
             array.append({"index": 0, "text":m.text})

with open('array_Tg.json', 'w', encoding='utf8') as file:
    json.dump(array, file, ensure_ascii=False)

client.disconnect()