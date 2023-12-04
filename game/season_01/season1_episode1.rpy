

label s1e1p1_01:
    # Intro
    "Life can be dull…"
    "Life can be boring…"
    "Day after day, it's just the same old routine."
    "But for the chosen few, everything is about to change."
    "Eleven Islanders are on their way to find love…"
    "And {b}you're{/b} one of them."
    "We've lined you up with a brand new Villa with all the mod cons."
    "A luxury pool, a fire pit, and that absolute holiday essential - a massive communal bedroom."
    "Get ready for the hottest summer of your life."

    # Text message
    "Congratulations, you've been selected for Love Island! Please get ready, your taxi is on its way. #welcometoparadise #gameon"

    # Character Customization
    $ mc.name = renpy.input("What is your name?", length=15)

    menu:
        "What is your job?"
        "Runway Model":
            $ mc_job = "Runway Model"
        "Social Media Influencer":
            $ mc_job = "Social Media Influencer"
        "Trainee Heart Surgeon":
            $ mc_job = "Trainee Heart Surgeon"
        "Conceptual Artist":
            $ mc_job = "Conceptual Artist"


    mc "Hi I am [mc.name] and my job is [mc_job]"