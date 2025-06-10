import os
import requests
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')
GEMINI_ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={GEMINI_API_KEY}"


class AiManager:
    @staticmethod
    def verify_solid(code: str) -> str:
        message = f"""
        You are an expert software engineer. I’d like you to review and refactor the following code based on the SOLID principles.

        Your tasks are:
        
        1. Identify and explain any violations of the SOLID principles in the code.
        2. Refactor the code to comply with each violated principle.
        3. Provide a brief explanation for each change and how it improves the design.



        SOLID Principles Reminder:

        S – Single Responsibility Principle**: A class should have one and only one reason to change.
        O – Open/Closed Principle**: Software entities should be open for extension but closed for modification.
        L – Liskov Substitution Principle**: Subtypes must be substitutable for their base types without altering correctness.
        I – Interface Segregation Principle**: Clients should not be forced to depend on interfaces they do not use.
        D – Dependency Inversion Principle**: High-level modules should not depend on low-level modules; both should depend on abstractions.

        Please be thorough and constructive in your analysis.

        Code to review:
        {code}
        """

        headers = {
            "Content-Type": "application/json",
        }

        payload = {
            "contents": [
                {
                    "parts": [
                        {"text": message}
                    ]
                }
            ]
        }

        response = requests.post(GEMINI_ENDPOINT, headers=headers, json=payload)

        if response.status_code != 200:
            print(f"Error: {response.status_code} - {response.text}")
            return "Error communicating with Gemini API."

        data = response.json()


        try:
            return data["candidates"][0]["content"]["parts"][0]["text"]
        except (KeyError, IndexError):
            return "Unexpected response format from Gemini API."