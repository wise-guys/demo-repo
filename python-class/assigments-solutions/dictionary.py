dictionary = ""
while dictionary != "close dictionary":
    dictionary = input("\nwhat would you like to do?\n use help to see directions ")
    if dictionary == "math":
        explain = input("""definition:a term used to make relationships with numbers.
         do you want to learn some facts? """)
        if explain == "yes":
            print("""fact1:pemdas references the order of math operations.
            (grouping, exponents, multiply, divide, add, and subtract. )""")
            print("fact2:the >,<, and = signs tell the user if the answer is greater than, less than or equal to.")
        else:
            print("sorry, but that dose not work...")
    elif dictionary == "language arts":
        explain = input("""definition:a learning structure involving a language of some kind, and learning how it works.
         do you want to learn some facts? """)
        if explain == "yes":
            print("""
            fact1:essays are a major part of LA, and consist of a intro, 3 body paragraphs, and a conclusion.
            fact2:in LA, other topics are learnt as wel, such as the way character reacts to their surroundings.
            """)
        else:
            print("sorry, but that dose not work...")
    elif dictionary == "history":
        explain = input("""definition: recorded parts of events that happened.
        do you want to learn about some facts? 
        """)
        if explain == "yes":
            print("""fact1:their are certain parts of history that were NOT recorded.
            these times are much harder to find out about, and ar referred to as bc, bce, and many more.
            fact2: certain parts of history have important events.
            these events include:
            the american and french revolution
             both world wars
              and the steam age/ industrial revolution.
            """)
        else:
            print("sorry, but that dose not work...")
    elif dictionary == "help":
        print("""options are:
        math
        LA (language arts)
        history
        you can also say yes while reviewing the definition to get some facts about the topic.
        as well as type close dictionary to stop the program.
        """)
    else:
        print("sorry, but that dose not work...")
