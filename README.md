# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose.  
  The app is a Streamlit number guessing game where the player selects a difficulty, then tries to guess a secret number within a limited number of attempts while watching their score change based on performance.
- [x] Detail which bugs you found.  
  Initially, the hints for "Too High" and "Too Low" were reversed, the secret number could change in unpredictable ways (especially when starting a new game), and the displayed range did not always match the actual difficulty range. The scoring and attempt counting were also confusing, with off‑by‑one behavior and invalid guesses still consuming attempts.
- [x] Explain what fixes you applied.  
  I refactored the core game logic into `logic_utils.py`, fixed the comparison logic so that high/low hints match the actual secret number, and made sure the secret number always stays within the difficulty range (including after starting a new game). I also simplified and corrected the scoring and attempt handling so that attempts and points behave in a more consistent and predictable way.

## 📸 Demo
<img width="1893" height="808" alt="Screenshot 2026-03-17 055218" src="https://github.com/user-attachments/assets/7311d727-9de6-4502-bf42-71a5f03da193" />



## 🚀 Stretch Features

- [ ] [If you choose to complete Challenge 4, insert a screenshot of your Enhanced Game UI here]
