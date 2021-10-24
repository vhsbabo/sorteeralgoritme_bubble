function mix () {
    for (let index = 0; index <= lijst.length - 1; index++) {
        j = randint(0, lijst.length - 1)
        wissel(index, j)
    }
}
input.onButtonPressed(Button.A, function () {
    mix()
    tekenGrafiek()
})
function tekenGrafiek () {
    basic.clearScreen()
    for (let index = 0; index <= lijst.length - 1; index++) {
        led.plot(index, 4 - lijst[index])
        music.playTone(noten[lijst[index]], music.beat(BeatFraction.Whole))
    }
}
function wissel (a: number, b: number) {
    dummy = lijst[a]
    lijst[a] = lijst[b]
    lijst[b] = dummy
}
input.onButtonPressed(Button.B, function () {
    sorteer()
})
function sorteer () {
    for (let index = 0; index <= lijst.length - 2; index++) {
        if (lijst[index] > lijst[index + 1]) {
            wissel(index, index + 1)
        }
    }
    tekenGrafiek()
}
let dummy = 0
let j = 0
let lijst: number[] = []
let noten: number[] = []
noten = [
262,
294,
330,
349,
392
]
lijst = [
0,
1,
2,
3,
4
]
