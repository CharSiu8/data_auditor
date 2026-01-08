import os
import json
from openai import OpenAI
from dotenv import load_dotenv

# Load the API key from your .env file
load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_audit_results(json_path):
    # 1. Open the JSON report the 'reporter.py' created
    try:
        with open(json_path, 'r') as f:
            audit_data = json.load(f)
    except FileNotFoundError:
        return "Error: Could not find the audit_summary.json file."

    # 2. Create the prompt for the AI
    prompt = f"""
    You are a senior data scientist doing inital analysis on uploaded CSV files. 
    NEVER MAKE UP INFORMATION. you were created to; 
    1. Perform statistical analysis (Null detection, Outlier analysis).
    2. use deterministic Python logic for 100% mathematical accuracy, 
    using AI only to *interpret* the findings and suggest remediation plans.
    YOU MUST NOT FABRICATE ANTYHING. ONLY USE THE PROVIDED JSON DATA.
    If the data is not in the JSON, say it is missing
    {json.dumps(audit_data, indent=2)}

    BASED EXCLUSIVELY ON THE AUDIT DATA PROVIDED ABOVE, Provide a 3-bullet point summary :
    1. The biggest data quality issue found (mention all specific row numbers for each quality issue).
    2. Which columns are ready for use (zero nulls, zero inconsistencies).
    3. Which columns have inconsistencies, identify every row with issues ().
    4. Suggest what Pandas datatype inconsistent columns should be converted to. 
    """
    # 3. Call OpenAI and return the response
    response = client.chat.completions.create(
        model='gpt-4o-mini',
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content
