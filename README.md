# PASSWORD-STRENGTH-CHECKER

#OVERVIEW:
This project gives you a solid password strength checker built into one Python function - no extra tools needed. It works by checking how long the password is while also looking at what kinds of characters are used. Instead of relying on outside packages, it runs on its own. The score depends partly on length, partly on variety like numbers or symbols mixed in.

#FEATURES:
Standalone: Works without extra tools or add-ons.
Pure Python: relies solely on string tools like isupper or isdigit, also uses any(); nothing extra added.
Tiered setup splits passwords into five groups: Very Weak, Weak, Moderate, Strong and Very Strong.
Gets specific - tells you exactly what’s missing, like capital letters or symbols, so your password gets tougher. Shows gaps clearly instead of just saying it’s weak. Helps fix flaws step by step without confusion. Makes building strong passwords way easier with clear hints.
Grading setup: gives a number score depending on how long it is plus how varied the content seems.

#TECHNOLOGIES/TOOLS USED:
Language: Python
Development: Github
Method used: String manipulation, Functions, Conditional statements

#INSTALLATION AND SETUP:
Since this project consists of a single function, installation involves cloning the repository and importing the function into your Python environment.
Clone the Repository:
Open your terminal or command prompt and run:
git clone https://github.com/aarna25mim10050-debug/Password-Strength-Checker.git
cd Password-Strength-Checker

#INSTRUCTION FOR TESTING:
A comprehensive testing script is included to validate the scoring and feedback for various password combinations.
1. Run Tests:
To execute the test suite (assuming you are using a standard testing framework like pytest or a simple test file named test_checker.py):
->Example if using unittest or a simple execution script
python test_checker.py
pip install pytest
pytest
2. Expected Test Cases
Ensure the following common scenarios yield the correct results:
short ->	5	Very Weak
mypassword ->	10 Weak
MyPass123 ->	9	Moderate
SecureP@ss12! -> 13 Strong
ExtraLongSecurePassword42@#$ ->	28 Very Strong

#SCREENSHOTS OF OUTPUTS:
1.
<img width="1006" height="58" alt="image" src="https://github.com/user-attachments/assets/149761a6-acc3-4ec9-b5bd-f1a20d729da3" />
2.
<img width="816" height="60" alt="image" src="https://github.com/user-attachments/assets/0e98904f-9f5f-446f-a0ed-1635429aaa57" />




