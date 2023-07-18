import serial
import time
import math
import struct
from inputimeout import inputimeout

arduino = serial.Serial(port='COM19',  baudrate=115200, timeout=.1)
x=0
y=0
d=0

dragging=False

balls = [
    [0,0,1,1], [1.5, 0, 1.5, 1]
]

REV = 1600
RAYON = 1.6
EMPIRICAL = 5.02

########## EVIDEMMENT CHANGER ###########
X_MIN = -30
X_MAX = 150
Y_MIN = -20
Y_MAX = 20
#########################################

def convertXtoSteps(x):
    return int((2*EMPIRICAL*x/(RAYON*math.pi))*REV)  #x in cm

def convertYtoSteps(y):
    return int(((EMPIRICAL*y/(RAYON*math.pi))*REV))  #y in cm

def stepsToX(s):
    return (RAYON*math.pi*s)/(2*EMPIRICAL*REV) #cm

def stepsToY(s):
    return (RAYON*math.pi*s)/(EMPIRICAL*REV)  #cm

ball_detected = False 
#ball_detected --> true if computer vision detects a ball


def sendTarget():
    if not ball_detected :
        try:
            #d = inputimeout("Enter a numberd: ",timeout = 5)
            #x = inputimeout("Enter a number1: ",timeout = 5)
            #y = inputimeout("Enter a number2: ",timeout = 5)
            d = input("Enter a numberd: ")
            x = input("Enter a number1: ")
            y = input("Enter a number2: ")
        except Exception:
            return
    else:
        '''CONDITION à DETERMINER QUAND S'ÉCHAPPER À GAUCHE A GAUCHE'''
        '''if d :'''
        d=1
        '''else:'''
        d=-1
        
    try : 
        d=int(d)
        if(not d):
            x = float(x)
            y = float(y)
            if x > X_MIN and x < X_MAX and y > Y_MIN and y < Y_MAX:
                print("CORRECT INPUT") 
                x = convertXtoSteps(x)
                y = convertYtoSteps(y)
                time.sleep(0.1)
                data = f"{d},{x},{y}\n"  # Format the data as per the expected delimiter                   
                #data = arduino.readline()
            else:
                print("WRONG INPUT2")
        elif(d==1 or d==-1): 
            data = f"{d}\n"
        else:
            print("WRONG INPUT d")
            return
        print(data)
        arduino.flush()
        arduino.write(data.encode())  # Encode and send the data

    except ValueError:
        print("WRONG INPUT")
    

while True:
    '''
    print("ard------")
    print(arduino.in_waiting)
    #while(arduino.in_waiting):
    if arduino.in_waiting >=1 and  arduino.in_waiting<7:
        #data_type = arduino.read().decode()
        #data = arduino.read()
        #print(data)
        #if data_type == 'b':  # Boolean value
        dragging = bool(ord(arduino.read()))
        # Process the received boolean values
        print("Received:", dragging)
        arduino.read()
        if(dragging):
            time.sleep(4)
    
    #time.sleep(4)

    elif arduino.in_waiting >=7 :
        #elif data_type == 'l':  # Long values
            long_value1_bytes = arduino.read(4)
            long_value2_bytes = arduino.read(4)

            long_value1 = struct.unpack('l', long_value1_bytes)[0]
            long_value2 = struct.unpack('l', long_value2_bytes)[0]

            print("Received Long Values:", stepsToX(long_value1), stepsToY(long_value2))
            time.sleep(0.5)
    '''
             
    #ICI COMPUTER VISION
    #JE PENSE QU'A UN CERTAIN MOMENT IL FAUT AVOIR UN TABLEAU QUI STOCKE LES BALLES QUI SONT DEJA ARRIVEES

    if(not dragging):
        sendTarget()


        #ICI DECIDER OU ALLER

        #Ceci n'est pas à ignorer
        #------- algo pour envoyer go_in_rest
        '''
        if(not ball_detected and not in_rest(x,y))
            x,y = go_in_rest();
        '''
        #NE PAS IGNORER



        #sendTarget()
        #time.sleep(0.01)

    '''
    while True:
        if arduino.in_waiting > 0:
            dragging = bool(ord(arduino.read()))
            # Process the received boolean values
            print("Received:", dragging)
            if(not dragging):
                break
        elif arduino.in_waiting <= 0 and not dragging:
            break
    '''
    '''
    if(not ball_detected and not in_rest(x,y))
        go_in_rest();
    '''
 

    
