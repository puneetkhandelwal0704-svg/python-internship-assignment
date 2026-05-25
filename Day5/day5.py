import requests

def weather_data(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=58fa4a2d0cadc4139545de442f7bfd26&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()                                 #api code                 
        print("\n-----WEATHER----")                         
        print("Temperature:", data['main']['temp'])
        print("pressure:",data['main']['pressure'])  
        print("feels like:",data['main']['feels_like'])
        print("humudity:",data['main']['humidity'],"%")

    except requests.exceptions.RequestException as e:
        print("Error:", e)


city = input("Enter the city name: ")
weather_data(city) 


'''import pywhatkit
pywhatkit.sendwhatmsg("+916375651525","m1",2,49)'''                         #watsapp open 



import random

print("===== ROCK PAPER SCISSORS GAME =====")

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0
rounds = 5

for round_num in range(1, rounds + 1):
            
    print(f"\n----- Round {round_num} -----")
 
    user = input("Enter rock, paper, or scissors: ").lower()                        #rock papaer scissor

    while user not in choices:
        print("Invalid choice!")
        user = input("Please enter rock, paper, or scissors: ").lower()

    computer = random.choice(choices)

    print("Computer chose:", computer)

    # Winning conditions
    if user == computer:
        print("It's a tie!")
        user_score+=1
        computer_score+=1


    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        print("You win this round!")
        user_score += 1

    else:
        print("Computer wins this round!")
        computer_score += 1

    # Display scores after every round
    print("\nCurrent Score:")
    print("User:", user_score)
    print("Computer:", computer_score)

# Final Result
print("\n===== FINAL RESULT =====")
print("Your Score:", user_score)
print("Computer Score:", computer_score)

if user_score > computer_score:
    print("🎉 Congratulations! You won the game!")

elif computer_score > user_score:
    print("💻 Computer won the game!")

else:
    print("🤝 The game is a tie!")






