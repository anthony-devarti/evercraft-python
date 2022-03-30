cpuModel = str.lower(input("Please enter your CPU model: "))
 
# The match statement evaluates the variable's value
# match cpuModel:
# case "celeron": # We test for different values and print different messages
#         print ("Forget about it and play Minesweeper instead...")
# case "core i3":
#         print ("Good luck with that ;)")
# case "core i5":
#         print ("Yeah, you should be fine.")
# case "core i7":
#         print ("Have fun!")
# case "core i9":
#         print ("Our team designed nice loading screens… Too bad you won't see them...")
# case _: # the underscore character is used as a catch-all.
#         print ("Is that even a thing?")

def modify(score):
    switcher={
            1:-5,
            2:-4,
            3:-4,
            4:'Thursday',
            5:'Friday',
            6:'Saturday',
            7: -2
        }
    return switcher.get(score,"Invalid day of week")