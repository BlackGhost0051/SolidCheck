# Solid Check

Author: `Black Ghost`

**Solid Check** is a web-based tool built with Flask that checks your code for adherence to the SOLID principles.

How It Works?


1. Sends a formatted prompt including the SOLID explanation and user code to Gemini API.
2. Parses the AI response.
3. Return a analysis and refactored version of the code.



SOLID:
- S – **Single Responsibility Principle**: A class should have one and only one reason to change.
- O – **Open/Closed Principle**: Software entities should be open for extension but closed for modification.
- L – **Liskov Substitution Principle**: Subtypes must be substitutable for their base types without altering correctness.
- I – **Interface Segregation Principle**: Clients should not be forced to depend on interfaces they do not use.
- D – **Dependency Inversion Principle**: High-level modules should not depend on low-level modules; both should depend on abstractions.

## Images

|![](https://github.com/BlackGhost0051/SolidCheck/blob/master/app/img/1.png)|![](https://github.com/BlackGhost0051/SolidCheck/blob/master/app/img/2.png)| ![](https://github.com/BlackGhost0051/SolidCheck/blob/master/app/img/3.png) |
|:-:|:-:|:---------------------------------------------------------------------------:|
|1|2|                                      3                                      |



## Getting Started

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YourUsername/SolidCheck.git
   cd SolidCheck
    ```

2. **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3. Set up Environment Variables

   Create a .env file in the root directory:
   ```bash
   touch .env
   ```
   
   Add your Gemini API key:
   ```bash
   GEMINI_API_KEY=your_gemini_api_key_here
   ```

4. **Run the application**:
    ```bash
    python run.py
    ```
   Access it via `http://127.0.0.1:5000`.

## Project Structure

```
├── app
│   ├── __init__.py
│   ├── Managers
│   │   ├── AiManager.py
│   ├── routes.py
│   ├── static
│   │   ├── css
│   │   │   └── style.css
│   │   └── js
│   │       └── script.js
│   └── templates
│       └── index.html
├── config.py
├── README.md
├── requirements.txt
└── run.py
```

## Configuration

`Config` Class

Contains sensitive configuration such as:

```python
class Config:
    DEBUG = True
```