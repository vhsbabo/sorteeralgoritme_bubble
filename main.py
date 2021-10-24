def on_button_pressed_a():
    lijst = mix([0,1,2,3, 4])
    noten = [Note.A, Note.B, Note.C, Note.D, Note.E]
    wis()
    teken(lijst,noten)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    wis()
input.on_button_pressed(Button.B, on_button_pressed_b)

def mix(list2: List[number]):
    for index in range(len(list2) - 1):
        i = randint(0, len(list2) - 1)
        dummy = list2[i]
        list2[i] = list2[index]
        list2[index] = dummy
    return list2

def teken(lijst: List[number], noten: List[Note]):
    for index in range(len(lijst)):
        print("%s %s"%(index, lijst[index]))
        led.plot(index, lijst[index])
        music.play_tone(noten[lijst[index]], music.beat())

def wis():
    for i in range(5):
        for j in range(5):
            led.unplot(i, j)