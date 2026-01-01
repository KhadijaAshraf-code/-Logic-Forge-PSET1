#challenge 1
def team_contribution_multiplier():
    contribution = []
    impact = []

    scores = input("Enter contribution scores (space separated): ")
    score_list = scores.split()

    # Convert input to integers
    for score in score_list:
        contribution.append(int(score))

    n = len(contribution)

    # Initialize impact with 1
    impact = [1] * n

    # Left product pass
    left_product = 1
    for i in range(n):
        impact[i] = left_product
        left_product *= contribution[i]

    # Right product pass
    right_product = 1
    for i in range(n - 1, -1, -1):
        impact[i] *= right_product
        right_product *= contribution[i]

    print("Contribution:", contribution)
    print("Impact:", impact)


team_contribution_multiplier()



