import hashlib

thePuzzle   = "0000000000000000000ffdd712a852e0d4234e6a"

puzzleID = "zoudji younes"

# Our acctual counter =  1102293691
puzzleX = 0 # from the first time x=0

# creating an object to hash with SHA-1
hashSHA1 = hashlib.sha1()
while 1:
    # concatinating the name with the x
    puzzleID_X = puzzleID + str(puzzleX)
    
    #hashing the "puzzleID_x" our string
    hashSHA1.update(puzzleID_X.encode('utf-8'))
    
    # taking the hash from hashSHA1 (string format)
    guessPuzzle = format(hashSHA1.hexdigest())
    
    #printing the hash
    print (guessPuzzle)
    
    # check if the guessPuzzle ≤ thePuzzle
    if (guessPuzzle <= thePuzzle):
        break;
    # Incrementing the counter or the key in our situation are the same
    puzzleX += 1;
    
    # Isolation between the next itreation
    # and showing the number of the next iteration
    print("___________________________________________\nIteration = ",puzzleX) 
    
# If the job is done it will show us all the data that made the hash
print("###################### Rresult found ######################")
print("puzzleID     :", puzzleID)
print("the key X    :", puzzleX)
print("Iteration(s) =", puzzleX)
print ("thePuzzle   =",thePuzzle)
print ("guessPuzzle =", guessPuzzle)
