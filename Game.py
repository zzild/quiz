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
    return "a"

def test(antwort):
    if antwort == "a":
        antwort = "ok"



# spielt das spiel und veraendert score
def spiel():
    s = "true"
    print("go go")

    print("wenn das wort in der ersten haelfte des alphabetes ist schreibe a wenn nicht dann b")
    while  s == "true":
        dingart = random()
        antwort = input_innerhalb_zeit()
        test(antwort)
        if antwort == "ok":
            s = "true"
            score = score + 1
    return

def ende():
    print("Punktzahl:" ,score)
    print("bye bye")
    return

begruessung()
spiel()
ende()
