####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'Food'
strategy_name = 'Fight with food'
strategy_description = '''\
Improvise haha'''
    
def move(my_history, their_history, my_score, their_score):
    '''Make my move based on the history with this player.
    
    history: a string with one letter (c or b) per round that has been played with this opponent.
    their_history: a string of the same length as history, possibly empty. 
    The first round between these two players is my_history[0] and their_history[0]
    The most recent round is my_history[-1] and their_history[-1]
    
    Returns 'c' or 'b' for collude or betray.
    '''
    if len(my_history)==0: # It's the first round; betray.
        return 'b'
    else:
        # If there was a previous round just like the last one,
        # do whatever they did in the round that followed it
        
        # Reference last round
        recent_round_them = their_history[-1]
        recent_round_me = my_history[-1]
                    
        # Look at rounds before that one
        for round in range(len(my_history)-1):
            prior_round_them = their_history[round]
            prior_round_me = my_history[round]
            # If one matches
            if (prior_round_me == recent_round_me) and \
                    (prior_round_them == recent_round_them):
                return 'b'
            elif my_history[-1]=='c' and their_history[-1]=='b':
                return 'b' # Betray if they were severely punished last time,
            elif my_history[-1]=='b' and their_history[-1]=='c':
                return 'b'
            else:
                return 'b' # otherwise collude.