#Задача №9
#Создать игру, в которой компьютер выбирает какое-либо слово, а игрок должен его отгадать.
#Компьютер сообщает игроку, сколько букв в слове, и дает пять попыток узнать, есть ли какая-либо буква в слове, причем программа может отвечать только "Да" и "Нет". 
#Вслед за тем игрок должен попробовать отгадать слово. 

import random
WORDS=("дом","кран","сложный","простой","машина","животное")
word=random.choice(WORDS)
live=3
bukva=""
slovo=""
(chislo)=len(word)
print("Я выбрал слово,угадай какое. В этом слове",str(chislo),"букв.")
print("У тебя"+str(live)+"попытки угадать буквы")
while live>0:
		#print (word)
		bukva=input("Введите букву\n")
		if bukva in list (word) :
			print("Да.")
			live=live-1
		else:
			print("Нет.")
			live=live-1
if live==0:
		slovo=input("Ваши попытки кончились")
		if slvo==word:
			print("Вы угадали слово")
		else:
			print("Вы не угадали слово")
input("Нажмите Enter для выхода")
