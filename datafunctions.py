from random import randint
from datetime import date, datetime

initials = ''
bDate = ''
passport = ''
certID = ''
certDate = ''

def getInitialsCensored():
    initials = list(map(list, input('Ваше ФИО: ').split()))
    for i in range(len(initials)):
        for j in range(1, len(initials[i])):
            initials[i][j] = '*'
    return ' '.join([str(''.join([str(i) for i in word])).title() for word in initials])


def getBirthDate():
    return input('Ваша дата рождения в формате ДД.ММ.ГГГГ: ')


def getPassportCensored():
    passport = list(input('Введите вашу серию и номер паспорта без пробелов: '))
    for i in range(2, len(passport) - 3):
        passport[i] = '*'
    passport.insert(4, ' ')
    return ''.join([str(symbol) for symbol in passport])


def getRandomCertID():
    return str('№ 1000 ' + ' '.join([str(str(randint(1000, 9999))) for i in range(3)]))


def getRandomDate():  # copypasted, but modificated!
    start_dt = date.today().replace(day=1, month=1).toordinal()
    end_dt = date.today().replace(day=31, month=12).toordinal()
    return date.fromordinal(randint(start_dt, end_dt)).strftime('%d.%m.%y')


def timeNow():
    return str(datetime.now().strftime('%H%M%S'))


def getAuthtoken():  # sry4this shitcode
    file = open('token_ngrok', 'r')
    token = file.readline()
    if token == 'empty':
        token = input('Enter your Ngrok authtoken: ')
        file.close()
        file = open('token_ngrok', 'w')
        file.write(token)
        file.close()
        return token
    else:
        return token

def profileExists():
    try:
        open('saved_profile', 'r').close()
        return True
    except FileNotFoundError:
        return False


def initialize():  # and4this
    global initials # esli chectno eto pizdec govnokod, no ya hochu spat, poetomy perepishy potom
    global bDate
    global passport
    global certID
    global certDate
    if profileExists():
        if input('Found saved profile, load it? y/n ') == 'y':
            file = open('saved_profile', 'r')
            initials = file.readline()
            bDate = file.readline()
            passport = file.readline()
            certID = file.readline()
            certDate = file.readline()
        else:
            initials = getInitialsCensored()
            bDate = getBirthDate()
            passport = getPassportCensored()
            certID = getRandomCertID()
            certDate = getRandomDate()
            if input('Save profile? y/n ') == 'y':
                file = open('saved_profile', 'w')
                file.write(str(initials + '\n'))
                file.write(str(bDate + '\n'))
                file.write(str(passport + '\n'))
                file.write(str(certID + '\n'))
                file.write(str(certDate + '\n'))
                file.close()




