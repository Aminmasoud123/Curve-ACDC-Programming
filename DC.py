# DC-style programming
# State changes happen explicitly and sequentially.
# Each step directly modifies the current state.

state = 0

for step in range(10):
    change = 1
    state += change

    print(
        "Step:", step,
        "Change:", change,
        "State:", state
    )