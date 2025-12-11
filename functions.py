#Not mine
import random, os, platform
def clear_console():
    #Clears the console screen.
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear') 

#Mine
import ships
def gameStart():
  while True:
    startChoice = input("Do you want to start the game?: Y/N").lower()
    if startChoice == "y" or startChoice == "yes":
      print("Loading.")
      return True
    elif startChoice == "n" or startChoice == "no":
      print("Returning")
      return False
    else: print("Please input either 'Y' or 'N'")

def pause(): input("[Press enter to continue]:")

def shipChoice():
  clear_console()
  print("Ships to choose from: ")
  shipDict = ["=-=-=-=-=-=","1: Carrier","2: Battleship",
  "3: Crusier","4: Destroyer","5: Submarine","=-=-=-=-=-="]
  for i in range(len(shipDict)): print shipDict[i]
  while True:
    flagship = input("Please pick a flagship: ").lower()
    if flagship=="carrier" or flagship=="1": 
      flagshipDict = ships.carrier
      break
    elif flagship=="battleship" or flagship=="2": 
      flagshipDict = ships.battleship
      break
    elif flagship=="cruiser" or flagship=="3": 
      flagshipDict = ships.cruiser
      break
    elif flagship=="destroyer" or flagship=="4": 
      flagshipDict = ships.destroyer
      break
    elif flagship=="submarine" or flagship=="5": 
      flagshipDict = ships.submarine
      break
    else: print("Please input the name or number of the ship type. ")
  print("You pick "+flagshipDict["name"]+" as your flagship. ")
  pause()
  clear_console()
  return flagshipDict

def weaponChoice(flagshipDict): 
  def carrierWeaponChoice(flagshipDict):
    weaponList = ["=-=-=-=-=-=","1: Dive Bomber","2: Torpedo Bomber","=-=-=-=-=-="]
    for i in range(len(weaponList)): print(weaponList[i])
    while True:
      PweaponChoice = input("Please pick a plane type to use: ").lower()
      if PweaponChoice=="1" or PweaponChoice=="dive" or PweaponChoice=="dive bomber":
        Pweapon = flagshipDict["Pweapon"]["diveBomber"]
        break
      elif PweaponChoice=="2" or PweaponChoice=="torpedo" or PweaponChoice=="torpedo bomber":
        Pweapon = flagshipDict["Pweapon"]["torpedoBomber"]
        break
      else: print("Please input the name or number of the weapon type. ")
    return Pweapon
  def battleshipWeaponChoice(flagshipDict):
    weaponList = ["=-=-=-=-=-=","1: 20in cannon","2: 18in cannon","3: 14in cannon","=-=-=-=-=-="]
    for i in range(len(weaponList)): print(weaponList[i])
    while True:
      PweaponChoice = input("Please pick a main gun type to use: ").lower()
      if PweaponChoice=="1" or PweaponChoice=="20" or PweaponChoice=="20in cannon":
        Pweapon = flagshipDict["Pweapon"]["cannon20in"]
        break
      elif PweaponChoice=="2" or PweaponChoice=="18" or PweaponChoice=="18in cannon":
        Pweapon = flagshipDict["Pweapon"]["cannon18in"]
        break
      elif PweaponChoice=="3" or PweaponChoice=="14" or PweaponChoice=="14in cannon":
        Pweapon = flagshipDict["Pweapon"]["cannon14in"]
        break
      else: print("Please input the name or number of the weapon type. ")
    return Pweapon
  def cruiserWeaponChoice(flagshipDict):
    weaponList = ["=-=-=-=-=-=","1: 14in cannon","2: 12in cannon","3: 10in cannon","=-=-=-=-=-="]
    for i in range(len(weaponList)): print(weaponList[i])
    while True:
      PweaponChoice = input("Please pick a main gun type to use: ").lower()
      if PweaponChoice=="1" or PweaponChoice=="14" or PweaponChoice=="14in cannon":
        Pweapon = flagshipDict["Pweapon"]["cannon14in"]
        break
      elif PweaponChoice=="2" or PweaponChoice=="12" or PweaponChoice=="12in cannon":
        Pweapon = flagshipDict["Pweapon"]["cannon12in"]
        break
      elif PweaponChoice=="3" or PweaponChoice=="10" or PweaponChoice=="10in cannon":
        Pweapon = flagshipDict["Pweapon"]["cannon10in"]
        break
      else: print("Please input the name or number of the weapon type. ")
    return Pweapon
  def destroyerWeaponChoice(flagshipDict):
    weaponList = ["=-=-=-=-=-=","1: 10in cannon","2: Torpedos","=-=-=-=-=-="]
    for i in range(len(weaponList)): print(weaponList[i])
    while True:
      PweaponChoice = input("Please pick a main weapon type to use: ").lower()
      if PweaponChoice=="1" or PweaponChoice=="10" or PweaponChoice=="10in cannon":
        Pweapon = flagshipDict["Pweapon"]["cannon10in"]
        break
      elif PweaponChoice=="2" or PweaponChoice=="torpedo" or PweaponChoice=="torpedos":
        Pweapon = flagshipDict["Pweapon"]["torpedo"]
        break
      else: print("Please input the name or number of the weapon type. ")
    return Pweapon
  def submarineWeaponChoice(flagshipDict):
    weaponList = ["=-=-=-=-=-=","1: Torpedos","=-=-=-=-=-="]
    for i in range(len(weaponList)): print(weaponList[i])
    print("Submarines only get torpedos as their primary. ")
    pause()
    Pweapon = flagshipDict["Pweapon"]["torpedo"]
    return Pweapon
  def secondaryWeaponChoice(flagshipDict):
    clear_console()
    print("Secondary weapons to choose from: ")
    weaponList = ["=-=-=-=-=-=","1: 8in cannon","2: 6in cannon","=-=-=-=-=-="]
    for i in range(len(weaponList)): print(weaponList[i])
    while True:
      SweaponChoice = input("Please pick a secondary type to use: ").lower()
      if SweaponChoice=="1" or SweaponChoice=="8" or SweaponChoice=="8in cannon":
        Sweapon = flagshipDict["Sweapon"]["cannon8in"]
        break
      elif SweaponChoice=="2" or SweaponChoice=="6" or SweaponChoice=="6in cannon":
        Sweapon = flagshipDict["Sweapon"]["cannon6in"]
        break
      else: print("Please input the name or number of the weapon type. ")
    return Sweapon
  def AAWeaponChoice(flagshipDict):
    clear_console()
    print("Anti-Air weapons to choose from: ")
    weaponList = ["=-=-=-=-=-=","1: Heavy Flak","2: Medium Flak","3: Light Flak","=-=-=-=-=-="]
    for i in range(len(weaponList)): print(weaponList[i])
    while True:
      AAweaponChoice = input("Please pick a Anti-Air type to use: ").lower()
      if AAweaponChoice=="1" or AAweaponChoice=="heavy" or AAweaponChoice=="heavy flak":
        AAweapon = flagshipDict["AAweapon"]["heavyFlak"]
        break
      elif AAweaponChoice=="2" or AAweaponChoice=="medium" or AAweaponChoice=="medium flak":
        AAweapon = flagshipDict["AAweapon"]["mediumFlak"]
        break
      elif AAweaponChoice=="3" or AAweaponChoice=="light" or AAweaponChoice=="light flak":
        AAweapon = flagshipDict["AAweapon"]["lightFlak"]
        break
      else: print("Please input the name or number of the weapon type. ")
    return AAweapon
  clear_console()
  print(flagshipDict["name"]+" weapons to choose from: ")
  if flagshipDict["name"]=="Carrier": flagshipDict["Pweapon"] = carrierWeaponChoice(flagshipDict)
  elif flagshipDict["name"]=="Battleship": flagshipDict["Pweapon"] = battleshipWeaponChoice(flagshipDict)
  elif flagshipDict["name"]=="Cruiser": flagshipDict["Pweapon"] = cruiserWeaponChoice(flagshipDict)
  elif flagshipDict["name"]=="Destroyer": flagshipDict["Pweapon"] = destroyerWeaponChoice(flagshipDict) #FIXME
  elif flagshipDict["name"]=="Submarine": flagshipDict["Pweapon"] = submarineWeaponChoice(flagshipDict)
  print("You pick "+flagshipDict["Pweapon"]["weaponName"]+" as your primary weapon. ")
  pause()
  flagshipDict["Sweapon"] = secondaryWeaponChoice(flagshipDict)
  print("You pick "+flagshipDict["Sweapon"]["weaponName"]+" as your secondary weapon. ")
  pause()
  flagshipDict["AAweapon"] = AAWeaponChoice(flagshipDict)
  print("You pick "+flagshipDict["AAweapon"]["weaponName"]+" as your anti-air weapon. ")
  pause()
  clear_console()
  return flagshipDict

def levelChoice(): 
  while True: 
    clear_console() 
    choiceList = ("Levels to choose from: ","=-=-=-=-=-=","0: Tutorial",
    "1: Randomizer","2: Battleship","3: Submarine","4: Carrier","=-=-=-=-=-=")
    for i in range(len(choiceList)): print(choiceList[i])
    #Choice
    choice = input("What level does the Admiral want to pick?: ").lower()
    if choice=="tutorial" or choice=="0": 
      eflagshipDict = ships.testTarget
      break
    elif choice=="randomizer" or choice=="1": 
      eflagshipDict = eflagshipChoice(0)
      break
    elif choice=="battleship" or choice=="2": 
      eflagshipDict = eflagshipChoice(2)
      break
    elif choice=="submarine" or choice=="3": 
      eflagshipDict = eflagshipChoice(5)
      break
    elif choice=="carrier" or choice=="4": 
      eflagshipDict = eflagshipChoice(1)
      break
    else: print("Please input either the name or number of the level. ")
    pause()
  eflagshipDict = eweaponChoice(eflagshipDict)
  return eflagshipDict 

def winCondition(flagshipDict,eflagshipDict):
  clear_console()
  if flagshipDict["health"] > 0 and eflagshipDict["health"] > 0: winCondition = 0
  else: 
    if flagshipDict["health"] <= 0 and eflagshipDict["health"] <= 0:
      print("You both sink. |Tie| ") #FIXME
      winCondition = 2
    elif eflagshipDict["health"] <= 0:
      print("The enemy ship sinks. |Win| ")
      winCondition = 1
    elif flagshipDict["health"] <= 0: 
      print("You sink. |Lose| ")
      winCondition = 2
  return winCondition 

def gameLoop(flagshipDict,eflagshipDict):
  while True:
    flagshipDict,eflagshipDict = playerChoice(flagshipDict,eflagshipDict) 
    flagshipDict,eflagshipDict = enemyChoice(flagshipDict,eflagshipDict)
    pause()
    end = winCondition(flagshipDict,eflagshipDict)
    if end != 0: break
  return end

#Actual Gameplay!!
def playerChoice(flagshipDict,eflagshipDict):
  while True: 
    clear_console() 
    def attack(flagshipDict,eflagshipDict):
      def primaryAttack(flagshipDict):
        Pdamage=flagshipDict["Pweapon"]["weaponDamage"]*flagshipDict["Pweapon"]["attackAmount"]
        totalDamage = 0
        for i in range(flagshipDict["PweaponNumber"]):
          aim = random.randint(0,100)
          if aim <= flagshipDict["Pweapon"]["accuracy"]:
            totalDamage += Pdamage
        return totalDamage
      def secondaryAttack(flagshipDict):
        Sdamage=flagshipDict["Sweapon"]["weaponDamage"]*flagshipDict["Sweapon"]["attackAmount"]
        totalDamage = 0
        for i in range(flagshipDict["SweaponNumber"]):
          aim = random.randint(0,100)
          if aim <= flagshipDict["Sweapon"]["accuracy"]:
            totalDamage += Sdamage
        return totalDamage
      def AAdefense(Pdamage,flagshipDict,eflagshipDict):
        if flagshipDict["Pweapon"]["attackAmount"] == 0:
          if flagshipDict["PweaponNumber"] == 0: print("There are no more "+flagshipDict["Pweapon"]["weaponName"]+" on the ship")
          else: 
            flagshipDict["Pweapon"]["attackAmount"] = 2
            flagshipDict["PweaponNumber"] -= 1
            print("Bringing out 2 reserve "+flagshipDict["Pweapon"]["weaponName"])
            return Pdamage,flagshipDict,eflagshipDict
        if Pdamage == 0: return Pdamage,flagshipDict,eflagshipDict
        else: 
          AAdamage=eflagshipDict["AAweapon"]["weaponDamage"]*eflagshipDict["AAweapon"]["attackAmount"]
          totalAADamage = 0
          for i in range(eflagshipDict["AAweaponNumber"]):
            aim = random.randint(0,100)
            if aim <= eflagshipDict["AAweapon"]["accuracy"]:
              totalAADamage += AAdamage
        if totalAADamage > 0: 
          print(totalAADamage,flagshipDict["Pweapon"]["attackAmount"]) #FIXME
          for i in range(flagshipDict["Pweapon"]["attackAmount"]):
            if totalAADamage > 0:
              oweaponHealth = flagshipDict["Pweapon"]["weaponHealth"]
              flagshipDict["Pweapon"]["weaponHealth"] = flagshipDict["Pweapon"]["weaponHealth"] - totalAADamage
              totalAADamage -= oweaponHealth
              if flagshipDict["Pweapon"]["weaponHealth"] <= 0:
                flagshipDict["Pweapon"]["attackAmount"] -= 1
                print("The enemy AA defense destroys one of your "+flagshipDict["Pweapon"]["weaponName"])
              flagshipDict["Pweapon"]["weaponHealth"] = oweaponHealth
            else: 
              print(totalAADamage,flagshipDict["Pweapon"]["attackAmount"]) #FIXME
              return Pdamage,flagshipDict,eflagshipDict
        print(totalAADamage,flagshipDict["Pweapon"]["attackAmount"]) #FIXME
        return Pdamage,flagshipDict,eflagshipDict
      
      ehealth = eflagshipDict["health"]
      Pdamage = 0 #FIXME (EVERYTHING IS BROKENNNNNNN)
      Pdamage,flagshipDict,eflagshipDict = AAdefense(Pdamage,flagshipDict,eflagshipDict)
      if flagshipDict["Pweapon"]["loaded"] == True:
        Pdamage = primaryAttack(flagshipDict)
        if flagshipDict["name"] =="Carrier":
          Pdamage,flagshipDict,eflagshipDict = AAdefense(Pdamage,flagshipDict,eflagshipDict)
          if Pdamage > 0: print("You launch a flight of "+flagshipDict["Pweapon"]["weaponName"]+" dealing "+str(Pdamage)+" damage to the enemy ship. ")
          elif Pdamage==0:print("You launch a flight of "+flagshipDict["Pweapon"]["weaponName"]+" but they all miss. ")
        else: 
          if Pdamage > 0: print("You launch a salvo from the "+flagshipDict["Pweapon"]["weaponName"]+" dealing "+str(Pdamage)+" damage to the enemy ship. ")
          elif Pdamage==0:print("You launch a salvo from the "+flagshipDict["Pweapon"]["weaponName"]+" but they all miss. ")
        ehealth -= Pdamage
      elif flagshipDict["Pweapon"]["loaded"] == False: 
        if flagshipDict["name"] =="Carrier": print(flagshipDict["Pweapon"]["weaponName"]+" is not armed")
        else: print(flagshipDict["Pweapon"]["weaponName"]+" is not loaded")
      flagshipDict["Pweapon"]["loaded"] = False
      #Secondary
      if flagshipDict["Sweapon"]["loaded"] == True:
        Sdamage = secondaryAttack(flagshipDict)
        if Sdamage > 0: print("You also fire a salvo from your secondary "+flagshipDict["Sweapon"]["weaponName"]+" batteries dealing "+str(Sdamage)+" damage to the enemy ship. ")
        elif Sdamage==0: print("You also fire a salvo from your secondary "+flagshipDict["Sweapon"]["weaponName"]+" batteries but all shots miss. ")
        ehealth -= Sdamage
      elif flagshipDict["Sweapon"]["loaded"] == False: print(flagshipDict["Sweapon"]["weaponName"]+" is not loaded!")
      flagshipDict["Sweapon"]["loaded"] = False
      #Accuracy increase per shot
      if flagshipDict["Pweapon"]["accuracy"] < 80: flagshipDict["Pweapon"]["accuracy"] += 5
      if flagshipDict["Sweapon"]["accuracy"] < 80: flagshipDict["Sweapon"]["accuracy"] += 5
      eflagshipDict["health"] = ehealth
      return flagshipDict,eflagshipDict
    
    def loading(flagshipDict):
      if flagshipDict["Pweapon"]["loaded"] == False: print(flagshipDict["Pweapon"]["weaponName"]+" rearmed and reloaded!")
      elif flagshipDict["Pweapon"]["loaded"] == True: print(flagshipDict["Pweapon"]["weaponName"]+" is already armed and loaded!")
      if flagshipDict["Sweapon"]["loaded"] == False: print(flagshipDict["Sweapon"]["weaponName"]+" reloaded!")
      elif flagshipDict["Sweapon"]["loaded"] == True: print(flagshipDict["Sweapon"]["weaponName"]+" is already loaded!")
      flagshipDict["Pweapon"]["loaded"] = flagshipDict["Sweapon"]["loaded"] = True
      return flagshipDict
    
    def evasion(flagshipDict,eflagshipDict):
      if flagshipDict["size"] == "large":
        eflagshipDict["Pweapon"]["accuracy"] -= 10
        eflagshipDict["Sweapon"]["accuracy"] -= 10
      elif flagshipDict["size"] == "medium":
        eflagshipDict["Pweapon"]["accuracy"] -= 15
        eflagshipDict["Sweapon"]["accuracy"] -= 15
      elif flagshipDict["size"] == "small":
        eflagshipDict["Pweapon"]["accuracy"] -= 20
        eflagshipDict["Sweapon"]["accuracy"] -= 20
      
      if eflagshipDict["Pweapon"]["accuracy"] < 10: eflagshipDict["Pweapon"]["accuracy"] = 10
      if eflagshipDict["Sweapon"]["accuracy"] < 10: eflagshipDict["Sweapon"]["accuracy"] = 10
      print("You preform evasive maneuvers reducing enemy accuracy. ")
      return flagshipDict,eflagshipDict
      
    choiceList = ("You are the helm of your "+flagshipDict["name"]+".",
    "You have orders to sink the enemy "+eflagshipDict["name"]+".",
    "=-=-=-=-=-=","1: Attack","2: Reload","3: Evasion","=-=-=-=-=-=")
    for i in range(len(choiceList)): print(choiceList[i])
    
    #Choice
    choice = input("What does the admiral want to do?: ").lower()
    if choice=="attack" or choice=="1": flagshipDict,eflagshipDict = attack(flagshipDict,eflagshipDict)
    elif choice=="reload" or choice=="2": flagshipDict = loading(flagshipDict)
    elif choice=="evasion" or choice=="3": flagshipDict,eflagshipDict = evasion(flagshipDict,eflagshipDict)
    else: print("Please input either the name or number of the choice you want ot make. ")
    pause()
    return flagshipDict,eflagshipDict


#Enemy Functions
def eflagshipChoice(flagshipChoice):
  if flagshipChoice == 0: flagship = random.randint(1,5)
  else: flagship = flagshipChoice
  if flagship=="carrier" or flagship==1: eflagshipDict = ships.ecarrier
  elif flagship=="battleship" or flagship==2: eflagshipDict = ships.ebattleship
  elif flagship=="cruiser" or flagship==3: eflagshipDict = ships.ecruiser
  elif flagship=="destroyer" or flagship==4: eflagshipDict = ships.edestroyer
  elif flagship=="submarine" or flagship==5: eflagshipDict = ships.esubmarine
  return eflagshipDict

def eweaponChoice(eflagshipDict):
  def carrierWeaponChoice(flagshipDict):
    PweaponChoice = random.randint(1,2)
    if PweaponChoice==1: Pweapon = flagshipDict["Pweapon"]["diveBomber"]
    elif PweaponChoice==2: Pweapon = flagshipDict["Pweapon"]["torpedoBomber"]
    return Pweapon
  def battleshipWeaponChoice(flagshipDict):
    PweaponChoice = random.randint(1,3)
    if PweaponChoice==1: Pweapon = flagshipDict["Pweapon"]["cannon20in"]
    elif PweaponChoice==2: Pweapon = flagshipDict["Pweapon"]["cannon18in"]
    elif PweaponChoice==3: Pweapon = flagshipDict["Pweapon"]["cannon14in"]
    return Pweapon
  def cruiserWeaponChoice(flagshipDict):
    PweaponChoice = random.randint(1,3)
    if PweaponChoice==1: Pweapon = flagshipDict["Pweapon"]["cannon14in"]
    elif PweaponChoice==2: Pweapon = flagshipDict["Pweapon"]["cannon12in"]
    elif PweaponChoice==3: Pweapon = flagshipDict["Pweapon"]["cannon10in"]
    return Pweapon
  def destroyerWeaponChoice(flagshipDict):
    PweaponChoice = random.randint(1,2)
    if PweaponChoice==1: Pweapon = flagshipDict["Pweapon"]["cannon10in"]
    elif PweaponChoice==2: Pweapon = flagshipDict["Pweapon"]["torpedo"]
    return Pweapon
  def secondaryWeaponChoice(flagshipDict):
    SweaponChoice = random.randint(1,2)
    if SweaponChoice==1: Sweapon = flagshipDict["Sweapon"]["cannon8in"]
    elif SweaponChoice==2: Sweapon = flagshipDict["Sweapon"]["cannon6in"]
    return Sweapon
  def AAWeaponChoice(flagshipDict):
    AAweaponChoice = random.randint(1,3)
    if AAweaponChoice==1: AAweapon = flagshipDict["AAweapon"]["heavyFlak"]
    elif AAweaponChoice==2: AAweapon = flagshipDict["AAweapon"]["mediumFlak"]
    elif AAweaponChoice==3: AAweapon = flagshipDict["AAweapon"]["lightFlak"]
    return AAweapon
  if eflagshipDict["name"]=="Carrier": eflagshipDict["Pweapon"] = carrierWeaponChoice(eflagshipDict)
  elif eflagshipDict["name"]=="Battleship": eflagshipDict["Pweapon"] = battleshipWeaponChoice(eflagshipDict)
  elif eflagshipDict["name"]=="Cruiser": eflagshipDict["Pweapon"] = cruiserWeaponChoice(eflagshipDict)
  elif eflagshipDict["name"]=="Destroyer": eflagshipDict["Pweapon"] = destroyerWeaponChoice(eflagshipDict) 
  elif eflagshipDict["name"]=="Submarine": eflagshipDict["Pweapon"] = eflagshipDict["Pweapon"]["torpedo"]
  eflagshipDict["Sweapon"] = secondaryWeaponChoice(eflagshipDict)
  eflagshipDict["AAweapon"] = AAWeaponChoice(eflagshipDict)
  return eflagshipDict

#echoice
def enemyChoice(flagshipDict,eflagshipDict):
  def eattack(flagshipDict,eflagshipDict):
    def primaryAttack(eflagshipDict):
      Pdamage=eflagshipDict["Pweapon"]["weaponDamage"]*eflagshipDict["Pweapon"]["attackAmount"]
      totalDamage = 0
      for i in range(eflagshipDict["PweaponNumber"]):
        aim = random.randint(0,100)
        if aim <= eflagshipDict["Pweapon"]["accuracy"]:
          totalDamage += Pdamage
      return totalDamage
    def secondaryAttack(eflagshipDict):
      Sdamage=eflagshipDict["Sweapon"]["weaponDamage"]*eflagshipDict["Sweapon"]["attackAmount"]
      totalDamage = 0
      for i in range(eflagshipDict["SweaponNumber"]):
        aim = random.randint(0,100)
        if aim <= eflagshipDict["Sweapon"]["accuracy"]:
          totalDamage += Sdamage
      return totalDamage
    def AAdefense(Pdamage,flagshipDict,eflagshipDict):
      if eflagshipDict["Pweapon"]["attackAmount"] == 0:
        if eflagshipDict["PweaponNumber"] == 0: print("The enemy "+eflagshipDict["name"]+" has no more "+eflagshipDict["Pweapon"]["weaponName"]+".")
        else: 
          eflagshipDict["Pweapon"]["attackAmount"] = 2
          eflagshipDict["PweaponNumber"] -= 1
          print("The enemy brings out reserve "+eflagshipDict["Pweapon"]["weaponName"])
          return Pdamage,flagshipDict,eflagshipDict
      if Pdamage == 0: return Pdamage,flagshipDict,eflagshipDict
      else: 
        AAdamage=flagshipDict["AAweapon"]["weaponDamage"]*flagshipDict["AAweapon"]["attackAmount"]
        totalAADamage = 0
        for i in range(flagshipDict["AAweaponNumber"]):
          aim = random.randint(0,100)
          if aim <= flagshipDict["AAweapon"]["accuracy"]:
            totalAADamage += AAdamage
      if totalAADamage > 0: 
        print(totalAADamage,eflagshipDict["Pweapon"]["attackAmount"]) #FIXME
        for i in range(eflagshipDict["Pweapon"]["attackAmount"]):
          if totalAADamage > 0:
            oweaponHealth = eflagshipDict["Pweapon"]["weaponHealth"]
            eflagshipDict["Pweapon"]["weaponHealth"] = eflagshipDict["Pweapon"]["weaponHealth"] - totalAADamage
            totalAADamage -= oweaponHealth
            if eflagshipDict["Pweapon"]["weaponHealth"] <= 0:
              eflagshipDict["Pweapon"]["attackAmount"] -= 1
              print("Your AA defense destroys one of the enemy "+eflagshipDict["Pweapon"]["weaponName"])
            eflagshipDict["Pweapon"]["weaponHealth"] = oweaponHealth
          else: 
            print(totalAADamage,flagshipDict["Pweapon"]["attackAmount"]) #FIXME
            return Pdamage,flagshipDict,eflagshipDict
      print(totalAADamage,flagshipDict["Pweapon"]["attackAmount"]) #FIXME
      return Pdamage,flagshipDict,eflagshipDict
    
    health = flagshipDict["health"]
    if eflagshipDict["Pweapon"]["loaded"] == True:
      Pdamage = primaryAttack(eflagshipDict)
      if eflagshipDict["name"] =="Carrier":
        Pdamage,flagshipDict,eflagshipDict = AAdefense(Pdamage,flagshipDict,eflagshipDict)
        if Pdamage > 0: print("The enemy launches a flight of "+eflagshipDict["Pweapon"]["weaponName"]+" dealing "+str(Pdamage)+" damage to your ship. ")
        elif Pdamage==0:print("The enemy launches a flight of "+eflagshipDict["Pweapon"]["weaponName"]+" but they all miss. ")
      else: 
        if Pdamage > 0: print("The enemy fires a salvo from their "+eflagshipDict["Pweapon"]["weaponName"]+" dealing "+str(Pdamage)+" damage to your ship. ")
        elif Pdamage==0:print("The enemy fires a salvo from their "+eflagshipDict["Pweapon"]["weaponName"]+" but they all miss. ")
      health -= Pdamage
    eflagshipDict["Pweapon"]["loaded"] = False
    #Secondary
    if eflagshipDict["Sweapon"]["loaded"] == True:
      Sdamage = secondaryAttack(eflagshipDict)
      if Sdamage > 0: print("The enemy also fires a salvo from their secondary "+eflagshipDict["Sweapon"]["weaponName"]+" batteries dealing "+str(Sdamage)+" damage to your ship. ")
      elif Sdamage==0: print("The enemy also fires a salvo from their secondary "+eflagshipDict["Sweapon"]["weaponName"]+" batteries but all shots miss. ")
      health -= Sdamage
    eflagshipDict["Sweapon"]["loaded"] = False
    #Accuracy increase per shot
    if eflagshipDict["Pweapon"]["accuracy"] < 80: eflagshipDict["Pweapon"]["accuracy"] += 5
    if eflagshipDict["Sweapon"]["accuracy"] < 80: eflagshipDict["Sweapon"]["accuracy"] += 5
    flagshipDict["health"] = health
    return flagshipDict,eflagshipDict
  
  def eloading(eflagshipDict):
    print("The enemy reloads all their "+eflagshipDict["Pweapon"]["weaponName"]+" and "+eflagshipDict["Sweapon"]["weaponName"])
    if eflagshipDict["Pweapon"]["loaded"] == False: eflagshipDict["Pweapon"]["loaded"] = True
    if eflagshipDict["Sweapon"]["loaded"] == False: eflagshipDict["Sweapon"]["loaded"] = True
    return eflagshipDict
  
  def eevasion(flagshipDict,eflagshipDict):
    if eflagshipDict["size"] == "large":
      flagshipDict["Pweapon"]["accuracy"] -= 10
      flagshipDict["Sweapon"]["accuracy"] -= 10
    elif eflagshipDict["size"] == "medium":
      flagshipDict["Pweapon"]["accuracy"] -= 15
      flagshipDict["Sweapon"]["accuracy"] -= 15
    elif eflagshipDict["size"] == "small":
      flagshipDict["Pweapon"]["accuracy"] -= 20
      flagshipDict["Sweapon"]["accuracy"] -= 20
    
    if flagshipDict["Pweapon"]["accuracy"] < 10: flagshipDict["Pweapon"]["accuracy"] = 10
    if flagshipDict["Sweapon"]["accuracy"] < 10: flagshipDict["Sweapon"]["accuracy"] = 10
    print("The enemy preforms evasive maneuvers reducing your accuracy. ")
    return flagshipDict,eflagshipDict
  
  #Choice 
  #FIXME Code intelligent actions into this thing later xd
  clear_console()
  choice = random.randint(1,2)
  if choice==1: 
    if eflagshipDict["Pweapon"]["loaded"] == True: flagshipDict,eflagshipDict = eattack(flagshipDict,eflagshipDict)
    elif eflagshipDict["Pweapon"]["loaded"] == False: eflagshipDict = eloading(eflagshipDict)
  elif choice==2: flagshipDict,eflagshipDict = eevasion(flagshipDict,eflagshipDict)
  return flagshipDict,eflagshipDict
  
#DID I JUST SWITCH SHIPS?!?!?!?!
#No. I AM GOING INSANEENENENENE






















