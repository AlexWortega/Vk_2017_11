import requests
import vk
from config import token
import speechkit
import voice
from random import choice

token = "55308ec062b6fa585d8e6704a87e1562146787104e2221958e91facbf66133a8f9bd16511820ad1044a80"
url = "https://api.vk.com/method/METHOD_NAME?PARAMETERS&access_token=ACCESS_TOKEN&v=V "
session = vk_api.Session(access_token=token)
vk_api = vk_api.API(session)
vk_api.users.get(user_id=1)
group_name = voice.recognize(3, lang='ru-RU')
print(group_name)
name_list = (q=group_vk_api.groups.searchname, count=1, v=2.02`)
search = name_list['items'][0]['screen_name']
text = voice.recognize(3)
records = vk_api.wall.search(domain=search, query=text, v=5.68, count=100)
print(text+" ")
print(group_name)

for i in range(10):
try:
random_record = choice(records['items'])

    voice.say(random_record['text'])
except:
    pass
