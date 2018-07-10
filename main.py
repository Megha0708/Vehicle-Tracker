import ultrasonic
import accelerometer
import icamera
import time
import gsm

print '\n\n...................VEHICLE TRACKER..............\n\n\n'
##velocity,speed = ultrasonic.ultrasonic()
speed = ultrasonic.ultrasonic()

if(speed>40):
	print '\n\nRule Break : Out of speed\n\n'
##x,y,z=accelerometer. accelerometer()
        stri=str(time.time())+'.jpg'
        no_plate=icamera.mycamera(stri)
#no_plate=' '
        p=no_plate
        gsm.gsm(p)
opt=raw_input('Do you want to search a particular vehicle? : (y/n)')
if opt=='y' :
	no_plate_check=input('Enter vehicle no : ')
	if no_plate==no_plate_check :
		print 'Found'
	else : 
		print 'Not found'
else:
        print 'ok'

print '\n\nODD...EVEN\n\n'

if ((int)(no_plate))%2==0 :
        print '\n\nEVEN VEHICLE NO\n\n'
else:
        print '\n\nODD VEHICLE NO\n\n'
