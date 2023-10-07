#install packages
# pip install "chatterbot==1.0.0"
# pip install pytz
#      OR
# pip install -r requirements.txt
import collections.abc
collections.Hashable = collections.abc.Hashable
# import required packages
from chatterbot import ChatBot
from chatterbot.conversation import Statement
from chatterbot.trainers import ChatterBotCorpusTrainer

# create ChatBot
chatBot = ChatBot('ChatBot')

# create ChatBot trainer
trainer = ChatterBotCorpusTrainer(chatBot)

# Train ChatBot with English language corpu
# you can train with different language
# or with your custom .yam file
trainer.train("chatterbot.corpus.english")

# keep communicating with ChatBot
while True:
    query = input(">>>")
    print(chatBot.get_response(Statement(text=query,search_text=query)))