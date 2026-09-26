#analyzer.py

def analyze_password(password):
    score = 0
    suggestions = []

    rules = {
        "length": len(password) >= 8,
        "upper": any(ch.isupper() for ch in password),
        "lower": any(ch.islower() for ch in password),
        "digit": any(ch.isdigit() for ch in password),
        "special": any(ch in "@#$%&*!" for ch in password)
    }

    unique_chars = set(password)
    rule_names = ("length", "upper", "lower", "digit", "special")

    for rule in rule_names:
        if rules[rule]:
            score += 20

    if not rules["length"]:
        suggestions.append("Use at least 8 characters")
    if not rules["upper"]:
        suggestions.append("Add an uppercase letter")
    if not rules["lower"]:
        suggestions.append("Add a lowercase letter")
    if not rules["digit"]:
        suggestions.append("Add a number")
    if not rules["special"]:
        suggestions.append("Add a special character")

    if len(unique_chars) >= 10:
        score += 5

    score = min(score, 100)

    if score >= 80:
        risk = "Low Risk"
    elif score >= 50:
        risk = "Medium Risk"
    else:
        risk = "High Risk"

    return score, risk, suggestions
