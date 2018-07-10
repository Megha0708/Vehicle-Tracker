import RPi.GPIO as GPIO
import time
def ultrasonic():
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    TRIG= 23
    ECHO= 24
    pulse_end=0
    pulse_end0=0
    total_distance=0
    velocity=0
    speed=0
    distance0=0
    total_speed=0
    total_velocity=0
    samp=50
    print'Distance measurement in Progress.......Tracking the vehicle'
    GPIO.setup(TRIG,GPIO.OUT)
    GPIO.setup(ECHO,GPIO.IN)
    for x in range(0,samp):
     GPIO.output(TRIG,False)
     print'Waiting for sensor to settle'
     time.sleep(2)
     GPIO.output(TRIG,True)
     time.sleep(0.00001)
     GPIO.output(TRIG,False)
     pulse_end0=pulse_end
     while GPIO.input(ECHO)==0:
       pulse_start= time.time()
     while GPIO.input(ECHO)==1:
       pulse_end= time.time()
     pulse_duration= pulse_end-pulse_start
     distance= pulse_duration*17150
     distance= round(distance,2)
##     total_distance=total_distance + distance
     if distance>2 and distance<200:
       print'Distance:', distance- 0.5,'cm'
     else:
       print' Out of Range'
     velocity=(distance-distance0)/(pulse_end-pulse_end0)
     speed=abs(velocity)
     speed=round(speed,2)
     distance0=distance
##     total_speed += speed
##     total_velocity += velocity
##     print' /n/nAverage speed= ',int(total_speed/samp),'/n Average velocity= ',int(total_velocity/samp),'cm/s'
     print 'SPEED ', speed
##    return int(total_velocity/samp),int(total_speed/samp)
     if(speed>40):
         break
    return speed

