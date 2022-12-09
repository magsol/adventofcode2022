import numpy as np

choice2points = {"X": 1, "Y": 2, "Z": 3}
plays2responses = {
    # Losses
    "X": {
        "A": "Z",
        "B": "X",
        "C": "Y"
    },

    # Ties
    "Y": {
        "A": "X",
        "B": "Y",
        "C": "Z"
    },

    # Wins
    "Z": {
        "A": "Y",
        "B": "Z",
        "C": "X"
    }
}

round_scores = []
with open("02_p1.txt", "r") as f:
    for line in f:
        opp, you = line.strip().upper().split()

        play = plays2responses[you][opp]
        choice_score = choice2points[play]
        # How should the round end?
        if you == "X": # lose
            outcome_score = 0
        elif you == "Y": # tie
            outcome_score = 3
        else: # win
            outcome_score = 6
        
        # Add 'em up.
        round_scores.append(choice_score + outcome_score)

# Part 2: Following the Elf's instructions for the second column, 
# what would your total score be if everything goes exactly 
# according to your strategy guide?
scores_numpy = np.array(round_scores)
print(f"My total score would be {scores_numpy.sum()}.")