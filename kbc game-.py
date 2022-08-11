question_list = ["1.How many continents are there?",
    "2.What is the capital of India?",
   "3.NG mei kaun se course padhaya jaata hai?"]

option_list = [
["1.Four", "2.Nine", "3.Seven", "4.Eight"],
["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"],
["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture"]]

solution_list = [3, 4, 1]
lifeline_list=["1.four","2.seven"
               "1.chandigarh","2.delhi"
               "1.software engineering","2.tourism"]
lifeline_option=[2,2,1]
name=input("enter your name")
print("welcome to KBC")
print("your question is on your screen")
print("your first question is :-")
i=0
count=1
am=0
while i<len(question_list):
    print(question_list[i])
    j=0
    while j<len(option_list[i]):
        print(option_list[i][j])
        j+=1
    if count <=1:
        lifeline=input(" do you need lifeline? ")
        if lifeline=="yes":
            b=0
            while b<len(lifeline_list[i]):
                print(lifeline_list[i][b])
                b+=1
            c=int(input("choose lifeline answers"))
            if c==lifeline_option[i]:
                am=am+2000
                print("you are right",am)
            else:
                print("you are wrong",am)
                break
            count+=1
        else:
            qu=int(input("please choose your ans"))
            if qu==lifeline_option[i]:
                am=am+2000
                print("you are right",am)
            else:
                print("you are wrong",am)
                break
    else:
        que=int(input("choose your answer"))
        if que==lifeline_option[i]:
            am=am+2000
            print("you are right",am)
        else:
            print("you are wrong",am)
            break
    i+=1            

            
    