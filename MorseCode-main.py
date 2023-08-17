from microbit import *
import music
import radio
radio.config(group=6)
radio.on()

mc_map = {
    ".-"   : "A",
    "-..." : "B",
    "-.-." : "C",
    "-.."  : "D",
    "."    : "E",
    "..-." : "F",
    "--."  : "G",
    "...." : "H",
    ".."   : "I",
    ".---" : "J",
    "-.-"  : "K",
    ".-.." : "L",
    "--"   : "M",
    "-."   : "N",
    "---"  : "O",
    ".--." : "P",
    "--.-" : "Q",
    ".-."  : "R",
    "..."  : "S",
    "-"    : "T",
    "..-"  : "U",
    "...-" : "V",
    ".--"  : "W",
    "-..-" : "X",
    "-.--" : "Y",
    "--.." : "Z",
    ".----": "1",
    "..---": "2",
    "...--": "3",
    "....-": "4",
    ".....": "5",
    "-....": "6",
    "--...": "7",
    "---..": "8",
    "----.": "9",
    "-----": "0"
}


dotInterval = 230
dashInterval = 470

letterThreshold = 1000

buf = ''

startedToWait = running_time()


def decode(buffer):
    return mc_map.get(buf, '?')


while True:
    
    # checking how long a key was not pressed
    waiting = running_time() - startedToWait
    signal = radio.receive()
    
    if button_a.was_pressed():
        display.show('.')
        radio.send('.')
        music.pitch(1200, duration=dotInterval, wait=True)
        sleep(50)
        display.clear()
        
    elif button_b.was_pressed():
        display.show('-')
        radio.send('-')
        music.pitch(1200, duration=dashInterval, wait=True)
        sleep(50)
        display.clear()
        
    # listening to morse code signals
    if signal:
        if signal == '.':
            buf += '.'
            display.show('.')
            sleep(dotInterval)
            display.clear()
        elif signal == '-':
            buf += '-'
            display.show('-')
            sleep(dashInterval)
            display.clear()

            
        # reset waiting time since a signal has been received
        startedToWait = running_time()

        
    # if waiting is greater than a second and there is buffer
    elif len(buf) > 0 and waiting > letterThreshold:
        character = decode(buf)
        buf = ''
        display.show(character)