import RPi.GPIO as IO 
import time 
import Adafruit_CharLCD as LCD 
 
IO.setmode(IO.BCM) 
lcd_rs = 12 
lcd_en = 16 
lcd_d4 = 25 
lcd_d5 = 24 
lcd_d6 = 23 
lcd_d7 = 18 
lcd_backlight = 2 
lcd_columns =16 
lcd_rows = 2 
lcd = LCD.Adafruit_CharLCD(lcd_rs, lcd_en, lcd_d4, lcd_d5, lcd_d6, lcd_d7, lcd_columns, lcd_rows, lcd_backlight) 
 
Entry_pin = 19 
Exit_pin =21 
servo_pin=2 
 
IO.setmode(IO.BCM) 
IO.setwarnings(False) 
 
IO.setup(Entry_pin,IO.IN) 
IO.setup(Exit_pin,IO.IN) 
IO.setup(servo_pin,IO.OUT) 
 
pwm=IO.PWM(2, 50) 
pwm.start(0) 
def SetAngle(angle): 
 duty = angle / 18 + 2 
 IO.output(2, True) 
 pwm.ChangeDutyCycle(duty) 
 time.sleep(1) 
 IO.output(2, False) 
 pwm.ChangeDutyCycle(0) 
 
 
 
available_space = 5 
 
try: 
 while True: 
    if IO.input(Entry_pin) ==IO.HIGH: 
        if available_space > 0: 
         available_space -= 1 
         print("Vehicle has entered, Available Spaces:", available_space) 
         lcd.message('vacantspace ' + str(available_space)) 
         time.sleep(2) 
         lcd.clear() 
         SetAngle(0) 
         time.sleep(0.5) 
         SetAngle(90) 
         time.sleep(0.1) 
 
 
 else: 
     print("No Available Spaces. Entry Denied") 
     lcd.message('NO SPACE') 
     time.sleep(2) 
     lcd.clear() 
     time.sleep(1) 
 
 
 
 if IO.input(Exit_pin) ==IO.HIGH: 
    if available_space < 5: 
     available_space += 1 
     print("Vehicle has exited, Available Spaces:", available_space) 
     lcd.message('vacantspace ' + str(available_space)) 
     time.sleep(2) 
     lcd.clear() 
 
 else: 
     print("No Cars Exited") 
     time.sleep(2) 
 
 
except KeyboardInterrupt: 
 print("Interrupted By USER") 
 
finally: 
 IO.cleanup()
