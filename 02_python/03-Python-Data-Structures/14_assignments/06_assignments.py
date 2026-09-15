words = ["apple", "banana", "kiwi", "cherry", "mango"]

word_info={}

for i in words:
    word_info.update({
        i:len(i)
    })


print(f"values of dict {word_info.items()}")