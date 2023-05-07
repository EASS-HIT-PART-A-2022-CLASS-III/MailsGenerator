import openai
import asyncio
from prompts import *

key = "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"

openai.api_key = key
modelCode = "gpt-3.5-turbo"


async def generateMailFromChatgpt(prompt):
    completion = openai.ChatCompletion.create(
        model=modelCode,
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    # print(completion.choices[0].message.content)

    return completion.choices[0].message.content


# calling the chatgpt in async, because the newer models don't have yet one http call for many prompts,
# need to send a request for each prompt
async def generateAllMails(companyName, businessAbout, clientsDream, clientsAvoid, clientsProblem, influencer):

    prompts = getAllPrompts(companyName, businessAbout,
                            clientsDream, clientsAvoid, clientsProblem, influencer)

    asyncTasks = []

    for prompt in prompts:
        asyncTasks.append(asyncio.create_task(generateMailFromChatgpt(prompt)))

    asyncResults = await asyncio.gather(*asyncTasks)
    print("++++++++++++++")
    print(asyncResults)

    final_result = [result for result in asyncResults]

    return final_result
