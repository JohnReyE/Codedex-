sent_message = "Hey there! This is a secret message."

with open("secret_message.txt", "w") as file:
    file.write(sent_message)

with open("secret_message.txt", "r+") as file:
    origainal_message = file.read()

    file.seek(0)

    unsent_message = "This message has been unsent."

    file.truncate(len(unsent_message))
    file.write(unsent_message)

print(f"Original message: {origainal_message}")
print(f"Unsent message: {unsent_message}")
