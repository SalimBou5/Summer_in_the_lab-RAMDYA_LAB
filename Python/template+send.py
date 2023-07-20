import serial
import time
import math
#from inputimeout import inputimeout

#-------LIBRARIES FOR COMPUTER VISION------
import numpy as np
from skimage.io import imshow, imread
from skimage.color import rgb2gray
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
from skimage.feature import match_template
from skimage.feature import peak_local_max



arduino = serial.Serial(port='COM19',  baudrate=115200, timeout=.1)
x=0
y=0
d=0

dragging=False

balls = []

balls_destination = [[65,105],[150,105],[235,105],[325,150],[410,105],[495,105],
                     [1561,105],[1646,105],[1731,105],[1816,105],[1900,105],[1985,105],
                     [3055,100],[3140,100],[3225,100],[3310,100],[3395,100],[3480,100]]

rest_positions=[]

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



#---------------------COMPUTER VISION----------
sample = imread('python\image0.jpg')
DIVIDE_REGIONS = [[25,550,130,450],  [1520,2050,130,450],[3020,3520,130,450],
                  [25,550,1300,1650],[1520,2050,1300,1650] , [3020,3520,1300,1650],
                  [25,550,2420,2820],[1520,2050,2420,2820], [3020,3520,2420,2820]]

PATCH_X_MIN=200
PATCH_X_MAX=230
PATCH_Y_MIN=245
PATCH_Y_MAX=275

THRESHOLD=10

#fig, ax = plt.subplots(1,2,figsize=(10,10))
#ax[0].imshow(sample,cmap='gray')
#ax[0].add_patch(Rectangle((patch_x_min, patch_x_max), patch_x_max-patch_x_min, patch_y_max-patch_y_min, edgecolor='b', facecolor='none'));
#ax[0].set_title('Patch Location',fontsize=15)
#Showing Patch
sample_div = sample[1300:1650, 1520:2050]
patch = sample_div[PATCH_X_MIN:PATCH_X_MAX, PATCH_Y_MIN:PATCH_Y_MAX]

balls_ready=[]
#ax[1].imshow(patch,cmap='gray')
#ax[1].set_title('Patch',fontsize=15)
#plt.show()

def convertPixelsToCm(x):
    '''
        To BE IMPLEMENTED
    '''
    return

def balls_detection():
    sample2 = imread('python\image2.jpg')
    fig, ax = plt.subplots(1,2,figsize=(10,10))
    ax[0].imshow(sample2,cmap='gray')
    ax[1].imshow(sample2,cmap='gray')
    ax[0].set_title('Grayscale',fontsize=15)
    ax[1].set_title('Template Matched',fontsize=15)

    patch_width, patch_height = patch.shape

    for region in DIVIDE_REGIONS:
        y_min, y_max, x_min, x_max = region
        sample_div = sample2[x_min:x_max, y_min:y_max]
        sample_mt = match_template(sample_div, patch)


        for x, y in peak_local_max(sample_mt, threshold_abs=0.76):
            rect = plt.Rectangle((y+y_min, x+x_min), patch_height, patch_width, color='r', 
                                    fc='none')
            ax[1].add_patch(rect)
            balls.append([x+x_min+patch_width/2,y+y_min+patch_height/2])
            x=convertPixelsToCm(x+x_min+patch_width/2)
            y=convertPixelsToCm(y+y_min+patch_height/2)
            for dest in balls_destination:
                if abs(dest[0]-x)<THRESHOLD and abs(dest[1]-y)<THRESHOLD:
                    balls_ready.append([x,y])
                    break

    plt.plot()



#---------------------SEND TARGET----------------
ball_detected = False 
#ball_detected --> true if computer vision detects a ball
THRESHOLD_REST = 0.05

def find_nearest_point(array, XA, YA):
    nearest_point = array[0]
    if len(array)>1:
        distances = np.sqrt((array[:, 0] - XA) ** 2 + (array[:, 1] - YA) ** 2)
        nearest_index = distances.argmin()
        nearest_point = array[nearest_index]
    return nearest_point

def sendTarget(x,y):
    if len(balls_ready) :
        try:
            '''CONDITION à DETERMINER QUAND S'ÉCHAPPER À GAUCHE A GAUCHE'''
            d = 1
            #encore à définir d = 1 ou -1
            x,y = find_nearest_point(balls_ready,x,y)                
        except Exception:
            return
    else:
        rest_check = False
        for rest in rest_positions:
            if abs(x-rest[0]) < THRESHOLD_REST and abs(y-rest[1])<THRESHOLD_REST:
                rest_check = True
                break
        if not rest_check :
            x,y = find_nearest_point(rest_check,x,y)
        rest_check = False
        d = 0
        
    try : 
        if(not d):
            x = float(x)
            y = float(y)
            if x > X_MIN and x < X_MAX and y > Y_MIN and y < Y_MAX:
                print("CORRECT INPUT") 
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
 

    
