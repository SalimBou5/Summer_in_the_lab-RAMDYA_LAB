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

#define RAIL_LENGTH 1917    //1.2 cm //!!!!!!!!!!!!!!!!!!! 

float x = 0;
float y = 0;



// Define a stepper and the PIns it will use
//AccelStepper stepper; // Defaults to AccelStepper::FULL4WIRE (4 PIns) on 2, 3, 4, 5
AccelStepper stepperX=AccelStepper(INTERFACE_X,STEP_PIN_X,DIR_PIN_X);
AccelStepper stepperY=AccelStepper(INTERFACE_Y,STEP_PIN_Y,DIR_PIN_Y);

void dragBack(){

  // reduce y-speed
  stepperY.setMaxSpeed(1000);
  stepperY.setAcceleration(500);
  while(Serial.available()>0)
    Serial.read();

  Serial.flush();

  //tells python that we enter in drag mode
  Serial.write("T");

  //drag on y-axis
  stepperY.move(RAIL_LENGTH);
  stepperY.runToPosition();
  
  //tells python that we left drag mode
  Serial.write("F");

  //reset speed
  stepperY.setMaxSpeed(8000);
  stepperY.setAcceleration(4000);
  return;
}

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

//Store current position of the motors
long currX = 0;
long currY = 0;

//escape == true --> enters drag_back mode
bool escape = false;

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

     //Read instructions sent by python
     while (Serial.available() > 0) {
        //delay(30);
        String data = Serial.readStringUntil(DELIMITER);
        escape = data.toInt();
        delay(50);

        if (data.length() > 0) {
          if (!escape) {
              // Read the two variables when the value is 0
              dir = true;
              arrived = false;
              x = Serial.readStringUntil(DELIMITER).toFloat();
              delay(50);
  
              y = Serial.readStringUntil(DELIMITER).toFloat();      
          }
          Serial.write("R");
        }
    } 

    
    if(escape){ 
      dragBack();
      escape = false;
      x = stepperX.currentPosition();
      y = stepperY.currentPosition();
    }else if(!escape){
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
      if(abs(currX - currX1) > 1000 || abs(currY - currY1)> 500){
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
      else if (!arrived and stepperX.currentPosition()==x && stepperY.currentPosition()==y){
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
    }else k++;

    
}
