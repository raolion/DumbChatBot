import random
import re

class ChatBot:
    def __init__(self):
        self.words = ['hello', 'yes', 'no', 'be', 'i', 'you', 'good', 'bad', 'me', 'love', 'hate']

    def get(self, message):
        msgsplit = re.findall(r'\b\w+\b', message.lower())
        self.words.extend(msgsplit)

    def generate_answer(self):
        response = ''
        answer_length = random.randint(1, 5)
        response = ' '.join(random.sample(self.words, answer_length))
        if not response.endswith(('!', '.', '?', ')', '(')):
            response += random.choice(('!', '.', '?', ')', '('))
        response = response.capitalize()
        print(f'🤖: {response}')

    def show_memory(self):
        print(self.words)

    def run(self):
        print("enter 'memory' to display a list of words, '0' to turn off the bot")
        while True:
            message = str(input("👨: "))
            if message.lower() == 'memory':
                self.show_memory()
            elif message == '0':
                break
            else:
                self.get(message)
                self.generate_answer()


bot = ChatBot()
bot.run()