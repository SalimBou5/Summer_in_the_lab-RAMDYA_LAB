import serial
import time
import math
import struct
#from inputimeout import inputimeout

#-------LIBRARIES FOR COMPUTER VISION------
import numpy as np
from skimage.io import imshow, imread
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from skimage.feature import match_template
from skimage.feature import peak_local_max
#-------------------------------------------

arduino = serial.Serial(port='COM19',  baudrate=115200, timeout=.1)

targetX=0
targetY=0
posX=0
posY=0
escape=0

dragging=False

#List containing all the detected balls --> not useful for the moment
#balls = []  --> NOT USEFUL FOR THE MOMENT

'''
    ENCORE À AJUSTER
'''
BALLS_DESTINATION = [
                        [[65,195],[150,195],[235,195],[325,195],[410,195],[495,195]], #top-left
                        [[1561,195],[1646,195],[1731,195],[1816,195],[1900,195],[1985,195]], #top_middle
                        [[3055,190],[3140,190],[3225,190],[3310,190],[3395,190],[3480,190]], #top_right
                        [[65,1350],[150,1350],[235,1350],[325,1350],[410,1350],[495,1350]], #middle_left
                        [[1561,1350],[1646,1350],[1731,1350],[1816,1350],[1900,1350],[1985,1350]], #middle_middle
                        [[3055,1350],[3140,1350],[3225,1350],[3310,1350],[3395,1350],[3480,1350]], #middle_top
                        [[65,2508],   [150,2508], [235,2508], [325,2508], [410,2508], [495,2508]], #bottom_left
                        [[1561,2508],[1646,2508],[1731,2508],[1816,2508],[1900,2508],[1985,2508]], #bottom_middle
                        [[3055,2508],[3140,2508],[3225,2508],[3310,2508],[3395,2508],[3480,2508]] #bottom_right
                    ]

REST_X=[1000,2500]

REV = 1600
RAYON = 1.6
EMPIRICAL = 5.02

########## EVIDEMMENT CHANGER ###########
X_MIN = -30
X_MAX = 30
Y_MIN = -20
Y_MAX = 20

RAIL_LENGTH = 1.2
RAIL_LENGTH_LAT = 0.2
#########################################

#----------------UTILS--------------------
def convertXtoSteps(x):
    return int((1.92*EMPIRICAL*x/(RAYON*math.pi))*REV)  #x in cm

def convertYtoSteps(y):
    return int(((EMPIRICAL*y/(RAYON*math.pi))*REV))  #y in cm

def stepsToX(s):
    return (RAYON*math.pi*s)/(2*EMPIRICAL*REV) #cm

def stepsToY(s):
    return (RAYON*math.pi*s)/(EMPIRICAL*REV)  #cm

def closeEnough(x,y,threshold):
    return abs(x-y)<threshold  #CHECK

def convertPixelsToCm(x):
    '''
        To BE CHECKED
    '''
    return x*4./661.

#---------------------COMPUTER VISION (Pattern Matching)-------------------------
sample = imread('python\image0.jpg')
#Regions to divide the image to 9 parts (The only parts where it is possible to find a ball)
DIVIDE_REGIONS = [[25,550,130,450],  [1520,2050,130,450],[3020,3520,130,450],
                  [25,550,1300,1650],[1520,2050,1300,1650] , [3020,3520,1300,1650],
                  [25,550,2420,2820],[1520,2050,2420,2820], [3020,3520,2420,2820]]

#The region from where the patter to be matched is taken
PATCH_X_MIN=200
PATCH_X_MAX=230
PATCH_Y_MIN=245
PATCH_Y_MAX=275


#Patch creation taken from the middle region to match the size
sample_div = sample[1300:1650, 1520:2050]
patch = sample_div[PATCH_Y_MIN:PATCH_Y_MAX, PATCH_X_MIN:PATCH_X_MAX]

#If needed, code to visualize the patch
'''
fig, ax = plt.subplots(1,2,figsize=(10,10))
ax[0].add_patch(Rectangle((PATCH_X_MIN, PATCH_Y_MIN), PATCH_X_MAX-PATCH_X_MIN, PATCH_Y_MAX-PATCH_Y_MIN, edgecolor='b', facecolor='none'));
ax[0].set_title('Patch Location',fontsize=15)
#Showing Patch
ax[0].imshow(sample_div,cmap='gray')
patch = sample_div[PATCH_Y_MIN:PATCH_Y_MAX, PATCH_X_MIN:PATCH_X_MAX]
ax[1].imshow(patch,cmap='gray')
ax[1].set_title('Patch',fontsize=15)
plt.show()
'''

#To be adjusted 
#Threshold to detect if a ball has reached a ball_destination
THRESHOLD_DETECTION_READY = 20

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

    #Do pattern matching for each of the divided regions
    for i in range(len(DIVIDE_REGIONS)):
        y_min, y_max, x_min, x_max = DIVIDE_REGIONS[i]
        sample_div = sample2[x_min:x_max, y_min:y_max]
        sample_mt = match_template(sample_div, patch)

        for x, y in peak_local_max(sample_mt, threshold_abs=0.76):
            #Add the detected rectangles to the image
            '''
            rect = plt.Rectangle((y+y_min, x+x_min), patch_height, patch_width, color='r', 
                                    fc='none')
            #ax[1].add_patch(rect)
            '''

            #List containing all of the detected balls 
            #balls.append([x+x_min+patch_width/2,y+y_min+patch_height/2])

            x = x + x_min + patch_width / 2
            y = y + y_min + patch_height / 2

            #Check if a ball reached a destination
            for dest in BALLS_DESTINATION[i]:
                #If a ball reached a destination, append the list balls_ready
                if closeEnough(dest[0],y,THRESHOLD_DETECTION_READY) and closeEnough(dest[1], x,THRESHOLD_DETECTION_READY):
                    x_cm = convertPixelsToCm(x)
                    y_cm = convertPixelsToCm(y)
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
THRESHOLD_SAME_GOAL = 0.01

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

def sendTarget(x,y,posX,posY):
    x_old,y_old = x,y
    print("---------------------------------")
    
    #*********************INTERPRETATION OF COMPUTER VISION*******************
    if len(balls_ready) :
        try:
            '''CONDITION à DETERMINER QUAND S'ÉCHAPPER À GAUCHE / À DROITE'''
                    #encore à définir d = 1 ou -1

            #Determine the closest ball_ready to the magnet --> Goal
            x,y = find_nearest_point(balls_ready,posX,posY) 
            
            #If the goal is close enough to the magnet, then trigger drag_back 
            # and remove the ball from the list balls_ready 
            if closeEnough(x,posX,THRESHOLD_MAGNET_ARRIVED) and closeEnough(y,posY,THRESHOLD_MAGNET_ARRIVED):
                escape=-1 #À ajuster, 1 ou -1 --> Il faut trouver le bon algorithme
                balls_ready.remove([x,y])
                print("CLOSE")

            #If the magnet is far from the ball, allow it to move towards it
            else: 
                escape = 0
        
        except Exception:
            print("ERROR 0")
            return
    
    #If no ball reached a desination, go to rest
    else:
        rest_check = False
        if(posX in REST_X):
            return  x_old,y_old
        else :
            #x,y = find_nearest_point(rest_check,posX,posY)
            rest_check = False
            escape = 0


    #********************GOAL ANALYSIS AND MOTORS CONTROL**********************
    try : 
        #if allowed to move
        if(not escape):
            #x = float(x)
            #y = float(y)

            if closeEnough(x,x_old,THRESHOLD_SAME_GOAL) and closeEnough(y,y_old,THRESHOLD_SAME_GOAL):
                return x_old, y_old
            if x > X_MIN and x < X_MAX and y > Y_MIN and y < Y_MAX:
                #print(x)
                #print(y)
                print("CORRECT INPUT") 
                time.sleep(0.1)
                data = f"{escape},{convertXtoSteps(x)},{convertYtoSteps(y)}\n"  # Format the data as per the expected delimiter                   
            else:
                print("WRONG INPUT2")
                return x_old,y_old
        elif(escape==1 or escape==-1): 
            data = f"{escape}\n"
        else:
            print("WRONG INPUT d")
            return x_old,y_old
        print(x)
        print(y)
        arduino.write(data.encode())  # Encode and send the data

    except ValueError:
        print("WRONG INPUT")
        return x_old, y_old,posX,posY

    return x,y
    

targetX=0
targetY=0
posX=0
posY=0

i=516

time.sleep(2)
while(arduino.in_waiting):
    arduino.read()

while True:
    #print("ard------")
    #print(arduino.in_waiting)
    #print(arduino.read())
    #while(arduino.in_waiting):
    #time.sleep(0.5)
    if arduino.in_waiting:
        data = arduino.read()

        if data == b'T':
        #if arduino.in_waiting >=1 and  arduino.in_waiting<7:
            #data_type = arduino.read().decode()
            dragging = True#arduino.read()))
            # Process the received boolean values
            print("Received:", dragging)
            #if not dragging:
                #x=x+coef*RAIL_LENGTH_LAT
                #y=y+RAIL_LENGTH
                #coef=0
            #time.sleep(0.5)  
        
        elif data == b'F':
            dragging = False#arduino.read()))
            # Process the received boolean values
            print("Received:", dragging)
            #time.sleep(0.5)
            
        elif data==b'R':
            print("RECU")

        
        #elif arduino.in_waiting >3 and not dragging:
            #elif data_type == 'l':  # Long values
        elif(data ==b'X'):
                #data=arduino.read()
                #if(data==b'X'):

                posX_bytes = arduino.read(4)

                posX = stepsToX(struct.unpack('l', posX_bytes)[0])
                #long_value2 = struct.unpack('l', long_value2_bytes)[0]

                print("Received Long Values:", posX)#, stepsToY(long_value2))
                #time.sleep(5)

                data=arduino.read()
                if(data==b'Y'):
                    posY_bytes = arduino.read(4)
    
                    posY = stepsToY(struct.unpack('l', posY_bytes)[0])
                    #long_value2 = struct.unpack('l', long_value2_bytes)[0]

                    print("Received YYYYYYyyy:", posY)#, stepsToY(long_value2))
        
    
    #print("------")'''

    #time.sleep(5)     
    #ICI COMPUTER VISION
    #JE PENSE QU'A UN CERTAIN MOMENT IL FAUT AVOIR UN TABLEAU QUI STOCKE LES BALLES QUI SONT DEJA ARRIVEES
    #image = 'python\image'+str(i)+'.jpg'
    image = f"C:\\Users\\salim\\Documents\\Summer_in_the_lab-RAMDYA_LAB\\Magnets_2\\image{i}.jpg"
    
    balls_detection(image)
    i=i+1
    #arduino.flushInput()
    if(not dragging):# and not arduino.in_waiting):
        targetX,targetY =  sendTarget(targetX,targetY,posX,posY)
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
 

    
