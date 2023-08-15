import serial
import time
import math
import struct

#from inputimeout import inputimeout

import graph_new as graph

#-------LIBRARIES FOR COMPUTER VISION------
import numpy as np
from skimage.io import imshow, imread
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from skimage.feature import match_template
from skimage.feature import peak_local_max
#-------------------------------------------

#Open the serial port to communicate with the arduino
arduino = serial.Serial(port='COM19',  baudrate=115200, timeout=.1)

#Open the serial port to communicate with the Zaber motor
zaber = serial.Serial('COM3', 115200, timeout=1)

#home the Zaber motor
command = "/home\n" 
zaber.write(command.encode())
#time.sleep(3)
command="/move abs 400000\n"
zaber.write(command.encode())

#time.sleep(1)
#Position of the final goal
targetX=0
targetY=0

#Position of the magnet
START_X = -6.2
START_Y = 0
posX=START_X
posY=START_Y

#transmitted to arduino to know whether to drag_back or to move
escape=0

#Boolean to inform if the magnet is currently dragging back
dragging=False


'''
    ENCORE À AJUSTER  --> Une idée possible est de hardcoder les destinations des balles en cm en plus des pixels 
    --> Comme ça au lieu de convertir pixels to cm, on envoie directement x_cm et y_cm et on évite la distortion due à la caméra
    ---> NE PAS OUBLIER QUE LA CAMERA N'EST QUE LE SUPPORT --> CE QUI IMPORTE C'EST L'ENVIRONNEMENT PHYSIQUE
'''

BALLS_DESTINATION = [ 
                        #[[71,195],[1540,195],[245,195],[327,195],[417,195],[500,195]], #top-left
                        [[6500,195],[15000,195],[23500,195],[32500,195],[41000,195],[49500,195]], #top-left
                        #[[1565,195],[1650,195],[1735,195],[1820,195],[1913,195],[2000,195]], #top_middle
                        [[156100,195],[164600,195],[173100,195],[181600,195],[190000,195],[198500,195]], #top_middle   
                        #[[3057,190],[3143,190],[3230   ,190],[3315,190],[3407,190],[3492,190]], #top_right
                        [[305500,190],[314000,190],[322500,190],[331000,190],[339500,190],[348000,190]], #top_right
                        #[[71,1350],[154,1350],[245,1350],[327,1350],[417,1350],[500,1350]], #middle_left
                        [[6500,1350],[15000,1350],[23500,1350],[32500,1350],[41000,1350],[49500,1350]], #middle_left
                        #[[1565,1350],[1650,1350],[1735,1350],[1820,1350],[1913,1350],[2000,1350]], #middle_middle
                        [[156100,1350],[164600,1350],[173100,1350],[181600,1350],[190000,1350],[198500,1350]], #middle_middle
                        #[[3057,1350],[3143,1350],[3230,1350],[3315,1350],[3407,1350],[3492,1350]], #middle_right
                        [[305500,1350],[314000,1350],[322500,1350],[331000,1350],[339500,1350],[348000,1350]], #middle_right
                        #[[71,2508],   [154,2508], [245,2508], [327,2508], [417,2508], [500,2508]], #bottom_left
                        [[6500,2508],   [15000,2508], [23500,2508], [32500,2508], [41000,2508], [49500,2508]], #bottom_left
                        #[[1565,2508],[1650,2508],[1735,2508],[1820,2508],[1913,2508],[2000,2508]], #bottom_middle
                        [[156100,2508],[164600,2508],[173100,2508],[181600,2508],[190000,2508],[198500,2508]], #bottom_middle
                        #[[3057,2508],[3143,2508],[3230,2508],[3315,2508],[3407,2508],[3492,2508]] #bottom_right
                        [[305500,2508],[314000,2508],[322500,2508],[331000,2508],[339500,2508],[348000,2508]] #bottom_right
                    ]

########## EVIDEMMENT CHANGER ###########
X_MIN = -30
X_MAX = 30
Y_MIN = -20
Y_MAX = 20

#########################################

#----------------UTILS--------------------
REV = 1600
RAYON = 1.6
EMPIRICAL = 5.02

def convertXtoSteps(x):
    return int((2*EMPIRICAL*x/(RAYON*math.pi))*REV)  #x in cm

def convertYtoSteps(y):
    return int(((EMPIRICAL*y/(RAYON*math.pi))*REV))  #y in cm

def stepsToX(s):
    return (RAYON*math.pi*s)/(2*EMPIRICAL*REV) #cm

def stepsToY(s):
    return (RAYON*math.pi*s)/(EMPIRICAL*REV)  #cm

def closeEnough(x,y,threshold):
    try:
        return abs(x-y)<threshold
    except Exception:
        print("Error in closeEnough function")
        return False 

#CHECK
def convertPixelsToCm(x):
    '''
        To BE CHECKED
    '''
    return x*4./659.


#---------------------COMPUTER VISION (Pattern Matching)-------------------------
'''
    Normalement A NE Pas Toucher --> TOUT FONCTIONNE PARFAITEMENT
    Maximum ajuster le threshold + si on hardcode les destinations des balles en cm, il faudra 
    changer convertPixelsToCm(dest[0]) en x_cm et convertPixelsToCm(dest[1]) en y_cm 
'''
sample = imread('python\image0.jpg')

#Regions to divide the image to 9 parts (The only parts where it is possible to find a ball)
DIVIDE_REGIONS = [[25,550,130,450],  [1520,2050,130,450],[3020,3520,130,450],
                  [25,550,1300,1650],[1520,2050,1300,1650] , [3020,3520,1300,1650],
                  [25,550,2420,2820],[1520,2050,2420,2820], [3020,3520,2420,2820]]

#If needed, patch creation taken from the middle region to match the size + code to visualize the patch
'''
PATCH_X_MIN=200
PATCH_X_MAX=230
PATCH_Y_MIN=245
PATCH_Y_MAX=275
sample_div = sample[1300:1650, 1520:2050]
patch = sample_div[PATCH_Y_MIN:PATCH_Y_MAX, PATCH_X_MIN:PATCH_X_MAX]

fig, ax = plt.subplots(1,2,figsize=(10,10))
ax[0].add_patch(Rectangle((PATCH_X_MIN, PATCH_Y_MIN), PATCH_X_MAX-PATCH_X_MIN, PATCH_Y_MAX-PATCH_Y_MIN, edgecolor='b', facecolor='none'));
ax[0].set_title('Patch Location',fontsize=15)

#Showing Patch
ax[0].imshow(sample_div,cmap='gray')
patch = sample_div[PATCH_Y_MIN:PATCH_Y_MAX, PATCH_X_MIN:PATCH_X_MAX]
ax[1].imshow(patch,cmap='gray')
ax[1].set_title('Patch',fontsize=15)
plt.show()

cv2.imwrite('python\patch.jpg',patch)
'''

#pattern to be matched (patch)
patch = imread('python\patch.jpg')

'''
    Il y a peut-être juste ça à ajuster
'''
#Threshold to detect if a ball has reached a ball_destination
THRESHOLD_DETECTION_READY = 20 

#List to store all the balls that are ready to be dragged back
balls_ready=[]


#Function to read an image and detect the balls that reached a destination
def balls_detection(image):
    #Read new image
    sample2 = imread(image)

    #plot new image
    '''
    fig, ax = plt.subplots(1,2,figsize=(10,10))
    ax[0].imshow(sample2,cmap='gray')
    ax[1].imshow(sample2,cmap='gray')
    ax[0].set_title('Grayscale',fontsize=15)
    ax[1].set_title('Template Matched',fontsize=15)
    '''
    
    patch_width, patch_height = patch.shape

    '''
    rect = plt.Rectangle((68, 1356), patch_height, patch_width, color='g', 
                fc='none')
    ax[1].add_patch(rect)
    '''
    #length ball_destination
    len_dest = len(BALLS_DESTINATION)

    #Do pattern matching for each of the divided regions
    for i in range(len(DIVIDE_REGIONS)):
        x_min, x_max, y_min, y_max = DIVIDE_REGIONS[i]
        sample_div = sample2[y_min:y_max, x_min:x_max]
        sample_mt = match_template(sample_div, patch)

        for y, x in peak_local_max(sample_mt, threshold_abs=0.76):
            #Add the detected rectangles to the image
            '''
            rect = plt.Rectangle((y+y_min, x+x_min), patch_height, patch_width, color='r', 
                                    fc='none')
            ax[1].add_patch(rect)
            '''

            '''CHECK if patch_width/2 and patch_height/2 are correct'''
            x = x + x_min + patch_width / 2
            y = y + y_min + patch_height / 2

            if i in range(len_dest):
                #Check if a ball reached a destination
                for dest in BALLS_DESTINATION[i]:
                    #If a ball reached a destination, append the list balls_ready
                    if closeEnough(dest[0],x,THRESHOLD_DETECTION_READY) and closeEnough(dest[1], y,THRESHOLD_DETECTION_READY):
                        '''
                            SUR LE VRAI SETUP, HARDCODER LES DESTINATIONS DES BALLES EN CM
                        '''
                        x_cm=convertPixelsToCm(dest[0])
                        y_cm=convertPixelsToCm(dest[1])

                        

                        '''
                        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                        !!!!!!!!!!! ENLEVER !!!!!!!!!!!
                        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                        '''
                        dest[0] = 6226256
                        dest[1] = 45665945
                        '''
                        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                        !!!!!!!!!!! ENLEVER !!!!!!!!!!!
                        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
                        '''
                        
                        if not [x_cm, y_cm] in balls_ready:
                            balls_ready.append([x_cm,y_cm])
                        break
    
                    #Add the detected rectangles that are matching a destination to the image
                    '''
                    rect = plt.Rectangle((dest[0], dest[1]), patch_height, patch_width, color='b', 
                                fc='none')
                    ax[1].add_patch(rect)
                    '''
    #plt.show()


#-------------------------SEND TARGET----------------------------
THRESHOLD_REST = 0.05
THRESHOLD_MAGNET_ARRIVED = 0.05
THRESHOLD_SAME_GOAL = 0.05

'''
    SUR LE VRAI SETUP, ADAPTER CES POSITIONS
    (Les * représentent les x de repos et les | représentent les rails)
    *||||||*  *||||||*  *||||||*
    *||||||*  *||||||*  *||||||*
    *||||||*  *||||||*  *||||||*

    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    EN CHANGEANT REST_X NE PAS OUBLIER DE CHANGER LA VALEUR DES COL DANS GRAPH_MAP
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
'''
REST_X = [-2, 5, 8, 14, 17, 23]

def find_nearest_point(array, XA, YA):
    nearest_point = array[0]
    if len(array)>1:
        min = np.sqrt((array[0][0] - XA) ** 2 + (array[0][1] - YA) ** 2)
        nearest_point=array[0]
        for ar in array:
            d=np.sqrt((ar[0] - XA) ** 2 + (ar[1] - YA) ** 2)
            if(min>d):
                min = d
                nearest_point = ar
    return nearest_point

def find_nearest_X(array, XA):
    nearest_X = array[0]
    if len(array)>1:
        min = abs(array[0] - XA)
        #nearest_point=array[0]
        for ar in array:
            d = abs(ar - XA)
            if(min>d):
                min = d
                nearest_X = ar
    return nearest_X

#******INTERPRETATION OF COMPUTER VISION****
def computerVisionInterpretation(x,y,posX,posY):
    towards_rest = False
    if len(balls_ready) :
        '''
        If at least a ball reached its destination, then the goal of the magnet is the closest ball
            *If the magnet reached the final destination, then escape = 1 to trigger dragBack + remove the ball from the list of balls_ready
            *If the magnet is not at the final destination, then escape = 0 to allow the magnet to move towards the ball
        '''
        #Determine the closest ball_ready to the magnet --> Goal
        x,y = find_nearest_point(balls_ready,posX,posY) 
        
        print("check dumm  ",x,"   ",y)
        print("check dumm  22  ",posX,"   ",posY)

        #If the goal is close enough to the magnet, then trigger drag_back 
        # and remove the ball from the list balls_ready 
        if closeEnough(x,posX,THRESHOLD_MAGNET_ARRIVED) and closeEnough(y,posY,THRESHOLD_MAGNET_ARRIVED):
            escape = 1
            balls_ready.remove([x,y])
            print("CLOSE")

        #If the magnet is far from the ball, allow it to move towards it
        else: 
            escape = 0
        
    #If no ball reached a desination, go to rest --> go to the nearest X where the magnet can rest
    # --> y is set to the current posY 
    else:
        escape = 0
        x = find_nearest_X(REST_X,posX)
        y = posY
        print(posX)
        print("x = ",x,"  y = ",y)
        towards_rest = True

    return x,y,escape,towards_rest

def goalReached(x, y, arrived, path, towards_rest):
    '''
        Qu'on soit clair le path retourné par graph_map ne contient pas le noeud de départ
        mais contient les noeuds qui "font les coins" + le noeud D'ARRIVEE !!!
    '''

    size_path = len(path)
    data =""
    ESCAPE = 0
    
    at_rest = False

    if(size_path > 1):  #New target = first node of the shortest path
        realTargetX, realTargetY = graph.getNodePosition(path[0])
        data = f"{escape},{convertXtoSteps(realTargetX-START_X)},{convertYtoSteps(realTargetY-START_Y)}\n" 
        arrived = False   
        #remove first node of the path since the command to go towards it has already been sent
        path.pop(0)
        #print("x  y   ",realTargetX,"   ",realTargetY)
        #print("pos  ",posX,"   ",posY)

    elif (size_path == 1): #Go directly towards the goal
        #print("else  x  y   ",x,"   ",y)
        #print("else  pos  ",posX,"   ",posY)
        data = f"{ESCAPE},{convertXtoSteps(x-START_X)},{convertYtoSteps(y-START_Y)}\n" 
        arrived = False
        path.pop(0)


    elif(size_path == 0):
        # If we were going towards rest and we reached the final destination, we are actually at rest
        if towards_rest:
            at_rest = True
        print("IN REST")

        '''
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            ENLEVER
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        '''
        time.sleep(2)
        BALLS_DESTINATION[4]=[[1561,1350],[1646,1350],[1731,1350],[1816,1350],[1900,1350],[1985,1350]] #middle_middle
        '''
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
            ENLEVER
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        '''

    arduino.write(data.encode())  # Encode and send the data to the Arduino

    return arrived,path, at_rest

def setNewGoal(x, y, posX, posY, path, towards_rest, at_rest):
    '''
        Set new goal --> establish new shortest path towards this goal
        --> new target = first node of the shortest path
    '''              
    ESCAPE = 0

    #Reset arrived to false 
    arrived = False

    #print("CORRECT INPUT") 
    #time.sleep(0.1)

    #Establish new shortest path
    if not towards_rest:
        path = graph.shortest_path([posX,posY],[x,y],at_rest)
    print("33333333")
        
    #Reset realTargetX and realTargetY
    realTargetX = 0
    realTargetY = 0
    path_size = len(path)

    if path_size > 1:  #New target = first node of the shortest path
        print("path", path)
        realTargetX, realTargetY = graph.getNodePosition(path[0])
        #remove first node of the path since the command to go towards will be sent now
        path.pop(0)

    else:  #Go directly towards the goal
        realTargetX = x
        realTargetY = y

    print("elif x  y   ",realTargetX,"   ",realTargetY)

    data = f"{ESCAPE},{convertXtoSteps(realTargetX-START_X)},{convertYtoSteps(realTargetY-START_Y)}\n"  
    arduino.write(data.encode())  # Encode and send the data to the Arduino

    return arrived,path

def dragBack():
    '''
        Trigger drag back --> push the ball
    '''
    ESCAPE = 1
    # Zaber goes down
    command ="/1 move rel 30000\n"  
    zaber.write(command.encode())
    data = f"{ESCAPE}\n"
    arduino.write(data.encode())  # Encode and send the data
    time.sleep(0.2)

#Function to send the target to the robot
def sendTarget(x,y,posX,posY,arrived,path, at_rest):
    x_old,y_old = x,y

    #********************COMPUTER VISION INTERPRETATION*************************
    try:
        x,y,escape,towards_rest=computerVisionInterpretation(x,y,posX,posY)
    except Exception:
        print("EXCEPTION 0")
        return x_old,y_old,arrived,path, at_rest

    #********************GOAL ANALYSIS AND MOTORS CONTROL**********************
    try : 

        #if allowed to move
        if(not escape):
            print("***************************************")
            #''''''''''''''''''''''If the goal did not change'''''''''''''''''''''''''''''''''''''''''
            if closeEnough(x,x_old,THRESHOLD_SAME_GOAL) and closeEnough(y,y_old,THRESHOLD_SAME_GOAL): 
                '''
                    Goal did not change --> the path does not change neither
                    --> The task is, therefore, to check the position of the 
                        magnet in respect to the previously-set path 

                        --> If (posMagnet == posFirstNode) *** Arrived ***
                            ---> Then the new target is the next node in the path

                        --> ELse If (posMagnet == Goal)  *** Arrived --> to goal ***
                            (This condition should never be satisfied since it is already checked above)
                            ---> return 

                        --> Else *** not arrived ***
                            ---> Then don't change the target and leave the function                                            
                '''
                
                if(arrived):  #---> if (posMagnet == posFirstNode)
                    arrived, path, at_rest = goalReached(x,y,arrived, path, towards_rest)

                elif(not arrived): # Do NOTHING
                    return x_old,y_old,arrived, path,at_rest
                
            #''''''''''''''''''''''''''''IF THE GOAL CHANGED'''''''''''''''''''''''''''
            #Check whether the position is acceptable
            elif x > X_MIN and x < X_MAX and y > Y_MIN and y < Y_MAX: 
                arrived, path = setNewGoal(x,y,posX,posY,path,towards_rest, at_rest)
                at_rest = False
        
            else:
                print("WRONG INPUT2")
                return x_old,y_old,arrived,path, at_rest
            
        #-----------------TRIGGER DRAG BACK--------------
        else: 
            dragBack()
            
    except ValueError:
        print("WRONG INPUT")
        return x_old, y_old,arrived,path, at_rest
    
    return x,y,arrived,path, at_rest
    

i=516
k=0
arrived = False
at_rest = True

#shortest path towards the goal
path=[]

'''
    Ce sleep est essentiel sinon la première commande envoyée à l'arduino est ignorée
'''
time.sleep(2) 

#graph.plotGraph()

#empty the serial before starting --> pour le fun
while(arduino.in_waiting):
    arduino.read()

while True:
    if arduino.in_waiting:
        data = arduino.read()
        if data == b'T':
            dragging = True
            print("Received:", dragging)
        
        elif data == b'F':
            dragging = False

            # Zaber goes up
            command ="/1 move rel -30000\n"  
            zaber.write(command.encode())

            print("Received:", dragging)
            time.sleep(0.2)
            
        elif data==b'R':
            print("RECU")

        elif(data==b'A'):
            arrived=True
            print("RECEIVED ARRIVED    ",arrived)

        elif(data ==b'X'):
                posX_bytes = arduino.read(4)

                #posX = stepsToX(struct.unpack('l', posX_bytes)[0])
                posX_temp = stepsToX(struct.unpack('l', posX_bytes)[0])

                #Normalement ce truc est inutile mais on ne sait jamais
                #Je l'ai mis parce que je me suis trompé et j'envoyer l'adresse d'une variable locale
                if(posX_temp < 30):
                    posX=posX_temp+START_X
            
                    #print("Received Long Values:", posX*659/4)
                    #time.sleep(0.5)

                    data=arduino.read()
                    if(data==b'Y'):
                        posY_bytes = arduino.read(4)
        
                        posY = stepsToY(struct.unpack('l', posY_bytes)[0])+START_Y
                        #print("Received YYYYYYyyy:", posY*659/4)
                    
                '''
                if(arduino.in_waiting):
                    data=arduino.read()
                    if(data==b'A'):
                       arrived=True
                       print("bncjdb")
                '''

    #while(arduino.in_waiting):
        #arduino.read() 
    
    #image = 'python\image'+str(i)+'.jpg'
    #Juste pour avancer moins rapidement 
    if(k%2==0):
        image = f"C:\\Users\\salim\\Documents\\Summer_in_the_lab-RAMDYA_LAB\\Magnets_2\\image{i}.jpg"
        print("iiiiii    ",i)
        balls_detection(image)
        i=i+1


        if(not dragging):# and not arduino.in_waiting):
            targetX,targetY,arrived,path, at_rest =  sendTarget(targetX,targetY,posX,posY,arrived,path, at_rest)
            #ICI DECIDER OU ALLER
            #time.sleep(0.2)
            
    k=k+1
