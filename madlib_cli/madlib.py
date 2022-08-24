def read_template(path):
    with open(path) as madlib:
        return madlib.read().strip()


def parse_template(story):
    stripped_story = ""
    in_template = False
    sentence_elements = []
    element_count = 0
    for character in story:
        if not in_template:
            stripped_story += character
            if character == '{':
                sentence_elements.append('')
                in_template = True
        else:
            if character == '}':
                stripped_story += character
                element_count += 1
                in_template = False
            else:
                sentence_elements[element_count] += character
    return [stripped_story, tuple(sentence_elements)]


def merge(stripped_story, new_words_tuple):
    new_story = ""
    new_words_arr = [*new_words_tuple]
    for character in stripped_story:
        if not character == '{' and not character == '}':
            new_story += character
        elif character == '{':
            new_story += new_words_arr.pop(0)
    print(new_story)
    return new_story


if __name__ == '__main__':
    print('Greetings, what name do you go by?')
    username = input('> ')

    print(f"\nWelcome {username}, feast your eyes on the Madlib Command Line Interface Game FOR THE AGES!!\n")
    print('The rules are simple, you will be prompted for words based on hints such as "noun", '
          '"adjective", "verb" etc until you have replaced all key words with your own. Upon completion you will be '
          'read your adjusted story and let me tell you, the results will surprise you!\n')

    input("Press Enter to begin...")

    story = read_template('assets/make_me_a_video_game_template.txt')
    stripped_story, sentence_elements = parse_template(story)
    new_sentence_elements = []
    for sentence_element in sentence_elements:
        new_sentence_elements.append(input(f'> {sentence_element}: '))
    new_story = merge(stripped_story, tuple(new_sentence_elements))

    print(new_story)
    file_name = input('\nWhat would you like to name this story\'s file? ')
    with open(f"finished_madlibs/{file_name}.txt", 'w') as story_writer:
        story_writer.write(new_story)


# with open('assets/make_me_a_video_game_template.txt') as madlib:
#     newStory = ""
#     inTemplate = False
#     sentenceElement = ""
#     for character in madlib.read():
#         if character == '{':
#             inTemplate = True
#             continue
#         if not inTemplate:
#             newStory += character
#         else:
#             if character == '}':
#                 newStory += input(f'> {sentenceElement}: ')
#                 sentenceElement = ""
#                 inTemplate = False
#             else:
#                 sentenceElement += character
#
# print('\n', newStory)``