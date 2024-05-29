# F = open("p3file.txt", "w")
# F.write(str(P))
# F.close()

F = open("p3file.txt", "r")
print("last score " + str(F.readlines()))
P = 0
Q_1 = input("How many chambers does the human heart have ?"
          " Choose how many options you want 2 or 4.")
if Q_1 == " 4":
    A_1 = input(list((1, 2, 3, 4)))
    if A_1 == " 4":
        print("Congrats, it's the right answer. You have earned 2 points.")
        P = P +2
    else:
        print("Unfortunately, this is not the correct answer.")
else:
    A_1 = input(list((2, 4)))
    if A_1 == " 4":
        print("Congrats, it's the right answer. You have earned a point.")
        P = P +1
    else:
        print("Unfortunately, this is not the correct answer.")
  
  
Q_2 = print("What is the name of the longest nerve in the human body ?")
A_2 = input(list(("spinal cord", "sciatic nerve","vagus nerve")))
if A_2 == " sciatic nerve":
    print("Congrats, it's the right answer. You have earned 3 points.")
    P = P +3
else:
    print("Unfortunately, this is not the correct answer.")
 
 
Q_3 = input("Which blood type is known as the uuniversal donor ?"
            " choose how many options you want 2 or 4.")
if Q_3 == " 4":
    A_3 = input(list(("O-", "A+", "B-", "AB+")))
    if A_3 == " O-":
        print("Congrats, it's the right answer. You have earned 2 points.")
        P = P +2
    else:
        print("Unfortunately, this is not the correct answer.")
else:
    A_3 = input(list(("O-", "B-")))
    if A_3 == " O-":
        print("Congrats, it's the right answer. You have earned a point.")
        P = P +1
    else:
        print("Unfortunately, this is not the correct answer.")

                    
Q_4 = input("Which organ has the ability to regenerate its tissue ? "
            " choose how many options do you want 2 or 4.")
if Q_4 == " 4":
    A_4 = input(list(("brain ", "liver ", "heart ", "lungs")))
    if A_4 == " liver":
        print("Congrats, it's the right answer. You have earned 2 points.")
        P = P +2
    else:
        print("Unfortunately, this is not the correct answer.")
else:
    A_4 = input(list(("lungs ", "liver")))
    if A_4 == " liver":
        print("Congrats, it's the right answer. You have earned a point.")
        P = P +1
    else:
        print("Unfortunately, this is not the correct answer.")


Q_5 = input("Where are the smallest bones in the human body located ? "
            " choose how many options do you want 2 or 4.")
if Q_5 == " 4":
    A_5 = input(list(("fingers ", "toes ", "ears ", "hands")))
    if A_5 == " ears":
        print("Congrats, it's the right answer. You have earned a point.")
        P = P +1
    else :
        print("Unfortunately, this is not the correct answer.")
else :
    A_5 = input(list(("toes ", "ears")))
    if A_5 == " ears":
        print("Congrats, it's the right answer. You have earned a point.")
        P = P +1
    else:
        print("Unfortunately, this is not the correct answer.")


Q_6 = print("What is the medical term for a heart attack ?")
A_6 = input(list(("cerebrovascular accident ", "hypertension ", "myocardial infarction")))
if A_6 == " myocardial infarction":
    print("Congrats, it's the right answer. You have earned a point.")
    P = P +1
else:
    print("Unfortunately, this is not the correct answer.")


Q_7 = input("What is the normal range for adult human bloodpressure ?"
            " choose how many options do you want 2 or 4.")
if Q_7 == " 4":
    A_7 = input(list(("130/80 mmHg ","120/80 mmHg ","140/80 mmHg ","130/70 mmHg")))
    if A_7 == " 120/80 mmHg":
        print("Congrats, it's the right answer. You have earned 2 points.")
        P = P +2
    else:
        print("Unfortunately, this is not the correct answer.")
else:
    A_7 = input(list(("120/80 mmHg ", "130/70 mmHg")))
    if A_7 == " 120/80 mmHg":
        print("Congrats, it's the right answer. You have earned a point.")
        P = P +1
    else:
        print("Unfortunately, this is not the correct answer.")


Q_8 = input("Which chamber of the heart receives oxygenated blood from the lungs ?"
            " choose how many options do you want 2 or 4.")
if Q_8 == " 4":
    A_8 = input(list(("left ventricle ","left atrium ","right ventricle ","right atrium")))
    if A_8 == " left atrium":
        print("Congrats, it's the right answer. You have earned 4 points.")
        P = P +4
    else:
        print("Unfortunately, this is not the correct answer.")
else :
    A_8 = input(list(("left ventricle ", "left atrium")))
    if A_8 == " left atrium":
        print("Congrats, it's the right answer. You have earned 2 points.")
        P = P +2
    else:
        print("Unfortunately, this is not the correct answer.")
        
        
Q_9 = input("What is the term for difficulty breathing ?"
            " choose how many options do you want 2 or 4.")
if Q_9 == " 4":
    A_9 = input(list(("asthma ","dysphagia ","dysarthria ","dyspnea")))
    if A_9 == " dyspnea":
        print("Congrats, it's the right answer. You have earned 2 points.")
        P = P +2
    else:
        print("Unfortunately, this is not the correct answer.")
else:
    A_9 = input(list(("asthma ","dyspnea")))
    if A_9 == " dyspnea":
        print("Congrats, it's the right answer. You have earned a point.")
        P = P +1
    else:
        print("Unfortunately, this is not the correct answer.")


Q_10 = input("Which vitamin is synthesized in the skin upo exposure to sunlight ?"
             "choose how many options do you want 2 or 4.")
if Q_10 == " 4":
    A_10 = input(list(("C ","E ","B ","D")))
    if A_10 == " D":
        print("Congrats, it's the right answer. You have earned a point.")
        P = P + 1
    else:
        print("Unfortunately, this is not the correct answer.")
else:
    A_10 = input(list(("C ","D ")))
    if A_10 == " D":
        print("Congrats, it's the right answer. You have earned a point.")
        P = P + 1
    else:
        print("Unfortunately, this is not the correct answer.")

if P == 20 :
    Q_11 = input("Which of these is the only human cell type not to contain any DNA in the human body ?"
          "Choose how many options do you want 2 or 4")
    if Q_11 == " 4":
        A_11 = input([" white blood cells"," nerve cells"," red blood cells"," plasma"])
        if A_11 == " red blood cells":
            print("Congrats, it's the right answer. You have earned 4 points.")
            P = P + 4
        else :
            print("Unfortunately, this is not the correct answer.")
    if Q_11 == " 2":
        A_11 = input([" white blood cells"," red blood cells"])
        if A_11 == " red blood cells":
            print("Congrats, it's the right answer. You have earned 2 points.")
            P = P + 2
        else :
            print("Unfortunately, this is not the correct answer.")

print("your total is " + str(P))

F = open("p3file.txt", "w")
F.write(str(P))
F.close()
