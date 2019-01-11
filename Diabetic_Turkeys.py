team_name = 'Diabetic Turkeys'
strategy_name = 'Best Strategy'
strategy_description = 'Win while being a nice boi'
'''Collude first round. Collude, except in a round after getting 
a severe punishment. If unwarrented betrayal, collude.'''
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    if len(my_history)==0:
        return 'c'
    elif my_history[-1]=='c' and their_history[-1]=='b':
        return 'b'
    elif my_history[-1]=='b' and their_history[-1]=='b':
       return 'b' 
    elif my_history [-1]=='b' and their_history[-1]=='c':
        return 'c'
    else:
        return 'c'