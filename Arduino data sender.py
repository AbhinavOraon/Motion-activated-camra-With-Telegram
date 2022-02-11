
import serial
import time
port=serial.Serial("COM12",115200)
count=0
while True:
    line = port.readline() #read data line by line
    if line:
        string = line.decode()  # convert the byte string to a unicode string                                                                                                                                                                                                        
        num = int(string) # convert the unicode string to an int                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
        #print(num)
        if num==1:
            time.sleep(0.5)
            
           
        else:
            print("...")
        


            