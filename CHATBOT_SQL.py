
from chatterbot import ChatBot
import logging

logging.basicConfig(level=logging.INFO)


bot = ChatBot(
    
    'Base de datos_Calculadora_Noe',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri=None,
    logic_adapters=[
        'chatterbot.logic.BestMatch',
        'chatterbot.logic.MathematicalEvaluation',
        'chatterbot.logic.TimeLogicAdapter'
        
        
    ]
)
while True:
  try:
    bot_input = bot.get_response(input())
    print(bot_input)

  except(KeyboardInterrupt, EOFError, SystemExit):
    break


# OPCIONES PARA PREGUNTAR:

#  What time is it?
#  7 * 7
#  6 + 6
#  5 - 2
# What is 7 plus 7?
      #etc etc etc

