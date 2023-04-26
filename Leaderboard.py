#Global Variables
leaderboardFile = "Catch_A_Leader.txt"

def getNames():
    names = []
    lb = open(leaderboardFile, "r") 

    for line in lb:
        player_name = ""
        index = 0
        while (line[index] != ","):
            player_name += line[index]
            index += 1
    
        names.append(player_name)

    lb.close()
    return names
    

def getScores():
  lb = open(leaderboardFile, "r")
 
  scores = []
  for line in lb:
    player_score = ""    
    index = 0
    while (line[index] != ","):
        index += 1
    index += 1    
    while(line[index] != "\n"):
      player_score += (line[index])
      index+=1
 
    scores.append(int(player_score))

  lb.close()
 
  return scores


def updateLeaderboard(player_score):
    lb_names = getNames()
    lb_scores = getScores()

    if len(lb_scores) < 7 or player_score > lb_scores[6]:

        #TODO have turtle print name thingy
        
        playername = input("What is your name")

     
    index = 0
    # TODO 8: loop through all the scores in the existing leaderboard list
    
    for s in range(len(lb_scores)):
        # TODO 9: check if this is the position to insert new score at
        if (lb_scores[index] < player_score):
            break
        else:
            index += 1
    
    
    # TODO 10: insert new player and score
    lb_names.insert(index, playername)
    lb_scores.insert(index, player_score)
    
    # TODO 11: keep both lists at 5 elements only (top 5 players)
    if (len(lb_scores) > 5):
        lb_names.pop()
        lb_scores.pop()
    
    
    # TODO 12: store the latest leaderboard back in the file
    
    leaderboard_file = open(leaderboardFile, "w")  # this mode opens the file and erases its contents for a fresh start
    
    # TODO 13 loop through all the leaderboard elements and write them to the the file
    index = 0
    for index in range(5):
        leaderboard_file.write(lb_names[index] + "," + str(lb_scores[index]) + "\n")
    
    leaderboard_file.close()
