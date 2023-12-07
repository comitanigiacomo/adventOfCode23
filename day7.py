class day7():
    
    
    def part1():
        cards = ['A', 'K', 'Q', 'J', 'T', 9, 8, 7, 6, 5, 4, 3, 2]
        out = 0
        with open('input.txt', 'r') as f:
            mapping = {}
            datas = f.read().splitlines()
            for data in datas:
                hand = data.split(' ')[0]
                value = data.split(' ')[1]
                if day7.check(hand) not in mapping:
                    mapping[day7.check(hand)] = []
                else:
                    mapping[day7.check(hand)].append((hand, value))
                    mapping[day7.check(hand)] = sorted(mapping[day7.check(hand)], key=lambda x: (cards.index(x[0][0]), cards.index(x[0][1]), cards.index(x[0][2]), cards.index(x[0][3]), cards.index(x[0][4])), reverse=True)

            
                
            for elem in mapping.items():
                print(elem)
                    
                    
            count = 0
            for elem in mapping.items():
                print(elem[1])

            print(out)

    def check(hand):
        map = {}
        for char in hand:
            if char not in map:
                map[char] = 1
            else:
                map[char] += 1

        if day7.five_of_a_kind(hand):
            return 6
        elif day7.four_of_a_kind(hand, map):
            return 5
        elif day7.full_house(hand, map):
            return 4
        elif day7.three_of_a_kind(hand, map):
            return 3
        elif day7.two_pair(hand, map):
            return 2
        elif day7.one_pair(hand, map):
            return 1
        else:
            return 0


    def five_of_a_kind(hand):
        if len(set(hand)) == 1:
            return True
        return False

    def four_of_a_kind(hand, map):
        if len(map) == 2 and 4 in map.values():
            return True
        return False

    def full_house(hand, map):
        if len(map) == 2 and 3 in map.values() and 2 in map.values():
            return True
        return False

    def three_of_a_kind(hand, map):
        if len(map) == 3 and 3 in map.values():
            return True
        return False

    def two_pair(hand, map):
        if len(map) == 3 and 2 in map.values():
            return True
        return False

    def one_pair(hand, map):
        if len(map) == 4 and 2 in map.values():
            return True
        return False

    def high_card(hand):
        if len(set(hand)) == 5:
            return True
        return False
            
        
        
day7.part1()