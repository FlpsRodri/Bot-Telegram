import requests
import time

token = "5598127327:AAF6iJjgwlnUNwsZdOGbvHFw6xmX81PU99A"

chat_id = "1022539399"



def send_message(message):
  url = "https://api.telegram.org/bot"+token+"/sendMessage?chat_id="+chat_id+"&text="
  result = requests.get(url+message)
  return print("ok")

inicio = time.time()

send_message("Bot iniciado")
min = 2
while True:
  now = time.time()
  
  if (now - inicio) > 120 :
    inicio = now
    send_message("passou "+str(min)+" minutos")
    min += 2
  

