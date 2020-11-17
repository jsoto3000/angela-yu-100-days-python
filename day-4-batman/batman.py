#Batman ASCII Art sourced from https://ascii.co.uk/art/batman

print('''
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:::::::::::::::::::::::::::::::::::::::::::::-'    `-::::::::::::::::::
::::::::::::::::::::::::::::::::::::::::::-'          `::::::::::::::::
:::::::::::::::::::::::::::::::::::::::-  '   /(_M_)\  `:::::::::::::::
:::::::::::::::::::::::::::::::::::-'        |       |  :::::::::::::::
::::::::::::::::::::::::::::::::-         .   \/~V~\/  ,:::::::::::::::
::::::::::::::::::::::::::::-'             .          ,::::::::::::::::
:::::::::::::::::::::::::-'                 `-.    .-::::::::::::::::::
:::::::::::::::::::::-'                  _,,-::::::::::::::::::::::::::
::::::::::::::::::-'                _,--:::::::::::::::::::::::::::::::
::::::::::::::-'               _.--::::::::::::::::::::::#####:::::::::
:::::::::::-'             _.--:::::::::::::::::::::::::::#####:::::####
::::::::'    ##     ###.-::::::###:::::::::::::::::::::::#####:::::####
::::-'       ###_.::######:::::###::::::::::::::#####:##########:::####
:'         .:###::########:::::###::::::::::::::#####:##########:::####
     ...--:::###::########:::::###:::::######:::#####:##########:::####
 _.--:::##:::###:#########:::::###:::::######:::#####:#################
'#########:::###:#########::#########::######:::#####:#################
:#########:::#############::#########::######:::#######################
##########:::########################::################################
##########:::##########################################################
##########:::##########################################################
#######################################################################
#######################################################################
#######################################################################
#######################################################################
''')
print("Welcome to Gotham City.")
print("Your mission is to find the Batcave, \nand ask Batman for help to save the city from the Legion of Doom.")
choice1 = input('You\'re at a cross road. Where do you want to go? \nType "left" or "right" \n').lower()
if choice1 == "left":
    choice2 = input('You\'ve come to the mouth of a cave. The mouth has a stream of moving water. \nType "wait" to wait for help. Type "enter" to walk into the cave. \n').lower()
    if choice2 == "enter":
        choice3 = input("You enter the Batcave unharmed. \nThere is a Bat Computer with 3 buttons. \nOne red, one yellow and one blue. \nWhich color button do you press? \n").lower()
        if choice3 == "red":
            print("You have pressed the auto-destruct button. \nThe Batcave explodes in a ball of fire, taking you with it. \nGame Over.")
        elif choice3 == "yellow":
            print('''
            \nYou found the alert button! Batman comes to your rescue. \nYou Win!\n
                                          .      .
                                 ./       |      |        \.
                               .:(        |i __ j|        ):`.
                             .'   `._     |`::::'|     _.'    `.
                           .'        "---.j `::' f.---"         `.
                     _____/     ___  ______      __    __   ___   \_   __
                    |      \   |   ||      |`__'|  \  /  | |   | |" \ |  |
                    |  .-.  | .'   `|_    _|\--/|   \/   |.'   `.|   \|  |
                    |  |_|  | |  i  | |  |  :"":|        ||  i  ||    |  |
                    |       / | .^. | |  |  ::::|        || .^. ||       |
                    |  .-.  \ | | | | |  |   :: |        || | | ||  |\   |
                    |  | |  |.' """ `.|  |      |  i  i  j' """ `.  | \  |
                    |  `-'  ||   _   ||  |      |  |\/|  |   _   |  | [  |
                   [|      / |  | |  ||  |      |  |  |  |  | |  |  | |  |].
                  ] `-----'  :--' `--::--'      `--' ::--"--::`--"--' `--':[
                  |      __  ::-"""`.:' "--.    .----::.----:: ,.---._    :|
                  [  .-""  "`'              \  /      "      `'       `-. :].
                 ]:.'                        \/                          `.:[
                 |/                                                        \|
            ''')
        elif choice3 == "blue":
            print("You called for Alfred Pennyworth the Butler. \nMistaking you for a criminal, he judiciously beats you to fatal pulp. \nGame Over.")
        else:
            print("Your poor choice has led to deadly consequences. \nThe Legion of Doom eliminates you before you can reach Batman. \nGame Over.")
    else:
        print("Joe Chill has come to finish the job and eliminate all witnesses to his crime. \nMistaking you for young Bruce Wayne he shoots you dead. \nGame Over.")
else:
  print("You fell into a dark hole full of bats. \nUnlike Batman, you break your neck and die. \nGame Over.")
