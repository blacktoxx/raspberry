#!/usr/bin/python3

import RPi.GPIO as GPIO
from time import sleep

pinA = 33
pinB = 31
pinC = 36
pinD = 38
pinE = 40
pinF = 35
pinG = 37
pinDP = 32

GPIO.setmode(GPIO.BOARD)

GPIO.setup(pinA, GPIO.OUT)
GPIO.setup(pinB, GPIO.OUT)
GPIO.setup(pinC, GPIO.OUT)
GPIO.setup(pinD, GPIO.OUT)
GPIO.setup(pinE, GPIO.OUT)
GPIO.setup(pinF, GPIO.OUT)
GPIO.setup(pinG, GPIO.OUT)
GPIO.setup(pinDP, GPIO.OUT)




def reset():
	GPIO.output(pinA, GPIO.LOW)
	GPIO.output(pinB, GPIO.LOW)
	GPIO.output(pinC, GPIO.LOW)
	GPIO.output(pinD, GPIO.LOW)
	GPIO.output(pinE, GPIO.LOW)
	GPIO.output(pinF, GPIO.LOW)
	GPIO.output(pinG, GPIO.LOW)
	GPIO.output(pinDP, GPIO.LOW)


def printOne():
	reset()
	GPIO.output(pinB, GPIO.HIGH)
	GPIO.output(pinC, GPIO.HIGH)


def printTwo():
	reset()
	GPIO.output(pinA, GPIO.HIGH)
	GPIO.output(pinB, GPIO.HIGH)
	GPIO.output(pinG, GPIO.HIGH)
	GPIO.output(pinE, GPIO.HIGH)
	GPIO.output(pinD, GPIO.HIGH)


def printThree():
	reset()
	GPIO.output(pinA, GPIO.HIGH)
	GPIO.output(pinB, GPIO.HIGH)
	GPIO.output(pinG, GPIO.HIGH)
	GPIO.output(pinC, GPIO.HIGH)
	GPIO.output(pinD, GPIO.HIGH)


def printFour():
	reset()
	GPIO.output(pinF, GPIO.HIGH)
	GPIO.output(pinG, GPIO.HIGH)
	GPIO.output(pinB, GPIO.HIGH)
	GPIO.output(pinC, GPIO.HIGH)


def printFive():
	reset()
	GPIO.output(pinA, GPIO.HIGH)
	GPIO.output(pinF, GPIO.HIGH)
	GPIO.output(pinG, GPIO.HIGH)
	GPIO.output(pinC, GPIO.HIGH)
	GPIO.output(pinD, GPIO.HIGH)


def printSix():
	reset()
	GPIO.output(pinF, GPIO.HIGH)
	GPIO.output(pinG, GPIO.HIGH)
	GPIO.output(pinC, GPIO.HIGH)
	GPIO.output(pinE, GPIO.HIGH)
	GPIO.output(pinD, GPIO.HIGH)
	GPIO.output(pinA, GPIO.HIGH)


def printSeven():
	reset()
	GPIO.output(pinA, GPIO.HIGH)
	GPIO.output(pinB, GPIO.HIGH)
	GPIO.output(pinC, GPIO.HIGH)


def printEight():
	reset()
	GPIO.output(pinA, GPIO.HIGH)
	GPIO.output(pinB, GPIO.HIGH)
	GPIO.output(pinC, GPIO.HIGH)
	GPIO.output(pinD, GPIO.HIGH)
	GPIO.output(pinE, GPIO.HIGH)
	GPIO.output(pinF, GPIO.HIGH)
	GPIO.output(pinG, GPIO.HIGH)


def printNine():
	reset()
	GPIO.output(pinA, GPIO.HIGH)
	GPIO.output(pinF, GPIO.HIGH)
	GPIO.output(pinG, GPIO.HIGH)
	GPIO.output(pinB, GPIO.HIGH)
	GPIO.output(pinC, GPIO.HIGH)
	GPIO.output(pinD, GPIO.HIGH)


def printDot():
	GPIO.output(pinDP, GPIO.HIGH)


def deleteDot():
	GPIO.output(pinDP, GPIO.LOW)


# Programm

try:
	delay = 0.2
	count = 0

finally:
	GPIO.cleanup()