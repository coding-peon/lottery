import lottery


largest_number = input("The largest number in the lottery: ")
if len(str(largest_number)) < 1:
    largest_number = 90

howmany = input("How many numbers to draw? ")
if len(str(howmany)) < 1:
    howmany = 5
  
pot = lottery.Lottery(largest_number)
result = pot.draw(howmany)

if type(result) is list:
    numbers = map(str, sorted(result))
    print("Lottery numbers: ", ', '.join(numbers))
else:
    print(result)
  