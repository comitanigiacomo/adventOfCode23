import re

class day6:
    def part1():
        out = 1
        with open('input.txt') as f :
            lines = f.read().splitlines()
            time = re.findall(r'\d+', lines[0])
            distance = re.findall(r'\d+', lines[1])
            for i in range(len(time)):
                number_of_ways = 0
                for j in range(int(time[i])):
                    if j*(int(time[i])-j) > int(distance[i]):
                        number_of_ways += 1
                out *= number_of_ways
                number_of_ways = 0
            print(out)
            
    def part2():
        total_time = ''
        total_distance = ''
        with open('input.txt') as f :
            lines = f.read().splitlines()
            time = re.findall(r'\d+', lines[0])
            distance = re.findall(r'\d+', lines[1])
            number_of_ways = 0
            for i in range (len(time)):
                total_time += time[i]
                total_distance += distance[i]
            for j in range(int(total_time)):
                if j*(int(total_time)-j) > int(total_distance):
                    number_of_ways += 1
            print(number_of_ways)
                     
#day6.part1()
#day6.part2()