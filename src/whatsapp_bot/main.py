#!/usr/bin/env python
import sys
from crew import WhatsappCrewCrew
from dotenv import load_dotenv
import os

# Load environment variables from .env file
#load_dotenv()

# Set the OpenAI API key
#os.environ["OPENAI_API_KEY"] = ""

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

# Create a test file with the messages from the last 24 hours
# and run the crew with it.
messages = 'AI LLMs'
sent_at = '2024-11-07'
sent_by = 'John Doe'
contact_name = 'Jane Doe'
contact_number = 'Jane Doe'
category = 'work'

def run():
    """
    Run the crew.
    """
    inputs = {
        'messages': messages
    }
    result = WhatsappCrewCrew().crew().kickoff(inputs=inputs)
    return result


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        "messages": messages
    }
    try:
        WhatsappCrewCrew().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")

def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        WhatsappCrewCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")

def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "messages": messages
    }
    try:
        WhatsappCrewCrew().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


if __name__ == "__main__":
    run()
