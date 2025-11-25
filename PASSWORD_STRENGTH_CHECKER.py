#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Converted from Jupyter Notebook: notebook.ipynb
Conversion Date: 2025-11-25T18:47:30.352Z
"""

def check_password_strength(password):
    length = len(password)
    score = 0
    feedback = []
    diversity_count = 0
    
    special_chars = r"!@#$%^&*()_+-=[]{};':\"\\|,.<>/?`~"

    has_upper = any(c.isupper() for c in password)
    if has_upper:
        diversity_count += 1
        score += 1
    else:
        feedback.append("Uppercase letter (A-Z)")

    has_lower = any(c.islower() for c in password)
    if has_lower:
        diversity_count += 1
        score += 1
    else:
        feedback.append("Lowercase letter (a-z)")

    has_digit = any(c.isdigit() for c in password)
    if has_digit:
        diversity_count += 1
        score += 1
    else:
        feedback.append("Digit (0-9)")

    has_special = any(c in special_chars for c in password)
    if has_special:
        diversity_count += 1
        score += 1
    else:
        feedback.append("Special character (!@#$...)")

    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if length >= 16:
        score += 1
    
    if length < 8 or diversity_count < 2:
        strength = "Very Weak"
    elif length >= 8 and diversity_count < 3:
        strength = "Weak"
    elif length >= 8 and diversity_count >= 3:
        strength = "Moderate"
    elif length >= 12 and diversity_count == 4:
        strength = "Strong"
    elif length >= 16 and diversity_count == 4:
        strength = "Very Strong"
    else:
        strength = "Moderate"

    result = {
        "strength": strength,
        "score": score,
        "feedback": "Missing: " + ", ".join(feedback) if feedback else "Password meets all complexity requirements."
    }
    
    return result
p=input('enter ur password:')
print('password:',p)
r=check_password_strength(p)
print(r)