import random  # This module is for the code to pick the arguments randomly

"""Code below conditions the inputs"""


def get_valid_character(message):
    while True:

        user_input = input(message).strip()  # .script() removes the spaces when being read by the coder

        if len(user_input) < 2:  # Measures the amount of characters and make sures that it is not LESS BY 2
            print("Input is too short. Please enter at least 2 characters.")
        elif not user_input.replace(" ", "").isalpha():  # Allows spaces and checks if there are symbols
            print("Input is invalid. Please enter only alphanumeric characters.")

        return user_input


def get_inputs(prompts):

    inputs = {}  # Here is where the user's input will be recorded upon

    for key, prompt in prompts:  # This is where the code will go through the tuples(sets) one by one. (key, prompt:)
        inputs[key] = get_valid_character(prompt)  # This is where the input adds the function get_valid_character

    return inputs


def generate_stories_templates():  # Here is where I generate the stories RANDOMLY
    return [
        "Once upon a {adjective} morning, I woke up feeling particularly {adjective}. " +
        "I stumbled to the dining room, only to find a {noun} eating my breakfast.",

        "Last Christmas, my friends and I decided to explore the old, {adjective} mansion on the street named " +
        "{noun} street. They say it's haunted by the ghost of a {occupation} who {verb} herself long ago.",

        "It was a {adjective} night, perfect for a {adjective} dinner party. Count {name} had invited all the " +
        "{noun} in the neighborhood to his {adjective} castle."
    ]


def print_stories_template():  # This is where the story gets printed FIRST before the INPUT
    templates = generate_stories_templates()  # Used to refer the stories in generate_stories_templates
    selected_template = random.choice(templates)  # Used to randomize the stories
    print("Here is the story you'll be filling out:\n")
    print(selected_template)
    print()
    return selected_template


def generate_stories(selected_template, noun, verb, adjective, name, occupation):  # This formats the story
    formatted_story = selected_template.format(
        noun=noun, verb=verb, adjective=adjective, name=name, occupation=occupation
    )  # Replaces the placeholders with the variables
    return formatted_story


def main():

    selected_template = print_stories_template()

    prompts = [  # Here are the prompts
        ("noun", "Type a noun/s: "),
        ("verb", "Type a verb/s: "),
        ("adjective", "Type a adjective/s: "),
        ("name", "Type a name/s: "),
        ("occupation", "Type a occupation/s: ")
    ]

    inputs = get_inputs(prompts)  # Here is where the inputs will become just a variable

    noun = inputs["noun"]  # Here are the variables now
    verb = inputs["verb"]
    adjective = inputs["adjective"]
    name = inputs["name"]
    occupation = inputs["occupation"]

    random_story = generate_stories(selected_template, noun, verb, adjective, name, occupation)  # Summarizes all of it

    print(random_story)  # This prints out the story with the output


if __name__ == "__main__":
    main()