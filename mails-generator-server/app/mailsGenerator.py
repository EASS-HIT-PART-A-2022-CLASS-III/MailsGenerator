import openai
import asyncio

from prompts import *

from models import *

key = "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"

openai.api_key = key
modelCode = "gpt-3.5-turbo"


async def generateMailFromChatgpt(prompt):
    print("generator , generateMailFromChatgpt start", flush=True)

    try:
        completion = openai.ChatCompletion.create(
            model=modelCode, messages=[{"role": "user", "content": prompt}]
        )

        print("generator , generateMailFromChatgpt end", flush=True)
        # print(completion.choices[0].message.content)

        return completion.choices[0].message.content

    except Exception as e:
        print("An error occurred in generateMailFromChatgpt:", str(e), flush=True)

        return None


# try to generate the mail from chatgpt a few times, if there is some problem with openAI server
async def tryGeneratingMailFromChatgpt(prompt):
    for i in range(3):
        result = await generateMailFromChatgpt(prompt)

        if result is not None:
            return result

    return None


# calling the chatgpt in async, because the newer models don't have yet one http call for many prompts,
# need to send a request for each prompt
async def generateAllMails(
    companyName, businessAbout, clientsDream, clientsAvoid, clientsProblem
):
    prompts = getAllPrompts(
        companyName,
        businessAbout,
        clientsDream,
        clientsAvoid,
        clientsProblem,
    )

    asyncTasks = []

    for prompt in prompts:
        asyncTasks.append(asyncio.create_task(tryGeneratingMailFromChatgpt(prompt)))

    asyncResults = await asyncio.gather(*asyncTasks)
    # print("++++++++++++++")
    # print(asyncResults, flush=True)

    final_result = [result for result in asyncResults if result is not None]

    print("generator , generateAllMails end", flush=True)

    return final_result
