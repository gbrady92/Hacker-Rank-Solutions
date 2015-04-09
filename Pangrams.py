input_string = raw_input("Please Enter String")
alpha_dict = {'a': 0,'b': 0,'c': 0,'d': 0,'e': 0,'f': 0,'g': 0,'h': 0,'i': 0,'j': 0,
'k': 0,'l': 0,'m': 0,'n': 0,'o': 0,'p': 0,'q': 0,'r': 0,'s': 0,'t': 0,'u': 0,'v': 0,'w': 0,'x': 0,'y': 0,'z': 0 }
input_list = list(input_string.lower())

for x in input_list:
    try:
        if alpha_dict[x] == 0:
            alpha_dict[x] = 1
        else:
            continue
    except:
        continue

result_set = set(alpha_dict.values())
if len(result_set) > 1:
    print "not pangram"
else:
    print "pangram"



