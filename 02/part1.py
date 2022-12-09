import numpy as np

choice2points = {"X": 1, "Y": 2, "Z": 3}
plays2points = {
    # Losses
    "AZ": 0,
    "BX": 0,
    "CY": 0,

    # Ties
    "AX": 3,
    "BY": 3,
    "CZ": 3,

    # Wins
    "AY": 6,
    "BZ": 6,
    "CX": 6
}

round_scores = []
with open("02_p1.txt", "r") as f:
    for line in f:
        opp, you = line.strip().upper().split()
        
        # Compute the two scores.
        choice_score = choice2points[you]
        outcome_score = plays2points[f"{opp}{you}"]
        
        # Add 'em up.
        round_scores.append(choice_score + outcome_score)

# Part 1: What would your total score be if everything 
# goes exactly according to your strategy guide?
scores_numpy = np.array(round_scores)
print(f"My total score would be {scores_numpy.sum()}.")

# Part 2: 