score = int(input('Enter a test score: '))
while score < 0 or score >100:
    print('ERROR: THe score cannot be negative')
    print('or greater than 100.')
    score = int(input('Enter the correct score:'))
print("The score is:",score)    