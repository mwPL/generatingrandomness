import random

# generating dictionary with triads and occurrences of 0s and 1s
def findtr(entry):
    result = {}
    triads = ['000', '001', '010', '011', '100', '101', '110', '111']

    for triad in triads:
        result[triad] = [entry.count(triad + "0"), entry.count(triad + "1")]

    return result


# predicting next figure based on triad entered
def predict(triad):
    p0 = result[triad][0] / (result[triad][0] + (result[triad][1]))
    p1 = result[triad][1] / (result[triad][0] + (result[triad][1]))
    if p0 > p1:
        return '0'
    else:
        return '1'


# predicting string using test string as input, and predict function
def createstring(ts):
    length = len(ts)
    ps = str(random.randint(0, 1)) + str(random.randint(0, 1)) + str(random.randint(0, 1))  # predicted string
    while len(ps) < len(ts):
        ps = ps + predict(ts[((len(ps))-3):len(ps)])
    print('prediction:')
    print(ps)
    return ps


# compare original and predicted string
def compare(original, predicted, balance):
    guessed = []
    for i in range(3, len(original)):
        if original[i] == predicted[i]:
            guessed.append(1)
        else:
            guessed.append(0)

    correct = guessed.count(1)
    incorrect = guessed.count(0)
    percentage = round(((correct/len(guessed)) * 100), 2)
    print(f'\nComputer guessed right {correct} out of {len(guessed)} symbols ({percentage} %)')
    balance = balance + incorrect - correct
    print(f'Your capital is now ${balance}')
    return balance

print('Please give AI some data to learn...\nThe current data length is 0, 100 symbols left')
fl = 100  # Final length
fs = ''  # Final string
triads = ['000', '001', '010', '011', '100', '101', '110', '111']
while len(fs) < fl:
    print('Print a random string containing 0 or 1:')
    entry = input()
    for i in entry:
        if i == '1' or i == '0':
            fs = fs + i
    if len(fs) >= fl:
        print('Final data string:')
        print(fs)
        print('\nYou have $1000. Every time the system successfully predicts your next press, you lose $1.')
        print('Otherwise, you earn $1. Print "enough" to leave the game. Let\'s go!\n')
        qtrs =[]
        for i in range(len(fs)-3):
            qtrs.append(fs[i:i+4])
        findtr(qtrs)
    else:
        print(f'The current data length is {len(fs)}, {fl - len(fs)} symbols left')

result = findtr(qtrs)
capital = 1000
ts = ''
while True:
    while (len(ts)<5):
        print('Print a random string containing 0 or 1:')
        entry = input()  # test string
        if entry == 'enough':
            print('Game over!')
            exit()
        for i in entry:
            if i == '0' or i == '1':
                ts = ts + i
    # print(ts)
    guessed = createstring(ts)
    capital = compare(ts, guessed, capital)
    ts = ''



