import time


def countMinutes(l, minutes, s):
    seconds = 60
    while minutes >= 1:
        minutes -= 1
        while seconds >= 1:
            seconds -= 1
            l.append(s + str(minutes) + ":" + str(seconds))


def main(workMinutes, pauseMinutes, cycles):
    l = []
    l.append("1")
    l.append("2")
    l.append("3")
    for i in range(cycles):
        if i==cycles-1:
            l.append("START!")
            s="WORK: "
            countMinutes(l, workMinutes, s)
        else:
            l.append("START!")
            s="WORK: "
            countMinutes(l, workMinutes, s)
            l.append("PAUSE!")
            s="REST: "
            countMinutes(l, pauseMinutes, s)
    return(l)
