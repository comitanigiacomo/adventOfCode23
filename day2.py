import re
import sys

class day2:
    
    def part1():
        with open('input.txt', 'r') as file:
            possible_games = []
            for line in file:
                sets = re.findall(r'\d+ \w+', line)
                game_possible = True
                for set in sets:
                    count, color = set.split()
                    if color == 'red' and int(count) > 12:
                        game_possible = False
                        break
                    elif color == 'green' and int(count) > 13:
                        game_possible = False
                        break
                    elif color == 'blue' and int(count) > 14:
                        game_possible = False
                        break
                if game_possible:
                    possible_games.append(line.split(':')[0].strip())
        
            print(possible_games)
            nums = []
            for game in possible_games:
                nums += (re.findall(r'\d+', game))
            
            sum = 0
            for n in nums:
                sum += int(n)
            print(sum)
            
    def part2():
        with open('input.txt', 'r') as file:
            sum = 0
            for line in file:
                min_red = 0
                min_green = 0
                min_blue = 0
                sets = re.findall(r'\d+ \w+', line)
                for set in sets:
                    count, color = set.split()
                    if color == 'red' and int(count) > min_red:
                        min_red = int(count)
                        
                    elif color == 'green' and int(count) > min_green:  
                        min_green = int(count)
                        
                    elif color == 'blue' and int(count) > min_blue:
                        min_blue = int(count)
                        
                sum += min_red * min_green * min_blue
            print(sum)
            
                
        
#day2.part1()     
day2.part2()
        