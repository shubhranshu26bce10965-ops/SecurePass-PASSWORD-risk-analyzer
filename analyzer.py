# analyzer.py

def analyze_password(password):
    score = 0
    suggestions = []

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    special_chars = "@#$%&*!"

    for ch in password:
        if ch.isupper():
            has_upper = True
        elif ch.islower():
            has_lower = True
        elif ch.isdigit():
            has_digit = True
        elif ch in special_chars:
            has_special = True

    if len(password) >= 8:
        score += 20
    else:
        suggestions.append("Use at least 8 characters")

    if has_upper:
        score += 20
    else:
        suggestions.append("Add an uppercase letter")

    if has_lower:
        score += 20
    else:
        suggestions.append("Add a lowercase letter")

    if has_digit:
        score += 20
    else:
        suggestions.append("Add a number")

    if has_special:
        score += 20
    else:
        suggestions.append("Add a special character")

    if score >= 80:
        risk = "Low Risk"
    elif score >= 50:
        risk = "Medium Risk"
    else:
        risk = "High Risk"

    return score, risk, suggestions
