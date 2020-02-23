movies = [
    "Alice in Wonderland","Waking Sleeping Beauty","Oceans","Prince of Persia: The Sands of Time","Toy Story 3",
    "The Sorcerer's Apprentice","The Crimson Wing: Mystery of the Flamingos","Secretariat","Do Dooni Chaar",
    "Tangled","The Boys: The Sherman Brothers' Story","Tron: Legacy","Anaganaga O Dheerudu",
    "Lilly the Witch: The Journey to Mandolan","Mars Needs Moms","Zokkomon","African Cats","Prom",
    "Pirates of the Caribbean: On Stranger Tides","Cars 2","Winnie the Pooh","The Muppets","John Carter",
    "Chimpanzee","Arjun: The Warrior Prince","Brave","The Odd Life of Timothy Green","Frankenweenie","Wreck-It Ralph",
    "Oz the Great and Powerful","Wings of Life","Monsters University","The Lone Ranger","Planes","Frozen",
    "Saving Mr. Banks","Muppets Most Wanted","Bears","Million Dollar Arm","Maleficent","Planes: Fire & Rescue",
    "Khoobsurat","Big Hero 6","Into the Woods","Cinderella","Monkey Kingdom","Tomorrowland","Inside Out","ABCD 2",
    "The Good Dinosaur","The Finest Hours","Zootopia","The Jungle Book","Tini: The Movie",
    "Alice Through the Looking Glass","Finding Dory","The BFG","Pete's Dragon","Queen of Katwe","Moana",
    "Growing Up Wild","Dangal","L'Empereur - March of the Penguins 2: The Next Step","Beauty and the Beast",
    "Born in China","Pirates of the Caribbean: Dead Men Tell No Tales","Cars 3","Ghost of the Mountains",
    "Jagga Jasoos","Coco","Expedition China","A Wrinkle in Time","Incredibles 2","Christopher Robin",
    "The Nutcracker and the Four Realms","Ralph Breaks the Internet","Mary Poppins Returns","Dumbo","Penguins",
    "Aladdin","Toy Story 4","The Lion King","Maleficent: Mistress of Evil","Lady and the Tramp","Noelle",
    "Frozen II","One Day at Disney","Togo"]

    import random

# Initalisation
secret_phrase = random.choice(movies)
avalible_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m",
                    "n","o","p","q","r","s","t","u","v","w","x","y","z"]
guessed_letters = [" "]
remaining_lives = 10
win = False
user_input = None

# Loop game while user has not won and still has avaliable lives
while win == False and remaining_lives > 0:

    # Get user input
    if user_input == None:
        user_input = ""
    else:
        while not user_input in avalible_letters:
            user_input = input("enter letter guess: ").lower()
            
        # Update guess lists
        avalible_letters.remove(user_input)
        guessed_letters.append(user_input)


    # Prepairing board
    output = []
    for letter in secret_phrase:
        if letter.lower() in avalible_letters:
            output.append("_")
        else:
            output.append(letter)

    # Print board
    print(" ".join(output), "   ( Lives: ", "*" * remaining_lives, ")")
    
    # Check for win
    if not "_" in output:
        win = True
        print("Whoo! you won.")
    
    # Check current guess
    if not guessed_letters[-1] in secret_phrase:
        remaining_lives = remaining_lives - 1
        if remaining_lives == 0:
            print("sorry, you lost! answer: ", secret_phrase)