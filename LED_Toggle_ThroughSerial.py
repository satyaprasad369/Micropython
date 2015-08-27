# A simple Python program to toggle LED's on Micropython board using
# serial communcation. LED1-4 are toggled in sequence
import serial   #This module provides the necessary functions for communicaiton
import time     #This module provides the delay functions used in the program

#Global Variables
ser = 0

#Function to Initialize the Serial Port
def init_serial():
    COMNUM = 1              #Enter Your COM Port Number Here.
    global ser              #Must be declared in Each Function
    ser = serial.Serial()
    ser.baudrate = 9600
    ser.port = COMNUM - 1   #COM Port Name Start from 0
    
    #Specify the TimeOut in seconds, so that SerialPort
    #Doesn't hangs
    ser.timeout = 10
      
    #Opens SerialPort dont forget to close the COM port 
    #at the end of program
    ser.open()

    # print port open or closed
    if ser.isOpen():
        print ('Open: ' + ser.portstr)
    else:
        print ('Serial port is not available\n')
 #serial initilization complete       

#Call the Serial Initilization Function, Main Program Starts from here
init_serial()

freq = 0.1 #Frequenc
timeDelay = 0.01
loops=100

temp='import pyb\r'             #importing PYB module, "\r" is required
ser.write(str(temp).encode())   #Writes to the SerialPort
time.sleep(timeDelay)           #Delay before sending next command

temp='myled1=pyb.LED(1)\r'      #Assigning LED1
ser.write(str(temp).encode())   #Writes to the SerialPort
time.sleep(timeDelay)

temp='myled2=pyb.LED(2)\r'      #Assigning LED2
ser.write(str(temp).encode())   #Writes to the SerialPort
time.sleep(timeDelay)

temp='myled3=pyb.LED(3)\r'      #Assigning LED3
ser.write(str(temp).encode())   #Writes to the SerialPort
time.sleep(timeDelay)

temp='myled4=pyb.LED(4)\r'      #Assigning LED4
ser.write(str(temp).encode())   #Writes to the SerialPort
time.sleep(timeDelay)

while loops:    
    bytes = ser.readline()            #Read from Serial Port
    print ('You sent: ' + str(bytes)) #Print What is Read from Port
    temp1='myled1.toggle()'
    temp3='\r'
    time.sleep(freq)
    ser.write(str(temp1).encode()+str(temp3).encode()) #Writes to the SerialPort
    temp2 = 'myled2.toggle()'
    time.sleep(freq)
    ser.write(str(temp2).encode()+str(temp3).encode()) #Writes to the SerialPort
    temp4 = 'myled3.toggle()'
    time.sleep(freq)
    ser.write(str(temp4).encode()+str(temp3).encode()) #Writes to the SerialPort
    temp5 = 'myled4.toggle()'
    time.sleep(freq)
    ser.write(str(temp5).encode()+str(temp3).encode()) #Writes to the SerialPort
    loops-=1 #Decrement loops by one
    #End of while loop

ser.close()  #closing serial port
# 
