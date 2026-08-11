# AC-style programming
# A continuously changing signal drives the system.
# The program observes the signal and reacts to its movement.

import math

state = 0.0

for t in range(20):
    signal = math.sin(t * 0.5)

    change = signal - state
    state += change * 0.3

    direction = "RISING" if change > 0 else "FALLING"

    print(
        "Time:", t,
        "Signal:", round(signal, 2),
        "State:", round(state, 2),
        "Direction:", direction
    )