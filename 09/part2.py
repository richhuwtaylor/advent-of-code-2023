def extrapolate(history):

    if all(x == 0 for x in history):
        return 0

    deltas = [b - a for a, b in zip(history, history[1:])]

    diff = extrapolate(deltas)

    return history[0] - diff

def sum_of_extrapolated_values(input_text):
    histories = [list(map(int, line.split())) for line in input_text.strip().splitlines()]
    extrapolated_values = [extrapolate(history.copy()) for history in histories]
    return sum(extrapolated_values)

with open("input.txt", "r") as file:
    input_text = file.read()

result = sum_of_extrapolated_values(input_text)
print(result)