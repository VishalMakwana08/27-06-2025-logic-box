#27-06-2025 logic-box exam
#menu driven program
#pattern generater 'Triangle'
#Number Analyzer Even Odd 
#Use Nested loop for build logic


#start program here entry point

print("Welcome To The Pattern Generator And Number Analyzer Python Program By 'Vishal Makwana'")

while(True):
    #Menu Driven Option For User
    print("\nSelect Any Option:\n")
    print("1.Generate A Pattern 'Triangle'")
    print("2.Analyze A Range Of Numbers 'even or odd'")
    print("3.Exit\n")
    user_input=int(input("Enter Your Choice:"))
    match user_input:
        case 1 :
            #pattern generate logic using if else and nested loop
            print("1.Left Angle Triangle")
            print("2.Right Angle Triangle")
            print("3.Full Triangle")
            triangle_shape=int(input("\nChoose Triangle Shape:\n"))
            num_row=int(input("Enter Numbers Of Rows:"))
            if(num_row<5 or num_row<0 or triangle_shape<0 or triangle_shape>3):
        
                if(num_row<5 and num_row>0):
                   print("Dear User For Generate Perfect Triangle Pattern Wants Minimum 5 rows")
                elif num_row<0:
                    print("Dear User Negative Number Not Allowed Plz Enter Only Positive Number")
                else:
                    print("Invalid Option For Shape")
            else:
                print("...Your Pattern Is Generated Successfully...")
                if triangle_shape==1:
                    #left angle triangle
                    for i in range(1,num_row+1):
                        for j in range(1,i+1):
                            print("*",end=" ")
                        print("")
                elif triangle_shape==2:
                    #right angle triangle
                    for i in range(1,num_row+1):
                        for j in range(1,6-i):
                            print(" ",end=" ")
                        for k in range(1,i+1):
                            print("*",end=" ")
                        print("")
                
                else:
                     #full triangle
                     for i in range(1,num_row+1):
                        for j in range(1,6-i):
                            print(" ",end="")
                        for k in range(1,i+1):
                            print("*",end=" ")
                        print("")
            

        case 2 :
            #Number Analyzer Logic For Find Even Odd In Range Of Number And Sum Of All Number In Range
            start_range=int(input("Enter The Start Range Number:"))
            end_range=int(input("Enter The End Range Number:"))
            sum=int(0)
            if end_range>start_range:
                
                print("\n...Even Or Odd Numbers Your Given Range...\n")
                for i in range(start_range,end_range+1):

                    if(i%2==0):
                        print(f"Number {i} Is Even")
                    else:
                        print(f"Number {i} Is Odd")
                    sum+=i
                print(f"Sum Of All Numbers From {start_range} To {end_range} Is: {sum}")
            else:
                print("\nThe End Range Must Be Greater Than Start Range\n")

        case 3 :
            #exit
            print("\nExisting The Program,GoodBye!\n")
            break
        case _:
            #default case if user not select given options
            print("Inavalid Option Or Choice")
print("End Of Python Program")
