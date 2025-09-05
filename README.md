# Tic-tac-toe
A simple tic-tac-toe game using Python GUI.

## Motivation:
While trying to wrap my head around complicated concepts which are nevertheless important for their influence in data science projects, I tried to start simple. This is a project where I ended up making a tic-tac-toe game by simply using python, complete with a GUI and full user interactibility. 

## Setup and Usage:

**1. Clone the repository:**
```bash
git clone [https://github.com/Jade2451/Tic-tac-toe]
cd [Tic-tac-toe]
```

**2. Create a virtual environment and install dependencies:**
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
pip install -r requirements.txt
```

The primary library used is `guizero`.

**3. Run the script**

```bash
python game.py
```
That's it!

---

## Thoughts:

It was a rather impromptu decision for making this game. My hope was to better understand the usage of a 2D list(matrix) to efficiently manage a game state. 
Understanding the indices was key in resolving the win condition but another tricky part was tracking each player's moves. The switching was suprisingly easy. What was hard was devising 
