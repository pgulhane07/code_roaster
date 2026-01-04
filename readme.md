# The Code Roast 

Your code doesn't just need fixing—it needs an exorcism.

The Code Roast is a creative, AI-powered application that turns the mundane task of code review into an entertaining (and slightly painful) experience. Instead of dry error messages, it uses a Generative AI "Persona" to roast your code quality before helping you fix it.

# 🚀 Key Features
Persona-Driven Reviews: Choose your judge—from a Medieval Peasant confused by technology to a Gen-Z TikToker who hates your "boomer syntax."

Visual Triage System: Errors are automatically sorted by severity:

**🔴 Fatal:** Runtime crashes (Infinite loops, Divide by Zero).

**🟠 Blocker:** Syntax errors that prevent the code from running.

**🟢 Cosmetic:** Ugly styling, bad variable names, or missing comments.

I**nteractive Visuals:** Fatal errors trigger a visual "Explosion" on screen to emphasize the catastrophe.

Smart Fixes: Beyond the jokes, the AI provides actual corrected code snippets and technical explanations.

# 📸 How It Works
1. The Setup
Choose a persona and paste your code snippet. The interface is clean and simple.

![Code window](https://file%2B.vscode-resource.vscode-cdn.net/Users/piyushgulhane/Documents/projects/relatecx_task/demo%20images/code%20box.png?version%3D1767567203379)



2. The Critical Failure (Interactive Twist)
If the AI detects a code-breaking runtime error (like while(true) without a break), the application reacts dramatically before showing the results.

![Crtical Failure Explosion](https://file%2B.vscode-resource.vscode-cdn.net/Users/piyushgulhane/Documents/projects/relatecx_task/demo%20images/explosion.png?version%3D1767567245115)


3. The Verdict (The Dashboard)
The results are displayed in a prioritized list.

Top: Critical/Fatal errors.

Middle: Syntax Warnings.

Bottom: Cosmetic Roasts.

Each card contains a witty one-liner (the roast) and an expandable "Fix" section with the technical solution.

![Code Roast and Fix](https://file%2B.vscode-resource.vscode-cdn.net/Users/piyushgulhane/Documents/projects/relatecx_task/demo%20images/roast%20and%20fix.png?version%3D1767567396895)



**🛠️ Tech Stack**
This project was built to demonstrate lightweight AI integration and creative prompt engineering.

Language: Python 3.10+

Frontend: Streamlit (for rapid UI development)

AI Logic: Google Gemini API (Model: gemini-1.5-flash-001)

Data Handling: JSON parsing for structured AI outputs.

**Installation & Setup**
Follow these steps to run the application locally.

1. Clone the repository

Bash

git clone https://github.com/pgulhane07/code_roaster
cd code_roaster


2. Create a Virtual Environment (Optional but recommended)

Bash

python -m venv venv
**Windows**
venv\Scripts\activate
**Mac/Linux**
source venv/bin/activate


3. Install Dependencies

Bash

pip install -r requirements.txt
(Ensure your requirements.txt contains: streamlit, google-generativeai, python-dotenv)

4. Set up your API Key Create a file named .env in the root folder and add your Google Gemini API key:

Plaintext

GEMINI_API_KEY=your_actual_api_key_here
(You can get a free key from Google AI Studio)

5. Run the App

Bash

streamlit run app.py


🧠 AI Implementation Details
To ensure the AI is "Smart" and not just an echo bot, I implemented System Prompt Engineering with strict constraints:

Structured Output: The AI is forced to return valid JSON, categorizing errors into fatal, warning, or cosmetic automatically.

Context Awareness: The prompt explicitly instructs the model to quote specific variable names and logic from the user's code in its "Roast" to prove it actually read the input.

Visual Triggers: The application logic parses the JSON to detect fatal: true flags, which triggers the frontend explosion animation dynamically.