# Import required libraries
import joblib
import os
model = joblib.load('salary.pk1')

# Function to predict salary
def salary_predict():
    os.system("clear")
    os.system('tput setaf 1')
    os.system('figlet -c Salary Prediction')
    os.system('tput setaf 3')

    exp = input("\nEnter experience in years : ")
    predict = model.predict([[int(exp)]])
    os.system('tput setaf 4')
    print("\nPredicted Salary is: {}".format(predict[0]))

# Menu to exit or continue
def menu():
    while True:
        os.system('tput setaf 3')
        ch = input("\nPress 1 to continue, press 2 to exit : ")
        if int(ch) == 1:
            salary_predict()
    
        elif int(ch) == 2:
            os.system('tput setaf 7')
            exit()

        else:
            os.system('tput setaf 4')
            input("\nSelect Valid Option, press enter to continue...")
            menu()

salary_predict()

menu()