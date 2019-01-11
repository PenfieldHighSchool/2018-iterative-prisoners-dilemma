team_name = 'Maddy2'
strategy_name = "whatever this is"
strategy_description = '''\
Win. '''
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    if my_history == 0 :  # It's the first round; betray.
        return 'b'
    elif len(my_history)%5 ==0: #Every fifth round betray. 
        return 'b'
    elif my_history[-1]=='b' and their_history[-1]=='b': #if they do the same as you the last round; do the same.
        return 'b'
    elif my_history[-1]== 'c' and their_history[-1]=='c': 
        return 'c'
    elif my_history[-1]=='c' and their_history[-1]== 'b': #If they betray when you collude; betray.
        return 'b' 
    else:
        return 'b' #All else fails; betray.