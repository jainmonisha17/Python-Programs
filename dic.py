message = input("Type something here >")
words = message.split(' ')
emojis = {
    ":)" : "😊",
    ":(" : "😞",
    ":D" : "😃",
    ";)" : "😉"
}

output = ""
for word in words:
    output += emojis.get(word, word) + ""
print(output)