import hashlib

thePuzzle   = "0000000000000000000000000000000000ddbaa6ca2498ef38a88a58ad48cdb4"

puzzleID = "zoudji younes"

# Our acctual counter = 0
puzzleX = 1001793136 # from the first time x=0

# creating an object to hash with SHA-256
hashSHA256 = hashlib.sha256()
while 1:
    # concatinating the name with the x
    puzzleID_X = puzzleID + str(puzzleX)
    
    # hashing the "puzzleID_x" our string
    hashSHA256.update(puzzleID_X.encode('utf-8'))
    
    # taking the hash from hashSHA256 (string format)
    guessPuzzle = format(hashSHA256.hexdigest())
    
    # printing the hash
    print (guessPuzzle)
    
    # check if the guessPuzzle ≤ thePuzzle
    if (guessPuzzle <= thePuzzle):
        break;
    # Incrementing the counter or the key in our situation are the same
    puzzleX += 1;
    
    # Isolation between the next itreation
    # and showing the number of the next iteration
    print("_________________________________________________________________\nIteration = ",puzzleX)
    
# If the job is done it will show us all the data that made the hash
print("###################### Rresult found ######################")
print("puzzleID     :", puzzleID)
print("the key X    :", puzzleX)
print("Iteration(s) =", puzzleX)
print ("thePuzzle   =",thePuzzle)
print ("guessPuzzle =", guessPuzzle)
