messages = ["I just died", "I am so immature", "We need to talk"]
sent_messages = []

def send_messages(unsent_messages, sent_messages):
    while unsent_messages:
        current_message = unsent_messages.pop()
        print(current_message)
        sent_messages.append(current_message)

send_messages(messages[:], sent_messages)

print(messages)
print(sent_messages)