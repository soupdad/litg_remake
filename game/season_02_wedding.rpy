#############################################################################
## Wedding Setup
#############################################################################

label s2w_set_up:
    $ s2w_mc_name = "You"

    scene edited_sandy_intro

    "Love is confusing."
    "Love can be messy."
    "But ultimately, love can change the world."
    "Out of the seven billion people on this planet…"
    "…and fourteen lucky islanders…"
    "You've found your love."
    "All that's left is to make it official…"
    "Welcome to Love Island The Wedding!"

    s2w_mc "I can't wait!"

    "Since we currently don't have a Season 2 there are a couple questions that need to be answered to customize your playthrough."

    jump s2w_customize_my_story

    #########################      UNCOMMENT ONCE S2 IS CREATED     ##########################
    # CHOICE
    # menu:
        # "Quick question - did you finish Day 30 of season 2? It's fine if you didn't!"
        # "I didn't finish season 2":
        #     "Do you want to answer some questions to customize your story, or just jump straight in?"
        #     # SUB-CHOICE
        #     menu:
        #         s2w_mc "I want to…"
        #         "Customise my story":
        #             "OK! Let's set this up."
        #             jump s2w_customize_my_story
                
        #         "Jump straight in!":
        #             # uses save data from s2 for who you're coupled up with, name, and what you look like, auto fills in other questions
        #             $ s2w_partner = s2_current_partner
        #             $ s2w_living_together = False
        #             $ s2w_secret_moment = "No one"
        #             $ s2w_travel_plans = "No one"
        #             $ s2w_win = True
        #             $ s2w_spent_prize_on = "Random"
        #             "Woah! Before you start, what do you want to be called?"
        #             # input name
        #             "Perfect! Now get ready… "
        #             "For the wedding!"
        
        # "I finished season 2":
        #     "Do you want to carry on your story from the end of Season 2, or customize some things?"
        #     # SUB-CHOICE
        #     menu:
        #         s2w_mc "I'm going to…"
        #         "…continue my Season 2 story":
        #             # uses save data from s2 playthrough
        #             $ s2w_mc_name == s2_mc_name
        #             $ s2w_partner = s2_current_partner
        #             $ s2w_living_together = False
        #             $ s2w_secret_moment = "No one"
        #             $ s2w_travel_plans = "No one"
        #             $ s2w_win = True
        #             $ s2w_spent_prize_on = "Random"

        #         "… customize my story":
        #             jump s2w_customize_my_story


label s2w_customize_my_story:
    "OK! Let's set this up."
    "First, we'll create your character."
    # character creator

    show s2w_mc at center
    with Dissolve(0.1)

    # CHOICE
    menu:
        "Is this the look?"
        "Yep! Nailed it!":
            pass
        "I want to try something else":
            jump s2w_customize_my_story

    "What do you want to be called?"
    # input name
    s2w_mc @ happy "Here I am!"

    "Next, we're going to ask you some questions to set up your story."
    "You can answer these questions however you want. They will set up your relationships going into this mini-series."
    "In this customised story, it is possible to set up some situations that weren't possible in the main game."
    "Firstly, and most importantly, who do you want to marry?"

label s2w_choose_partner:
    
    scene edited_sandy_intro
    # CHOICE
    # create screen with character's profile shots and arrows to hit next, showing 3-4 at a time
    menu: 
        "Bobby, the boisterous booper":
            $ s2w_partner = "Bobby"
        "Gary, the construction hunk":
            $ s2w_partner = "Gary"
        "Ibrahim, the gentle golfer":
            $ s2w_partner = "Rahim"
        "Marisol, the hopeless romantic":
            $ s2w_partner = "Marisol"
            $ s2w_partner_pronouns = ["she", "her", "hers"]
        "Lucas, the charming daredevil":
            $ s2w_partner = "Lucas"
        "Next":
            menu:
                "Henrik, the Swedish outdoorsman":
                    $ s2w_partner = "Henrik"
                "Jakub, the muscular hustler":
                    $ s2w_partner = "Jakub"
                "Arjun, the cheeky charmer":
                    $ s2w_partner = "Arjun"
                "Kassam, the quiet DJ":
                    $ s2w_partner = "Kassam"
                "Felix, the party animal":
                    $ s2w_partner = "Felix"
                "Next":
                    menu:
                        "Elijah, the suave sophisticate":
                            $ s2w_partner = "Elijah"
                        "Carl, the successful scientist":
                            $ s2w_partner = "Carl"
                        "Elisa, the outrageous influencer":
                            $ s2w_partner = "Elisa"
                            $ s2w_partner_pronouns = ["she", "her", "hers"]
                        "Noah, the luscious librarian":
                            $ s2w_partner = "Noah"
                        "Next":
                            jump s2w_choose_partner

    show s2w_mc at mc_spot

    if s2w_partner == "Bobby":
        show bobby at npc_2
        bobby "I'm so lucky!"
    elif s2w_partner == "Gary":
        show gary at npc_2
        gary "I'm so lucky!"
    elif s2w_partner == "Rahim":
        show rahim at npc_2
        rahim "I'm so lucky!"
    elif s2w_partner == "Marisol":
        show marisol at npc_2
        marisol "I'm so lucky!"
    elif s2w_partner == "Lucas":
        show lucas at npc_2
        lucas "I'm so lucky!"
    elif s2w_partner == "Henrik":
        show henrik at npc_2
        henrik "I'm so lucky!"
    elif s2w_partner == "Jakub":
        show jakub at npc_2
        jakub "I'm so lucky!"
    elif s2w_partner == "Arjun":
        show arjun at npc_2
        arjun "I'm so lucky!"
    elif s2w_partner == "Kassam":
        show kassam at npc_2
        kassam "I'm so lucky!"
    elif s2w_partner == "Felix":
        show felix at npc_2
        felix "I'm so lucky!"
    elif s2w_partner == "Elijah":
        show elijah at npc_2
        elijah "I'm so lucky!"
    elif s2w_partner == "Carl":
        show carl at npc_2
        carl "I'm so lucky!"
    elif s2w_partner == "Noah":
        show noah at npc_2
        noah "I'm so lucky!"
    elif s2w_partner == "Elisa":
        show elisa at npc_2
        elisa "I'm so lucky!"

    # VERIFY CHOICE
    menu:
        "Am I sure I want to marry [s2w_partner]?"
        "Of course!":
            pass
        "Let me choose again...":
            jump s2w_choose_partner

    s2w_mc "Nobody else has ever made me feel the way [s2w_partner] makes me feel."

    "Are you and [s2w_partner] living together?"
    
    # CHOICE
    menu:
        "Are [s2w_partner] and I living together?"
        "Yep":
            $ s2w_living_together = True
            "Happily cohabiting."
        "Nope":
            $ s2w_living_together = False
            "We decided not to, at first. Life is too complex right now"

    "The next few questions are about choices you could have made in the finale of Love Island. answer them however you like."
    "First - did you have a secret intimate moment with Lottie or Hannah, right before the series ended?"

    # CHOICE
    menu:
        "Did I have a secret moment with Lottie or Hannah?"
        "Yes, with Lottie":
            $ s2w_secret_moment = "Lottie"
            s2w_mc "I still think about it all the time..." 
        "Yes, with Hannah":
            $ s2w_secret_moment = "Hannah"
            s2w_mc "I still think about it all the time..." 
        "No, I didn't":
            $ s2w_secret_moment = "No one"
            s2w_mc "Nah, that's not me."
            

    "Did you promise to go travelling with anyone?"

    # CHOICE
    menu:
        "Did I make travel plans with any of the Islanders?"
        "Yes, with Shannon":
            $ s2w_travel_plans = "Shannon"
            s2w_mc "I was so excited for our trip to Monaco."
        "Yes, with Hope":
            $ s2w_travel_plans = "Hope"
            s2w_mc "I was really touched when Hope said she'd pay for a holiday for me and her."
        "No, I didn't":
            $ s2w_travel_plans = "No one"
            "I needed a bit of a break from everyone by then."
    
    "And finally, did you win Love Island?"
    
    # CHOICE
    menu:
        "Did I win?"
        "Totally":
            $ s2w_win = True
            # SUB-CHOICE
            menu:
                "And I spent the prize money on..."
                "... travelling the world!":
                    $ s2w_spent_prize_on = "Travel"
                "... a lot of clothes":
                    $ s2w_spent_prize_on = "Clothes"
                "... helping people less well off than me":
                    $ s2w_spent_prize_on = "Charity"
                "... a bit of this, a bit of that":
                    $ s2w_spent_prize_on = "Random"
        "No, I didn't":
            $ s2w_win = False
            s2w_mc "It's about the taking part, babes."
    
    s2w_mc "OK, that's all done. Here we go!"

    ## Intro
    "After the finale, you and [s2w_partner] left the Villa hand in hand."

    # IF STATEMENT
    if s2w_living_together:
        "The two of you soon found a place of your own and got busy decorating it."
        $ pronoun = s2w_partner_pronouns[2].capitalize()
        thought "[pronoun] painting skills left a lot to be desired."
    else:
        "The two of you took things slow and didn't move together straight away."
        s2w_mc "That didn't stop [s2w_partner] from pointing out places to live every time we passed an estate agent."
    
    # IF STATEMENT
    if s2w_win:
        if s2w_spent_prize_on == "Travel":
            "You didn't hang around long. You took your price money and spent it traveling the world, with [s2w_partner] in tow."
        elif s2w_spent_prize_on == "Clothes":
            "You spent the weeks following the finale using the prize money to expand your wardrobe."
            s2w_mc "Not gonna lie, I've done a lot of cover shoots."
        elif s2w_spent_prize_on == "Charity":
            "After the show ended, you made good on your plans to donate the prize money to charity."
            "You put your new-found fame to use and did a circle of fundraisers and galas. It kept you surprisingly busy."
        else:
            "You didn't spend the prize money all at once, but that didn't stop you having some fun with it."
            s2w_mc "Yeah, we totally lived it up."

    # IF STATEMENT
    if s2w_secret_moment != "No one":
        "After the show ended, you and [s2w_secret_moment] messaged quite a bit, trying to figure out a time you could meet up."
        "But you were both so busy, and one last-minute cancellation followed another. It felt like the world was against you."
        "And for all the good will in the world, you didn't end up seeing each other, and eventually stopped messaging entirely."
        s2w_mc "I still think about her now and then…"

    if s2w_travel_plans == "Shannon":
        "You left [s2w_partner] alone for a couple of weeks while you and Shannon took your trip to Monaco."
        "You lived like royalty. You bathed in champagne."
        thought "Some stuff happened that neither of us will tell anyone about. What happens in Monaco stays in Monaco, after all."

    "And then, out of the blue, the invite for the reunion arrived."
    "And the timing was perfect, because by then you'd make an important decision."
    "There was a question you'd been meaning to ask [s2w_partner]"
    thought "A pretty big question."
    "And what better time to propose than surrounded by the friends you'd made together during your time in the Villa?"
    "The main thing to figure out was what to wear."

    # outfit customizer opens

    thought "This is the outfit! I can't wait to propose to [s2w_partner] in it…"
    "And now it's time. The day's arrived. And in your pocket…"
    "Is a ring."



#############################################################################
## Wedding Part 1
#############################################################################

label s2w_part1:
    scene wedding_partyroom

    show s2w_mc at mc_spot

    # IF STATEMENT
    if s2w_partner == "Bobby":
        show bobby at beside_mc
        show bobby behind s2w_mc
    elif s2w_partner == "Gary":
        show gary at beside_mc
        show gary behind s2w_mc
    elif s2w_partner == "Rahim":
        show rahim at beside_mc
        show rahim behind s2w_mc
    elif s2w_partner == "Marisol":
        show marisol at beside_mc
        show marisol behind s2w_mc
    elif s2w_partner == "Lucas":
        show lucas at beside_mc
        show lucas behind s2w_mc
    elif s2w_partner == "Henrik":
        show henrik at beside_mc
        show henrik behind s2w_mc
    elif s2w_partner == "Jakub":
        show jakub at beside_mc
        show jakub behind s2w_mc
    elif s2w_partner == "Arjun":
        show arjun at beside_mc
        show arjun behind s2w_mc
    elif s2w_partner == "Kassam":
        show kassam at beside_mc
        show kassam behind s2w_mc
    elif s2w_partner == "Felix":
        show felix at beside_mc
        show felix behind s2w_mc
    elif s2w_partner == "Elijah":
        show elijah at beside_mc
        show elijah behind s2w_mc
    elif s2w_partner == "Carl":
        show carl at beside_mc
        show carl behind s2w_mc
    elif s2w_partner == "Noah":
        show noah at beside_mc
        show noah behind s2w_mc
    elif s2w_partner == "Elisa":
        show elisa at beside_mc
        show elisa behind s2w_mc  

    "You and [s2w_partner] walk into the room and the bright lights dazzle you. It smells like pineapple and mango."
    "All around you are the friends you spent the summer with."
    "It's loud with the music and chatter of the other Islanders. At first, nobody notices you."

    # IF STATEMENT
    if s2w_partner == "Bobby":
        bobby "Looks like we're the last ones to arrive."
        bobby "That's so us."
        s2w_mc "Um, is it?"
        bobby "Everything OK, babe? You look a little pale."

        # CHOICE
        menu:
            "Tonight's the night I propose to [s2w_partner]! I'm really nervous…"
            "I'm fine! Everything's fine!":
                "[s2w_partner] raises an eyebrow at you."
                bobby "Well, that was convincing."
                bobby "It's ok if you're a bit overwhelmed. There is so much going on in this room right now. Maybe we should…"

            "Yeah, it's just a lot to take in.":
                "He smiles at you and pulls you into a reassuring embrace."
                bobby "Hey, it's alright."
                bobby "It's ok if you're a bit overwhelmed. There is so much going on in this room right now. Maybe we should…"
            
            "I really need to pee!":
                bobby "Oh…"
                bobby "Um, I think the loos are just over there."
                "You dash into the toilets, which you don't need to use, and take a few deep breaths to gather yourself."
                "When you exit, [s2w_partner] is waiting for you with his arm out ready to link it back with yours."
                bobby "It's ok if you're a bit overwhelmed. There is so much going on in this room right now. Maybe we should…"

    elif s2w_partner == "Gary":
        gary "Looks like we're the last ones to arrive."
        gary "That's so us."
        s2w_mc "Um, is it?"
        gary "Everything OK, babe? You look a little pale."

        # CHOICE
        menu:
            "Tonight's the night I propose to [s2w_partner]! I'm really nervous…"
            "I'm fine! Everything's fine!":
                "[s2w_partner] raises an eyebrow at you."
                gary "Well, that was convincing."
                gary "It's ok if you're a bit overwhelmed. There is so much going on in this room right now. Maybe we should…"

            "Yeah, it's just a lot to take in.":
                "He smiles at you and pulls you into a reassuring embrace."
                gary "Hey, it's alright."
                gary "It's ok if you're a bit overwhelmed. There is so much going on in this room right now. Maybe we should…"
            
            "I really need to pee!":
                gary "Oh…"
                gary "Um, I think the loos are just over there."
                "You dash into the toilets, which you don't need to use, and take a few deep breaths to gather yourself."
                "When you exit, [s2w_partner] is waiting for you with his arm out ready to link it back with yours."
                gary "It's ok if you're a bit overwhelmed. There is so much going on in this room right now. Maybe we should…"

    elif s2w_partner == "Rahim":
        rahim "Looks like we're the last ones to arrive."
        rahim "That's so us."
        s2w_mc "Um, is it?"
        rahim "Everything OK, babe? You look a little pale."

        # CHOICE
        menu:
            "Tonight's the night I propose to [s2w_partner]! I'm really nervous…"
            "I'm fine! Everything's fine!":
                "[s2w_partner] raises an eyebrow at you."
                rahim "Well, that was convincing."
                rahim "It's ok if you're a bit overwhelmed. There is so much going on in this room right now. Maybe we should…"

            "Yeah, it's just a lot to take in.":
                "He smiles at you and pulls you into a reassuring embrace."
                rahim "Hey, it's alright."
                rahim "It's ok if you're a bit overwhelmed. There is so much going on in this room right now. Maybe we should…"
            
            "I really need to pee!":
                rahim "Oh…"
                rahim "Um, I think the loos are just over there."
                "You dash into the toilets, which you don't need to use, and take a few deep breaths to gather yourself."
                "When you exit, [s2w_partner] is waiting for you with his arm out ready to link it back with yours."
                rahim "It's ok if you're a bit overwhelmed. There is so much going on in this room right now. Maybe we should…"

    elif s2w_partner == "Marisol":
        marisol "Looks like we're the last ones to arrive."
        marisol "That's so us."
        s2w_mc "Um, is it?"
        marisol "Everything OK, babe? You look a little pale."

        # CHOICE
        menu:
            "Tonight's the night I propose to [s2w_partner]! I'm really nervous…"
            "I'm fine! Everything's fine!":
                "[s2w_partner] raises an eyebrow at you."
                marisol "Well, that was convincing."
                marisol "It's ok if you're a bit overwhelmed. There is so much going on in this room right now. Maybe we should…"

            "Yeah, it's just a lot to take in.":
                "He smiles at you and pulls you into a reassuring embrace."
                marisol "Hey, it's alright."
                marisol "It's ok if you're a bit overwhelmed. There is so much going on in this room right now. Maybe we should…"
            
            "I really need to pee!":
                marisol "Oh…"
                marisol "Um, I think the loos are just over there."
                "You dash into the toilets, which you don't need to use, and take a few deep breaths to gather yourself."
                "When you exit, [s2w_partner] is waiting for you with his arm out ready to link it back with yours."
                marisol "It's ok if you're a bit overwhelmed. There is so much going on in this room right now. Maybe we should…"

    elif s2w_partner == "Lucas":
        lucas "Looks like we're the last ones to arrive."
        lucas "That's so us."
        s2w_mc "Um, is it?"
        lucas "Everything OK, babe? You look a little pale."

        # CHOICE
        menu:
            "Tonight's the night I propose to [s2w_partner]! I'm really nervous…"
            "I'm fine! Everything's fine!":
                "[s2w_partner] raises an eyebrow at you."
                lucas "Well, that was convincing."
                lucas "It's ok if you're a bit overwhelmed. There is so much going on in this room right now. Maybe we should…"

            "Yeah, it's just a lot to take in.":
                "He smiles at you and pulls you into a reassuring embrace."
                lucas "Hey, it's alright."
                lucas "It's ok if you're a bit overwhelmed. There is so much going on in this room right now. Maybe we should…"
            
            "I really need to pee!":
                lucas "Oh…"
                lucas "Um, I think the loos are just over there."
                "You dash into the toilets, which you don't need to use, and take a few deep breaths to gather yourself."
                "When you exit, [s2w_partner] is waiting for you with his arm out ready to link it back with yours."
                lucas "It's ok if you're a bit overwhelmed. There is so much going on in this room right now. Maybe we should…"

    elif s2w_partner == "Henrik":
        henrik "Looks like we're the last ones to arrive."
        henrik "That's so us."
        s2w_mc "Um, is it?"
        henrik "Everything OK, babe? You look a little pale."

        # CHOICE
        menu:
            "Tonight's the night I propose to [s2w_partner]! I'm really nervous…"
            "I'm fine! Everything's fine!":
                "[s2w_partner] raises an eyebrow at you."
                henrik "Well, that was convincing."
                henrik "It's ok if you're a bit overwhelmed. There is so much going on in this room right now. Maybe we should…"

            "Yeah, it's just a lot to take in.":
                "He smiles at you and pulls you into a reassuring embrace."
                henrik "Hey, it's alright."
                henrik "It's ok if you're a bit overwhelmed. There is so much going on in this room right now. Maybe we should…"
            
            "I really need to pee!":
                henrik "Oh…"
                henrik "Um, I think the loos are just over there."
                "You dash into the toilets, which you don't need to use, and take a few deep breaths to gather yourself."
                "When you exit, [s2w_partner] is waiting for you with his arm out ready to link it back with yours."
                henrik "It's ok if you're a bit overwhelmed. There is so much going on in this room right now. Maybe we should…"

    elif s2w_partner == "Jakub":
        jakub "Looks like we're the last ones to arrive."
        jakub "That's so us."
        s2w_mc "Um, is it?"
        jakub "Everything OK, babe? You look a little pale."

        # CHOICE
        menu:
            "Tonight's the night I propose to [s2w_partner]! I'm really nervous…"
            "I'm fine! Everything's fine!":
                "[s2w_partner] raises an eyebrow at you."
                jakub "Well, that was convincing."
                jakub "It's ok if you're a bit overwhelmed. There is so much going on in this room right now. Maybe we should…"

            "Yeah, it's just a lot to take in.":
                "He smiles at you and pulls you into a reassuring embrace."
                jakub "Hey, it's alright."
                jakub "It's ok if you're a bit overwhelmed. There is so much going on in this room right now. Maybe we should…"
            
            "I really need to pee!":
                jakub "Oh…"
                jakub "Um, I think the loos are just over there."
                "You dash into the toilets, which you don't need to use, and take a few deep breaths to gather yourself."
                "When you exit, [s2w_partner] is waiting for you with his arm out ready to link it back with yours."
                jakub "It's ok if you're a bit overwhelmed. There is so much going on in this room right now. Maybe we should…"

    elif s2w_partner == "Arjun":
        arjun "Looks like we're the last ones to arrive."
        arjun "That's so us."
        s2w_mc "Um, is it?"
        arjun "Everything OK, babe? You look a little pale."

        # CHOICE
        menu:
            "Tonight's the night I propose to [s2w_partner]! I'm really nervous…"
            "I'm fine! Everything's fine!":
                "[s2w_partner] raises an eyebrow at you."
                arjun "Well, that was convincing."
                arjun "It's ok if you're a bit overwhelmed. There is so much going on in this room right now. Maybe we should…"

            "Yeah, it's just a lot to take in.":
                "He smiles at you and pulls you into a reassuring embrace."
                arjun "Hey, it's alright."
                arjun "It's ok if you're a bit overwhelmed. There is so much going on in this room right now. Maybe we should…"
            
            "I really need to pee!":
                arjun "Oh…"
                arjun "Um, I think the loos are just over there."
                "You dash into the toilets, which you don't need to use, and take a few deep breaths to gather yourself."
                "When you exit, [s2w_partner] is waiting for you with his arm out ready to link it back with yours."
                arjun "It's ok if you're a bit overwhelmed. There is so much going on in this room right now. Maybe we should…"

    elif s2w_partner == "Kassam":
        kassam "Looks like we're the last ones to arrive."
        kassam "That's so us."
        s2w_mc "Um, is it?"
        kassam "Everything OK, babe? You look a little pale."

        # CHOICE
        menu:
            "Tonight's the night I propose to [s2w_partner]! I'm really nervous…"
            "I'm fine! Everything's fine!":
                "[s2w_partner] raises an eyebrow at you."
                kassam "Well, that was convincing."
                kassam "It's ok if you're a bit overwhelmed. There is so much going on in this room right now. Maybe we should…"

            "Yeah, it's just a lot to take in.":
                "He smiles at you and pulls you into a reassuring embrace."
                kassam "Hey, it's alright."
                kassam "It's ok if you're a bit overwhelmed. There is so much going on in this room right now. Maybe we should…"
            
            "I really need to pee!":
                kassam "Oh…"
                kassam "Um, I think the loos are just over there."
                "You dash into the toilets, which you don't need to use, and take a few deep breaths to gather yourself."
                "When you exit, [s2w_partner] is waiting for you with his arm out ready to link it back with yours."
                kassam "It's ok if you're a bit overwhelmed. There is so much going on in this room right now. Maybe we should…"

    elif s2w_partner == "Felix":
        felix "Looks like we're the last ones to arrive."
        felix "That's so us."
        s2w_mc "Um, is it?"
        felix "Everything OK, babe? You look a little pale."

        # CHOICE
        menu:
            "Tonight's the night I propose to [s2w_partner]! I'm really nervous…"
            "I'm fine! Everything's fine!":
                "[s2w_partner] raises an eyebrow at you."
                felix "Well, that was convincing."
                felix "It's ok if you're a bit overwhelmed. There is so much going on in this room right now. Maybe we should…"

            "Yeah, it's just a lot to take in.":
                "He smiles at you and pulls you into a reassuring embrace."
                felix "Hey, it's alright."
                felix "It's ok if you're a bit overwhelmed. There is so much going on in this room right now. Maybe we should…"
            
            "I really need to pee!":
                felix "Oh…"
                felix "Um, I think the loos are just over there."
                "You dash into the toilets, which you don't need to use, and take a few deep breaths to gather yourself."
                "When you exit, [s2w_partner] is waiting for you with his arm out ready to link it back with yours."
                felix "It's ok if you're a bit overwhelmed. There is so much going on in this room right now. Maybe we should…"

    elif s2w_partner == "Elijah":
        elijah "Looks like we're the last ones to arrive."
        elijah "That's so us."
        s2w_mc "Um, is it?"
        elijah "Everything OK, babe? You look a little pale."

        # CHOICE
        menu:
            "Tonight's the night I propose to [s2w_partner]! I'm really nervous…"
            "I'm fine! Everything's fine!":
                "[s2w_partner] raises an eyebrow at you."
                elijah "Well, that was convincing."
                elijah "It's ok if you're a bit overwhelmed. There is so much going on in this room right now. Maybe we should…"

            "Yeah, it's just a lot to take in.":
                "He smiles at you and pulls you into a reassuring embrace."
                elijah "Hey, it's alright."
                elijah "It's ok if you're a bit overwhelmed. There is so much going on in this room right now. Maybe we should…"
            
            "I really need to pee!":
                elijah "Oh…"
                elijah "Um, I think the loos are just over there."
                "You dash into the toilets, which you don't need to use, and take a few deep breaths to gather yourself."
                "When you exit, [s2w_partner] is waiting for you with his arm out ready to link it back with yours."
                elijah "It's ok if you're a bit overwhelmed. There is so much going on in this room right now. Maybe we should…"

    elif s2w_partner == "Carl":
        carl "Looks like we're the last ones to arrive."
        carl "That's so us."
        s2w_mc "Um, is it?"
        carl "Everything OK, babe? You look a little pale."

        # CHOICE
        menu:
            "Tonight's the night I propose to [s2w_partner]! I'm really nervous…"
            "I'm fine! Everything's fine!":
                "[s2w_partner] raises an eyebrow at you."
                carl "Well, that was convincing."
                carl "It's ok if you're a bit overwhelmed. There is so much going on in this room right now. Maybe we should…"

            "Yeah, it's just a lot to take in.":
                "He smiles at you and pulls you into a reassuring embrace."
                carl "Hey, it's alright."
                carl "It's ok if you're a bit overwhelmed. There is so much going on in this room right now. Maybe we should…"
            
            "I really need to pee!":
                carl "Oh…"
                carl "Um, I think the loos are just over there."
                "You dash into the toilets, which you don't need to use, and take a few deep breaths to gather yourself."
                "When you exit, [s2w_partner] is waiting for you with his arm out ready to link it back with yours."
                carl "It's ok if you're a bit overwhelmed. There is so much going on in this room right now. Maybe we should…"

    elif s2w_partner == "Noah":
        noah "Looks like we're the last ones to arrive."
        noah "That's so us."
        s2w_mc "Um, is it?"
        noah "Everything OK, babe? You look a little pale."

        # CHOICE
        menu:
            "Tonight's the night I propose to [s2w_partner]! I'm really nervous…"
            "I'm fine! Everything's fine!":
                "[s2w_partner] raises an eyebrow at you."
                noah "Well, that was convincing."
                noah "It's ok if you're a bit overwhelmed. There is so much going on in this room right now. Maybe we should…"

            "Yeah, it's just a lot to take in.":
                "He smiles at you and pulls you into a reassuring embrace."
                noah "Hey, it's alright."
                noah "It's ok if you're a bit overwhelmed. There is so much going on in this room right now. Maybe we should…"
            
            "I really need to pee!":
                noah "Oh…"
                noah "Um, I think the loos are just over there."
                "You dash into the toilets, which you don't need to use, and take a few deep breaths to gather yourself."
                "When you exit, [s2w_partner] is waiting for you with his arm out ready to link it back with yours."
                noah "It's ok if you're a bit overwhelmed. There is so much going on in this room right now. Maybe we should…"

    elif s2w_partner == "Elisa":
        elisa "Looks like we're the last ones to arrive."
        elisa "That's so us."
        s2w_mc "Um, is it?"
        elisa "Everything OK, babe? You look a little pale."

        # CHOICE
        menu:
            "Tonight's the night I propose to [s2w_partner]! I'm really nervous…"
            "I'm fine! Everything's fine!":
                "[s2w_partner] raises an eyebrow at you."
                elisa "Well, that was convincing."
                elisa "It's ok if you're a bit overwhelmed. There is so much going on in this room right now. Maybe we should…"

            "Yeah, it's just a lot to take in.":
                "He smiles at you and pulls you into a reassuring embrace."
                elisa "Hey, it's alright."
                elisa "It's ok if you're a bit overwhelmed. There is so much going on in this room right now. Maybe we should…"
            
            "I really need to pee!":
                elisa "Oh…"
                elisa "Um, I think the loos are just over there."
                "You dash into the toilets, which you don't need to use, and take a few deep breaths to gather yourself."
                "When you exit, [s2w_partner] is waiting for you with his arm out ready to link it back with yours."
                elisa "It's ok if you're a bit overwhelmed. There is so much going on in this room right now. Maybe we should…"


    show chelsea at npc_2

    chelsea "[s2w_mc_name]!"
    "Chelsea throws up her arms and strides towards you."
    # CHOICE
    menu:
        "Chelsea!"
        "Scream her name and meet her hug":
            s2w_mc "Chelsea!"
            "You charge towards her and hug her tightly. Wheel she pulls back, she has tears in her eyes."
            chelsea "I've missed you, girl!"

        "Politely wave but don't hug her":
            s2w_mc "Oh, hey girl."
            "You wave. She stands still with her arms up for a moment, then jazz hands at you with another squeal of delight."
            chelsea "I've missed you, girl!"

        "Barrel into her and pick her up in a hug.":
            "Without saying a word you charge at Chelsea, wrap your arms around her waist and pull her up off the ground in a tight embrace."
            chelsea "Wheee! I'm a floating fairy of love and fizzy!"
            chelsea "I've missed you, girl!"
            s2w_mc "I've missed you, too."
    
    chelsea "Oh, and you, [s2w_partner]."
    "She turns to the others.."

    # IF STATEMENT
    if s2w_partner == "Bobby":
        bobby "Hey, Chelsea, how are…"
    elif s2w_partner == "Gary":
        gary "Hey, Chelsea, how are…"
    elif s2w_partner == "Rahim":
        rahim "Hey, Chelsea, how are…"
    elif s2w_partner == "Marisol":
        marisol "Hey, Chelsea, how are…"
    elif s2w_partner == "Lucas":
        lucas "Hey, Chelsea, how are…"
    elif s2w_partner == "Henrik":
        henrik "Hey, Chelsea, how are…"
    elif s2w_partner == "Jakub":
        jakub "Hey, Chelsea, how are…"
    elif s2w_partner == "Arjun":
        arjun "Hey, Chelsea, how are…"
    elif s2w_partner == "Kassam":
        kassam "Hey, Chelsea, how are…"
    elif s2w_partner == "Felix":
        felix "Hey, Chelsea, how are…"
    elif s2w_partner == "Elijah":
        elijah "Hey, Chelsea, how are…"
    elif s2w_partner == "Carl":
        carl "Hey, Chelsea, how are…"
    elif s2w_partner == "Noah":
        noah "Hey, Chelsea, how are…"
    elif s2w_partner == "Elisa":
        elisa "Hey, Chelsea, how are…"

    chelsea "Everyone! [s2w_mc_name]'s finally here!"
    chelsea "Oh, and [s2w_partner], too. "
    "The others turn to see you and cheer."

    # close up
    show priya at npc_3
    priya "There she is! I thought I was going to be the one to make the dramatic entrance."
    
    # IF STATEMENT
    # CREATE A SCREEN THAT DOES CLOSEUP SHOTS FOR WHEN PEOPLE ARENT IN THE DIRECT VACINITY
    if s2w_partner != 'Gary':
        show priya at npc_exit

        # close up
        show gary at npc_3
        gary "Now it's a proper party!"
        show gary at npc_exit
    else:
        show priya at npc_exit

    # IF STATEMENT
    # close up
    if s2w_secret_moment == "Lottie":
        lottie "Across the room, you spot Lottie. You make eye contact and her cheeks flush red. She gives you a coy smile."
    elif s2w_secret_moment == "Hannah":
        hannah "Across the room, you spot Hannah. You make eye contact and her cheeks flush red. She gives you a coy smile."
    else:
        show lottie at npc_3
        lottie "It's great to have the gang all back together."
        show lottie at npc_exit

    "Chelsea turns back to you."
    chelsea "I missed everyone being together, but especially you, babe."
    chelsea "What have you been up to?"

    # CHOICE
    menu:
        "Since leaving the Villa I've…"
        "Been wanting to come back!":
            chelsea "Same!"
        "Not been up to much":
            chelsea "Whaaat? That doesn't seem like the [s2w_mc_name] I know!"
        "Moved in with this one" if s2w_living_together:
            "You rest your head on [s2w_partner]'s shoulder."
            chelsea "Awww! That's so cute. "
            chelsea "I bet you have the nicest place!"
            chelsea "You have to get me round to look at it if you want some decoration advice!"
        "Been busy working with some charities" if s2w_spent_prize_on == 'Charity':
            chelsea "That's good to hear!"
            chelsea "I'd like to think I'd do that too, but honestly, I'd probably spend the time scrolling social and sending selfies to my group chats."
        "Been to Monaco with Shannon" if s2w_travel_plans == 'Shannon':
            chelsea "Whaaat?"
            chelsea "Where was my invite, babes?"
            chelsea "I bet you got up to all sorts!"
            chelsea "Me and you need to go somewhere nice as well soon. Like, Italy or something. "
        "Been traveling around the world." if s2w_spent_prize_on == 'Travel':
            chelsea "I'm so jealous!"
            chelsea "I want to travel the world some day. Maybe somewhere really mysterious like Luxembourg or something. "
            s2w_mc "Is Luxembourg mysterious?"
            chelsea "For sure! Like, who knows what even goes on there. "
            chelsea "Do you know what happens in Luxembourg?"
            s2w_mc "I've got no idea. "
            chelsea "Exactly. "
        "Been busy upgrading my wardrobe" if s2w_spent_prize_on == 'Clothes':
            chelsea "Oh yeah! I saw the photo shoot on your Insta."
            chelsea "You looked amazing, babes!"

    chelsea "I've been so bored without everyone!"
    chelsea "I had this one really fun job, though. This guy wanted me to make his house into the Villa. "
    chelsea "But it was only a two-up-two-down terrace and so I had to get creative. "
    chelsea "I replaced his cooker with a fire pit. And I had to fill the sitting room with sand. "
    chelsea "He tried to say the Villa didn't actually have sand, but I wanted a beach outing feel…"
    "There is a pause as she takes a breath."
    chelsea "Anyway! I'm going to go and get us some drinks. See you in a bit, babes!"
    s2w_mc "See you in a bit, girl. "
    "She hugs you and then practically skips off."

    show chelsea at npc_exit

    # IF STATEMENT
    if s2w_partner == "Bobby":
        bobby "See you, Chelsea!"
        bobby "She's exactly as I remember."
    elif s2w_partner == "Gary":
        gary "See you, Chelsea!"
        gary "She's exactly as I remember."
    elif s2w_partner == "Rahim":
        rahim "See you, Chelsea!"
        rahim "She's exactly as I remember."
    elif s2w_partner == "Marisol":
        marisol "See you, Chelsea!"
        marisol "She's exactly as I remember."
    elif s2w_partner == "Lucas":
        lucas "See you, Chelsea!"
        lucas "She's exactly as I remember."
    elif s2w_partner == "Henrik":
        henrik "See you, Chelsea!"
        henrik "She's exactly as I remember."
    elif s2w_partner == "Jakub":
        jakub "See you, Chelsea!"
        jakub "She's exactly as I remember."
    elif s2w_partner == "Arjun":
        arjun "See you, Chelsea!"
        arjun "She's exactly as I remember."
    elif s2w_partner == "Kassam":
        kassam "See you, Chelsea!"
        kassam "She's exactly as I remember."
    elif s2w_partner == "Felix":
        felix "See you, Chelsea!"
        felix "She's exactly as I remember."
    elif s2w_partner == "Elijah":
        elijah "See you, Chelsea!"
        elijah "She's exactly as I remember."
    elif s2w_partner == "Carl":
        carl "See you, Chelsea!"
        carl "She's exactly as I remember."
    elif s2w_partner == "Noah":
        noah "See you, Chelsea!"
        noah "She's exactly as I remember."
    elif s2w_partner == "Elisa":
        elijah "See you, Chelsea!"
        elijah "She's exactly as I remember."

    s2w_mc "Hard to forget."

    # IF STATEMENT
    if s2w_partner != "Bobby":
        show bobby at npc_2
        "The smell of fresh bread and cakes wafts in your direction, as a familiar figure cuts across the crowd towards you."
        bobby "Oh hey! Look who it is. "
        "Quick as a flash, Bobby prods your nose. "
        bobby "Boop!"

        # CHOICE
        menu:
            "Bobby booped me…"
            "Give him a massive hug":
                "You laugh as you wrap your arms around him and squeeze tightly."
                bobby "I've missed you, [s2w_mc_name]."
                s2w_mc "I missed you and your silliness, too!"
            "Don't respond":
                # FILL
                pass
            "Sneeze suddenly":
                # FILL
                pass
            "Boop him back.":
                "You look at him for a moment, then quickly dart your finger out towards his nose. "
                "It makes contact with his soft skin…"
                s2w_mc "Boop."
                "The others gasp and then silence follows. "
                bobby "… I was booped?"
                bobby "Finally! Why has no one done that before?"

        # IF STATEMENT
        if s2w_partner == "Gary":
            gary "Where is my boop?"
            bobby "Boops are reserved for a select few, like [s2w_mc_name]."
            bobby "If I gave them out to everyone, they wouldn't be special, would they?"
            "[s2w_partner] rubs his own nose."
            gary "Alright, fair enough. How're you doing, cake man?"
            bobby "How'd you know?"
            s2w_mc "Know what?"
            bobby "What I'm going to call my bakery! The cake man."
            gary "Your bakery?"
        elif s2w_partner == "Rahim":
            rahim "Where is my boop?"
            bobby "Boops are reserved for a select few, like [s2w_mc_name]."
            bobby "If I gave them out to everyone, they wouldn't be special, would they?"
            "[s2w_partner] rubs his own nose."
            rahim "Alright, fair enough. How're you doing, cake man?"
            bobby "How'd you know?"
            s2w_mc "Know what?"
            bobby "What I'm going to call my bakery! The cake man."
            rahim "Your bakery?"
        elif s2w_partner == "Marisol":
            marisol "Where is my boop?"
            bobby "Boops are reserved for a select few, like [s2w_mc_name]."
            bobby "If I gave them out to everyone, they wouldn't be special, would they?"
            "[s2w_partner] rubs his own nose."
            marisol "Alright, fair enough. How're you doing, cake man?"
            bobby "How'd you know?"
            s2w_mc "Know what?"
            bobby "What I'm going to call my bakery! The cake man."
            marisol "Your bakery?"
        elif s2w_partner == "Lucas":
            lucas "Where is my boop?"
            bobby "Boops are reserved for a select few, like [s2w_mc_name]."
            bobby "If I gave them out to everyone, they wouldn't be special, would they?"
            "[s2w_partner] rubs his own nose."
            lucas "Alright, fair enough. How're you doing, cake man?"
            bobby "How'd you know?"
            s2w_mc "Know what?"
            bobby "What I'm going to call my bakery! The cake man."
            lucas "Your bakery?"
        elif s2w_partner == "Henrik":
            henrik "Where is my boop?"
            bobby "Boops are reserved for a select few, like [s2w_mc_name]."
            bobby "If I gave them out to everyone, they wouldn't be special, would they?"
            "[s2w_partner] rubs his own nose."
            henrik "Alright, fair enough. How're you doing, cake man?"
            bobby "How'd you know?"
            s2w_mc "Know what?"
            bobby "What I'm going to call my bakery! The cake man."
            henrik "Your bakery?"
        elif s2w_partner == "Jakub":
            jakub "Where is my boop?"
            bobby "Boops are reserved for a select few, like [s2w_mc_name]."
            bobby "If I gave them out to everyone, they wouldn't be special, would they?"
            "[s2w_partner] rubs his own nose."
            jakub "Alright, fair enough. How're you doing, cake man?"
            bobby "How'd you know?"
            s2w_mc "Know what?"
            bobby "What I'm going to call my bakery! The cake man."
            jakub "Your bakery?"
        elif s2w_partner == "Arjun":
            arjun "Where is my boop?"
            bobby "Boops are reserved for a select few, like [s2w_mc_name]."
            bobby "If I gave them out to everyone, they wouldn't be special, would they?"
            "[s2w_partner] rubs his own nose."
            arjun "Alright, fair enough. How're you doing, cake man?"
            bobby "How'd you know?"
            s2w_mc "Know what?"
            bobby "What I'm going to call my bakery! The cake man."
            arjun "Your bakery?"
        elif s2w_partner == "Kassam":
            kassam "Where is my boop?"
            bobby "Boops are reserved for a select few, like [s2w_mc_name]."
            bobby "If I gave them out to everyone, they wouldn't be special, would they?"
            "[s2w_partner] rubs his own nose."
            kassam "Alright, fair enough. How're you doing, cake man?"
            bobby "How'd you know?"
            s2w_mc "Know what?"
            bobby "What I'm going to call my bakery! The cake man."
            kassam "Your bakery?"
        elif s2w_partner == "Felix":
            felix "Where is my boop?"
            bobby "Boops are reserved for a select few, like [s2w_mc_name]."
            bobby "If I gave them out to everyone, they wouldn't be special, would they?"
            "[s2w_partner] rubs his own nose."
            felix "Alright, fair enough. How're you doing, cake man?"
            bobby "How'd you know?"
            s2w_mc "Know what?"
            bobby "What I'm going to call my bakery! The cake man."
            felix "Your bakery?"  
        elif s2w_partner == "Elijah":
            elijah "Where is my boop?"
            bobby "Boops are reserved for a select few, like [s2w_mc_name]."
            bobby "If I gave them out to everyone, they wouldn't be special, would they?"
            "[s2w_partner] rubs his own nose."
            elijah "Alright, fair enough. How're you doing, cake man?"
            bobby "How'd you know?"
            s2w_mc "Know what?"
            bobby "What I'm going to call my bakery! The cake man."
            elijah "Your bakery?"
        elif s2w_partner == "Carl":
            carl "Where is my boop?"
            bobby "Boops are reserved for a select few, like [s2w_mc_name]."
            bobby "If I gave them out to everyone, they wouldn't be special, would they?"
            "[s2w_partner] rubs his own nose."
            carl "Alright, fair enough. How're you doing, cake man?"
            bobby "How'd you know?"
            s2w_mc "Know what?"
            bobby "What I'm going to call my bakery! The cake man."
            carl "Your bakery?"
        elif s2w_partner == "Noah":
            noah "Where is my boop?"
            bobby "Boops are reserved for a select few, like [s2w_mc_name]."
            bobby "If I gave them out to everyone, they wouldn't be special, would they?"
            "[s2w_partner] rubs his own nose."
            noah "Alright, fair enough. How're you doing, cake man?"
            bobby "How'd you know?"
            s2w_mc "Know what?"
            bobby "What I'm going to call my bakery! The cake man."
            noah "Your bakery?"
        elif s2w_partner == "Elisa":
            elisa "Where is my boop?"
            bobby "Boops are reserved for a select few, like [s2w_mc_name]."
            bobby "If I gave them out to everyone, they wouldn't be special, would they?"
            "[s2w_partner] rubs his own nose."
            elisa "Alright, fair enough. How're you doing, cake man?"
            bobby "How'd you know?"
            s2w_mc "Know what?"
            bobby "What I'm going to call my bakery! The cake man."
            elisa "Your bakery?"

        bobby "That's the plan. I've decided to open a shop of my own."

        # CHOICE
        menu:
            "Bobby wants to open his own bakery…"
            "I should have expected that":
                bobby "Hey, I like what I like, and that happens to be cakes and the making of them. "
            "Do you ever get sick of cakes?":
                # FILL
                pass
            "It should be called Bobby's Boops":
                bobby "You're right!"
                bobby "I need to call my neon sign guy first thing tomorrow morning."

        bobby "But look, don't let me steal you for the whole night."
        bobby "The others have been champing at the bit waiting for you two!"
        bobby "I just couldn't resist that nose of yours, [s2w_mc_name], and I'm not exactly patient."
        bobby "I'll see you in a bit!"
        "He does an energetic jig towards a plate of cocktail sausages on toothpicks."
        show bobby at npc_exit

        if s2w_partner == "Gary":
            gary "I'm glad Bobby's not changed a bit."
            # said from across the room
            # close up
            bobby "How many of these sausages do you think I can fit in my mouth, Chelsea?"
            gary "Not one bit."
        elif s2w_partner == "Rahim":
            rahim "I'm glad Bobby's not changed a bit."
            # said from across the room
            bobby "How many of these sausages do you think I can fit in my mouth, Chelsea?"
            rahim "Not one bit."
        elif s2w_partner == "Marisol":
            marisol "I'm glad Bobby's not changed a bit."
            # said from across the room
            bobby "How many of these sausages do you think I can fit in my mouth, Chelsea?"
            marisol "Not one bit."
        elif s2w_partner == "Lucas":
            lucas "I'm glad Bobby's not changed a bit."
            # said from across the room
            bobby "How many of these sausages do you think I can fit in my mouth, Chelsea?"
            lucas "Not one bit."
        elif s2w_partner == "Henrik":
            henrik "I'm glad Bobby's not changed a bit."
            # said from across the room
            bobby "How many of these sausages do you think I can fit in my mouth, Chelsea?"
            henrik "Not one bit."
        elif s2w_partner == "Jakub":
            jakub "I'm glad Bobby's not changed a bit."
            # said from across the room
            bobby "How many of these sausages do you think I can fit in my mouth, Chelsea?"
            jakub "Not one bit."
        elif s2w_partner == "Arjun":
            arjun "I'm glad Bobby's not changed a bit."
            # said from across the room
            bobby "How many of these sausages do you think I can fit in my mouth, Chelsea?"
            arjun "Not one bit."
        elif s2w_partner == "Kassam":
            kassam "I'm glad Bobby's not changed a bit."
            # said from across the room
            bobby "How many of these sausages do you think I can fit in my mouth, Chelsea?"
            kassam "Not one bit."
        elif s2w_partner == "Felix":
            felix "I'm glad Bobby's not changed a bit."
            # said from across the room
            bobby "How many of these sausages do you think I can fit in my mouth, Chelsea?"
            felix "Not one bit."
        elif s2w_partner == "Elijah":
            elijah "I'm glad Bobby's not changed a bit."
            # said from across the room
            bobby "How many of these sausages do you think I can fit in my mouth, Chelsea?"
            elijah "Not one bit."
        elif s2w_partner == "Carl":
            carl "I'm glad Bobby's not changed a bit."
            # said from across the room
            bobby "How many of these sausages do you think I can fit in my mouth, Chelsea?"
            carl "Not one bit."
        elif s2w_partner == "Noah":
            noah "I'm glad Bobby's not changed a bit."
            # said from across the room
            bobby "How many of these sausages do you think I can fit in my mouth, Chelsea?"
            noah "Not one bit."
        elif s2w_partner == "Elisa":
            elisa "I'm glad Bobby's not changed a bit."
            # said from across the room
            bobby "How many of these sausages do you think I can fit in my mouth, Chelsea?"
            elisa "Not one bit."

    # IF STATEMENT
    if s2w_partner == "Bobby":
        bobby "Right, who should we say hi to first?"
    elif s2w_partner == "Gary":
        gary "Right, who should we say hi to first?"
    elif s2w_partner == "Rahim":
        rahim "Right, who should we say hi to first?"
    elif s2w_partner == "Marisol":
        marisol "Right, who should we say hi to first?"
    elif s2w_partner == "Lucas":
        lucas "Right, who should we say hi to first?"
    elif s2w_partner == "Henrik":
        henrik "Right, who should we say hi to first?"
    elif s2w_partner == "Jakub":
        jakub "Right, who should we say hi to first?"
    elif s2w_partner == "Arjun":
        arjun "Right, who should we say hi to first?"
    elif s2w_partner == "Kassam":
        kassam "Right, who should we say hi to first?"
    elif s2w_partner == "Felix":
        felix "Right, who should we say hi to first?"
    elif s2w_partner == "Elijah":
        elijah "Right, who should we say hi to first?"
    elif s2w_partner == "Carl":
        carl "Right, who should we say hi to first?"
    elif s2w_partner == "Noah":
        noah "Right, who should we say hi to first?"
    elif s2w_partner == "Elisa":
        elisa "Right, who should we say hi to first?"

    jump s2wp1_talk_to_who

label s2wp1_talk_to_who:
    # CHOICE
    menu:
        "I'd like to speak to…"
        "Priya, Rocco, Lottie" if 'Priya' not in s2wp1_talked_to:
            jump s2wp1_talk_to_priya_rocco_lottie
        "Henrik, Lucas, Jakub, Marisol" if ('Henrik' not in s2wp1_talked_to and s2w_partner != 'Lucas') or  ('Henrik' not in s2wp1_talked_to and s2w_partner != 'Henrik') or ('Henrik' not in s2wp1_talked_to and s2w_partner != 'Marisol') or ('Henrik' not in s2wp1_talked_to and s2w_partner != 'Jakub'):
            jump s2wp1_talk_to_henrik_lucas_jakub_marisol
        "Hope, Noah, Hannah, Shannon" if 'Hope' not in s2wp1_talked_to:
            jump s2wp1_talk_to_hope_noah_hannah_shannon
        "Gary, Ibrahim, Jo" if ('Gary' not in s2wp1_talked_to and s2w_partner != 'Rahim') or ('Gary' not in s2wp1_talked_to and s2w_partner != 'Gary'):
            jump s2wp1_talk_to_gary_ibrahim_jo
    # else:
        # jump #FILL

label s2wp1_talk_to_priya_rocco_lottie:
    # Priya, Rocco, Lottie
    $ s2wp1_talked_to.append("Priya")
    
    show priya at npc_1
    show rocco at npc_2
    show lottie at npc_3

    "You and [s2w_partner] walk up to the group as Rocco is in the middle of his sentence."
    rocco "And then things got really intense after I remembered about the clown suit i had in the trunk…"
    priya "Look who's here!"
    rocco "Oh, OK, I'll finish the story later."
    lottie "[s2w_mc_name] and [s2w_partner]!"
    priya "So glad you guys are finally here!"
    "You all fold into a large group hug."

    # IF STATEMENT
    if s2w_partner == "Bobby":
        bobby "It's so great seeing you all! What have you been up to?"
        priya "Well, I arrived here a little late. Got a few down me, then danced with…"
        bobby "I meant while we've been out of the Villa."
    elif s2w_partner == "Gary":
        gary "It's so great seeing you all! What have you been up to?"
        priya "Well, I arrived here a little late. Got a few down me, then danced with…"
        gary "I meant while we've been out of the Villa."
    elif s2w_partner == "Rahim":
        rahim "It's so great seeing you all! What have you been up to?"
        priya "Well, I arrived here a little late. Got a few down me, then danced with…"
        rahim "I meant while we've been out of the Villa."
    elif s2w_partner == "Marisol":
        marisol "It's so great seeing you all! What have you been up to?"
        priya "Well, I arrived here a little late. Got a few down me, then danced with…"
        marisol "I meant while we've been out of the Villa."
    elif s2w_partner == "Lucas":
        lucas "It's so great seeing you all! What have you been up to?"
        priya "Well, I arrived here a little late. Got a few down me, then danced with…"
        lucas "I meant while we've been out of the Villa."
    elif s2w_partner == "Henrik":
        henrik "It's so great seeing you all! What have you been up to?"
        priya "Well, I arrived here a little late. Got a few down me, then danced with…"
        henrik "I meant while we've been out of the Villa."
    elif s2w_partner == "Jakub":
        jakub "It's so great seeing you all! What have you been up to?"
        priya "Well, I arrived here a little late. Got a few down me, then danced with…"
        jakub "I meant while we've been out of the Villa."
    elif s2w_partner == "Arjun":
        arjun "It's so great seeing you all! What have you been up to?"
        priya "Well, I arrived here a little late. Got a few down me, then danced with…"
        arjun "I meant while we've been out of the Villa."
    elif s2w_partner == "Kassam":
        kassam "It's so great seeing you all! What have you been up to?"
        priya "Well, I arrived here a little late. Got a few down me, then danced with…"
        kassam "I meant while we've been out of the Villa."
    elif s2w_partner == "Felix":
        felix "It's so great seeing you all! What have you been up to?"
        priya "Well, I arrived here a little late. Got a few down me, then danced with…"
        felix "I meant while we've been out of the Villa."   
    elif s2w_partner == "Elijah":
        elijah "It's so great seeing you all! What have you been up to?"
        priya "Well, I arrived here a little late. Got a few down me, then danced with…"
        elijah "I meant while we've been out of the Villa."
    elif s2w_partner == "Carl":
        carl "It's so great seeing you all! What have you been up to?"
        priya "Well, I arrived here a little late. Got a few down me, then danced with…"
        carl "I meant while we've been out of the Villa."
    elif s2w_partner == "Noah":
        noah "It's so great seeing you all! What have you been up to?"
        priya "Well, I arrived here a little late. Got a few down me, then danced with…"
        noah "I meant while we've been out of the Villa."
    elif s2w_partner == "Elisa":
        elisa "It's so great seeing you all! What have you been up to?"
        priya "Well, I arrived here a little late. Got a few down me, then danced with…"
        elisa "I meant while we've been out of the Villa."

    priya "Oooh."
    priya "I've actually been trying to get out of property. I've decided selling fashion is more glamorous than houses."
    priya "And I'm all about the glam."

# CHOICE
    menu:
        "Priya's been trying to get into fashion…"
        "Yay! That's so you":
            priya "Right?"
            priya "I just wish I'd had the courage to do it sooner!"
        "That seems risky":
            priya "It is!"
            priya "But what's life without a few risks?"
            priya "Boring! That's what."
        "How's it going?":
            priya "It's hard!"
            priya "Not the selling part. I've always been good at that."
            priya "But actually having to learn to sew to work out the designs is tough."

    rocco "Damn, Priya, you're so amazing. How'd we never couple up?"
    priya "Probably because you grafted on every girl in the Villa behind our backs?"
    rocco "Oh, um… yeah."
    lottie "She got you there."
    s2w_mc "So what have you been up to, Rocco?"
    rocco "I was just telling these guys…"
    rocco "I've been mixing up my cocktail menu for the van."
    rocco "I've been trying to recreate the various fragrances of the Villa's dressing room."
    rocco "Some have done better than others…"

    # CHOICE
    menu:
        "Rocco's been creating new cocktails…"
        "That sounds delish!":
            rocco "thanks!"
            rocco "It's been a nice distraction on quieter days."
        "You've not done anything else?":
            rocco "Um, not really"
            rocco "Other than trying to write some songs on my guitar."
            rocco "Cocktail creation is hard."
        "What's the most popular?":
            rocco "So far the strawberry is!"
            rocco "But that could just be because it's basically a regular daiquiri."

    # IF STATEMENT
    if s2w_partner == "Bobby":
        bobby "What's gone down the worst?"
    elif s2w_partner == "Gary":
        gary "What's gone down the worst?"
    elif s2w_partner == "Rahim":
        rahim "What's gone down the worst?"
    elif s2w_partner == "Marisol":
        marisol "What's gone down the worst?"
    elif s2w_partner == "Lucas":
        lucas "What's gone down the worst?"
    elif s2w_partner == "Henrik":
        henrik "What's gone down the worst?"
    elif s2w_partner == "Jakub":
        jakub "What's gone down the worst?"
    elif s2w_partner == "Arjun":
        arjun "What's gone down the worst?"
    elif s2w_partner == "Kassam":
        kassam "What's gone down the worst?"
    elif s2w_partner == "Felix":
        felix "What's gone down the worst?"
    elif s2w_partner == "Elijah":
        elijah "What's gone down the worst?"
    elif s2w_partner == "Carl":
        carl "What's gone down the worst?"
    elif s2w_partner == "Noah":
        noah "What's gone down the worst?"
    elif s2w_partner == "Elisa":
        elisa "What's gone down the worst?"

    rocco "Hairspray flavoured."
    lottie "Ugh!"
    rocco "Yeah, I don't know what I was thinking. Though, it really did taste like hairspray."
    lottie "Speaking of hairspray…"
    lottie "I've been approached by someone big to become their personal stylist!"

    # IF STATEMENT
    if s2w_partner == "Bobby":
        bobby "Whaaat? Who?!"
        lottie "I can't say. Not yet. But they're American and you'd know them if I said."
        bobby "That doesn't narrow it down."
    elif s2w_partner == "Gary":
        gary "Whaaat? Who?!"
        lottie "I can't say. Not yet. But they're American and you'd know them if I said."
        gary "That doesn't narrow it down."
    elif s2w_partner == "Rahim":
        rahim "Whaaat? Who?!"
        lottie "I can't say. Not yet. But they're American and you'd know them if I said."
        rahim "That doesn't narrow it down."
    elif s2w_partner == "Marisol":
        marisol "Whaaat? Who?!"
        lottie "I can't say. Not yet. But they're American and you'd know them if I said."
        marisol "That doesn't narrow it down."
    elif s2w_partner == "Lucas":
        marisol "Whaaat? Who?!"
        lottie "I can't say. Not yet. But they're American and you'd know them if I said."
        marisol "That doesn't narrow it down."
    elif s2w_partner == "Henrik":
        henrik "Whaaat? Who?!"
        lottie "I can't say. Not yet. But they're American and you'd know them if I said."
        henrik "That doesn't narrow it down."
    elif s2w_partner == "Jakub":
        jakub "Whaaat? Who?!"
        lottie "I can't say. Not yet. But they're American and you'd know them if I said."
        jakub "That doesn't narrow it down."
    elif s2w_partner == "Arjun":
        arjun "Whaaat? Who?!"
        lottie "I can't say. Not yet. But they're American and you'd know them if I said."
        arjun "That doesn't narrow it down."
    elif s2w_partner == "Kassam":
        kassam "Whaaat? Who?!"
        lottie "I can't say. Not yet. But they're American and you'd know them if I said."
        kassam "That doesn't narrow it down."
    elif s2w_partner == "Felix":
        felix "Whaaat? Who?!"
        lottie "I can't say. Not yet. But they're American and you'd know them if I said."
        felix "That doesn't narrow it down."
    elif s2w_partner == "Elijah":
        elijah "Whaaat? Who?!"
        lottie "I can't say. Not yet. But they're American and you'd know them if I said."
        elijah "That doesn't narrow it down."
    elif s2w_partner == "Carl":
        carl "Whaaat? Who?!"
        lottie "I can't say. Not yet. But they're American and you'd know them if I said."
        carl "That doesn't narrow it down."
    elif s2w_partner == "Noah":
        noah "Whaaat? Who?!"
        lottie "I can't say. Not yet. But they're American and you'd know them if I said."
        noah "That doesn't narrow it down."
    elif s2w_partner == "Elisa":
        elisa "Whaaat? Who?!"
        lottie "I can't say. Not yet. But they're American and you'd know them if I said."
        elisa "That doesn't narrow it down."

    lottie "That's the point!"

    # CHOICE
    menu:
        "A famous American wants Lottie to be their personal stylist…"
        "That's incredible!":
            lottie "Right?!"
            lottie "I still can't believe it."
        "Tell us who it is!":
            lottie "Babe, don't ask again. I already said I can't."
            lottie "Besides, it doesn't matter who, just that it's happening!"
        "I can see why. You always look hot.":
            # IF STATEMENT
            if s2w_secret_moment == 'Lottie':
                "Lottie's face blushes again, though, that could just be her make up."
                "She lets out a little cough."
                lottie "Um, thanks, babe…"
            else:
                lottie "I know. I'm just glad someone's actually recognised that."
        "Is it the president?":
            lottie "What? No! Ew."

    # IF STATEMENT
    if s2w_partner == "Bobby":
        bobby "Wait, does that mean you're moving to America?"
    elif s2w_partner == "Gary":
        gary "Wait, does that mean you're moving to America?"
    elif s2w_partner == "Rahim":
        rahim "Wait, does that mean you're moving to America?"
    elif s2w_partner == "Marisol":
        marisol "Wait, does that mean you're moving to America?"
    elif s2w_partner == "Lucas":
        lucas "Wait, does that mean you're moving to America?"
    elif s2w_partner == "Henrik":
        henrik "Wait, does that mean you're moving to America?"
    elif s2w_partner == "Jakub":
        jakub "Wait, does that mean you're moving to America?"
    elif s2w_partner == "Arjun":
        arjun "Wait, does that mean you're moving to America?"
    elif s2w_partner == "Kassam":
        kassam "Wait, does that mean you're moving to America?"
    elif s2w_partner == "Felix":
        felix "Wait, does that mean you're moving to America?"   
    elif s2w_partner == "Elijah":
        elijah "Wait, does that mean you're moving to America?"
    elif s2w_partner == "Carl":
        carl "Wait, does that mean you're moving to America?"
    elif s2w_partner == "Noah":
        noah "Wait, does that mean you're moving to America?"
    elif s2w_partner == "Elisa":
        elisa "Wait, does that mean you're moving to America?"    

    lottie "It does!"
    priya "Wait, what?"
    lottie "Sorry guys. This wasn't an easy decision, but I've got that wanderlust again."
    lottie "And when it happens, I need to move on."

    # CHOICE
    menu:
        "Lottie's moving to America soon…"
        "I'm so thrilled for you!":
            lottie "Thanks, babes!"
            lottie "I knew you'd understand. "
        "Don't forget to write":
            lottie "I promise to leave secret messages in my client's outfits that you'll see in magazines and know are from me."
            priya "Texting is also a thing, yeah?"
        "What will I do without my witch queen?":
            lottie "Well, for one, have a lot fewer black clothes in your life."
            lottie "And I guess just generally be sad, right?"
        "No…":
            "She sends a loving smile your way"
            lottie "Hey babe, don't fret. It's not like we won't see each other."
            lottie "I'll just be going to sleep when you are waking up, is all."

    lottie "But let's not think about it right now! Tonight's about partying!"
    rocco "Now that I can get behind."
    "After a few more minutes, Rocco gets distracted by canapés and Lottie goes to the bar. The group disperses."

    show lottie at npc_exit
    show rocco at npc_exit
    show priya at npc_exit

    jump s2wp1_talk_to_who
    # if len(s2wp1_talked_to) == 4:
    #     # FILL
    #     pass
    #     # jump s2wp1_talk_to_who
    # else:
    #     jump s2wp1_talk_to_who

label s2wp1_talk_to_henrik_lucas_jakub_marisol:
    # Henrik, Lucas, Jakub, Marisol

    show lucas at npc_1
    show jakub at npc_2
    show marisol at npc_3

    "You and [s2w_partner] make your way over to the group, who are deep in conversation"
    lucas "Did you guys see Arjun and Elijah's Insta story earlier?"
    lucas "They look like they're having the best time in Malta."
    jakub "It's well cute."
    marisol "So obvious they'd end up together."
    marisol "There were always longing glances."

    show marisol at npc_exit
    show henrik at npc_3

    "Henrik sees you and [s2w_partner] approach."
    henrik "Hey you two!"
    henrik "I was wondering when we'd get to catch up."

    # CHOICE
    menu:
        "How has…"
        "Henrik's hair got more lush?":
            henrik "I just use natural water."
            jakub "Natural water? Isn't all water natural?"
            henrik "No, like waterfalls and streams. Gives my hair a nice sheen."
            jakub "Gross."

            show henrik at npc_exit
            show marisol at npc_3
        "Lucas' face got more chiselled?":
            lucas "I've been getting really good at chin ups"
            "The others groan."
            "[s2w_partner] theatrically clutches at his chest."
            # IF STATEMENT
            if s2w_partner == "Bobby":
                bobby "A man after my own heart."
            elif s2w_partner == "Gary":
                gary "A man after my own heart."
            elif s2w_partner == "Rahim":
                rahim "A man after my own heart."
            elif s2w_partner == "Arjun":
                arjun "A man after my own heart."
            elif s2w_partner == "Kassam":
                kassam "A man after my own heart."
            elif s2w_partner == "Felix":
                felix "A man after my own heart."  
            elif s2w_partner == "Elijah":
                elijah "A man after my own heart."
            elif s2w_partner == "Carl":
                carl "A man after my own heart."
            elif s2w_partner == "Noah":
                noah "A man after my own heart."
            elif s2w_partner == "Elisa":
                elisa "A man after my own heart."
            
            show henrik at npc_exit
            show marisol at npc_3

            marisol "I'm pretty sure he's just shaved extra close today."
            lucas "Guilty as charged."
        "Jakub got more buff":
            "He flexes"
            jakub "A body like this needs constant work to maintain it."
            jakub "I'm not going to make it as a professional bodybuilder if I slack off."
            lucas "The fact he's wearing a shirt four sizes too small doesn't hurt either."

            show henrik at npc_exit
            show marisol at npc_3
        "Marisol's eyebrow game improved?":
            show henrik at npc_exit
            show marisol at npc_3

            "She raises her eyebrow at you."
            marisol "Practice, babe."
            marisol "I thought it would be a good tool to use on clients."
            henrik "It's the same as if Jakub flexed at people during a meeting."
            "Jakub flexes."
            jakub "Marisol gets it."

    marisol "Oh! Lucas, you should tell them about what you and Henrik got up to before the reunion."
    jakub "Yeah, that was an unbelievable story."

    # IF STATEMENT
    if s2w_partner == "Bobby":
        bobby "What happened?"
    elif s2w_partner == "Gary":
        gary "What happened?"
    elif s2w_partner == "Rahim":
        rahim "What happened?"
    elif s2w_partner == "Arjun":
        arjun "What happened?"
    elif s2w_partner == "Kassam":
        kassam "What happened?"
    elif s2w_partner == "Felix":
        felix "What happened?"
    elif s2w_partner == "Elijah":
        elijah "What happened?"
    elif s2w_partner == "Carl":
        carl "What happened?"
    elif s2w_partner == "Noah":
        noah "What happened?"
    elif s2w_partner == "Elisa":
        elisa "What happened?"

    lucas "It wasn't that weird. Just a funny coincidence."
    lucas "I'd decided to go biking around the Alps after the show. To clear my head and get away for a while. "
    lucas "One day I'm riding down this deserted little back country road…"
    lucas "When all of a sudden this guy walks out of a bush in front of me."

    show marisol at npc_exit
    show henrik at npc_3

    henrik "It was me!"
    lucas "Mate! Dramatic tension. I was getting to that."
    lucas "But yeah, it was Henrik."
    henrik "I'd decided to go climbing in the Alps. After bumping into each other, we decided to do a roadtrip. "
    henrik "I tried to teach Lucas how to climb."
    lucas "My bum's still sore from all the falling I did."

    # CHOICE
    menu:
        "Lucas and Henrik bumped into each other in the Alps!"
        "That's so sweet!":
            lucas "It was pretty great, yeah. We had an amazing time together."
        "What are the odds?":
            lucas "Probably too high a number to count to, that's for sure."
        "You had to have planned it":
            henrik "I swear we didn't!"
            jakub "It was fate."

    # IF STATEMENT
    if s2w_partner == "Bobby":
        bobby "And Jakub, it looks like you've been hitting the gym non-stop still."
    elif s2w_partner == "Gary":
        gary "And Jakub, it looks like you've been hitting the gym non-stop still."
    elif s2w_partner == "Rahim":
        rahim "And Jakub, it looks like you've been hitting the gym non-stop still."
    elif s2w_partner == "Arjun":
        arjun "And Jakub, it looks like you've been hitting the gym non-stop still."
    elif s2w_partner == "Kassam":
        kassam "And Jakub, it looks like you've been hitting the gym non-stop still."
    elif s2w_partner == "Felix":
        felix "And Jakub, it looks like you've been hitting the gym non-stop still."
    elif s2w_partner == "Elijah":
        elijah "And Jakub, it looks like you've been hitting the gym non-stop still."
    elif s2w_partner == "Carl":
        carl "And Jakub, it looks like you've been hitting the gym non-stop still."
    elif s2w_partner == "Noah":
        noah "And Jakub, it looks like you've been hitting the gym non-stop still."
    elif s2w_partner == "Elisa":
        elisa "And Jakub, it looks like you've been hitting the gym non-stop still."

    jakub "Pretty much. Had a couple of health magazines ask me to model for them."

    # CHOICE
    menu:
        "Jakub modelled for health magazines…"
        "That sounds so fun!":
            jakub "It was! They got me to do a bunch of different poses."
            jakub "In the end, they just used my 'neutral' pose."
        "That's so you it hurts":
            marisol "Yeah, to be fair, I'm surprised you weren't already doing that. "
            jakub "Who says I wasn't?"
        "I saw it! You were dressed like a bull!":
            jakub "I the China shop. Yeah. That was me. "
            jakub "They thought it made sense after my time in the Villa…"

    # IF STATEMENT
    if s2w_partner == "Bobby":
        bobby "And what about you, Marisol?"
    elif s2w_partner == "Gary":
        gary "And what about you, Marisol?"
    elif s2w_partner == "Rahim":
        rahim "And what about you, Marisol?"
    elif s2w_partner == "Arjun":
        arjun "And what about you, Marisol?"
    elif s2w_partner == "Kassam":
        kassam "And what about you, Marisol?"
    elif s2w_partner == "Felix":
        felix "And what about you, Marisol?"
    elif s2w_partner == "Elijah":
        elijah "And what about you, Marisol?"
    elif s2w_partner == "Carl":
        carl "And what about you, Marisol?"
    elif s2w_partner == "Noah":
        noah "And what about you, Marisol?"
    elif s2w_partner == "Elisa":
        elisa "And what about you, Marisol?"
    
    show jakub at npc_exit
    show marisol at npc_2

    marisol "Oh, nothing interesting. I've just been studying hard. "
    marisol "When can I have another month-long holiday? Back to the Villa, anyone?"
    
    # IF STATEMENT
    if s2w_partner == "Bobby":
    # CHOICE
        menu:
            "I want another month in the Villa?"
            "Sign me up!":
                marisol "Yes!"
                marisol "Maybe this time I'd even find someone…"
            "We could go on holiday together":
                marisol "That'd be great!"
                bobby "Yeah, I'd love that."
            "I'd rather go somewhere new":
                bobby "Yeah. I think one month in the Villa is enough for a lifetime"
    elif s2w_partner == "Gary":
    # CHOICE
        menu:
            "I want another month in the Villa?"
            "Sign me up!":
                marisol "Yes!"
                marisol "Maybe this time I'd even find someone…"
            "We could go on holiday together":
                marisol "That'd be great!"
                gary "Yeah, I'd love that."
            "I'd rather go somewhere new":
                gary "Yeah. I think one month in the Villa is enough for a lifetime"
    elif s2w_partner == "Rahim":
    # CHOICE
        menu:
            "I want another month in the Villa?"
            "Sign me up!":
                marisol "Yes!"
                marisol "Maybe this time I'd even find someone…"
            "We could go on holiday together":
                marisol "That'd be great!"
                rahim "Yeah, I'd love that."
            "I'd rather go somewhere new":
                rahim "Yeah. I think one month in the Villa is enough for a lifetime"
    elif s2w_partner == "Arjun":
    # CHOICE
        menu:
            "I want another month in the Villa?"
            "Sign me up!":
                marisol "Yes!"
                marisol "Maybe this time I'd even find someone…"
            "We could go on holiday together":
                marisol "That'd be great!"
                arjun "Yeah, I'd love that."
            "I'd rather go somewhere new":
                arjun "Yeah. I think one month in the Villa is enough for a lifetime"
    elif s2w_partner == "Kassam":
    # CHOICE
        menu:
            "I want another month in the Villa?"
            "Sign me up!":
                marisol "Yes!"
                marisol "Maybe this time I'd even find someone…"
            "We could go on holiday together":
                marisol "That'd be great!"
                kassam "Yeah, I'd love that."
            "I'd rather go somewhere new":
                kassam "Yeah. I think one month in the Villa is enough for a lifetime"
    elif s2w_partner == "Felix":
    # CHOICE
        menu:
            "I want another month in the Villa?"
            "Sign me up!":
                marisol "Yes!"
                marisol "Maybe this time I'd even find someone…"
            "We could go on holiday together":
                marisol "That'd be great!"
                felix "Yeah, I'd love that."
            "I'd rather go somewhere new":
                felix "Yeah. I think one month in the Villa is enough for a lifetime"
    elif s2w_partner == "Elijah":
    # CHOICE
        menu:
            "I want another month in the Villa?"
            "Sign me up!":
                marisol "Yes!"
                marisol "Maybe this time I'd even find someone…"
            "We could go on holiday together":
                marisol "That'd be great!"
                elijah "Yeah, I'd love that."
            "I'd rather go somewhere new":
                elijah  "Yeah. I think one month in the Villa is enough for a lifetime"
    elif s2w_partner == "Carl":
    # CHOICE
        menu:
            "I want another month in the Villa?"
            "Sign me up!":
                marisol "Yes!"
                marisol "Maybe this time I'd even find someone…"
            "We could go on holiday together":
                marisol "That'd be great!"
                carl "Yeah, I'd love that."
            "I'd rather go somewhere new":
                carl "Yeah. I think one month in the Villa is enough for a lifetime"
    elif s2w_partner == "Noah":
    # CHOICE
        menu:
            "I want another month in the Villa?"
            "Sign me up!":
                marisol "Yes!"
                marisol "Maybe this time I'd even find someone…"
            "We could go on holiday together":
                marisol "That'd be great!"
                noah "Yeah, I'd love that."
            "I'd rather go somewhere new":
                noah "Yeah. I think one month in the Villa is enough for a lifetime"
    elif s2w_partner == "Elisa":
    # CHOICE
        menu:
            "I want another month in the Villa?"
            "Sign me up!":
                marisol "Yes!"
                marisol "Maybe this time I'd even find someone…"
            "We could go on holiday together":
                marisol "That'd be great!"
                elisa "Yeah, I'd love that."
            "I'd rather go somewhere new":
                elisa "Yeah. I think one month in the Villa is enough for a lifetime"    
    
    "You chat for a while longer. Everyone seems happy to be back together again."

    jump s2wp1_talk_to_who

# -Hope, Noah, Hannah, Shannon
# 	"You walk up to the group as Shannon is in the middle of a story."
# --------If You went on a trip with Shannon-----------------
# Shannon: And then me and MC's paraglider blew off course and we ended up in the mayor's house!
# Noah: What?
# Hannah: That's so intense!
# Shannon: MC! I was just filling them in on Monaco. Remember the mayor's house?
# s2w_mc "Oh yeah she…"
# 	-Gave us the best lunch!
# 		Shannon: It was so good!
# 		Shannon: I'm glad she was so understanding
# 	-Was not happy
# 		Shannon: Can't really blame her. We did take out her bird bath, after all. 
# 	-Had the nicest curtains
# 		Shannon: She did! They were so plush. 
# Shannon: Shame we destroyed them after crashing through her window…
#  Noah: Sounds like you had an amazing adventure!

# -----If you went on holiday with Hope or did not go on a holiday with anyone------
# Shannon: …so yeah, I ran to the car, slammed the door, and sped away. I can never go back . 
# Shannon: It was a pretty tame holiday for me. 
# Shannon: Really needed a good travel partner, you know?
# "She turns to yo"
# Shannon: Oh, hey you guys!

# Hope: Hey, girl! So glad you made it. 
# s2w_mc "Hey guys!"
# Noah: Hannah, didn't I see something about you finishing your first draft of a novel?
# Hannah: Yeah!
# Hannah: Editing's really hard, though… It's worse than writing!
# Noah: I'm sure it'll be great
# Hannah: I'm just struggling with the ending at the moment. It doesn't feel right. I don't think I've been inspired properly yet. 
# MC thoughts: Hanna's struggling to end her novel…
# 	-Give it a surprise twist!
# 		Hannah: Nooo, that's so lame. 
# 		Hannah: Twists are so cheap. 
# 	-Make everyone fall in love
# 		Hannah: Like, literally everyone?
# 		s2w_mc "Why not?"
# 		"She thinks for a moment."
# 		Hannah: But why would the lake monster and judge suddenly fall in love?
# 	-make it descend into violence. 
# 		Noah: Damn, that's dark!
# 		"She thinks for a moment."
# 		Hannah: It could work, though. 
# 		Hannah: It'd definitely be cathartic for me!
# bobby "Speaking of books, I saw that you had some pretty exciting news, Noah?"
# Noah: Oh, it's nothing much. 
# Shannon: Don't be modest!
# Noah: Well, they put me in charge of revamping all the kids areas in our local libraries. 
# s2w_mc "That sounds…"
# 		-Right up your street
# 			Noah: They said it was because they saw how good I was with kids.
# 		-Like hard work
# 			Noah: It's not that bad. Kids are good at telling you what they want. 
# 			Noah: Though, I can't get them an actual spaceship or racecar…
# 		-super dull!
# 			Noah: What? No. 
# Noah: It's actually loads of fin! I get to mess around with fun designs all day.
# 	bobby "And what about you, Hope?"
# 	Hope: Oh, I've been designing a new range of toys at work!
# Hope: I never thought I'd be the one designing stuff, but so far it seems to be going well!
# # Thought
# "Hope's designing a new toy range. "
# 	-That sounds like so much fun!
# 		Hope: It is!
# Hope: Means I have to spend a lot of time around the kids testing them, though. 
# Hope: Luckily, I can just leave them in a room with toys and take notes. 
# Shannon: Nothing better than interacting with kids through science. 
# 	-Don't you have to be around kids for that?
# 		Hope: Yeah, it's a bit of a downside, not gonna lie. 
# Hope: Luckily, I can just leave them in a room with toys and take notes. 
# Shannon: Nothing better than interacting with kids through science. 
# 	-Make a Gary action figure
# 		Shannon: Yes! Give him a functional toy crane. 
# 		Hope: An Islander range? That sounds hilarious. 
# Noah: Well, if you'll excuse me, there are some mini-quiches with my name on them. 
# "The rest of you chat for a little while longer, before you and Bobby move on."

# -Gary, Ibrahim, Jo
# 	"Bobby dances his way across the room with you towards the others."
# 	rahim "Nice moves, Bobby. "
# bobby "Why walk when you can dance?"
# Jo: Come join us, guys. Gary was just telling us what he'd been up to. 
# gary "Oh, nothing much…"
# gary "Only had a morning TV show get in touch is all!"
# rahim "What for?"
# gary "They want me and nan to have an advice slot on it called ‘Gary and His Nan'!"
# # Thought
# "Gary's been given his own morning TV slot!"
# 	-That's incredible!
# 		bobby "Yeah, that's not what I was expecting at all!"
# 	-There's no escaping you
# 		gary "Tired of my mug, are you?"
# 	-I want advice from your nan!
# 		gary "So does the rest of the nation!"
# 		gary "I just wish she'd see that. "
# rahim "I honestly thought you were going to just say you'd been up a new crane or something. "
# gary "Oh mate, I have been. "
# gary "But there's only one thing more thrilling than being in the cab of a brand new EC-B tower crane, and that's getting a call from a TV company"
# Jo: What did your nan say?
# gary "She's not convinced. "
# gary "Every time I mention it, she sends me out to stand in the snow. "
# gary "Thank goodness it hasn't snowed yet. "
# rahim "You have to convince her!"
# gary "Yeah, I'm doing my best. Buth, what have you been up to, Rahim?"
# s2w_mc "Let me guess…"
# 	-You cosplayed as Violet Man
# 		rahim "You're bang on. I went to this great comic convention. "
# 		rahim "I posed for one too many photos and my suit ripped apart. "
# 		Jo: I told you to be careful flexing!
# 	-It was golf stuff, right?
# 		rahim "That was too easy. "
# 		rahim "…but you're not wrong. "
# 		"He turns to Jo."
# 		rahim "Am I really that predictable?"
# 		Jo: Well, you are a professional golf player, babe. 
# 		Jo: I don't think it's that hard to predict you'd be playing golf. 
# 	-You went in search of Blackbeard's treasure?
# 		rahim "… I did not. "
# 		rahim "But now I really wish I had. Is that even a thing?"
# rahim "Oh, and I also got to see this one perform her sweet BMX skills around the world. "
# "He takes a hold of Jo's hand, she smiles at him."
# Jo: You should have seen Rahim during his last game, though. He sunk a birdie almost every hole!
# Jo: Even got a hole-in-one on the last!
# rahim "I did alright, but Jo's the real champ. She smashed her championship and came first!"
# Jo: I was just in the zone this year, that's all. 
# MC thoughts: Ibrahim and Jo have been watching each other compete and win…
# 	-It must be amazing to watch that
# Jo: Seeing the person you love doing their all and achieving is so rewarding!
# Jo: And hot…
# 	-Could you warn me next time there's this much cheese?
# 		gary "Yeah, usually the waiter asks you to say when. "
# 		rahim "I don't care if you think it's cheese. I've had a great time. "
# 	-I wonder if you could combine gold and BMXing
# 		bobby "Wouldn't that just be, like, extreme polo?"
# 		gary "Ah mate, extreme polo sounds mint!"
# 		Jo: We should give it a try, babe. 
# "After a little more chatter, the group disperses to get drinks and nibbles."

# "You look around at the Islanders mingling."
# MC thoughts: Right, I've waited long enough. 
# MC thoughts: It's time. 
# MC thoughts: How should I get everyone's attention?
# -Tap the side of your glass
# 	"You tap the side of your glass several times with a spoon."
# "The high-pitched dings ring out across the venue. Everyone turns to look at you."
# -Clap your hands loudly
# 	"You clap your hands together hard several times."
# "It takes the others a while to realise you're not just celebrating something."
# -Shout over the noise of everyone. 
# 	"You take a deep breath and yell loudly."
# 	s2w_mc "Oi! Everyone listen to me!"
# 	"Several Islanders jump and then turn to look at you, puzzled."
# Shannon: What's up babe?
# Shannon: Are you doing a speech?
# s2w_mc "Um, sort of…"
# "You turn to Bobby, who looks as confused as the others."
# MC thoughts: Here we go! 
# s2w_mc "Bobby…"
# 	-In the time I've known you…
# 	-Since first seeing you in the Villa…
# 	-Every since I fell for your silly face…
# s2w_mc "I've…"
# 	-Grown to love you more every day…
# 	-Not been able to keep you out of my mind…
# 	-Found it hard not to fall completely in love with you…
# Hannah: Is she…?
# lottie "No way. "
# s2w_mc "And so, Bobby…"
# 	-Go down on one knee
# 		"You take a knee and pull out the ring."
# 		"A chorus of gasps bounces around the roo"
# 		priya "It's happening!"
# 		Hannah: How'd I not see this coming?
# 		"Chelsea lets put a high-pitched squeal"
# 	-Stay standing
# 		"You take the ring box out while standing in front of Bobby."
# 	-Pull the ring out from behind his ear
# "You reach behind Bobby's ear, and return it with the ring clasped in your fingers."
# s2w_mc "Will you marry me?"
# "The room is silent, waiting for Bobby's answer. (Is different for other LIs) - but this is Bobby specific route tho :"
# "Bobby clasps his hands over his mouth in shock."
# "His eyes tear up."
# bobby "Yes! Yes I will, babe!"
# "He takes the ring and puts it on his finger."
# bobby "Woah that's tight!"
# s2w_mc "Huh?"
# bobby "Kidding! It's perfect. "
# "The room bursts into applause."
# chelsea "This. "
# chelsea "Is. "
# chelsea "Amazing!"
# MC thoughts: Me and Bobby are getting married!
# 	-Pull him in for a kiss
# "You wrap your fingers around the back of Bobby's neck and gently pull him towards yo"
# "You've kissed Bobby countless times, but something about this is different. It's electrifying."
# "You're no longer simply kissing your boyfriend."
# "You're kissing your fianc"
# -Give him a massive hug
# "You wrap your arms around Bobby's waist and pull him into a strong embrace."
# "In the warmth of his body, you feel safe and comforted."
# 	-Turn and cheer with the others. 
# 		"You turn, holding up Bobby's arm, and let out a loud cheer."
# 		"The others shout encouragement back at yo"
# 		lottie "Yes, girl!"
# 		chelsea "Agh! Too exciting!"
# "Your friends run up to you, giving you both a huge group hug."
# priya "Congrats, babe!"
# gary "Mate! Nice one. "
# chelsea "You have to let me help plan your wedding!!!"
# bobby "Of course!"
# "He turns to you."
# bobby "Let's start right away!"
# lottie "Aren't you rushing a bit?"
# bobby "Why wait? We should do it as soon as possible!"
# s2w_mc "Yeah, I like that!. Let's not mess about. Let's just do it!"
# Shannon: I guess first things first. 
# "She turns to you."
# Shannon: Who's going to be your maid of honour?
# Shannon: And who's going to be Bobby's best man?
# bobby "Wait, what if I also want a maid of honour?"
# lottie "Ugh, all these terms are so old fashioned. Why do we have so many?"
# lottie "Why not just call them Best Person and be done with it?"
# bobby "Hey, yeah! I like that. "
# bobby "Who do you want as your best person, babe?"
# s2w_mc "For my best person, I choose…"
# 	-Chelsea
# 		chelsea "Really?"
# 		chelsea "Agh!"
# 		chelsea "I…"
# chelsea "Have…"
# chelsea "All.."
# chelsea "the…"
# chelsea "Ideas!"
# chelsea "Whoa, I'm feeling faint!"
# lottie "You OK?"
# chelsea "Yeah! I'm fine now. Just got all fluttery!"
# 	-Shannon
# 		Shannon: Really?!
# 		Shannon: I won't let you down babe!
# 	-Ibrahim
# 		rahim "Really?!"
# 		rahim "I won't let you down, babe!"

# s2w_mc "What about you, babe? Who are you going to have as your best person?"
# bobby "I don't know! I'm stuck on my choice. "
# bobby "Who do you think it should be?"
# s2w_mc "Really? You want me to choose?"
# bobby "Yeah! I trust your judgement.. "
# "You go over to Bobby and whisper your recommendation."
# s2w_mc "You should pick…"
# 	-Marisol
# 		bobby "That's a great idea!"
# 		bobby "Hey, Marisol!"
# 		bobby "How would you like to be my best person?"
# 		marisol "I'd love to!"
# 		marisol "I need to find a better dress!"
# 	-Lucas
# bobby "That's a great idea!"
# 		bobby "Hey, Lucas!"
# 		bobby "How would you like to be my best person?"
# 		lucas "I'd love to!"
# 		lucas "I take it I can't wear my leather jacket to the ceremony?"
# 	-Gary
# 		bobby "That's a great idea!"
# 		bobby "Hey, Gary!"
# 		bobby "How would you like to be my best person?"
# 		gary "I'd love to!"
# 		gary "Oh mate… I need to get a better suit"

# lottie "By the way, I can totally do the wedding, too. "
# lottie "I've done one before. "
# rocco "Oh! I can do ceremonies too! I got a licence over the internet. "
# priya "Wait, if that's an option, I want to volunteer. "
# priya "I'd love to marry you two. "
# priya "As in, make you an official couple. Not like, marry both of you."
# Noah: I actually married two friends of mine a few summers back, so i could do it. 
# bobby "I love this! Babe, who should do it?"
# s2w_mc "I'm going to pick…"
# 	-Priya
# 	-Lottie
# 	-Rocco
# 	-Noah

# bobby "That's who I was going to pick! "
# bobby "We're sickeningly in-sync and we're not even married yet. "
# bobby "So, is that it? Have we planned our wedding?"
# chelsea "Oh honey, you haven't even started planning the wedding!"
# chelsea "But I'm here to help. "
# "She runs over to you."
# chelsea "MC!"
# chelsea "*If you chose her as BP* As your official best person, I have an amazing idea already!"
#     *If you chose someone else as BP* I know I'm not part of the wedding party, but I have this amazing idea!
# chelsea "What if we get a carriage pulled by unicorns!"
# s2w_mc "Unicorns? "
# 	-It might be hard to find some
# 		rocco "I heard it isn't the right season. "
# 		priya "They're not real!"
# 		chelsea "But I saw one once!"
# 	-They're not real, babes
# chelsea "But I saw one once!"
# 	-Yes! Get me my unicorns!
# 		chelsea "Yay!"
# 		priya "I hate to be the one to tell you this, babes…"
# 		priya "But unicorns aren't real."
# 		chelsea "But I saw one once!"
# "She pouts for a moment."
# chelsea "OK! How about this instead?"
# chelsea "Doves! Just loads of doves. They're, like, a symbol of weddings, right?"
# bobby "We'll put that on the maybe pile. "
# chelsea "Wait! I've got it!"
# chelsea "Let me design you a ‘Memories' box!"
# chelsea "During the wedding, everyone can leave a note for you and Bobby, which you can then read afterwards!"
# chelsea "It'll be so sweet!"
# bobby "That's actually a great idea!"
# MC thoughts: Do I want Chelsea to make me a memory box?
# 	- Yes! That sounds amazing!
# chelsea "Yes!"
# 		chelsea "I'll get started right away!"
# 		chelsea "Where did I put my emergency glitter kit?"
# 	-Nah, I don't think we need that…
# 		chelsea "Oh…"
# 		bobby "But, babe, that sounds like such a great idea. "
# 		bobby "I'd love to read what everyone says about us after the ceremony"
# 		MC thoughts: It would be nice to read everyone's messages after the wedding
# 			-In that case, let's do it
# 				chelsea "Yes!"
# 				chelsea "I'll get started right away!"
# 				chelsea "Where did I put my emergency glitter kit?"
# 			-I still don't think we need it. 
# 				chelsea "OK…"
# chelsea "I guess I don't need to find my emergency glitter kit after all. "

# "For the rest of the night, you hold hands with Bobby, even when you're busy dancing."
# "Surrounded by all the friends you made during your time in the Villa, you feel content and excited for what's to come next."
# "The wedding."
# "Your wedding."
# "But for now, tonight, it's about partying it up with those you love."
# LI commentator: It's me! I'm back!
# LI Commentator: Just when you thought you were safe from my outstanding wit and charm. 
# LI commentator: IT's so great to have the gang back together! And now there's a wedding!
# LI commentator: I'm determined to make an appearance, even if I don't get an invite. 
# LI commentator: I wonder how I can get hold of one of those giant cakes people hide in?
# LI commentator: Coming up!
# LI commentator: MC and Bobby's wedding!



#############################################################################
## Wedding Part 2
#############################################################################



#############################################################################
## Wedding Part 3
#############################################################################