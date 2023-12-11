from telethon  import TelegramClient, sync
import json
import time

# получаем TelegramClient с помощью api_id и api_hash
api_id = 27554330
api_hash = '28b416f2ead6f6dcda06b83f78d517d2'

client = TelegramClient('session_1', api_id, api_hash, system_version ='4.16.30-vxCUSTOM')

# подключаемся к Telegram
client.start()

# список тг каналов
#def main():
lines = ['https://t.me/comentlentach ', 'https://t.me/readovchat', 'https://t.me/chatzvz', 'https://t.me/Ateo_Chat', 'https://t.me/specchatZ']
ar = ['хохлы', 'хохлов', 'хохлам', 'хохлами', 'хохлах', 'укры', 'укр', 'украм', 'укров', 'украми', 'украх', 'укропы', 'укропов', 'укропам', 'укропов', 'укропами', 'укропах', 'ВСУшники', 'ВСУшников', 'ВСУшникам', 'ВСУшников', 'ВСУшниками', 'ВСУшниках', 'ВСУшник', 'ВСУшника', 'ВСУшнику', 'ВСУшника', 'ВСУшнику', 'ВСУшника', 'ВСУшником', 'ВСУшнике','хохол', 'хохла', 'хохлу', 'хохла', 'хохлом', 'хохле', 'хохлуши', 'хохлуш', 'хохлушам', 'хохлуш', 'хохлушами', 'хохлушах']
# создаем пустой список для хранения сообщени7979й
res = []

# проходим по каждому каналу в цикле
for channel in lines:
    print(channel)
    for  m in client.iter_messages(channel, limit=1000):
        if (m.text is not None) and ('реклама' not in m.text) and (len(m.text) != 0) and any(word in m.text for word in ar):
            #тут еще добавить
             res.append({"index": 1, "text": m.text})


             res.append(m.text)
        else:
                res.append({"index": 0, "text": m.text})

for channel in lines:

        channel_messages = client.get_messages(channel, limit=1000)


        for mes in channel_messages:
            res.append(mes.message)
           
    

with open('message.json', 'w', encoding='utf8') as w:
        json.dump(res, w, ensure_ascii=False)

#if __name__ == '__main__':
#    main()





#with open('res.json', 'w') as f:
#    json.dump(res, f)

# закрываем подключение к Telegram
#client.disconnect()