import random
import sys, select

score = 0

time  = 3000

# liefert zuefaelligen buchstaben zuerueck
def Random():
    zz = random.randint(97,122)
    Random = chr(zz)
    print(Random)
    return Random

# begruesst den spieler
def begruessung():
    print("hei")
    return

# wartet bis zeit zuende oder eingabe kommt
# liefert die eingabe oder "nichts" zurueck
def input_innerhalb_zeit(millisekunden):
    # alte implementierung:
    # return input()
    return input_with_timeout(millisekunden)


#Liefert ok zueruck wenn nicht nichts
def test(buchstabe, antwort):
    ordnung = int(ord(buchstabe))
    if ordnung <= 109:
        loesung = "a"
    else:
        loesung = "b"
    if antwort == loesung:
        antwort = "ok"
    else:
        antwort = ""
    return antwort



# spielt das spiel und veraendert score
def spiel():
    global score
    global time
    s = "true"
    print("go go")

    print("wenn das wort in der ersten haelfte des alphabetes ist schreibe a wenn nicht dann b")
    while  s == "true":
        zufbu = Random()
        antwort = input_innerhalb_zeit(time)
        antwort = test(zufbu, antwort)
        if antwort == "ok":
            s = "true"
            score = score + 1
            time = time * 0.95

        else:
            break
    return

def ende():
    print("Punktzahl:" ,score)
    print("bye bye")
    return


def input_with_timeout(timeout):
    ready, _, _ = select.select([sys.stdin], [],[], float(timeout) / 1000)
    if ready:
        return sys.stdin.readline().rstrip('\n')
    return ''

begruessung()
spiel()
ende()
