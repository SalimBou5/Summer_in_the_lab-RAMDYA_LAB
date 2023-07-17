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

#define convertXtoSteps(x) (long)((2*EMPIRICAL*x/(RAYON*PI))*REV)//x in cm
#define convertYtoSteps(y) (long)((EMPIRICAL*y/(RAYON*PI))*REV)//y in cm

#define stepsToX(s) (float)((RAYON*PI*s)/(2*EMPIRICAL*REV))
#define stepsToY(s) (float)((RAYON*PI*s)/(EMPIRICAL*REV))

#define DELIMITER ','

#define RAIL_LENGTH 1.2 //cm //!!!!!!!!!!!!!!!!!!! 
    
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
bool dragBack(){
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
}


void loop()
{   
    /*if(abs(x)>5){ stepperX.setMaxSpeed(3000);
      stepperX.setAcceleration(1000);}
    else stepperX.setMaxSpeed(2000);*/
       

    bool tempBool = false;
    while (Serial.available() > 0) {
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
        }
      delay(50);
      Serial.println(x);
      Serial.println(y);
      Serial.println("----------");
    }
 
      
    long currX = stepperX.currentPosition();
    long currY = stepperY.currentPosition();
    if(x>70){//stepsToY(x)>70){ 
      dragBack();
      x = stepsToX(stepperX.currentPosition());
      y = stepsToY(stepperY.currentPosition());
    
    }else {

      stepperX.moveTo(convertXtoSteps(x));
      stepperY.moveTo(convertYtoSteps(y));
      stepperX.runToPosition();
      stepperY.runToPosition();
      /*if(!(stepperX.isRunning()) and !(stepperY.isRunning())and currX != stepperX.currentPosition() || currY != stepperY.currentPosition()){
        currX = stepperX.currentPosition();
        currY = stepperY.currentPosition();
        Serial.write((byte*)&currX, sizeof(long));
        Serial.write((byte*)&currY, sizeof(long));
      }*/
    
    }
    
    /*if(stepperX.distanceToGo() == 0 && stepperY.distanceToGo() == 0){
       Serial.println("++++++++++++++");
       Serial.println(stepsToX(stepperX.currentPosition()));
       Serial.println(stepsToY(stepperY.currentPosition()));
       //Serial.println((stepperX.currentPosition()));
       //Serial.println((stepperY.currentPosition()));
       Serial.println("++++++++++++++");
       
    }*/
    /*stepper.moveTo(0);
    stepper.runToPosition();
    delay(1000);*/
}
