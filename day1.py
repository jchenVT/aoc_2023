import re
def part1(file):
    sum = 0
    for line in file:
        nums = re.findall(r'\d', line)
        sum += int(f"{nums[0]}{nums[-1]}")
    print(sum)
                         
def part2(file):
    numbers = {"1":1,"2":2,"3":3,"4":4,"5":5,"6":6,"7":7,"8":8,"9":9,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
    sum = 0
    for line in file:
        nums = re.findall(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))', line)
        sum += (numbers[nums[0]] * 10) + numbers[nums[-1]]
    print(sum)
            
with open("input_day1") as f:
    part2(f)
