def funny_or_not(num_of_strings):
    string = raw_input()
    length = len(string)
    for x in range(1,length): 
        temp = abs(ord(string[x]) - ord(string[x - 1]))
        if temp == abs(ord(string[length - x]) - ord(string[length - (x + 1)])):
            continue
        else:
            return False
    return True

num_of_strings = int(raw_input())
    for x in range(int(num_of_strings)):
    result = funny_or_not(num_of_strings)
    if result == True:
        print "Funny"
    else:
        print "Not Funny"