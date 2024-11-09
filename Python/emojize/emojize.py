import emoji

emo = input("Input: ")
emo = emoji.emojize(emo, language = 'alias')
emo = emoji.emojize(emo, language = 'es')
print(f"Output: {emo}")

