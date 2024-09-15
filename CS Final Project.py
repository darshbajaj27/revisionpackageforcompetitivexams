#Question Bank for Exams

import webbrowser
import numpy
import matplotlib.pyplot as plt
import random 
import time

while True:
    
    print("\n1:Maths Question Bank\n2:Physics Question Bank\n3:Chemistry Question Bank\n4:Calculator\n5: Graphical Representation\n6: Formula Book\n7: Percentile Calculator\n8: Play a Game\n9: Feeling Down? Click 9\n10:Press Anything else to Exit")
    n=int(input("\nInput Your Choice"))
    
    if n==1:
        k=webbrowser.open_new_tab("C:\Darsh\Computer\PROJECT FINALS\Maths.html")
        print(k)
        
    elif n==2:
        k=webbrowser.open_new_tab("C:\Darsh\Computer\PROJECT FINALS\Physics.html")
        print(k)
        
    elif n==3:
        k=webbrowser.open_new_tab("C:\Darsh\Computer\PROJECT FINALS\Chemistry.html")
        print(k)
        
    elif n==4:
        print("1: Addition\n2:Substraction\n3:Multiplication\n4:Division\n5:Exponent")
        i=int(input("Enter Choice: "))
        
        if i==1:
            a=int(input("Enter first number: "))
            b=int(input("Enter second number: "))
            print("Sum = ",a+b)
            
        if i==2:
            a=int(input("Enter first number: "))
            b=int(input("Enter second number: "))
            print("Diffrence = ",a-b)
            
        if i==3:
            a=int(input("Enter first number: "))
            b=int(input("Enter second number: "))
            print("Multiplication = ",a*b)
            
        if i==4:
            a=int(input("Enter first number: "))
            b=int(input("Enter second number: "))
            print("Division = ",a+b)
            
        if i==5:
            a=int(input("Enter first number: "))
            b=int(input("Enter second number: "))
            print("Exponent = ",a**b)

    elif n==5:
        r=numpy.arange(3)
        m=int(input("Enter Choice:     1. Bar Graph          2. Line Graph          3. Pie Chart"))

        if m==1:
            #Bar Graph
            phy=int(input("Enter Marks in Physics"))
            chem=int(input("Enter Marks in Chemistry"))
            math=int(input("Enter Marks obtained in Maths"))
            marks=[phy,chem,math]
            plt.title("Graphical Representation of Marks")
            plt.bar(r, marks, color=['cyan','gold','skyblue'], width=0.25)
            plt.show()
            
        elif m==2:
            #Line Graph
            phy=int(input("Enter Marks in Physics"))
            chem=int(input("Enter Marks in Chemistry"))
            math=int(input("Enter Marks obtained in Maths"))
            marks1=[phy,chem,math]
            print("Shows comparative representation")
            time.sleep(2)
            plt.plot(r,marks1,'gold',marker='d',markeredgecolor='silver')
            plt.show()
            
        elif m==3:
            #Pie Chart
            phy=int(input("Enter Marks in Physics"))
            chem=int(input("Enter Marks in Chemistry"))
            math=int(input("Enter Marks obtained in Maths"))
            marks1=[phy,chem,math]
            print("Shows comparative representation")
            time.sleep(2)
            plt.pie(marks1, labels=["Physics Test", "Chemistry Test", "Maths Test"], autopct='%4.2f%%')
            plt.show()
            
    elif n==6:
        
        print("Formula Book")
        n=int(input("Enter: 1. Physics, 2. Chemistry, 3. Maths"))
        
        if n==1:
              file = open(r"C:\Darsh\Computer\PROJECT FINALS\PhysicsFormula.html", 'r', encoding="utf8")
              for each in file:
                  print(each)
              file.close()
              
        if n==2:
            file = open(r"C:\Darsh\Computer\PROJECT FINALS\ChemistryFormulas.html", 'r', encoding="utf8")
            for each in file:
                print(each)
            file.close()
            
        if n==3:
              file=open(r"C:\Darsh\Computer\PROJECT FINALS\MathsFormulas.html",'r', encoding="utf8")
              for each in file:
                  print(each)
              file.close()
              
    elif n==7:             
        percentile=float(input("Enter your Percentile:"))
        n=int(input("Enter total number of Students:"))
        rank=n*(100-percentile)/(100)
        if int(rank) == 0:
            print("Your Expected Rank is: 1")
        else:
            print("Your Expected Rank is:",int(rank))

    elif n==9:
        k=webbrowser.open_new_tab("https://www.edtimes.in/what-to-tell-yourself-when-you-get-low-marks/")
        print(k)

    elif n==8:
        
        name = input("What is your name? ") 
        # Here the user is asked to enter the name first 

        print("Good Luck ! ", name) 
        time.sleep(1)

        words = ['abstraction',
                      'inheritance',
                      'encapsulation',
                      'polymorphism',
                      'python']

        
        print("Guess the characters.\nEnter ONLY ONE character at a time for 12 times to find out if you can form a logical word related to Computer Science.")
        print("Hint:")

        # Function will choose one random 
        # word from this list of words 
        word = random.choice(words)
        
        for x in range (len(words)):
            if word==words[x]:
                if x==0:
                    print("Showing important things")
                    break
                elif x==1:
                    print("Derived Class, Base Class")
                    break
                elif x==2:
                    print("Wrapping up data")
                    break
                elif x==3:
                    print("Same Name-Different Use")
                    break
                else:
                    print("An Interesting Language")
                    break
            
        time.sleep(2)        

        guesses = '' 

        # any number of turns can be used here 
        turns = 12


        while turns > 0: 
                
                # counts the number of times a user fails 
                failed = 0
                
                # all characters from the input 
                # word taking one at a time. 
                for char in word: 
                        
                        # comparing that character with 
                        # the character in guesses 
                        if char in guesses: 
                                print(char) 
                                
                        else: 
                                print("_") 
                                
                                # for every failure 1 will be 
                                # incremented in failure 
                                failed += 1
                                

                if failed == 0: 
                        # user will win the game if failure is 0 
                        # and 'You Win' will be given as output 
                        print("You Win") 
                        
                        # this print the correct word 
                        print("The word is: ", word) 
                        break
                
                # if user has input the wrong alphabet then 
                # it will ask user to enter another alphabet 
                guess = input("Guess a character:")
                if len(guess)>1:
                    print("Sorry. Only one character at a time. You are disqualified. Word is:",word)
                    break
                
                # every input character will be stored in guesses 
                guesses += guess 
                
                # check input with the character in word 
                if guess not in word: 
                        
                        turns -= 1
                        
                        # if the character doesn’t match the word 
                        # then “Wrong” will be given as output 
                        print("Wrong") 
                        
                        # this will print the number of 
                        # turns left for the user 
                        print("You have", + turns, 'more guesses') 
                        
                        
                        if turns == 0: 
                                print("You Loose")
                                            

    else: 
        print("Thank You")
        time.sleep(1)
        print("This Code has been designed and compiled by Darsh Bajaj under the guidance of Gifty Jobs Ma'am.")
        time.sleep(1)
        break
