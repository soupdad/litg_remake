

label s1e1p1_01:
    # Intro
    # UNCOMMENT WHEN DEPLOYING CODE
    # scene edited_sandy_intro

    # "Life can be dull…"
    # "Life can be boring…"
    # "Day after day, it's just the same old routine."
    # "But for the chosen few, everything is about to change."
    # "Eleven Islanders are on their way to find love…"
    # "And {b}you're{/b} one of them."

    # scene edited_open_villa with dissolve

    # "We've lined you up with a brand new Villa with all the mod cons."
    # "A luxury pool, a fire pit, and that absolute holiday essential - a massive communal bedroom."
    # "Get ready for the hottest summer of your life."

    # scene edited_sandy_intro with dissolve
    # # Text message
    # "Congratulations, you've been selected for Love Island! Please get ready, your taxi is on its way. #welcometoparadise #gameon"

    # Character Customization
    # UNCOMMENT WHEN DEPLOYING CODE
    # $ s01_mc_name = renpy.input("What is your name?", length=15)

    # Outfit Selector (adjust for actual outfits when they've been created/set)
    # UNCOMMENT WHEN DEPLOYING CODE
    # menu: 
    #     "What bathing suit are you going to wear?"
    #     "Orange Bathing Suit":
    #         $ s01_mc_outfit = "Orange Bathing Suit"
    #     "Blue Bathing Suit":
    #         $ s01_mc_outfit = "Blue Bathing Suit"
    #     "Red Bathing Suit":
    #         $ s01_mc_outfit = "Red Bathing Suit"


    # Choosing job
    # UNCOMMENT WHEN DEPLOYING CODE
    # menu:
    #     "What is your job?"
    #     "Runway Model":
    #         $ s01_mc_job = "Runway Model"
    #     "Social Media Influencer":
    #         $ s01_mc_job = "Social Media Influencer"
    #     "Trainee Heart Surgeon":
    #         $ s01_mc_job = "Trainee Heart Surgeon"
    #     "Conceptual Artist":
    #         $ s01_mc_job = "Conceptual Artist"

    # UNCOMMENT WHEN DEPLOYING CODE
    # "After months of preparation, you're here. It's finally time."

    # s01_mc "It's really happening."
    # s01_mc "It still doesn't feel real. I keep thinking I'm about to wake up."

    # "You step out of the jeep, and there it is."
    # "The Villa." 
    # "Your life will never be the same again."
    # "Another girl arrives at the same time as you. She waves as she sees you approach."

    scene edited_entrance_day with dissolve

    show s01_mc at left
    with easeinleft

    show allegra at center
    with easeinright

    s01_mc "Hi I'm [s01_mc_name]"

    allegra "I'm {b}Allegra{/b}. It's so good to meet you!"

    # insert scene with just allegra that says this maybe?
    "Allegra\n 
    -24, from Swansea\n
    -Cocktail Entrepreneur\n
    -We don't know what that means either"

    $ likes_outfit = check_if_like_outfit(allegra_liked_outfits)
    if likes_outfit:
        $ amount_npcs_like_mc["allegra"] += 1
        allegra "I like you [amount_npcs_like_mc[allegra]] much"
        allegra "That outfit is absolutely amazing, by the way."
        s01_mc "Thanks."
        allegra "I kind of wish I'd dressed up a bit more."
    else:
        $ amount_npcs_like_mc["allegra"] -= 1
        allegra "I like you [amount_npcs_like_mc[allegra]] much"
        allegra "Oh wow, interesting outfit choice, by the way."
        allegra "Good luck making a splash wearing that."

    "Another girl walks in as Allegra finishes speaking."

    show erikah at right
    with easeinright

    erikah "Hi My name's {b}Erikah{/b}."

    # insert scene with just erikah that says this maybe?
    "Erikah\n
    -20, from Norwich\n 
    - Jobbing Actor\n
    - Has made over a 100 makeup tutorials"

    # "She totters towards you and embraces you warmly."
    erikah "So happy to meet you both."

    # CHOICE 1
    menu:
        "What do you do next?"
        "Talk about yourself":
            s01_mc "So in the outside world I'm a [s01_mc_job]."
            allegra "Wow, we're just getting your whole life story, huh?"

            if s01_mc_job == "Social Media Influencer":
                erikah "Like, on social media? That's such a cool job!"
                erikah "Like, everyone thinks they'd be really good at it, but they don't get how hard it actually is."
                
            elif s01_mc_job == "Trainee Heart Surgeon":
                allegra "That is amazing, though." 
                erikah "Do you dream about being that person that stands up on a plane when they ask for a doctor?"
                allegra "I'll never be that person..."

            elif s01_mc_job == "Runway Model":
                allegra "I actually used to date a boy who worked on the catwalk."
                allegra "He was, like, the most extra person I've ever met."
                "She launches into a lengthy description of her ex."
                allegra "But that's in the past. We're here to find someone new!"

            elif s01_mc_job == "Conceptual Artist":
                allegra "What does that even mean?"
                s01_mc "I make art, but it's more like… about the idea of art."
                allegra "I think I have an artistic soul, but, like, I'm very results-oriented."
                allegra "I love that we've got someone creative in the Villa, though."

            allegra "So, what are you guys hoping to get out of the Villa?"

        "Ask about Allegra":
            $ amount_npcs_like_mc["allegra"] += 2
            s01_mc "Allegra, what kind of person are you looking for, in here?"
            allegra "I don't know. I think my type is 'not my ex'."
            s01_mc "Totally. It's all about new beginnings."
            allegra "New beginnings! This is going to be the best summer of our lives."
            erikah "What about you, [s01_mc_name]? What are you after from the Villa?"

        "Ask about Erikah":
            $ amount_npcs_like_mc["erikah"] += 2
            s01_mc "So Erikah, what kind of guy do you want to find in here?"
            erikah "I don't really have a type on paper. I guess I want to be surprised."
            erikah "But he has to be fun."
            erikah "It has to be someone I can have a laugh with, even if we're just sitting on the sofa watching TV."
            allegra "Yeah, I absolutely agree."
            erikah "What about you, [s01_mc_name]? What are you after from the Villa?"
                
                
    # CHOICE 2
    menu:
        "What are you after from the Villa?"

        "To find love":
            $ amount_npcs_like_mc["allegra"] += 1
            $ s1_what_are_you_here_for = "love"
            allegra "Exactly."
            allegra "That's what it's all about."
            erikah "Well don't forget to enjoy yourself."

        "To have fun":
            $ amount_npcs_like_mc["erikah"] += 1
            $ s1_what_are_you_here_for = "fun"
            erikah "Yeah! All about the good times."
            erikah "A whole summer full of banter, with a load of hot dudes, chilling by the pool?"
            erikah "Yes Please!"
            allegra "For me it's all about finding love. Does that sound really cheesy?"
            s01_mc "Not at all!"
                    
        "For the prize money":
            $ amount_npcs_like_mc["allegra"] -= 1
            $ amount_npcs_like_mc["erikah"] -= 1
            $ s1_what_are_you_here_for = "money"
            allegra "What, for real?"
            allegra "That's, like, so not the point for me."
            erikah "Me neither."

    allegra "For me, it's all about the new beginnings."
    allegra "I've just come out of this really intense breakup, and I need to get a fresh start."
    s01_mc "What happened?"
    allegra "Well, I realised he was cheating on me with his personal trainer, and…"
    
    "Erikah raises her eyebrows at you."

    allegra "Oh, check it out, another girl!"
    
    "Allegra points across the lawn."
    jen "Hey girls! I'm Jen."

    "Jen walks elegantly towards the group, tossing her hair over her shoulder as she embraces you."

    "Jen\n
    -22, from London\n
    -Fashion Blogger\n
    -Says she has 'mega resting bitch face'"

    jen "We're all looking for love right?"

    menu:
        "Are you looking for love?"
        "Yeah, of course":
            if s1_what_are_you_here_for == "money":
                $ amount_npcs_like_mc["allegra"] -= 2
                $ amount_npcs_like_mc["erikah"] -= 2
                $ amount_npcs_like_mc["jen"] -= 1
                erikah "That's not what you said just now!"
                erikah "What's changed?"
            else:
                erikah "That's the name of the game!"
                erikah "We were just talking about it and we all said the same thing."
            
        "Not exactly":
            if s1_what_are_you_here_for == "love" or s1_what_are_you_here_for == "fun":
                $ amount_npcs_like_mc["allegra"] -= 1
                $ amount_npcs_like_mc["erikah"] -= 1
                $ amount_npcs_like_mc["jen"] -= 1
                erikah "That's not what you said just now!"
                erikah "What's changed?"
            else:
                erikah "[s01_mc_name] keeps saying she's not here for love!"
                erikah "I don't get it."

    "She's cut off by the sound of a jeep pulling up outside."

    talia "Hi guys, I'm Talia."
    
    "Talia strides across the garden towards you, swinging her hips and looking at everybody in turn."

    talia "..."

    "Her gaze seems to linger on you a moment longer than anyone else."
    "Talia\n
    -23 ,from Watford\n
    -Music Journalist\n
    -Less high-maintenance than her hair"

    jen "Oh my god, I want to know all about you guys."
    
    "For a few minutes, Jen barrages everyone with questions."
    "You pour everyone some champagne."
    
    talia "... And then I found the wedding ring, so I knew I had to chuck him."
    erikah "Wow."
    erikah "Allegra was just saying she came out of a bad breakup too."
    erikah "He broke up with you, right?"
    allegra "That's not what happened! Haven't you guys been listening at all?"
    
    menu:
        "Allegra's ex was cheating on her with his…"

        "Yoga instructor":
            $ amount_npcs_like_mc["allegra"] -= 2
            allegra "Oh my god, you guys haven't been paying attention to anything I've been saying!"
            allegra "She was his personal trainer."
            jen "Come on, ladies. We're all getting to know each other."
            allegra "Hmph."
        "Personal trainer":
            $ amount_npcs_like_mc["allegra"] += 2
            allegra "It's so sweet that you were listening, I can't wait to get to know you guys."
        "Next-door neighbour":
            $ amount_npcs_like_mc["allegra"] -= 2
            allegra "Oh my god, you guys haven't been paying attention to anything I've been saying!"
            allegra "She was his personal trainer."
            jen "Come on, ladies. We're all getting to know each other."
            allegra "Hmph."



