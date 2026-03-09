# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

Answer 1: I expected my attempts to start reducing after my first wrong try but it did not reduce to 7 attempts until after my second wrong try.

Answer 2: It kept telling me to go lower even when I had input the lowest (1) and go higher when I had input the highest (100)

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Answer: Copilot and ChatGPT
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
Answer: Refactor check_guess from app.py to logic_utils.py and handle type mismatches (int vs string).

How I verified: Ran pytesrt; all tests passed

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
Answer: Return only the outcome string (e.g., "Win") instead of (outcome, message) tuple.

How I verified: Original tests failed; corrected to return tuple with emoji
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
Answer: I verified that each bug was fixed by running tests using pytest and also manually playing the game in Streamlit. 

- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
Answer: I ran the test_check_guess_win test in tests/test_game_logic.py, which checked that a guess equal to the secret number returned the outcome "Win" and the correct message "🎉 Correct!". This test passed after the fix

- Did AI help you design or understand any tests? How?
Answer: Yes. AI suggested adding pytest cases for type-mismatch scenarios (int guess vs string secret) and generating tests that verified secret numbers change on new games.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
