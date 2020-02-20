####
# Each team's file must define four tokens:
#     team_name: a string
#     strategy_name: a string
#     strategy_description: a string
#     move: A function that returns 'c' or 'b'
####

team_name = 'E1'
strategy_name = 'Betray'
strategy_description = 'Always betray.'
    
def move_2(my_history, their_history, my_score, their_score):
  if my_history !=40:
    return 'b'
  if my_history >=40
    if 'b' in their_history:
      if their_history[-1]=='b':
        return 'b'
      else:
        return 'c'