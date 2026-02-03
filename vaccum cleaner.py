import random

environment = {
    "A": random.choice(["Dirty", "Clean"]),
    "B": random.choice(["Dirty", "Clean"])
}

vacuum_location = random.choice(["A", "B"])

def vacuum_agent(location, environment):
    print(f"Vacuum is in room {location}")
    print(f"Room status: {environment}")

    if environment[location] == "Dirty":
        environment[location] = "Clean"
        print(f"Action: Clean room {location}")
    else:
        if location == "A":
            location = "B"
            print("Action: Move Right to room B")
        else:
            location = "A"
            print("Action: Move Left to room A")

    return location

for step in range(5):
    print(f"\nStep {step + 1}")
    vacuum_location = vacuum_agent(vacuum_location, environment)
