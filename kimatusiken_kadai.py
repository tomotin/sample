import RPi.GPIO as GPIO
import Tkinter
GPIO.setmode(GPIO.BOARD)
LED=11
GPIO.setup(LED,GPIO.OUT,initial=GPIO.LOW)


p=GPIO.PWM(LED,100)
root=Tkinter.Tk()
led_val=Tkinter.DoubleVar()
led_val.set(0)
p.start(0)

def change_duty(dc):
    p.ChangeDutyCycle(led_val.get())
    
s=Tkinter.Scale(root,label='LED',orient='h',\
                from_=0,to=100,variable=led_val,command=change_duty)

def change_0():
    GPIO.output(LED,GPIO.LOW)
    led_val.set(0)
    p.ChangeDutyCycle(led_val.get())

root=Tkinter.Tk()
label=Tkinter.Label(root,text='PWM=0')
label.pack()

button=Tkinter.Button(root,text='0',command=change_0)

s.pack()
button.pack()
root.mainloop()
p.stop()
GPIO.cleanup()
