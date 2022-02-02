from asyncio.windows_events import NULL


def SentenceSpeechDescriber():
    sentence = input("Please make a sentence: ")
    speech = NULL
    if sentence[len(sentence) - 1] == "?":
        speech = "Question Speech"
    elif sentence[len(sentence) - 1] == "!":
        speech = "Angry Speech/ Hypeed Speech"
    elif sentence[len(sentence) - 1] == ".":
        speech = "Normal Speech"
    else:
        speech = "not finished"
    print("I am {} type of speech.".format(speech))

SentenceSpeechDescriber()

