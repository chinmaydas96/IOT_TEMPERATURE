import time
import subprocess
temp_address="/sys/bus/w1/devices/28-03160140daff/w1_slave"
print "hello mr BAT" 
while True:
        file=open(temp_address,"r")
        data=file.read()
        file.close()
        a=data.split()
        b=a[len(a)-1]
        reading=b[2:]
        temp=float(reading)/1000
        print("hello Mr CHINMAY")
        print ("room temperture="+str(temp)+"*C")  
        time.sleep(2) 
        subprocess.call("clear")
        
