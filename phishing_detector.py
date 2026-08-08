def check_email(email):
    suspicious_words = [
        "urgent",
        "verify your account",
        "click here",
        "password",
        "winner",
        "bank account",
        "confirm your account"
    ]

    email_lower = email.lower()

    found_words = []

    for word in suspicious_words:
        if word in email_lower:
            found_words.append(word)

    if found_words:
        print("\n⚠️ Suspicious/Phishing Email Detected!")
        print("Suspicious words:", found_words)
    else:
        print("\n✅ Email appears safe.")


print("===== Phishing Email Detector =====")

email = input("Enter email text: ")

check_email(email)
