# logic.py
import os
import json
import google.generativeai as genai
from dotenv import load_dotenv

# Load API key
load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

def get_roast_and_fix(user_code, persona):
    """
    Sends code to Gemini and returns a JSON object.
    """
    
    
    generation_config = {
        "temperature": 0.7,
        "response_mime_type": "application/json",
    }
    # Selecting the model
    model = genai.GenerativeModel(
        # model_name="gemini-1.5-flash",
        model_name="gemini-2.5-flash",
        generation_config=generation_config,
    )

    # The Prompt
    prompt = f"""
    You are a code reviewer with this persona: {persona}.
    
    Analyze the following code:
    {user_code}
    
    Your goal is to provide a "Roast" and a "Fix".

    CRITICAL INSTRUCTION:
    If you find a "Fatal" error (e.g., Infinite Loop, Divide by Zero, Memory Leak, Exposed API Key, `rm -rf`), 
    mark "fatal": true in that specific critique object. Otherwise set it to false.
    
    STRICT RULES FOR THE ROAST:
    1. It must be a SINGLE SENTENCE with atmost 5-6 words.
    2. If it is fatal error provide mean, hard hitting roast.
    2. It must be a witty one-liner, a pun, or a dry insult.
    3. Refer to specific variables or logic in the code to make it sting.
    4. Provide code line specific puns in case of multiple problems.
    5. Do not offer help in the roast. Save that for the fix.

    
    Identify issues and categorize them STRICTLY into these 3 types:
    
    1. "fatal" (Red): RUNTIME CRASHES. Logic that allows the code to start but causes it to crash or freeze later.
       - Examples: Infinite loops, Divide by Zero, Index Out of Bounds, Recursion Depth Exceeded.
       
    2. "warning" (Orange): COMPILER/SYNTAX ERRORS. Issues that prevent the code from running at all.
       - Examples: SyntaxError, IndentationError, NameError (undefined variables), Import errors.
       
    3. "cosmetic" (Green): Style issues.
       - Examples: Bad variable names (x, y), missing comments, ugly formatting, unused imports (that don't crash).

    Return a JSON object with a SINGLE key "critiques" which is a list of objects.
    Each object must follow this schema:
    {{
        
        "line" : "The line number (e.g., 5) or 'General'",
        "category": "cosmetic" OR "warning" OR "fatal",
        "roast": "The single-line witty roast",
        "fix_explanation": "Brief explanation of the error",
        "fixed_code": "The corrected code snippet"
        
    }}
    """
    #returning response to UI
    try:
        response = model.generate_content(prompt)
        return json.loads(response.text)
    except Exception as e:
        return {
            "roast": "404: Humor not found. (API Error)",
            "fix_explanation": f"Error: {str(e)}",
            "fixed_code": ""
        }