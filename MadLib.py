#MadLib.py
#Name:
#Date:
#Assignment:

def main():
  print("Madlib")
  #Ask user for words
noun1 = input("Enter a noun: ")
noun2 = input("Enter a noun: ")
noun3 = input("Enter a noun: ")
place1 = input("Enter a place: ")
place2 = input("Enter a place: ")
place3 = input("Enter a place: ")
place4 = input("Enter a place: ")
adjective1 = input("Enter a adjective: ")
adjective2 = input("Enter a adjective ")
adjective3 = input("Enter a adjective: ")
verb1 = input("Enter a verb: ")
  #Print the story with the user supplied words.
print("Once upon a time there was a " + adjective1 + " " + noun1 + ".")
print("The " + noun1 + " lived in " + place1 + " with a " + adjective2 + " " + noun2 + ".")
print("One day the " + noun1 + " and " + noun2 + " were bored and decided to go on an adventure.")
print("There were many different places they wanted to go, like " + place2 + " and " + place3 + ", but ultimately "
+ "they decided to go to " + place4 + ".")
print("Throughout their journey they encountered many trials like having to " + verb1 + " through a forest and battle a "
+ adjective3 + " " + noun3 + ", but in the end they were able to overcome each of these obstacles by working together.")
print("After many days of travel the " + noun1 + " and " + noun2 + " made it to " + place4 + ".")
print("But after spending some time there they realized they misssed " + place1 + ", so they began the journey back with a new "
+ "found appreciation for their home and their friendship.")
print("The End")
#Call the main function if this is the file being run.
if __name__ == '__main__':
    main()
