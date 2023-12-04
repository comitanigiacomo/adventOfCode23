class day4:
    def part1():
        with open("input.txt") as file:
            lines = file.readlines()
            total_sum = 0
            for line in lines:
                round = False
                card_value = 0
                check = line.split("|")[0].split(":")
                winning = check[1].strip().split(" ")
                to_check = (line.split("|")[1].strip().split(" "))
                for num in to_check:
                    if num != '' and num in winning:
                        if not round: 
                            card_value += 1
                        else:
                            card_value = card_value * 2
                        round = True
                total_sum += card_value
            print(total_sum)
            
    def part2():
        mapping = {}
        with open("input.txt") as file:
            card_number = 1
            lines = file.readlines()
            
            for line in lines:
                mapping[card_number] = 1
                card_number += 1
                
            card_number = 1
                
            for line in lines:
                card_value = day4.card_value(line)
                for i in range(card_number+1, card_number + card_value+1):
                    mapping[i] += mapping[card_number]    
                card_number += 1           
                    
            sum = 0
     
            for val in mapping.values():
                sum += val
                
            print(sum)
            
            
    def card_value(line) -> int:
        card_value = 0
        check = line.split("|")[0].split(":")
        winning = check[1].strip().split(" ")
        to_check = (line.split("|")[1].strip().split(" "))
        for num in to_check:
            if num != '' and num in winning:
                card_value += 1
        return card_value
    
#day4.part1()
#day4.part2()