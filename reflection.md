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
The primary way I decided was to manually test the game and verify that the behavior/output reflected the fix I was after. I also used the agent to write several pytests that confirm that the hints and the game reset were both working.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I manually tested the higher/lower hint output. This was easy to do using the debug info in the app.
- Did AI help you design or understand any tests? How?
Yes AI helped me to create tests that covered that the game was resetting during new games. It also added a test to verify that game increment logic was working and that there were not abrupt stops during the new game.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
I would say that the edits are not "hot-edits" and that they should definitely be prepared to edit small parts of logic and restart the entire app. I'd also tell them that the code that is executed at the time the app is launch is the code that you will experience for the duration of that launch. 

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
I want to definitely use the micro-edit habit. I really felt like narrowing in on one function at a time felt much better than for instance just saying I need a feature to work and to keep having it iterate until it finished and I got what I wanted. 
Furthermore I hadn't been in the practice of having tests generated directly after finishing a class/part of the code. I will definitely be using that as I go further into developing with AI so that I can feel comfortable in the edits and verify the behaviors that I see on the surface are working under the hood.
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
As stated above, I really felt a better outcome when I atomized the tasks I was having the AI work on. I feel like it took me way fewer prompts to get what I was asking for by moving a bit more slowly through the code/task. I would also try to come up with a sort of build order for my classes/functions and to make sure that I was developing everything in the correct order. 
- In one or two sentences, describe how this project changed the way you think about AI generated code.
I feel like I had always appreciated the speed of AI generated code and yet I remained leery of the correctness of the code. In the past I was using it to generate "whole behaviors" by saying I need something to do or to look like x, y, z. Now I feel like I have some insight into a different way to work on code with AI that isn't so much typing out a huge task and hoping I get what I want in the end, but to break down the goal into set steps. It's much easier to control the outcome and to measure where things are going wrong or right by doing this.