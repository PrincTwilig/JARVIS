def isCommand(message, *commands):
    message = message.lower()
    message = message.removeprefix("the").strip()
    jarvis_words = [
        "jarvis",
        "джарвіс",
        "гарвіс",
        "garvis",
        "чарльз",
        "сервіс",
    ]

    for word in jarvis_words:
        if message.startswith(word):
            message = message.removeprefix(word).strip()
            break
    
    successes = 0
    for command in commands:
        for word in command:
            if message.startswith(word):
                successes += 1
                message = message.removeprefix(word).strip()
                break

    if successes == len(commands):
        return message, True
    return message, False