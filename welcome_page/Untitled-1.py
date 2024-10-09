def printMaxActivities(s, f):
    n = len(f)
    print("Following activities are selected")

    # The first activity is always selected
    i = 0 
    print(i, end=' ')

    # Consider rest of the activities
    for j in range(1, n): # Since the first activity is at index 0, the rest of the activities from index i to n are being
        #iterated

    # If this activity has start time greater than
    # or equal to the finish time of previously
    # selected activity, then select it
        if s[j] >= f[i]: # condition for the selection 
            print(j, end=' ')
            i = j #print and extract that activity
# Driver code
if __name__ == '__main__':
    s = [1, 3, 0, 5, 8, 5]
    f = [2, 4, 6, 7, 9, 9]

    

# Function call
printMaxActivities(s, f) # Selecting the max number of activities based on the startime >= finish time