import discord
import os
import platform
from discord.ext import commands

bot = commands.Bot(command_prefix='.', self_bot=True) # Bot Configuration / Settings.

# Functions

def wipeConsole(): # Wipes the console Screen for a More Appealing Output.
    if platform.system() == "Windows":
        os.system('cls')  # Clear console for Windows
    else:
        os.system('clear')  # Clear console for Unix/Linux/Mac

def printRed(text):  # ANSI escape code for colored text
    RED = "\033[31m"  # Escape code for red text
    RESET = "\033[0m"  # Escape code to reset to default color
    print(f"{RED}{text}{RESET}")  # Print the text in red and reset color

def centerAText(text): # Function to Center Ascii Art.
    console_width = os.get_terminal_size().columns
    lines = text.splitlines()
    centered_lines = []
    
    for line in lines:
        line_length = len(line)
        padding = (console_width - line_length) // 2
        centered_line = ' ' * padding + line
        centered_lines.append(centered_line)
    centered_text = '\n'.join(centered_lines)
    
    return centered_text

def centerText(text): # Function to Center ANY text.
    console_width = os.get_terminal_size().columns    
    text_length = len(text)    
    padding = (console_width - text_length) // 2     # Calculate the padding needed on each side
    centered_text = ' ' * padding + text    
    return centered_text


# Start Up / Insert Token
wipeConsole()
printRed(centerText("https://redsmods.com"))
printRed(centerText("Guide Made with love by Red ♥"))
printRed(centerText("Please enter your Discord Token: "))
token = input().strip()
printRed(centerText(f"Token Submitted {token}"))

# Events

@bot.event # bot event that is called on Successful Token Login.
async def on_ready():
    landingLogo = """         +++$X;                                               :;+;++            
                             X&$&&&X                                              x&&&&&x           
  :Xxx xX++  xxxxx;     x+xxX$&&&&&X    x+xx+xxxxxxx +++XXx     +xx++++      ++;;x$&&&&&$ ;;;;++;   
  x&&$$&&$$&$&&&&&$X+ x$&&&&&&&&&&&X    x&&&&&&&&&&&&&&&&&&&$ $&&&&&&&&X+. ;X&&&&&&&&&&&$xX&&&&&&+  
  x&&&&$XX&&&&&&&&&&$$$&&&&&&&&&&&&X    X&&&&&X &&&&&$x$&&&&&&&&&&&&&&&&&X$X&&&&&&&&&&&&&$&&&&&&&   
  x&&&$   X&&&&&&&&&&&&&&&&&&&&&&&&X    X&&&&&x X&&&&X X&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&$  
  x&&&X   ;$&&&&&&&&& &&&&&&&&&&&&&X    x&&&&&+ x&&&&x +&&&&$&&&&&&&&&&&&X$$&&&&&&&&&&&&&$&&&&&&&&  
  x&&&X    ;X$&&&&&$Xx XX$&&&$$$&&&x    +$&&&$; x&&&&X x&&&&& $&$&&&&$$x+: ;X$&&&&$$$&&$$$&&&&&&$x  
  ;xxX+       +;x++;     ++xx+  xXx      ;Xxx+  +x+xx  +$$$&&   ;xxx+;:       x+x+;  +x+  +xx++x    """
    wipeConsole()
    printRed(centerAText(landingLogo))
    printRed(centerText("__________________________________________________________________"))
    printRed(centerText("Commands"))
    printRed(centerText("Prefix: ."))
    printRed(centerText(".ping"))
    printRed(centerText(".hi"))

@bot.event # bot event that is called whenever the bot receives a message.
async def on_message(message):
    printRed(centerText("Message Received!"))

@bot.event # bot event that is called whenever the bot Reconnects to discord.
async def on_reconnect():
    printRed(centerText(f"{bot.user.name} has Reconnected to Discord."))

@bot.event # bot event that is called whenever the bot disconnects from discord.
async def on_disconnect():
    printRed(centerText(f"{bot.user.name} has lost Connection to Discord."))

# Commands

@bot.command() # Set ping Command.
async def ping(ctx):
    latency = round(bot.latency * 1000)
    await ctx.message.delete() # Delete the Command Message.
    await ctx.send(f'Response: Pong\nLatency: {latency} ms') # send Message

@bot.command()
async def hi(ctx):
    await ctx.send(f'Hello, {ctx.author.name}! How can I assist you today?') # ctx.author.name gets the name of the message author.

# redEmbed / Send Embeds

@bot.command()
async def embed(ctx, embedTitle, embedDescription, embedURL, embedHexColorCode, hidden, embedImage):
    # Prepare the data to send
    data = {
        'embedTitle': embedTitle,
        'embedDescription': embedDescription,
        'embedURL': embedURL,
        'embedHexColorCode': embedHexColorCode,
        'hidden': hidden,  # Include the hidden parameter
        'embedImage': embedImage
            }
                        
            # Send a POST request to the PHP backend
            response = requests.post('https://redsmods.com/api/redEmbed.php', data=data)
                        
            # Parse the JSON response
            result = response.json()
                        
            if 'url' in result:
                await ctx.send(f'Here is your embed link: {result["url"]}')
            else:
                await ctx.send(f'Error: {result["error"]}')

@bot.command()
async def sendEmbed(ctx):
    redEmbed = "GENERATED_REDEMBED_LINK_HERE" # Embed Link To Display

    await ctx.message.delete() # Deletes the Message that Executes the Command
    await ctx.send(redEmbed) # Send Embed

bot.run(token) # Run the Token / Start the Bot.

