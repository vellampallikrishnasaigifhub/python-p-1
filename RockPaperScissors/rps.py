import random

def play():
    user=input("What Your choice'r' for rock,'p' for paper,'s' for scissors\n")
    computer= random.choice(['r','p','s'])

    if user==computer:
        return 'It\'s a tie'
    
    elif is_win(user,computer):
        return 'You Win'
    else:
        return 'You Lost' 
def is_win(player, opponent):
    if(player =='r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
print(play())