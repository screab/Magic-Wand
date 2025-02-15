#!/usr/bin/env python3
#!Hogwarts Legacy Wand!
#This code is created/modified by 'That's So Mo', the code itself is a modified verison/based off of maspieljr (https://www.instructables.com/SmartWand/)
#This code uses the kano_wand library/module which was created by GammaGames (https://github.com/GammaGames/kano_wand)
#This code uses code that turns the RPI Zero to a USB HID device - I followed RandomNerdTutorials tutorial (https://randomnerdtutorials.com/raspberry-pi-zero-usb-keyboard-hid/)
#Thanks to GammaGames, RandomNerdTutorials, maspieljr - without them, I wouldn't have been able to do this. Thank You. 
#And a special thanks to the Harry Potter fans who contribute so much to the wikias - helped fill in the blanks for some wand movements
#This code is opensource/free to use and modify etc.
#Check my YouTube Channel!: https://www.youtube.com/thatssomo1
#  _    _                                _         _                                  __          __             _ 
# | |  | |                              | |       | |                                 \ \        / /            | |
# | |__| | ___   __ ___      ____ _ _ __| |_ ___  | |     ___  __ _  __ _  ___ _   _   \ \  /\  / /_ _ _ __   __| |
# |  __  |/ _ \ / _` \ \ /\ / / _` | '__| __/ __| | |    / _ \/ _` |/ _` |/ __| | | |   \ \/  \/ / _` | '_ \ / _` |
# | |  | | (_) | (_| |\ V  V / (_| | |  | |_\__ \ | |___|  __/ (_| | (_| | (__| |_| |    \  /\  / (_| | | | | (_| |
# |_|  |_|\___/ \__, | \_/\_/ \__,_|_|   \__|___/ |______\___|\__, |\__,_|\___|\__, |     \/  \/ \__,_|_| |_|\__,_|
#                __/ |                                         __/ |            __/ |                              
#               |___/                                         |___/            |___/                               
#

from kano_wand.kano_wand import Shop, Wand, PATTERN
import moosegesture as mg
import time
import random

#Wand Module classes and definitions
class GestureWand(Wand):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Basic gesture dictionary
        # We use them as tuples so we can use them as keys
        self.gestures = {
            ("U", "U"): "lumos",
            ("D", "D"): "nox",
            ("DL", "R", "DL"): "stupefy",
            ("DR", "R", "UR", "D"): "wingardium_leviosa",
            ("DR", "R", "U"): "levioso",
            ("UL", "UR"): "reducio",
            ("DR", "U", "UR", "DR", "UR"): "flipendo",
            ("R", "D"): "expelliarmus",
            ("UR", "DR", "L"): "incendio",
            ("U", "D", "DR", "R", "L"): "locomotor",
            ("DR", "DL"): "engorgio",
            ("UR", "R", "DR"): "aguamenti",
            ("UR", "R", "DR", "UR", "R", "DR"): "avis",
            ("D", "R", "U"): "reducto",
            ("DR", "R", "UR", "UL", "UR", "R", "DR"): "reparo",
            ("DR", "R", "UR", "U", "UL"): "reparo",
            ("DR", "R", "UR", "UL", "L", "R"): "reparo",
            ("DR", "R", "UR", "UL", "UR", "R"): "reparo",
            ("DR", "R", "UR", "UL", "L", "UL", "R"): "reparo",
            ("DR", "R", "UR", "UL", "R", "DR"): "reparo",
            ("DR", "R", "UL", "L", "R", "D"): "reparo",
            ("U", "DR", "DL", "DR"): "revelio",
            ("DR", "UR"): "protego",
            ("UR", "R", "DR"): "accio",
            ("DR", "U", "DL"): "ancient",
            ("R", "L"): "basic",
            ("L", "R"): "basic",
            ("U", "DL", "U"): "changespells",
            ("UR", "R", "DR", "DL", "L", "UL", "UR", "R", "DR", "DL"): "disillusionment",
            ("R", "DL", "R"): "ancient_throw"
        }
        self.spell = None
        self.pressed = False
        self.positions = []

    def post_connect(self):
        self.subscribe_button()
        self.subscribe_position()

    def post_disconnect(self):
        print("Disconnected...")


    def on_position(self, x, y, pitch, roll):
        if self.pressed:
            # While holding the button,
            #   append the position to the positions array
            self.positions.append(tuple([x, -1 * y]))

    def on_button(self, pressed):
        self.pressed = pressed

        if pressed:
            self.spell = None
        else:
            # If releasing the button, get the gesture
            gesture = mg.getGesture(self.positions)
            self.positions = []
            closest = mg.findClosestMatchingGesture(gesture, self.gestures, maxDifference=1)

            if closest != None:
                # Just use the first gesture in the list using the gesture key
                self.spell = self.gestures[closest[0]]
                self.vibrate(PATTERN.SHORT)
            # Print out the gesture
            print("{}: {}".format(gesture, self.spell))


def main():
    # Create the manager and shop to search for wands
    shop = Shop(wand_class=GestureWand)
    wands = []
    colors = ["#a333c8", "#2185d0", "0x21ba45", "#fbbd08", "#f2711c", "#db2828"]

    try:
        # Scan for wands until it finds one
        while len(wands) == 0:
            print("Scanning...")
            wands = shop.scan(connect=True)

        wand = wands[0]
        while wand.connected:
            # Make a random sleep and transition time
            sleep = random.uniform(0.1, 0.2)
#            transition = math.ceil(sleep * 10)

            if wand.spell == "protego":
                print('protego spell detected')
                wand.spell = None
            if wand.spell == "changespells":
                print('changle spells detected')
                wand.spell = None
            if wand.spell == "ancient":
                print('ancient spell detected')
                wand.spell = None
            if wand.spell == "revelio":
                print('revelio spell detected')
                wand.spell = None
            if wand.spell == "basic":
                print('basic spell detected')
                wand.spell = None
            if wand.spell == "ancient_throw":
                print('ancient_throw spell detected')
                wand.spell = None

            #LEVEL 1 - FIRST ROW OF SPELLS
            if wand.spell == "expelliarmus":
                print('expelliarmus spell detected')

                sleep = random.uniform(0.1, 0.2)
                wand.disconnect()

                wand.spell = None
            if wand.spell == "incendio":
                print('incendio spell detected')
                wand.spell = None
            if wand.spell == "levioso":
                print('levioso spell detected')
                wand.spell = None
            if wand.spell == "accio":
                print('accio spell detected')
                wand.spell = None

            #LEVEL 2 -SECOND ROW OF SPELLS
            if wand.spell == "lumos":
                print('lumos spell detected')

                color_random = random.randint(0, len(colors)-1)
                print(color_random)
                print(colors[color_random])
                wand.set_led(colors[color_random])

                wand.spell = None
            if wand.spell == "nox":
                print('nox charm detected')
                wand.spell = None
            if wand.spell == "disillusionment":
                print('dissillusionment charm detected')
                wand.spell = None
            if wand.spell == "reparo":
                print('reparo spell detected')
                wand.spell = None
            if wand.spell == "accio":
                print('accio spell detected')
                wand.spell = None

            #LEVEL 3 - THIRD ROW OF SPELLS
            if wand.spell == "lumos":
                print('lumos spell detected')
                wand.spell = None
            if wand.spell == "nox":
                wand.spell = None
            if wand.spell == "flipendo":
                print('flipendo spell detected')
                wand.spell = None
            if wand.spell == "reparo":
                print('reparo spell detected')
                wand.spell = None
            if wand.spell == "wingardium_leviosa":
                print('wingardium_leviosa spell detected')
                wand.spell = None

            #LEVEL 4 -Fourth ROW OF SPELLS
            if wand.spell == "lumos":
                print('lumos spell detected')
                wand.spell = None
            if wand.spell == "nox":
                print('nox spell detected')
                wand.spell = None
            if wand.spell == "wingardium_leviosa":
                print('wingardium_leviosa spell detected')
            if wand.spell == "reparo":
                print('reparo spell detected')
                wand.spell = None
            if wand.spell == "levioso":
                print('levioso spell detected')
                wand.spell = None                
            time.sleep(sleep)

            print('While loop ended')

        print('While loop exited')


#    # Detect keyboard interrupt and disconnect wands,
    except KeyboardInterrupt as e:
        for wand in wands:
            wand.disconnect()
#        manager.reset()


if __name__ == "__main__":
    main()
