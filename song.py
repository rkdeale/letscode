  # Trying to code a program that will write the song "99 bottles of beer on the wall" without using numbers in print function #

def Song():
    drink="bottles"
    for i in range(99, 1, -1):

        if i == 1:
            drink="bottle"
            print(1, drink, "of beer on the wall", "only", 1, drink, "of beer", "if that", 0, drink,
                  'should happen to fall, what a waste of alcohol')
        else:
            drink="bottles"
            print(i, drink, "of beer on the wall", i, drink, "of beer", "Take one down and pass it around", i-1, drink, " of beer on the wall.")

        if i == 0:
            print("No more bottles of beer.")
Song()
      
