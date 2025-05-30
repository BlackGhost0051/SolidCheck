# 🧠 Solid Check

**Solid Check** is a web-based tool built with Flask that checks your code for adherence to the SOLID principles.


## 🚀 Getting Started

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

## 📁 Project Structure

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

