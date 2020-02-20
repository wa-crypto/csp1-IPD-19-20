####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'E0'
strategy_name = 'Collude'
strategy_description = 'Always collude.'
    
def move_1(my_history, their_history, my_score, their_score):
  #Collude all the time till the 20th round
  if len(their_history)!=20:
    return c
  # If the betrayed in first 20 rounds, betray them
  if len(their_history)==20:
    if 'b' in their_history:
      return 'b'
      #After turn 20, check eery move and either retaliate or keep colluding.
      if len(their_history)>20:
        if their_history[-1]=='b':
          return 'b'
        else:
          return 'c'
    #If the opponent doesnt betray in first 20 turns collude until turn 100 then move depending on the opponents previous move.
    else:
      return 'c'
      if my_history==100:
        if their_history[-1]=='b':
          return 'b'
        else:
          return 'c'