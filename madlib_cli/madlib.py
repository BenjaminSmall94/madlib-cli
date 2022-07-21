print('Greetings, what name do you go by?')
username = input('> ')

print(f"\nWelcome {username}, to the Madlib Command Line Interface Game FOR THE AGES\n")
print('The rules are simple, you will be prompted for words based on hints such as "noun", '
      '"adjective", "verb" etc until you have replaced all key words with your own. Upon completion you will be '
      'read your adjusted story and let me tell you, the results will surprise you!\n')

input("Press Enter to begin...")

with open('assets/make_me_a_video_game_template.txt') as madlib:
    newStory = ""
    inTemplate = False
    sentenceElement = ""
    for character in madlib.read():
        if character == '{':
            inTemplate = True
            continue
        if not inTemplate:
            newStory += character
        else:
            if character == '}':
                newStory += input(f'> {sentenceElement}: ')
                sentenceElement = ""
                inTemplate = False
            else:
                sentenceElement += character

print('\n', newStory)
# print('Which story would you like to do?\n\nMaking a Video Game\n\n')
