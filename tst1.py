import random

#
words_list = ["orange", "banana", "cherry"]

random_word = random.choice(words_list)
word_length = len(random_word)
attempts = 7

guessed_letters = ["*" for _ in range(word_length)]


def display_word():
    print(" ".join(guessed_letters))


while attempts > 0:
    print(f"\nУ вас залишилося {attempts} спроб")
    display_word()
    user_input = input("Введіть букву або слово: ").lower()

    if len(user_input) > 1:

        if user_input == random_word:
            print("Ви вгадали слово! Вітаємо!")
            break
        else:
            print("Слово не правильне.")
            attempts -= 1
    else:

        if user_input in random_word:
            print("Така літера є!")

            for i in range(word_length):
                if random_word[i] == user_input:
                    guessed_letters[i] = user_input
        else:
            print("Такої літери немає.")
            attempts -= 1

    if "*" not in guessed_letters:
        print("Ви вгадали слово! Вітаємо!")
        break

if attempts == 0:
    print(f"Ви програли! Загадане слово було '{random_word}'.")
