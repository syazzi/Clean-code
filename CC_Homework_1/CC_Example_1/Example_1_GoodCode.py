def main():
    sentence = input("Please make a sentence: ")
    what_sentence = SentenceSpeechDescriber(sentence)
    

class SentenceSpeechDescriber:
    def __init__(self, sentence):
        self.sentence = sentence
        self.get_speech()

    def get_speech(self):
        if self.sentence[len(self.sentence) - 1] == "?":
            self.get_Question()
        elif self.sentence[len(self.sentence) - 1] == "!":
            self.get_Exclamation()
        elif self.sentence[len(self.sentence) - 1] == ".":
            self.get_Normal()
        else:
            self.get_Else()

    def get_Question(self):
        print("I am Question type of speech")

    def get_Exclamation(self):
        print("I am Angry or Excited type of speech")

    def get_Normal(self):
        print("I am Normal type of speech")

    def get_Else(self):
        print("I am Incomplete")

    
if __name__ == "__main__":
    main()