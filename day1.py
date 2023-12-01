class day1:
    
    def part1() -> int:
        sum = 0
        with open('input.txt', 'r') as file:
            for line in file:
                first = ''
                last = ''
                for i in range(len(line)):
                    if line[i].isdigit():
                        if first == '':
                            first = line[i]
                        last = line[i]
                sum += int(first + last)
        return sum

        
    def part2() -> None:
        word_to_number = {
            'zer': 0,
            'one': 1,
            'two': 2,
            'thr': 3,
            'fou': 4,
            'fiv': 5,
            'six': 6,
            'sev': 7,
            'eig': 8,
            'nin': 9
        }
        with open('input.txt', 'r') as file:
            calibration_sum = 0
            for line in file:
                first = ''
                last = ''
                for i in range(len(line)):
                    if line[i].isdigit():
                        if first == '':
                            first = line[i]
                        last = line[i]
                    else:
                        if i <= len(line)-3:
                            string = line[i:i+3]
                            num = word_to_number.get(string)
                            if num != None:
                                if first == '':
                                    first = str(num)
                                last = str(num)
                calibration_sum += int(first +  last)
                     
            return calibration_sum
                                        
                                    
#print(day1.part1())
#print(day1.part2())
        
        
        
           
        