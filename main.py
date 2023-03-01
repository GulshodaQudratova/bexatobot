import re
def has_cyrillic(text):
    return bool(re.search('[\u0400-\u04FF]', text))
from function import to_cyrillic
print(to_cyrillic('G‘'))
import requests
BASE_URL='https://gulshoda.up.railway.app//api'
import json
def get_user():
    response=requests.get(url=BASE_URL)
    rest=json.loads(response.text)
    print(rest)
def create_user(name,telegram_id):
    response=requests.post(url=BASE_URL,data={'name':name,'telegram_id':telegram_id})
    return 'ok'