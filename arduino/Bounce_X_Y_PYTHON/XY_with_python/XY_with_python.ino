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
//#define REV 1600.0
//#define RAYON 1.6
//#define EMPIRICAL 5.02

//#define convertXtoSteps(x) (long)((2*EMPIRICAL*x/(RAYON*PI))*REV)//x in cm
//#define convertYtoSteps(y) (long)((EMPIRICAL*y/(RAYON*PI))*REV)//y in cm

//#define stepsToX(s) (float)((RAYON*PI*s)/(2*EMPIRICAL*REV))
//#define stepsToY(s) (float)((RAYON*PI*s)/(EMPIRICAL*REV))

#define DELIMITER ','

#define RAIL_LENGTH 1918//1.2 cm //!!!!!!!!!!!!!!!!!!! 

#define RAIL_LENGTH_LAT 400//1.2 cm //!!!!!!!!!!!!!!!!!!! 

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
int dragBack(int escape){
  //Serial.println("DRAG");

  // reduce y-speed
  stepperY.setMaxSpeed(800);
  stepperY.setAcceleration(400);

  //tells python that we enter in drag mode
  //Serial.flush();
  Serial.write(true);
  //Serial.flush();
  //drag on y-axis
  stepperY.move(RAIL_LENGTH);
  stepperY.runToPosition();
  
  // reduce x-speed
  stepperX.setMaxSpeed(800);
  stepperX.setAcceleration(400);  
  //escape on x-axis
  stepperX.move(escape*RAIL_LENGTH_LAT);
  stepperX.runToPosition();
  //Serial.flush();
  //tells python that we left drag mode
  Serial.write(false);
  //Serial.flush();
  
  //reset speed
  stepperY.setMaxSpeed(8000);
  stepperY.setAcceleration(4000);
  stepperX.setMaxSpeed(30000);
  stepperX.setAcceleration(15000);
  //Serial.println("+++++++++++");
  return 0;
}

    long currX = 0;
    long currY = 0;
    int escape = 0;
void loop()
{   
   if(currX != stepperX.currentPosition() || currY != stepperY.currentPosition()){
        currX = stepperX.currentPosition();
        currY = stepperY.currentPosition();
        //Serial.println(currX);
        //Serial.println(currY);
        //if(Serial.available()==0){
          //Serial.write((byte*)&currX, sizeof(long));
          //delay(100);
          //Serial.write((byte*)&currY, sizeof(long));
        //}
        //delay(100);
     }

    bool tempBool = false;
    /*while (Serial.available() > 0) {
      String data = Serial.readStringUntil(DELIMITER);
      float value = data.toFloat();
      delay(100);
      if(data.length()>0)
        if (!tempBool) {
          //if(value<50)
          x = value;
          tempBool = true;
        } else {  
          y = value;
          tempBool  =false;
        }
    }*/
    
    while (Serial.available() > 0) {
        String data = Serial.readStringUntil(DELIMITER);
        escape = data.toFloat();
        delay(100);

        if (data.length() > 0) {
          if (escape == 0) {
            // Read the two variables when the value is 0
            x = Serial.readStringUntil(DELIMITER).toFloat();
            delay(100);

            y = Serial.readStringUntil(DELIMITER).toFloat();      
          }
          else{
            //Serial.flush();
            x = stepperX.currentPosition();
            y = stepperY.currentPosition();
          }
        }
        //delay(100);

        /*
        Serial.println(escape);
        Serial.println(x);
        Serial.println(y);
        Serial.println("----------");*/
    } 
      
    //escape=random(2)-1;
    if(escape!=0){ 
      escape = dragBack(escape);
      x = stepperX.currentPosition();
      y = stepperY.currentPosition();
    }else {
      stepperX.moveTo(x);
      stepperY.moveTo(y);
      stepperX.runToPosition();
      /*if(currX != stepperX.currentPosition()){
        currX = stepperX.currentPosition();
        Serial.write((byte*)&currX, sizeof(long));
      }*/
      stepperY.runToPosition();
      /*if( currY != stepperY.currentPosition()){
        currY = stepperY.currentPosition();
        Serial.write((byte*)&currY, sizeof(long));
        delay(500);
      }*/
    
    }

    //Serial.flush();
    
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
