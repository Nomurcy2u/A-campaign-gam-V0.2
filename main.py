import functions,ships,random, os, platform
#SHIP CAMPAGIN?
#War? Pacific?
#WW2 Era? maybe not.
#Minigame?
#Base gameloop exists
#I lowkey wanted to add a story but whatev.
start = functions.gameStart() 

if start == False:
  functions.clear_console()
  print("Closing.")

flagshipDict = functions.shipChoice()
flagshipDict = functions.weaponChoice(flagshipDict)
eflagshipDict = functions.levelChoice()
#Customizes the ship 
end = functions.gameLoop(flagshipDict,eflagshipDict) 

  
