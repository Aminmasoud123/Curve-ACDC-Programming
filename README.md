# Curve: AC/DC Programming — An Experimental Paradigm

An experimental Python project exploring whether concepts inspired by **DC and AC electrical systems** can provide a useful framework for thinking about computation, state, and continuously changing information.

## 1. Core Concept

Traditional programming often represents computation as a sequence of **explicit state changes**. A program performs an operation, updates its state, and continues to the next operation. This project calls this approach **DC-style programming**.

An alternative approach is to treat values as **continuously changing signals** and allow computation to continuously respond to those changes. We call this experimental approach **AC-style programming**.

The analogy is inspired by the difference between:

* **DC:** a relatively stable direction of electrical flow.
* **AC:** an electrical signal that continuously changes direction and magnitude.

The project does **not** claim that programming literally behaves like electricity. Instead, it asks whether this analogy can inspire useful computational models.

## 2. Initial Experiments

The project currently compares two simple models.

### DC-style

A value changes explicitly and sequentially:

```text
State → Change → State → Change → State
```

### AC-style

A value continuously varies according to a signal:

```text
Signal → Observation → Reaction → New State
              ↑                  ↓
              └──── Feedback ────┘
```

The initial Python experiments use mathematical functions such as `sin()` to simulate continuously changing signals and compare them with explicit step-by-step state updates.

## 3. Future Direction

The long-term goal is to investigate whether AC-style computation can become more than an analogy and lead to practical programming abstractions.

Possible areas include:

* Reactive data structures
* Continuous state machines
* Signal-based APIs
* Feedback-driven computation
* Real-time systems
* Event and stream processing
* Adaptive algorithms
* AI systems that continuously respond to changing information

The project is an **open-ended experiment**. The purpose is to test the idea through increasingly sophisticated implementations and determine whether the AC/DC distinction provides genuine technical value rather than simply being a metaphor.
