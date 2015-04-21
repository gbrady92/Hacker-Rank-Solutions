def anagram(string1,string2):
    if string1 == string2:
        return False
    string1_dict = {}

    for c in string1:
        if c in string1_dict:
            string1_dict[c] += 1
        else:
            string1_dict[c] = 1
    for c in string2:
        if c in string1_dict:
            string1_dict[c] -= 1
        else:
            return False

    if len(set(string1_dict.values())) > 1:
        return False
    else:
        return True

string1 = raw_input("Please Enter String 1: ")
string2 = raw_input("Please Enter String 2: ")
result =  anagram(string1.lower(), string2.lower())
if result == True:
    print "True"
else:
    print "False"

