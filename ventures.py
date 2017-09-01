print("Wanna go on Ventures?")
venture = input("Lets see were you'll end up at?")
if venture == "Yes" :
  print("Where do you wanna go?")
  go = input("Downtown Fresno, School, Hiking, RoadTrip :")
  
  if go == "Downtown Fresno":
      print("Downtown Fresno A ")
      print("Downtown Fresno B ")
      print ("Downtown Fresno C ")
      
      dt = input(">")
      
      if dt == "Downtown Fresno A": 
        print("You've Ventured to SMLK Blvd and Belgravia Ave at 1:45am" )
      elif dt == "Downtown Fresno B": 
        print("Your Venture Begins at 761 Hammond Ave march 12, 2004 Marcus Wessons Home" )
      elif dt == "Downtown Fresno C":
        print("Ventures in Tower District at 10pm on Olive and Echo st")
      else:
        print("No Ventures for you!")
    
  if go == "School":
      print("School A ")
      print("School B ")
      print ("School C ")
      
      sch = input(">")
      
      if sch == "School A": 
        print("You've Ventured to Blath School Massacare in Bath Township, Michigan May 18, 1927" )
      elif sch == "School B": 
        print("You've Ventured to Columbine! in Columbine, Colorado April 20, 1999" )
      elif sch == "School C":
        print("You Ventured into Bitwise South Stadium GeekWise Academy, Fresno Ca")
      else:
        print("No Ventures for you!")
        
  if go == "Hiking":
      print("Hiking A ")
      print("Hiking B ")
      print ("Hiking C ")
      
      hiking = input(">")
      
      if hiking == "Hiking A": 
        print("You ventured Off a Cliff well hiking" )
      elif hiking == "Hiking B": 
        print("Mt Whitney Hiked 22miles in the Kingscanyon National Park" )
      elif hiking == "Hiking C":
        print("Mirror Lake Trail 2miles in Yosemite National Park")
      else:
        print("No Ventures for you!")
        
  if go == "Roadtrip":
      print("Roadtrip A ")
      print("Roadtrip B ")
      print ("Roadtrip C ")
      
      rt = input(">")
      
      if rt == "Roadtrip A": 
        print("You're on a venture roadtrip with The Donner Party in 1846" )
      elif rt == "Roadtrip B": 
        print("Venture roadtrip to Parlier Cat House on the Kings" )
      elif rt == "RoadTrip C":
        print("Venture roadtip with the Hell's Angles in 1962")
      else:
        print("No Ventures for you!")