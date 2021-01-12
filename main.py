from chatterbot import ChatBot
"""
a basic example of an artificially intelligent calculator, or an AI calculator.
This is how the application works:

    It takes in inputs as text
    Translates them into mathematical notation
    Returns the answers in the numerical form

Use the following keywords for their associated operations:

    plus for addition
    minus for subtraction
    times for multiplication
    divided by for division


"""
# naming the Chatbot calculator
# using mathematical evaluation logic
# the calculator AI will not learn with user input


Bot = ChatBot(name='Calculator',
              read_only=True,
              logic_adapters=["chatterbot.logic.MathematicalEvaluation"],
              storage_adapter='chatterbot.storage.SQLStorageAdapter')

print('\033c')
print("Hello, I am a calculator. How may I help you?")
while True:
    user_input = input("me: ")

    if user_input.lower() == 'quit':
        print("Existing")
        break

    try:
        response = Bot.get_response(user_input)
        print("Calculator", response)

    except:
        print("Calculator: Please enter valid input.")
