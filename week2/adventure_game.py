def forest_path():
    print("Welcome to the Enchanted Forest Adventure!")
    print("You find yourself at the entrance of a mystical forest.")
    print("As you step in, the path splits into two.")
    print("Choices:\n1. Take the glowing path on the left\n2. Explore the shadowy path on the right")
    choice = int(input())
    
    if choice == 1:
        glowing_path()
    else:
        shadowy_path()

def glowing_path():
    print("You chose the glowing path and encounter fireflies lighting up the way.")
    print("Choices:\n1. Follow the fireflies deeper into the forest\n2. Investigate a strange noise nearby")
    choice = int(input())

    if choice == 1:
        follow_fireflies()
    else:
        investigate_noise()

def follow_fireflies():
    print("The fireflies lead you to a magical meadow.")
    print("Choices:\n1. Dance with the fairies in the meadow\n2. Continue exploring the forest")
    choice = int(input())

    if choice == 1:
        dance_with_fairies()
    else:
        continue_exploring()

def dance_with_fairies():
    print("You join the fairies in a joyful dance, and they reward you with a magic amulet.")
    print("The amulet shimmers with mysterious energy.")

def investigate_noise():
    print("You investigate the noise and discover a lost unicorn.")
    print("Choices:\n1. Help the unicorn find its way home\n2. Leave the unicorn and explore further")
    choice = int(input())

    if choice == 1:
        help_unicorn()
    else:
        continue_exploring()

def help_unicorn():
    print("You help the unicorn find its way home, and it grants you a ride to a hidden grove.")
    print("In the grove, you find a secret passage to a treasure chamber.")

def continue_exploring():
    print("You continue exploring the forest and come across a mysterious old tree.")
    print("Choices:\n1. Talk to the tree\n2. Climb the tree for a better view")
    choice = int(input())

    if choice == 1:
        talk_to_tree()
    else:
        climb_tree()

def talk_to_tree():
    print("The old tree shares ancient wisdom and points you to the path of enlightenment.")

def climb_tree():
    print("As you climb the tree, you spot a hidden path that leads to a magical waterfall.")
    print("Choices:\n1. Follow the path to the waterfall\n2. Return to the forest trail")
    choice = int(input())

    if choice == 1:
        waterfall_path()
    else:
        forest_path()

def waterfall_path():
    print("You follow the path and discover a breathtaking waterfall with a mysterious aura.")
    print("Choices:\n1. Dive into the waterfall\n2. Examine the surroundings before deciding")
    choice = int(input())

    if choice == 1:
        dive_into_waterfall()
    else:
        examine_surroundings()

def dive_into_waterfall():
    print("You take a leap of faith into the waterfall and find yourself in a hidden underwater cavern.")
    print("In the cavern, you uncover an ancient chest filled with treasure.")
    print("Congratulations! You've completed the Enchanted Forest Adventure and found the hidden treasure.")

def examine_surroundings():
    print("You carefully examine the surroundings and discover a hidden passage behind the waterfall.")
    print("Choices:\n1. Enter the hidden passage\n2. Return to the forest trail")
    choice = int(input())

    if choice == 1:
        hidden_passage()
    else:
        forest_path()

def hidden_passage():
    print("You enter the hidden passage and find yourself in an underground chamber.")
    print("In the chamber, you encounter a guardian spirit who grants you a magical blessing.")
    print("Congratulations! You've completed the Enchanted Forest Adventure.")

# Start the game
forest_path()
