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


//#define PI 3.14
#define REV 1600.0
#define RAYON 1.6
#define EMPIRICAL 5.02

#define convertXtoSteps(x) (long)((1.92*EMPIRICAL*x/(RAYON*PI))*REV)//x in cm
#define convertYtoSteps(y) (long)((EMPIRICAL*y/(RAYON*PI))*REV)//y in cm

#define stepsToX(s) (float)((RAYON*PI*s)/(2*EMPIRICAL*REV))
#define stepsToY(s) (float)((RAYON*PI*s)/(EMPIRICAL*REV))

#define DELIMITER ','

#define RAIL_LENGTH 1918 //cm //!!!!!!!!!!!!!!!!!!! 
#define RAIL_LENGTH_LAT 900 //cm //!!!!!!!!!!!!!!!!!!! 

    
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

/*void goToRest(){
  stepperX.moveTo();
  stepperX.run();
}*/
/*bool dragBack(){
  Serial.println("DRAG");
  stepperY.setMaxSpeed(400);
  stepperY.setAcceleration(100);
  Serial.write(true);
  
  stepperY.move(convertYtoSteps(RAIL_LENGTH));
  
  stepperY.runToPosition();
  // Send the bytes over serial
  delay(100);
  Serial.write(false);
  stepperY.setMaxSpeed(8000);
  stepperY.setAcceleration(4000);
}*/

int dragBack(int escape){
  //Serial.println("DRAG");
  stepperY.setMaxSpeed(800);
  stepperY.setAcceleration(400);
  Serial.write(true);
 
  stepperY.move(RAIL_LENGTH);
  
  stepperY.runToPosition();
  // Send the bytes over serial
  stepperX.setMaxSpeed(800);
  stepperX.setAcceleration(400);  
  stepperX.move(escape*RAIL_LENGTH_LAT);
  stepperX.runToPosition();
  Serial.write(false);
  stepperY.setMaxSpeed(8000);
  stepperY.setAcceleration(4000);
  stepperX.setMaxSpeed(30000);
  stepperX.setAcceleration(15000);
  Serial.println("----------");
  return 0;
}

    long currX = 0;
    long currY = 0;
    int escape = 0;
    int k=0;
void loop()
{   
    /*if(abs(x)>5){ stepperX.setMaxSpeed(3000);
      stepperX.setAcceleration(1000);}
    else stepperX.setMaxSpeed(2000);*/
       
    /*if(currX != stepperX.currentPosition() || currY != stepperY.currentPosition()){
        currX = stepperX.currentPosition();
        currY = stepperY.currentPosition();
        Serial.println(currX);
        Serial.println(currY);
        //Serial.write((byte*)&currX, sizeof(long));
        //Serial.write((byte*)&currY, sizeof(long));
      }*/
        bool dir = true; //true --> x ; false -->y

    bool tempBool = false;
    /*while (Serial.available() > 0) {
      String data = Serial.readStringUntil(DELIMITER);
      float value = data.toFloat();
      if(data.length()>0)
        if (!tempBool) {
          //if(value<50)
          x = value;
          tempBool = true;
        } else {  
          y = value;
          tempBool  =false;
        }*/
      while (Serial.available() > 0) {
        String data = Serial.readStringUntil(DELIMITER);
        escape = data.toFloat();
        delay(50);
        if (data.length() > 0) {
          if (escape == 0) {
            // Read the two variables when the value is 0
            x = Serial.readStringUntil(DELIMITER).toFloat();
            delay(50);
            y = Serial.readStringUntil(DELIMITER).toFloat();  
            dir=true;    
          }
        }

      delay(50);
      /*Serial.println(escape);
      Serial.println(x);
      Serial.println(y);
      Serial.println("----------");*/
    }
 

    if(escape==1 || escape ==-1){ 
      escape = dragBack(escape);
      x = stepperX.currentPosition();
      y = stepperY.currentPosition();
    }else if(escape==0){
      stepperX.moveTo(convertXtoSteps(x));
      stepperY.moveTo(convertYtoSteps(y));
      
      stepperX.run();
      
      if(dir and stepperX.currentPosition()== convertXtoSteps(x))
        dir = false;
      
      if(!dir){
        stepperY.run();
      }
    }
    
    if(k>20){
      long currX1 = stepperX.currentPosition();
      long currY1 = stepperY.currentPosition();
        if(abs(currX - currX1) >250 || abs(currY - currY1)> 250){
          currX = currX1;
          currY = currY1;
          //Serial.println(currX);
          //Serial.println(currY);
          if(Serial.available()==0){
            Serial.println("+-+-+-+-+-+-");
            //Serial.println(currX);
            Serial.write((byte*)&currX, sizeof(long));
            //delay(500);
            //Serial.println(currY);
            Serial.write((byte*)&currY, sizeof(long));
          }
          //delay(250);
       }
       k=0;
    }
     k++;
  
    /*stepper.moveTo(0);
    stepper.runToPosition();
    delay(1000);*/
}
