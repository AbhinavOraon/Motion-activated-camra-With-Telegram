''''
     Author@=Abhinav Etwa Oraon
     youtube=Omega Electronics
     created on 10 feb 2022
'''
import cv2 #pip inatall opencv-python
import datetime
import time
import telegram#pip install telegram-python
import serial#pip install pyserial

TELEGRAM_BOT_TOKEN = '5276243407:AAEsevcPv34Z3GetAV88vB1mVMADP-IPpTc'#paste your bot token
TELEGRAM_CHAT_ID = '1398078283'#paste  your chat id

def Send_telegram():
    bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
    bot.send_message(chat_id=TELEGRAM_CHAT_ID, text="INTRUDER IN ROOM ALERT!")
    bot.send_photo(chat_id=TELEGRAM_CHAT_ID, photo=open(PHOTO_PATH, 'rb')) 
    print("Photo clicked and sent to telegram")


port_num="COM12"#port number in which your arduino is connected
baud_rate=115200#speed throw which data will communicate as speed in arduino program
port=serial.Serial(port_num,baud_rate)
cap = cv2.VideoCapture(0)#0 is adress of webcam of pc
while True:                   
    _, frame = cap.read()
    original_frame = frame.copy()#make a copy of original frame
    line = port.readline() #read data line by line
    if line:
        string = line.decode()  # convert the byte string to a unicode string                                                                                                                                                                                                        
        num = int(string) # convert the unicode string to an int                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
        #print(num)
        if num==1:#if data is 1 
            time.sleep(0.5)

            time_stamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')#get current date day time
            file_name = f'Burglar-{time_stamp}.jpg'#unique name of image generated
            cv2.imwrite(file_name, original_frame)#it accept name of image and data
            PHOTO_PATH =file_name

            time.sleep(3)
            Send_telegram()
        else:
            print(".")   
   