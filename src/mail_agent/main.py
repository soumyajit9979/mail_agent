#!/usr/bin/env python
# src/mail_agent/main.py
import sys
import warnings
from mail_agent.crew import MailAgent

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

def run():
    """
    Run the crew.
    """
    inputs = {
        'input': input("please let me know what mail you want to draft and to whomeasdasd: ")
    }

    MailAgent().crew().kickoff(inputs=inputs)


if __name__ == "__main__":
    run()