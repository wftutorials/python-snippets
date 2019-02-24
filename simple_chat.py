can_talk = True
responses = {
    "hello,hi,sup": "Hey you. Whats up?",
    "bye, goodbye, later, ltr": "Alrite, Later.",
    "name, title": "Simple Chat Bot",
    "age": "Im new",
    "exit,close": "Closing program"
}


def check_matches(chat_key, user_input):
    matches = chat_key.split(",")
    question_array = user_input.split(" ")
    counter = 0
    for match in matches:
        for word in question_array:
            if set(word.strip().lower()) == set(match.strip().lower()):
                counter = counter + 1
    return counter


def get_response(question):
    matched_key = ""
    for key in responses:
        max_matches = 0
        matched_count = check_matches(key, question)
        if matched_count > max_matches:
            matched_key = key
            max_matches = matched_count
    return matched_key


def talk():
    global responses
    response = input("You:")
    res = get_response(response)
    if not res:
        print("I don't understand")
    else:
        print(responses[res])


while can_talk:
    talk()

