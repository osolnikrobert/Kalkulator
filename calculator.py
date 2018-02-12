print "Pozdravljeni v kalkulatorju!"
x = raw_input("Vnseite prvo stevilo:")
a = raw_input ("Katero operacijo zelite izvesti (+, -, *, /)?")
if a=="+":
        y = raw_input("Vnseite drugo stevilo:")

        x = int(x)
        y = int(y)
        print x + y
elif a == "-":
        y = raw_input("Vnseite drugo stevilo:")

        x = int(x)
        y = int(y)
        print x - y
elif a == "*":
        y = raw_input("Vnseite drugo stevilo:")

        x = int(x)
        y = int(y)
        print x * y
elif a == "/":
        y = raw_input("Vnseite drugo stevilo:")

        x = int(x)
        y = int(y)
        print x / y
else:
        print "Izbrali ste napacno operacijo!"# Kalkulator
