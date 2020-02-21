import random
from tweet import twitter_bot


def remove_slash_ns(input_list):
    return [word.rstrip('\n') for word in input_list]


def createLists(peopleListLocation, templateListLocation):
    try:
        with open(peopleListLocation) as input:
            people_list = input.readlines()
    except:
        print("Error. Could not read " + peopleListLocation)
    try:
        with open(templateListLocation) as input:
            template_list = input.readlines()
    except:
        print("Error. Could not read " + peopleListLocation)

    people_list = remove_slash_ns(people_list)
    template_list = remove_slash_ns(template_list)
    return people_list, template_list


def find_and_replace(person, template):
    '''As of 2/19/20, there is only variable per template. This may change in the future, so I have created a method in order to make it easier to change in the future.'''
    return template.replace("PERSON", person)


if __name__ == "__main__":
    people_list, template_list = (
        createLists("people.txt", "template.txt")
        )
    con_bot = twitter_bot()
    con_bot.send_tweet(find_and_replace(random.choice(people_list), random.choice(template_list)))
