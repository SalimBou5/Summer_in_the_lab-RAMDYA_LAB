// Bounce.pde
// -*- mode: C++ -*-
//
// Make a single stepper bounce from one limit to another
//
// Copyright (C) 2012 Mike McCauley
// $Id: Random.pde,v 1.1 2011/01/05 01:51:01 mikem Exp mikem $

#include <AccelStepper.h>
#define dirPin 9
#define stepPin 6
#define interface 1

// Define a stepper and the pins it will use
//AccelStepper stepper; // Defaults to AccelStepper::FULL4WIRE (4 pins) on 2, 3, 4, 5
AccelStepper stepper=AccelStepper(interface,stepPin,dirPin);


long convertXtoSteps(float x){ //x in cm
    return (long)((5.02*x/(1.6*3.14))*1600.0);
}

void setup()
{  
  // Change these to suit your stepper if you want
  stepper.setMaxSpeed(2000);
  stepper.setAcceleration(500);
}

void loop()
{
    stepper.moveTo(convertXtoSteps(-11.23));
    stepper.runToPosition();
    delay(1000);
    /*stepper.moveTo(0);
    stepper.runToPosition();
    delay(1000);*/
}
