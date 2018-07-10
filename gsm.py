import serial 
import time 
def gsm(msg):
    port= serial.Serial("/dev/ttyS0",9600,timeout=3.0)
    port.write('AT\r')
    rcv = port.read(20) 
    print"GSM" + rcv
    try:
        print 'Sending message ...'
        port.write('AT+CMGF=1'+'\r')
        number=raw_input("Enter mobile number: ")  
        port.write('AT+CMGS="'+number+'"\r\n')  
        time.sleep(2)
        print msg
        j=msg
        port.write(j)
        print '\n\n\n\nVEHICLE NO: =', j,'\n\n'
        time.sleep(2)  
        port.write('\x1A\r\n')  
        print port.read(50)
    except:
        port.close()
    print 'done'
