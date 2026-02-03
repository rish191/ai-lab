import random

states = [
    ("A", "Dirty", "Dirty"),
    ("A", "Dirty", "Clean"),
    ("A", "Clean", "Dirty"),
    ("A", "Clean", "Clean"),
    ("B", "Dirty", "Dirty"),
    ("B", "Dirty", "Clean"),
    ("B", "Clean", "Dirty"),
    ("B", "Clean", "Clean")
]

actions = ["Clean", "Left", "Right"]

Q = {(s, a): 0 for s in states for a in actions}

alpha = 0.1
gamma = 0.9
epsilon = 0.1

def get_state(location, env):
    return (location, env["A"], env["B"])

def choose_action(state):
    if random.random() < epsilon:
        return random.choice(actions)
    return max(actions, key=lambda a: Q[(state, a)])

def take_action(action, location, env):
    reward = -1

    if action == "Clean":
        if env[location] == "Dirty":
            env[location] = "Clean"
            reward = 10
    elif action == "Left":
        location = "A"
    elif action == "Right":
        location = "B"

    return location, reward

for episode in range(500):
    env = {"A": random.choice(["Dirty", "Clean"]),
           "B": random.choice(["Dirty", "Clean"])}
    location = random.choice(["A", "B"])

    for step in range(20):
        state = get_state(location, env)
        action = choose_action(state)
        new_location, reward = take_action(action, location, env)
        new_state = get_state(new_location, env)

        Q[(state, action)] += alpha * (
            reward + gamma * max(Q[(new_state, a)] for a in actions)
            - Q[(state, action)]
        )

        location = new_location

print("Training complete")
