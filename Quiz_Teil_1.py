Score = 0
print("Hallo.")
print("Willkommen bei der besten Quizshow!")
print("Wie soll ich dich nennen?")
username = input()
print ("Hallo", username, ",ich werde dir gleich ein paar Fragen stellen bei denen es immer 4 Antwortmoeglichkeiten gibt.")
print ("Am Ende werde ich dir dann dein Ergebnis praesentieren. Sag sag bzw. schreib wenn du bereit bist!")
la = input()
print("Hier deine Erste Frage!")
print("In Welchem Jahr wurde der Bau des Eifelturms beendet A 1887 B 1889 C 1891 D 1893")
print ("Bitte gebe jetzt deine Loesung als einen Buchstaben an (grossgeschrieben)")
Frage1 = input()
if Frage1 == "B":
     print("Das ist richtig, sehr gut. Ein Punkt fuer dich!")
     Score = Score + 1
else:
    print("Das ist leider falsch!")

print("Der Bau des Eifelturms begann 1887 und endete 1889.")
print("Naechste Frage!")
print("Wie alt wurde Michel Jackson? A 50 B 51 C 52 D 53")
Frage2 = input()
if Frage2 == "A":
    print("Das ist richitg!")
    Score = Score + 1
    if Score == 2:
        print("Du bist Ja richtig gut dabei! Weiter So!")
else:
    print("Schade.")
    if Score == 1:
        print("Immerhin eine Frage richtig!")
print("Michael Joseph Jackson wurde am 29.8.1958 geboren und verstarb am 25 6. 2009 und hat somit 50 Jahre gelebt. ")

print("Der Kater Scooter ist der aelteste Kater der Welt und kommt aus Texas...")
print("Wie alt ist dieser Kater A 27 B 29 C 30 D 31")
Frage3 = input()

if Frage3 == "C":
    print("Das ist koooooorrreeeekt!")
    Score = Score + 1
else:
    print("Das iiiiiist .......................................... leider falsch")
print("Der Kater ist zurzeit 30 Jahre alt!")
print("und jetzt die naechste Frage!")
print("Wie die meisten wissen ist Tokio die groesste Stadt der Welt. Wie viele Einwohner hat sie eigentlich?")
print("A 34 Millionen B 35 Millionen C 36 Millionen D 37 Millionen")
frage4 = input()
if frage4 == "D":
    print("Genau!")
    Score = Score + 1
else:
    print("Leider falsch!")
print("In Tokio leben zurzeit 37.000.000 Einwohner, das sind ca. 20mal soviele wie in Hamburg")
print("und die naechste Frage!")
print("Was sind die ersten 5 Nachkommastellen von Pi?")
print("A 3,14158 B 3,14159 C 3,14169 D 3,14168")
frage5 = input()
if frage5 == "B":
    print ("genau richtig!")
    Score = Score + 1
else:
    print("ne nicht richtig...")
    if Score == 0:
        print ("von dir haette ich echt mehr erwartet...")
print("pi entspricht: 3,14159265359...")
print("Nachste!")
print("Wie viele Moeglichkeiten gibt es beim Schach nachdem Weiss einmal gezogen hat und Schwarz einmal gezogen hat?")
print("A 256 B 324 C 400 D 484 ")
Frage6 = input()
if Frage6 == "C":
    print("Jap das ist korrekt")
    Score = Score + 1
else:
    print("Nope")
print("Es gibt genau 400 Moeglichkeiten")
print("Jetzt kommt leider schon die letzte Frage meines kurzen Quiz' ")
print("Wie alt ist die aelteste Katze der Welt, Creme Puff geworden?")
print("A 35 B 36 C 37 D 38 ")
Frage7 = input()
if Frage7 == "D":
    print("Ja das stimmt!")
    Score = Score + 1
else:
    print("wirklich Schade!")
print("Creme Puff ist mit 38 Jahren und 3 Tagen in Texas")

print("Liebe/r ", username ,"du hast von 7 moeglichen Punkten", Score ," Punkte erreicht")
Prozent= Score/7 * 100
print("Damit hast du", Prozent,"Prozent erreicht." )