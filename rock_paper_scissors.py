import random;
player = raw_input("Enter your choice(rock/paper/scissor)")
player = player.lower();
while(player != "rock" and player != "paper" and player != "scissor"):
    print player
    player = input("hey ? cheater thats not a valid input -_-")
    player = player.lower();
computerInt = random.randint(0,2);
if(computerInt == 0):
    computer = "rock";
elif(computerInt == 1):
    computer = "paper";
elif(computerInt == 2):
    computer = "scissors";
else:
    computer = " thats not a valid input";
if(player == computer):
    print("draw !!");
elif(player == "rock"):
    if(computer == "paper"):
        print('computer wins :/');
    else:
        print("you win !! :)");
elif(player == "paper"):
    if(computer =="rock"):
     print ("you win :");
    else:
        print("computer wins");
elif(player == "scissors"):
    if(computer == "rock"):
     print("computer wins!!");
    else:
        print("you win");
print("your choice: " + player + "\nComputer choice "+ computer )
raw_input("enter any key to exit.")

