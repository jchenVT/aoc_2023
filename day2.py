def p1(f):
    total = 0
    for line in f:
        legit = True
        id = int(line.split()[1][:-1])
        pulls = line[6:].split(";")
        for pull in pulls:
            if (loc := pull.find("red")) != -1:
                if int(pull[loc-3:loc-1].strip()) > 12:
                    legit = False
                    break
            if (loc := pull.find("green")) != -1:
                if int(pull[loc-3:loc-1].strip()) > 13:
                    legit = False
                    break
            if (loc := pull.find("blue")) != -1:
                if int(pull[loc-3:loc-1].strip()) > 14:
                    legit = False
                    break
                
        if legit:
            total += id

    print(total)
def p2(f):
    total = 0
    for line in f:
        min_red, min_green, min_blue = 0,0,0
        pulls = line[6:].split(";")
        for pull in pulls:
            if (loc := pull.find("red")) != -1:
                if (new_red := int(pull[loc-3:loc-1].strip())) > min_red:
                    min_red = new_red
            if (loc := pull.find("green")) != -1:
                if (new_green := int(pull[loc-3:loc-1].strip())) > min_green:
                    min_green = new_green
            if (loc := pull.find("blue")) != -1:
                if (new_blue := int(pull[loc-3:loc-1].strip())) > min_blue:
                    min_blue = new_blue
        total += min_red * min_green * min_blue
    print(total)
                
with open("input_day2") as f:
    p2(f)
