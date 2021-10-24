def mix():
    global j
    index = 0
    while index <= len(lijst) - 1:
        j = randint(0, len(lijst) - 1)
        wissel(index, j)
        index += 1

def on_button_pressed_a():
    mix()
    tekenGrafiek()
input.on_button_pressed(Button.A, on_button_pressed_a)

def tekenGrafiek():
    basic.clear_screen()
    index2 = 0
    while index2 <= len(lijst) - 1:
        led.plot(index2, 4 - lijst[index2])
        music.play_tone(noten[lijst[index2]], music.beat(BeatFraction.WHOLE))
        index2 += 1
def wissel(a: number, b: number):
    global dummy
    dummy = lijst[a]
    lijst[a] = lijst[b]
    lijst[b] = dummy

def on_button_pressed_b():
    sorteer()
input.on_button_pressed(Button.B, on_button_pressed_b)

def sorteer():
    index3 = 0
    while index3 <= len(lijst) - 2:
        if lijst[index3] > lijst[index3 + 1]:
            wissel(index3, index3 + 1)
        index3 += 1
    tekenGrafiek()
dummy = 0
j = 0
lijst: List[number] = []
noten: List[number] = []
noten = [262, 294, 330, 349, 392]
lijst = [0, 1, 2, 3, 4]