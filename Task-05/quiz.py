import aiohttp
import asyncio
import random
import time

fetching_url = "https://opentdb.com/api.php?amount=5&type=multiple"
async def get_questions():
    async with aiohttp.ClientSession() as d:
        async with d.get(fetching_url) as resp:
            data = await resp.json()
            return data["results"]
async def play_quiz():
    score = 0
    questions = await get_questions()

    for i, q in enumerate(questions, start=1):

        print(f"nQ{i} : {q['question']}")
        options = q["incorrect_answers"] + [q["correct_answer"]]
        random.shuffle(options)
        for i, opt in enumerate(options, 1):
            print(f"  {i}. {opt}")
        start = time.time()
        answer = int(input("Your choice (1-4): "))
        elapsed = time.time() - start
        if elapsed > 15:
            print("No points because time exceded 15 seconds")
            continue
        if options[answer - 1] == q["correct_answer"]:
            print("Correct")
            score += 1
        else:
            print("Wrong")

    print(f"Your score: {score}/{len(questions)}")

asyncio.run(play_quiz())
