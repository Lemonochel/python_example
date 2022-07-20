import random

guessesTaken = 0

print('Привет! Как тебя зовут?')
myName = input()

number = random.randint(1, 20)
print('Что ж, ' + myName + ', я загадываю число от 1 до 20.')

for guessesTaken in range(6):
	print('Попробуй угадать')
	guess = int(input())

	if guess < number:
		print('Твое число слишком маленькое.')

	if guess > number:
		print('Твое число слишком большое.')

	if guess == number:
		break

if guess == number:
	guessesTaken = str(guessesTaken + 1)
	print(myName + ' справился за ' + guessesTaken + ' попытки!')

if guess != number:
	number = str(number)
	print('Число было ' + number)
