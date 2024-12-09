# LLM Prompt Creator

This project uses the Pydantic library to define models and implement an AI-based system for generating task-specific prompts. It integrates a structured workflow for creating prompts based on user input and a customizable metaprompt template.

## Features

- Dynamically generates AI prompts based on user input.
- Supports structured prompt creation with pre-defined templates.
- Uses Pydantic for type-safe model definitions.
- Includes an interactive user input mechanism.

## Prerequisites

Ensure the following are installed on your system:

- **Python 3.12+**
- **Git**
- **Virtualenv** (optional but recommended)

## Installation

1. Clone the repository:
   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. Set up a virtual environment:
   - **MacOS/Linux**:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```
   - **Windows**:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Ensure the `metaprompt.txt` file exists in the root directory. This file contains the template for the metaprompt.
2. Optionally, prepare a `user_input.txt` file with a sample format for user inputs.
3. Run the program:
   ```bash
   python main.py
   ```

### User Input Creation

If no `user_input.txt` file exists, the program will prompt you to create one interactively:
- Provide a purpose.
- Input instructions, line by line, ending with `Ctrl+D` (or `Ctrl+Z` on Windows).
- Specify additional sections, examples, and variables.

The program saves the input to `user_input.txt` for future use.

## Environment Variables

- **Model Specification**: The agent uses `openai:gpt-4o-mini` by default. This can be configured in the code.
- Ensure API keys and other required credentials are configured if using external services. (Eg, OPENAI_API_KEY)

## License

This project is licensed under the MIT License.
