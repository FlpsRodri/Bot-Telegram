import requests
import time


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
  

