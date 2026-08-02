def accuracy(
    correct,
    total
):

    if total == 0:
        return 0


    return correct / total



def print_metric(
    name,
    score
):

    print(
        f"{name}: {score:.2%}"
    )