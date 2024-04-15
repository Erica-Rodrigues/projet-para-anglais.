#projet 2.1
#Q = input("Combien de ° ?")
#A = ((float(Q)) - 32)
#print((str(int((int(A))/1.8))) + "° Celsius")

#projet 2.2
#Q = input("mètres vers pieds ou pieds vers mètres ?")
#C = input("Combien ?")
#if Q == " mètres vers pieds" :
    #print((str(int(float(C)*3.281))) + " pieds")
#else :
    #print((str(int(float(C)/3.281))) + " mètres")

#projet 2.3
#H = input("Combien d'heures se sont écoulées ?")
#M = input("Combien de minutes se sont écoulées ?")
#S = input("Combien de secondes se sont écoulées ?")
#print(str(((int(H))*(60**2)) + ((int(M))*60) + int(S)) + " secondes se sont écoulées au total.")

Stotal = input("Combien de secondes se sont écoulées ?")
H = ((int(Stotal))//(60**2))
M = (((int(Stotal)) - ((int(H))*(60**2)))//60)
S = ((int(Stotal)) - (int(H))*(60**2) - ((int(M))*60))
print("Cela fait " + str(H) + " heures, " + str(M) + " minutes et " + str(S) + " secondes.")

