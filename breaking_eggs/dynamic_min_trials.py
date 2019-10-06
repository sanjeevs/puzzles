"""Dynamic program to search exhaustively."""

def egg_drop(num_stories, num_eggs):
    """Exhaustive search for the min trials in the worst case to find the floor.

    Keyword arguments:
    num_stories -- the number of stories in the building.
    A building cannot have 0 stories.
    if level of egg was 0 and we drop from 0, then it breaks.
    """
    print("egg_drop", "num_stories=", num_stories, "num_eggs=", num_eggs)
    assert num_eggs > 0
    if num_stories == 0:
        return 0
    if num_stories == 1:
        return 1

    if num_eggs == 1:
        return num_stories

    num_tries = 0
    for k in range(1, num_stories):
        print("k=", k)
        result = max(egg_drop(k -1, num_eggs -1),  # Egg breaks and so move down
                       egg_drop(num_stories -k, num_eggs)) #Egg does not break
        if result < num_tries:
            num_tries = result

    return num_tries

def x__test_1_eggs_drop():
    num_tries = egg_drop(13, 1)
    assert num_tries == 13
    
def test_2_eggs_drop():
    num_tries = egg_drop(4, 2)
    assert num_tries == 13
    
