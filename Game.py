score = 0

# liefert zuefaelligen buchstaben zuerueck
def random():
    print("a")
    return ("a")

# begruesst den spieler
def begruessung():
    print("hei")
    return

# wartet bis zeit zuende oder eingabe kommt
# liefert die eingabe oder "nichts" zurueck
def input_innerhalb_zeit():
    return input()

#Liefert ok zueruck wenn nicht nichts
def test(antwort):
    if antwort == "a":
        antwort = "ok"
    else:
        antwort = ""
    return antwort



# spielt das spiel und veraendert score
def spiel():
    global score
    s = "true"
    print("go go")

    print("wenn das wort in der ersten haelfte des alphabetes ist schreibe a wenn nicht dann b")
    while  s == "true":
        zufbu = random()
        antwort = input_innerhalb_zeit()
        antwort = test(antwort)
        if antwort == "ok":
            s = "true"
            score = score + 1
        else:
            break
    return

def ende():
    print("Punktzahl:" ,score)
    print("bye bye")
    return

begruessung()
spiel()
ende()
