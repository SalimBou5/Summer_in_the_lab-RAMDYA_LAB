import serial
import time
import math
#from inputimeout import inputimeout



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

RAIL_LENGTH = 1.2
RAIL_LENGTH_LAT = 0.2
#########################################


def convertXtoSteps(x):
    return int((2*EMPIRICAL*x/(RAYON*math.pi))*REV)  #x in cm

def convertYtoSteps(y):
    return int(((EMPIRICAL*y/(RAYON*math.pi))*REV))  #y in cm

def stepsToX(s):
    return (RAYON*math.pi*s)/(2*EMPIRICAL*REV) #cm

def stepsToY(s):
    return (RAYON*math.pi*s)/(EMPIRICAL*REV)  #cm






#---------------------SEND TARGET----------------
ball_detected = False 
#ball_detected --> true if computer vision detects a ball

def sendTarget(x,y):
    if not ball_detected :
        try:
            #d = inputimeout("Enter a numberd: ",timeout = 5)
            #x = inputimeout("Enter a number1: ",timeout = 5)
            #y = inputimeout("Enter a number2: ",timeout = 5)
            d = input("Enter a numberd: ")
            if int(d)==0:  #Ce truc va disparaâitre quand il n'y aura plus d'input donc 
                            #pour le moment, on peut laisser cette mocheté
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
                #x = convertXtoSteps(x)
                #y = convertYtoSteps(y)
                time.sleep(0.1)
                data = f"{d},{convertXtoSteps(x)},{convertYtoSteps(y)}\n"  # Format the data as per the expected delimiter                   
            else:
                print("WRONG INPUT2")
        elif(d==1 or d==-1): 
            data = f"{d}\n"
        else:
            print("WRONG INPUT d")
            return
        arduino.write(data.encode())  # Encode and send the data

    except ValueError:
        print("WRONG INPUT")
    return d,x,y
    
coef=0
while True:

    #print("ard------")
    #print(arduino.in_waiting)
    #print(arduino.read())
    #while(arduino.in_waiting):
    if arduino.in_waiting >=1:# and  arduino.in_waiting<7:
        #data_type = arduino.read().decode()
        dragging = bool(ord(arduino.read()))#arduino.read()))
        # Process the received boolean values
        print("Received:", dragging)
        if not dragging:
            x=x+coef*RAIL_LENGTH_LAT
            y=y+RAIL_LENGTH
            coef=0
        time.sleep(0.5)

    '''
    if arduino.in_waiting >=7 and not dragging:
        #elif data_type == 'l':  # Long values
            long_value1_bytes = arduino.read(4)
            long_value2_bytes = arduino.read(4)

            long_value1 = struct.unpack('l', long_value1_bytes)[0]
            long_value2 = struct.unpack('l', long_value2_bytes)[0]

            print("Received Long Values:", stepsToX(long_value1), stepsToY(long_value2))
            time.sleep(0.5)
    '''
        
    #print("------")'''

    #time.sleep(5)     
    #ICI COMPUTER VISION
    #JE PENSE QU'A UN CERTAIN MOMENT IL FAUT AVOIR UN TABLEAU QUI STOCKE LES BALLES QUI SONT DEJA ARRIVEES
    #arduino.flushInput()
    if(not dragging):# and not arduino.in_waiting):
        coef,x,y =  sendTarget(x,y)
        time.sleep(0.2)
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
 

    
