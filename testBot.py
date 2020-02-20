import os
import requests

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

if __name__ == "__main__":
    print(
        createLists("people.txt", "template.txt")
        )