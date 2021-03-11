frame = [' ' for x in range(10)]


def insertLetter(letter, pos):
    frame[pos] = letter


def showFrame(frame):
    # print(' |  |  ')
    print(frame[1]+' | '+frame[2]+' | '+frame[3])
    print('---------')
    print(frame[4]+' | '+frame[5]+' | '+frame[6])
    print('---------')
    print(frame[7]+' | '+frame[8]+' | '+frame[9])


def spaceFree(pos):
    return frame[pos] == ' '


def isFrameFull(frame):
    if frame.count(' ') > 1:
        return False
    else:
        return True


def isWinner(f, l):
    return((f[1] == l and f[2] == l and f[3] == l) or
           (f[4] == l and f[5] == l and f[6] == l) or
           (f[7] == l and f[8] == l and f[9] == l) or
           (f[1] == l and f[4] == l and f[7] == l) or
           (f[2] == l and f[5] == l and f[8] == l) or
           (f[3] == l and f[6] == l and f[9] == l) or
           (f[1] == l and f[5] == l and f[9] == l) or
           (f[7] == l and f[5] == l and f[3] == l))


def playerMove():
    start = True
    while start:
        move = int(input("Select position between 1 to 9 : "))
        try:
            if move > 0 and move < 10:
                if spaceFree(move):
                    start = False
                    insertLetter('X', move)
                else:
                    print('Sorry this space is full')
            else:
                print('Number must be in between 1 and 9')

        except:
            print('Please Enter a Number')


def computerMove():
    possibleMoves = [x for x, letter in enumerate(
        frame) if letter == ' ' and x != 0]
    move = 0
    for let in ['0', 'x']:
        for i in possibleMoves:
            frameCopy = frame[:]
            frameCopy[i] = let
            if isWinner(frameCopy, let):
                move = i
                return move
    cornerOpen = []
    for i in possibleMoves:
        if i in [1, 3, 7, 9]:
            cornerOpen.append(i)

    if len(cornerOpen) > 0:
        move = selectRandom(cornerOpen)
        return move
    if 5 in possibleMoves:
        move = 5
        return move



    edgesOpen = []
    for i in possibleMoves:
        if i in [2, 4, 6, 8]:
            edgesOpen.append(i)

    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)
        return move


def selectRandom(li):
    import random
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def main():
    print("lets get going")
    showFrame(frame)

    while not(isFrameFull(frame)):
        if not(isWinner(frame, 'O')):
            playerMove()
            showFrame(frame)
        else:
            print("you loose 🤣")
            break
        if not(isWinner(frame, 'X')):
            move = computerMove()
            if move == 0:
                print('')
            else:
                insertLetter('O', move)
                print('Computer opted position', move, ':')
                showFrame(frame)
        else:
            print('You Won 😒')
            break

    if isFrameFull(frame):
        print('Its a tie')


while True:
    x = input("Do you want to play ? (y/n)")
    if x.lower() == 'y':
        frame = [' ' for x in range(10)]
        print('-------------------')
        main()
    else:
        break
