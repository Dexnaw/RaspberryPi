'''Importation des fonctions utiles à la réalisation du projet.'''
import numpy as np
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from time import sleep

'''Fixe les fonctions de chaque direction du joystick.'''
def refresh():

    sense.stick.direction_up = push_up
    sense.stick.direction_down = push_down
    sense.stick.direction_left = push_left
    sense.stick.direction_right = push_right

'''Fonction déclanchée lors d'une pression vers la droite du joystick : affiche la température en degrés Celcius.'''
def push_right(event):
	if event.action != ACTION_RELEASED:
		celsius(sense)
        sleep(1)

'''Fonction déclanchée lors d'une pression vers la gauche du joystick : affiche la température en degrés Fahrenheit.'''
def push_left(event):
	if event.action != ACTION_RELEASED:
		fahrenheit(sense)
        sleep(1)

'''Fonction déclanchée lors d'une pression vers le haut du joystick : appelle la fonction display_readings.'''
def push_up(event):
    if event.action != ACTION_RELEASED:
        display_readings(sense)
        sleep(1)

'''Fonction déclanchée lors d'une pression vers le haut du joystick : appelle la fonction display_readings_two.'''
def push_down(event):
    if event.action != ACTION_RELEASED:
        display_readings_two(sense)
        sleep(1)	

'''Evalue le résultat de l'orientation du SenseHat en degré et retourne une valeur comprise entre 0 et 7 permettant un intervalle correct facilitant l'affichage sur la matrice 8x8 des LEDs du SenseHat.'''
def evaluate (axe):
    val = 0
    if axe > 0 :
        if axe < 45:
            val = 4
        elif axe < 90:
            val = 5
        elif axe < 135:
            val = 6
        else :
            val = 7
    else :
        if axe > -45:
            val = 3
        elif axe > -90:
            val = 2
        elif axe > -135:
            val = 1
        else :
            val = 0
    return val

'''Evalue le résultat de l'orientation du SenseHat en degré et retourne une valeur comprise entre 0 et 7 permettant un intervalle correct facilitant l'affichage sur la matrice 8x8 des LEDs du SenseHat (Pour le deuxième mode d'affichage).'''
def evaluate_two(axe):
	if axe >= 360:
        axe = axe - 360
    val = 0
    if axe <= 22 :
        val = 0
    elif axe <= 67 :
        val = 7
    elif axe <= 112 :
        val = 6
    elif axe <= 157 :
        val = 5
    elif axe <= 202 :
        val = 4
    elif axe <= 247 :
        val = 3
    elif axe <= 292 :
        val = 2
    elif axe <= 337 :
        val = 1
    else :
        val = 0
    return val
	

def celsius(hat):

		temp = round(sense.get_temperature(), 1)

		sense.show_message("{0}C".format(temp), text_colour=[255, 0, 0])
		refresh()

def fahrenheit(hat):
	
		temp = sense.get_temperature()
		temp = round((temp * 1.8) + 32, 1)

		sense.show_message("{0}F".format(temp), text_colour=[255, 0, 0])
		
		refresh()
		
'''Permet l'affichage des différents axes d'orientation sur un graphique à bâtonnets.'''
def display_readings(hat):

    test = True
    i = 0

    while test :

        for event in sense.stick.get_events():
            if "{}".format(event.action) == "pressed" :
                test = False
                sense.show_message("Choice", text_colour=[255, 0, 0])
                refresh()


        n = (0, 0, 0)
        r = (255, 0, 0)
        g = (0, 255, 0)
        b = (0, 0, 255)

        acceleration = sense.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']

        orientation = sense.get_orientation_degrees()
        lacet = orientation['yaw']

        value_X = evaluate(x*180)
        value_Y = evaluate(y*180)
        value_Z = evaluate(lacet-180)

        i = i+1
        if(i==30) :
            i = 0

            screen = [  n, n, n, n, n, n, n, n,
                        n, n, n, n, n, n, n, n,
                        n, n, n, n, n, n, n, n,
                        n, n, n, n, n, n, n, n,
                        n, n, n, n, n, n, n, n,
                        n, n, n, n, n, n, n, n,
                        n, n, n, n, n, n, n, n,
                        n, n, n, n, n, n, n, n]

            if value_X >= 4 :
                for i in range (4, value_X+1):
                    screen[i] = r
                    screen[8+i] = r
            else :
                for i in range (value_X, 4):
                    screen[i] = r
                    screen[8+i] = r

            if value_Y >= 4 :
                for i in range (4, value_Y+1):
                    screen[24+i] = g
                    screen[32+i] = g
            else :
                for i in range (value_Y, 4):
                    screen[24+i] = g
                    screen[32+i] = g

            if value_Z >= 4 :
                for i in range (4, value_Z+1):
                    screen[48+i] = b
                    screen[56+i] = b
            else :
                for i in range (value_Z, 4):
                    screen[48+i] = b
                    screen[56+i] = b

            sense.set_pixels(screen)

'''Permet un affichage des différents axes d'orientation. Les axes X et Y sont représentés par une croix et l'axe Z par un point représentant le nord.'''
def display_readings_two(hat):

    test = True
    i = 0

    while test :

        for event in sense.stick.get_events():
            if "{}".format(event.action) == "pressed" :
                test = False
                sense.show_message("Choice", text_colour=[255, 0, 0])
                refresh()


        n = (0, 0, 0)
        r = (255, 0, 0)
        g = (0, 255, 0)
        b = (0, 0, 255)
        w = (150,150,150)

        acceleration = sense.get_accelerometer_raw()
        x = acceleration['x']
        y = acceleration['y']

        orientation = sense.get_orientation_degrees()
        lacet = orientation['yaw']

        value_X = evaluate(x*180)
        value_Y = evaluate(y*180)
        value_Z = evaluate_two(lacet+180)

        i = i+1
        if(i==30) :
            i = 0

            screen = [  n, n, n, n, n, n, n, n,
                        n, n, n, n, n, n, n, n,
                        n, n, n, n, n, n, n, n,
                        n, n, n, w, w, n, n, n,
                        n, n, n, w, w, n, n, n,
                        n, n, n, n, n, n, n, n,
                        n, n, n, n, n, n, n, n,
                        n, n, n, n, n, n, n, n]

            if value_Y >= 4 :
                screen[43] = g
                screen[44] = g
                if value_Y >= 6 :
                    screen[51] = g
                    screen[52] = g
            elif value_Y <= 3 :
                screen[19] = g
                screen[20] = g
                if value_Y <= 1 :
                    screen[11] = g
                    screen[12] = g

            if value_X >= 4 :
                screen[29] = r
                screen[37] = r
                if value_X >= 6 :
                    screen[30] = r
                    screen[38] = r
            elif value_X <= 3 :
                screen[26] = r
                screen[34] = r
                if value_X <= 1 :
                    screen[25] = r
                    screen[33] = r

            if value_Z == 0 :
                screen[16] = b
                screen[24] = b
                screen[32] = b
                screen[40] = b
            elif value_Z == 1 :
                screen[0] = b
                screen[1] = b
                screen[8] = b
            elif value_Z == 2 :
                screen[2] = b
                screen[3] = b
                screen[4] = b
                screen[5] = b
            elif value_Z == 3 :
                screen[6] = b
                screen[7] = b
                screen[15] = b
            elif value_Z == 4 :
                screen[23] = b
                screen[31] = b
                screen[39] = b
                screen[47] = b
            elif value_Z == 5 :
                screen[55] = b
                screen[62] = b
                screen[63] = b
            elif value_Z == 6 :
                screen[58] = b
                screen[59] = b
                screen[60] = b
                screen[61] = b
            elif value_Z == 7 :
                screen[48] = b
                screen[56] = b
                screen[57] = b

            sense.set_pixels(screen)

sense = SenseHat()
sense.clear()

'''Boucle infinie permettant au programme d'être utilisé de façon continue.'''
while True :
    refresh()
    sleep(1)