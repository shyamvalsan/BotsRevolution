import sys
import subprocess
import telepot
import time
import os

def handle(msg):
	chat_id = msg['chat']['id']
	command = msg['text']

	words = command.split()
        str = ' '.join(words[1:999])      

	if words[0] == '/speak':
		os.system("/home/pi/dev/TTS/speak %s" % str)
 		bot.sendMessage(chat_id, "ack")
        elif words[0] == '/play':
		os.system("/home/pi/pi/dev/youtube-music/play-from-youtube.sh %s &" % str)
        elif words[0] == '/photo':
 		filename = 'sendimg' + '.jpg'
                os.system('raspistill -o ' + filename)
                img = open('IMG_01.jpg', 'rb')
                bot.sendPhoto(chat_id, img)
                img.close()
                bot.sendMessage(chat_id,"ack")
	elif words[0] == '/stop':
		os.system("kill -9 `cat /home/pi/dev/telegrambot/pidfile`")
                bot.sendMessage(chat_id,"ack")
        else:
 		bot.sendMessage(chat_id, "nack")

bot = telepot.Bot('322060273:AAHjszgt4w95TKgGMtpAN-I1Nbv7VA7-5Lg')
bot.message_loop(handle)

while 1:
	time.sleep(10)
