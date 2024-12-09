import os
from pydantic_ai import Agent
from pydantic import BaseModel, Field

class PromptResponse(BaseModel):
    prompt: str = Field(description="The new prompt to accomplish the task.")

def create_prompt(metaprompt: str = "", user_input: str = "") -> PromptResponse:
    if not metaprompt:
        metaprompt = get_metaprompt()
    if not user_input:
        user_input = get_user_input()
    prompt = metaprompt.format(user_input=user_input)
    agent = Agent(
        model="openai:gpt-4o-mini",
        result_type=PromptResponse,
    )
    return agent.run_sync(prompt)

def get_metaprompt() -> str:
    with open("metaprompt.txt", "r") as file:
        return file.read()


def create_user_input() -> str:
    with open("user_input_template.txt", "r") as file:
        contents = file.read()
    print("Create new user input.  Template example:")
    print(contents)
    print("-" * 80)
    print()
    purpose = input("Purpose: ")
    contents = []
    while True:
        try:
            line = input("")
        except EOFError:
            break
        contents.append(line)
    instructions = "\n".join(contents)
    sections = input("Sections: ")
    examples = input("Examples: ")
    variables = input("Variables: ")
    new_input = f"""
Purpose: {purpose}
Instructions: {instructions}
Sections: {sections}
Examples: {examples}
Variables: {variables}
"""
    with open("user_input.txt", "w") as file:
        file.write(new_input)
    return new_input


def get_user_input():
    if os.path.exists("user_input.txt"):
        with open("user_input.txt", "r") as file:
            return file.read()

    return create_user_input()

def main():
    response = create_prompt()
    print(response.data.prompt)

if __name__ == "__main__":
    main()
