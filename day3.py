import re

class day3:
    def solution() -> (list[str], dict):
        with open('input.txt') as f:
            numbers = {}
            mapping = {}
            lines = f.read().splitlines()
            for i in range(len(lines)):
                numbers = (re.finditer('[0-9]+', lines[i]))
                for matches in numbers:
                    if i not in mapping:
                        mapping[i] = []
                    if matches.start() != 0:
                        mapping[i].append((int(matches.group()), matches.start()-1, matches.end()))
                    else:
                        mapping[i].append((int(matches.group()), matches.start(), matches.end()))
            out1 = 0
            out2 = 0
            gears = []
            for i in range (len(lines)):
                j = 0
                for char in lines[i]:
                    if not char.isdigit() and char != '.':
                        if i -1 in mapping:
                            for element in mapping[i-1][:]:
                                if element[1] <= j <= element[2]:
                                    gears.append(element[0])
                                    if len(gears) == 2:
                                        out2 += day3.calculate_gears(gears)
                                        gears = []
                                    out1 += element[0]
                                    #mapping[i-1].remove(element)
                        if i +1 in mapping:
                            for element in mapping[i+1][:]:
                                if element[1] <= j <= element[2]:
                                    gears.append(element[0])
                                    if len(gears) == 2:
                                        out2 += day3.calculate_gears(gears)
                                        gears = []
                                    out1 += element[0]
                                    #mapping[i+1].remove(element)
                        if i in mapping:
                            for element in mapping[i][:]:
                                if j == element[2] or j == element[1]:
                                    gears.append(element[0])
                                    if len(gears) == 2:
                                        out2 += day3.calculate_gears(gears)
                                        gears = []
                                    out1 += element[0]
                                    #mapping[i].remove(element)
                    j+= 1
                    gears = []
            #print(out1)
            #print(out2)
            
    def calculate_gears(gears):
        return gears[0] * gears[1]
    
day3.solution()
