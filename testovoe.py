import random

count = 0

print("Привет, призыватель. Как тебя зовут?")
name = str(input())

number = random.randint(1, 7)

for count in range(3):
	print("Сообщи число, которое я загадал!")
	guess = int(input())

	if guess < number:
		print("НЕТ, БОЛЬШЕ")

	if guess > number:
		print("НЕТ, МЕНЬШЕ")

	if guess == number:
		break

if guess == number:
	count = str(count + 1)
	print('Отлично! Ты молодец, ты справился за ' + count + ' попытки')

if guess != number:
	print("ты проиграл!")
