import os, re, random as rd, time as t
from unicodedata import name

def game(rps, ai_choice):
    while True:
        try:
            print('\n')
            print(rps)
            print('\v')
            t.sleep(3)
            print('Rock, Paper, Scissos - Shoot!')

            # the users choice
            player_choice = str(input('Choose [R, P, S]: ')).upper()
            print('\n')
            t.sleep(2)
            if not re.match("[RrPpSs]", player_choice):
                print('That is not one of the choices')
                print('Please enter letter R, P, or S')
                continue
            print(f'You chose {player_choice}')
            rand_rps = rd.choice(ai_choice)
            t.sleep(2)
            print(f'I chose {rand_rps}')
            
            # decides on who wins
            t.sleep(3)
            if rand_rps == player_choice:
                print('Tie!')
            elif rand_rps == 'R' and player_choice == 'S':
                print('Rock beats scissors, I win!')
            elif rand_rps == 'S' and player_choice == 'P':
                print('Scissors beats paper! I win!')
            elif rand_rps == 'P' and player_choice == 'R':
                print('Paper beats rock, I win!')
            else:
                print('You win!')
            # continue playing?
            keep_playing = str(input('Keep playing? (Y or N): ')).upper()
            if keep_playing == 'Y':
                continue
            else:
                t.sleep(3)
                break
        except ValueError:
            t.sleep(4)
            print('That is not a string (meaning a letter or word')

def main():
    os.system('cls' if os.name=='nt' else 'clear')
    rps = "Choices: \n R for Rock \n P for Paper \n S for Scissor"
    ai_choice = ['R', 'P', 'S']
    game(rps, ai_choice)

if __name__ == "__main__":
    main()
