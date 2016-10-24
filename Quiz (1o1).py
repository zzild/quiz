print("Hallo Liebe Freunde!")
Score1 = 0
Score2 = 0
print("Wilkommen zum Schaetzquiz!")
print("Wie soll Spieler 1 heissen?")
Player1 = input()
print("Spieler 1 wurde als",Player1, "regestriert")
print("Falls Das falsch ist gebe den Buchstaben 'n' ein ")
schleife = input()
while schleife == "n":
    print("gebe jetzt deinen Namen ein")
    Player1 = input()
    print("Spieler 1 wurde als ",Player1," regstriert")
    print("Falls Das falsch ist gebe den Buchstaben 'n' ein ")
    schleife = input()

print("Jetzt zu Spieler 2!")
Player2 = input()
print("Spieler 2 wurde als",Player2, "regestriert")
print("Falls Das falsch ist gebe den Buchstaben 'n' ein ")
schleife = input()
while schleife == "n":
    print("gebe jetzt deinen Namen ein")
    Player2 = input()
    print("Spieler 2 wurde als ", Player2, " regstriert")
    print("Falls Das falsch ist gebe den Buchstaben 'n' ein ")
    schleife = input()
print("Dann kanns ja losgehen!")
print("Hier kommt die erste Schaetzfrage")
print("Wie viele Bilder hat van gogh selber verkauft?")
print("Zuerst Spieler 1")
Frage11 = input()
for i in range (1,40):
    print ("don't look")
print("Jetzt Spieler 2")
Frage12 = input()

Frage111 = int(Frage11) - 1
Frage121 = int(Frage12) - 1
print("van gogh hat genau 1 bild selber verkauft.")
antwort11 = int(Frage111) * int(Frage111)
antwort12 = int(Frage121) * int(Frage121)
if antwort11 < antwort12:
    print("Damit geht ein Punkt an Spieler1!")
    Score1 = Score1 + 1
if antwort11 > antwort12:
    print("Damit gehtein Punkt an Spieler2!")
    Score2 = Score2 + 1
if antwort11 == antwort12:
    print("Beide gleich nah dran. Kein Punkt fuer niemanden.")
print("Kommen wir zur zweiten Quizfrage!")
print("Wie viele Sekunden haben 10 Jahre")
print("Zuerst",Player1)
Frage21 = input()
for i in range (1,40):
    print ("don't look")
print("Jetzt", Player2)
Frage22 = input()
loesung2 = 315360000
print("10 Jahre entsprechen 315360000 Sekunden")
Frage211 = int(Frage21) - 315360000
Frage221 = int(Frage22) - 315360000
antwort21 = int(Frage211) * int(Frage211)
antwort22 = int(Frage221) * int(Frage221)
if antwort21 < antwort22:
    print("Damit geht der Punkt an", Player1)
    Score1 = Score1 + 1
if antwort21 > antwort22:
    print ("Damit geht der Punkt an ",Player2)
    Score2 = Score2 + 1
if antwort21 == antwort22:
    print("beide gleich gut. Keine Punkte!")
print("Die dritte Frage!")
print("Wie alt ist der aelteste Mensch geworden?")
print(Player1, "Deine Antwort:")
Frage31 = input()
for i in range (1,40):
    print ("don't look")
print("Deine Antwort",Player2)
Frage32 = input()
print("Die Franzoesin Jeanne Calment ist 122 Jahre alt geworden")
Frage311 = int(Frage31) - 122
Frage321 = int(Frage32) - 122
antwort31 = int(Frage311) * int(Frage311)
antwort32 = int(Frage321) * int(Frage321)
if antwort31 < antwort32:
    print("Damit geht der Punkt an",Player1)
    Score1 = Score1 + 1
if antwort31 > antwort32:
    print("Damit gewinnt",Player2)
    Score2 = Score2 + 1
if antwort31 == antwort32:
    print("kein Punkt fuer irgendwen!")
print("Jetzt kommt Frage 4:")
print("Wie viele Alben haben die Beatles veroeffentlicht?")
print(Player1,"?")
Frage41 = input()
for i in range (1,40):
    print ("don't look")
print (Player2,"?")
Frage42 = input()
print("Die Beatles haben insgesamt 13 Alben veroeffentlich")
Frage411=int(Frage41) - 13
Frage421=int(Frage42) - 13
antwort41 = int(Frage411) * int(Frage411)
antwort42 = int(Frage421) * int(Frage421)
if antwort41 < antwort42:
    print ("Der Punkt geht somit an", Player1)
    Score1 = Score1 + 1
if antwort41 > antwort42:
    print ("Der Punkt geht somit an",Player2)
    Score2 = Score2 + 1
if antwort41== antwort42:
    print("Kein Punkt")
print("Kommen wir zur naechsten Frage")
print("Wie viele Staffeln Simpsons gibt es aktuell?")
print(Player1,"?")
Frage51 = input()
for i in range (1,40):
    print ("don't look")
Frage52 = (input)
print("Es gibt aktuell 27 Staffeln der Simpsons")
Frage511 = int(Frage51) - 27
Frage521 = int(Frage52) - 27
antwort51 = int(Frage511) * int(Frage511)
antwort52 = int(Frage521) * int(Frage521)
if antwort51 < antwort52
    print("Der Punkt geht somit an ",Player1)
    Score1 = Score1 + 1
if antwort51 > antwort52
    print("Der Punkt geht somit an", Player2)
    Score2 = Score2 + 1

