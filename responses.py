import random
import time
from DB.jokes.jokes_db import jokes
from DB.quotes.quotes_db import quotes

joke_list = jokes
quote_list = quotes

def handle_response(message) -> str:
    #? Lowercases message to be more readable by the bot
    p_message = message.lower()

    if p_message == 'hello':
        return "Hey there!"
    
    if p_message == "roll":
        return str(random.randint(1, 6))
    
    if p_message == "!help":
        return """
            ```
Hello, I am the Citadel channel discord bot. I have few things I can do, but here they are.

1.) Sending "roll" in the chat input will give you a random dice roll (1-6 if you didn't know).

2.) Try sending "hello" in the chat input.

3.) Ask me "How was your day?".

4.) If your day is "bad", "not good", "could've been better", or just "ehh", I will try to cheer you up.

5.) If you day was "good", "great" or "awesome" I am liable to respond

6.) If you add a "?" in front of any of these commands, I will DM you personally!

7.) Try "joke" or "quote"

There will be more functionality soon, but Jon's ass is definitely taking his time.
            ```
            """
    
    if p_message == "how was your day" or p_message == "how was your day?" or p_message == "how is your day" or p_message == "how is your day?":
        return "My day was pretty great being a bot an all! How about yours?"
    
    if p_message == "great" or p_message == "good" or p_message == "waesome":
        return "I'm happy to hear that, I hope it keeps going good"
    
    if p_message == "bad" or p_message == "ehh" or p_message == "eh" or p_message == "could've been better" or p_message == "not good":
        return "I'm sorry, I hope it gets better! And I know it will."
    
    if p_message == "tell me a joke" or p_message == "joke":
        joke = random.choice(joke_list)
        return f"{joke['setup']}....   {joke['punchline']}"
    
    if p_message == "give me a good quote" or p_message == "quote":
        quote = random.choice(quote_list)
        return f"{quote['text']}   ---{quote['author']}"
    
    return "Are you talking to me?"