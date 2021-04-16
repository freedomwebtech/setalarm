import datetime
from ai import audio
import os



a=audio().replace("hours","").replace("minutes","").replace(" ","").replace(".","").upper()
print(a)
while True:

    

    datetime1 = (datetime.datetime.today().strftime("%-I%M%p"))

    if a==datetime1:
        print("wakeup")
        os.system("sudo amixer cset numid=3 80% ")
        os.system("sudo mpg321 beautiful_guitar_ringtone.mp3")    
        break  
        

