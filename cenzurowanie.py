# takie zadanie sobie wymyśliłem: jest lista wulgarnych słów i program ma zamienić wulgaryzmy na ocenzurowane słowa
#zostawiając pierwszą literę, a reszte zastępując *

vulgar_words = ["kurwa", "chuj", "dupa"]

user_phrase = input("Napisz coś miłego: ")
user_words = user_phrase.lower().replace(","," ,").replace("."," .").split(" ")

for i in range(len(user_words)):
    for j in range(len(vulgar_words)):
        if user_words[i] == vulgar_words[j]:
            user_words[i] = user_words[i][0] + "*" * (len(vulgar_words[j]) - 1)

censored_user_phrase = ""
for i in range(len(user_words)):
    censored_user_phrase += user_words[i] + " "

censored_user_phrase = censored_user_phrase.replace(" ,",",").replace(" .",".")
print(f"Oto twoja wypowiedź po cenzurze: {censored_user_phrase}")

