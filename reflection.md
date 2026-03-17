# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it? 
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

When I first ran the game, it looked like a simple number guessing app with a sidebar for difficulty and a main input box for guesses. Pretty quickly I noticed that the hints for "Too High" and "Too Low" were backwards, telling me to go in the wrong direction. I also saw that the displayed range in the instructions did not always match the actual difficulty range, especially on Hard mode. Another issue was that the score and attempts felt inconsistent, with attempts being off by one and even invalid guesses still consuming an attempt. Finally, starting a new game sometimes produced a secret number outside the difficulty range, which made the game feel unfair.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

For this project I mainly used the built‑in AI assistant in Cursor (powered by GPT) to read the code and help reason about the logic. One helpful suggestion was identifying that the hints for "Too High" and "Too Low" were inverted and that the new game logic was ignoring the difficulty range; after applying those fixes, I verified the behavior by playing several rounds and confirming the hints and ranges matched my expectations. The AI also pointed out the odd use of string comparison for the secret number on alternating turns, which matched the strange behavior I was seeing during play. At least once, an AI explanation of the scoring logic was a bit misleading, focusing on even/odd attempts rather than on designing a more intuitive scoring system, so I had to think through what scoring rules I actually wanted. That experience reminded me that AI is good at surfacing issues, but I still need to make the final design decisions and verify behavior myself.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I treated a bug as fixed only after I could describe the root cause in my own words and then see the game behave correctly in several scenarios. One manual test I ran repeatedly was guessing numbers that were clearly too high or too low and checking that the hint direction and outcome matched the actual secret number. I also changed difficulties and used the debug section to confirm that the secret number always stayed inside the advertised range and that the attempt counter and score changed in predictable ways. The AI assistant helped me think of edge cases, like entering invalid input or hitting the attempt limit exactly, and suggested checking both the UI text and the underlying session state. Those tests gave me confidence that my fixes were robust and not just covering a single happy path.

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

I learned that the secret number kept changing in the original app because it was being re‑generated on each rerun instead of being stored persistently in `st.session_state`. Streamlit reruns the script from top to bottom every time the user interacts with a widget, so any plain variables get reset unless they are stored in session state or some other persistent place. To a friend, I would explain session state as a little dictionary where you can keep values that should survive these reruns, like the current secret number, attempt count, and score. The key change was only setting the secret once when the corresponding key was missing in `st.session_state`, instead of creating a new random number on every run. After that, the secret stayed stable across guesses until I explicitly started a new game.

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to keep is writing down clear hypotheses about bugs before changing code, then using simple tests or prints to confirm or reject each hypothesis. I also found that giving the AI specific, focused questions (like "why is this score formula weird?") produced much more useful help than vague prompts. Next time I work with AI on a coding task, I want to be more deliberate about double‑checking suggestions against the actual code and requirements instead of accepting the first answer that sounds plausible. This project made me see AI‑generated code as a strong starting point or brainstorming partner, but not something I should trust blindly. It reinforced that my job is to understand, test, and refine the logic, even when AI writes most of the initial implementation.
