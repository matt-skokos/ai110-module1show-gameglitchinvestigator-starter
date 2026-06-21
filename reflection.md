# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
I noticed that the game UI was well organized and plain. There are several affordances for interacting with the game, the settings and submitting / adjusting the games response.  There is also a debug scaffold for testing and fixing the glitches
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
    - Bug 1: 
      - From debugger, target == 79 
      - I guessed 90 and got "Go HIGHER" back
      - Guess #2 95, "Go HIGHER" .... Guess #3 75, "Go LOWER"
      - Seems to be a return glitch, I wonder if the logic for guesses is flipped or if something is wrong with the way the inputs are being read
    - Bug 2:
      - Lost game, started a new game and the debug info from the last game still exists
      - I can't submit guesses and nothing is being input when I hit any other buttons
      - Happens even when I restart another game, need to reload browser
**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|Guess 44|  Go Higher!          | 📉Go LOWER!    |     N/A
|Guess 88|  Go Lower!           | 📈Go HIGHER!    |    N/A
|New Game| Reset Cache, New Game   | Frozen stats, no new game |   N/A
|Difficulty| logic doesn't make sense | switched up max guesses |  N/A



---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used the Claude Code extension in the VSCode app.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
The AI found that the hints were backwards, found the bug and fixed it:
The bug was in check_guess (app.py:38-40): when guess > secret (too high), the message said "📈 Go HIGHER!" and when guess < secret (too low) it said "📉 Go LOWER!" — both backwards. The fix swaps the messages so the directions match the outcome labels correctly.

I've verified this by running another session and checking that the output was expected using the debugger.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
Claude located a bug in app.py at The root cause is in the "New Game" handler at app.py:118-122:
if new_game:
    st.session_state.attempts = 0
    st.session_state.secret = random.randint(1, 100)
    st.success("New game started.")
    st.rerun()
This was the wrong location for the bug while it was, I checked in the file and it was referring to code a bit lower... the actual hint was correct just the wrong location.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
