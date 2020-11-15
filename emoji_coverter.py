# lets do this
# music on
# earphone pluged
# glasses on
# let's go
 # brrrrrrrrrrrrrrrrrrr

print("Emoji conveter = 0.1")
print("also known as a worst conveter")
'''
upgrade needed:
                add more emojis
                customize a range of times you can use emoji in one sentence mostly it is used ad the last
                make a fully usable program which can run whil typing like in discord or facebook chat
                others I guess I will think while making it
'''
emojis = {
    ":)"      : "😄",
    ":("      : "😢",
    "lol"     : "🤣",
    "money"   : "🤑",
    "whew!"   : "😅",
    "love it" : "😍",
    "hmmm"    : "🤔",
    "boring"  : "😪",
    "bored"   : "😴",
    "iq"      : "🤯",
    "oh"      : "😯",
    "piss"    : "😤",
    "ok"      : "👌"

}
print("-------------Welcome to emoji converter-----------------")
print('emoji convertor version: 0.1')
print('Since it is the first version it is the worst version')

print()
print()

print("if you are new here enter 'help'")
mainloop = True

while mainloop:
    result = ""
    user_input = input(">")
    emoji_converter = user_input.split(" ")
    if user_input == "help":
        print('''    
    quit    : closes the program
    :)      : 😄
    :(      : 😢
    lol     : 🤣
    money   : 🤑
    whew!   : 😅
    love it : 😍
    hmmm    : 🤔
    boring  : 😪
    bored   : 😴
    iq      : 🤯
    oh      : 😯
    piss    : 😤
    ok      : 👌
        ''')
    elif user_input == "quit":
        break
    elif user_input != "help":
        for word in emoji_converter:
            result += emojis.get(word, word) + " "
    print(result)
            
print("Done , well I have lot of fun making it")


