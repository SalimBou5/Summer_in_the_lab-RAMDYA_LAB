  // Bounce.pde
// -*- mode: C++ -*-
//
// Make a single stepper bounce from one limit to another
//
// Copyright (C) 2012 Mike McCauley
// $Id: Random.pde,v 1.1 2011/01/05 01:51:01 mikem Exp mikem $

#include <AccelStepper.h>

#define DIR_PIN_X 5
#define STEP_PIN_X 3
#define INTERFACE_X 1
#define DIR_PIN_Y 9
#define STEP_PIN_Y 6
#define INTERFACE_Y 1

#define DELIMITER ','

#define RAIL_LENGTH 1918    //1.2 cm //!!!!!!!!!!!!!!!!!!! 

#define RAIL_LENGTH_LAT 1500  //1.2 cm //!!!!!!!!!!!!!!!!!!! 


float x = 0;
float y = 0;



// Define a stepper and the PIns it will use
//AccelStepper stepper; // Defaults to AccelStepper::FULL4WIRE (4 PIns) on 2, 3, 4, 5
AccelStepper stepperX=AccelStepper(INTERFACE_X,STEP_PIN_X,DIR_PIN_X);
AccelStepper stepperY=AccelStepper(INTERFACE_Y,STEP_PIN_Y,DIR_PIN_Y);


void setup()
{  
    Serial.begin(115200);
    Serial.setTimeout(1);

    // Change these to suit your stepper if you want
    stepperX.setMaxSpeed(12000);
    stepperX.setAcceleration(8000);
    stepperY.setMaxSpeed(8000);
    stepperY.setAcceleration(4000);

}

int dragBack(int escape){

  // reduce y-speed
  stepperY.setMaxSpeed(1000);
  stepperY.setAcceleration(500);
  while(Serial.available()>0)
    Serial.read();

  Serial.flush();
  //Serial.write("B");
  //tells python that we enter in drag mode
  Serial.write("T");

  //drag on y-axis
  stepperY.move(RAIL_LENGTH);
  stepperY.runToPosition();
  
  // reduce x-speed
  stepperX.setMaxSpeed(1500);
  stepperX.setAcceleration(750);  
  
  //escape on x-axis
  stepperX.move(escape*RAIL_LENGTH_LAT);
  stepperX.runToPosition();
  
  //tells python that we left drag mode
  Serial.write("F");

  //reset speed
  stepperY.setMaxSpeed(8000);
  stepperY.setAcceleration(4000);
  stepperX.setMaxSpeed(30000);
  stepperX.setAcceleration(15000);
  return 0;
}

long currX = 0;
long currY = 0;
int escape = 0;
int k = 0;

bool dir = true; //true --> x ; false -->y
bool arrived = false;


void loop()
{   
    /*if(currX != stepperX.currentPosition() || currY != stepperY.currentPosition()){
        currX = stepperX.currentPosition();
        currY = stepperY.currentPosition();
        //Serial.println(currX);
        //Serial.println(currY);
        if(Serial.available()==0){
          Serial.write((byte*)&currX, sizeof(long));
          delay(100);
          Serial.write((byte*)&currY, sizeof(long));
        }
        delay(250);
     }*/

     while (Serial.available() > 0) {
        delay(30);
        String data = Serial.readStringUntil(DELIMITER);
        escape = data.toInt();
        delay(100);

        if (data.length() > 0) {
          if (escape == 0) {
              // Read the two variables when the value is 0
              dir = true;
              arrived = false;
              x = Serial.readStringUntil(DELIMITER).toFloat();
              delay(100);
  
              y = Serial.readStringUntil(DELIMITER).toFloat();      
          }
          Serial.write("R");
        }
    } 

    
    if(escape==1 || escape ==-1){ 
      escape = dragBack(escape);
      x = stepperX.currentPosition();
      y = stepperY.currentPosition();
    }else if(escape==0){
      stepperX.moveTo(x);
      stepperY.moveTo(y);
      
      stepperX.run();
      if(dir and stepperX.currentPosition()== x)
        dir = false;
      if(!dir){
        stepperY.run();
      }
    }

    if(k>10){
        long currX1 = stepperX.currentPosition();
        long currY1 = stepperY.currentPosition();
        if(abs(currX - currX1) > 600 || abs(currY - currY1)> 300){
          currX = currX1;
          currY = currY1;
          //Serial.println(currX);
          //Serial.println(currY);
          //if(Serial.available()==0){
            //Serial.println("+-+-+-+-+-+-");
            //Serial.println(currX);
            Serial.write("X");
            Serial.write((byte*)&currX, sizeof(long));
            //delay(500);
            //Serial.println(currY);
            Serial.write("Y");
            Serial.write((byte*)&currY, sizeof(long));
            //delay(100);
          //} 
        }
        else if (!arrived and abs(currX1-x)<300 and abs(currY1-y)<20){
            arrived = true;
            currX=x;
            currY=y;
            //if(Serial.available()==0){
              //Serial.println("+-+-+-+-+-+-");
              //Serial.println(currX);
              Serial.write("A");
              //delay(50);
              Serial.write("X");
              Serial.write((byte*)&currX, sizeof(long));
              //delay(500);
              //Serial.println(currY);
              Serial.write("Y");
              Serial.write((byte*)&currY, sizeof(long));
              //delay(100);
            //} 
          }
      k=0;
    }else        k++;
 
}
