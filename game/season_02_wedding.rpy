#############################################################################
## Wedding Part 1
#############################################################################

label s2_wedding_set_up:

    "Love is confusing."
    "Love can be messy."
    "But ultimately, love can change the world."
    "Out of the seven billion people on this planet…"
    "…and fourteen lucky islanders…"
    "You've found your love."
    "All that's left is to make it official…"
    "Welcome to Love Island The Wedding!"

    s2_wedding_mc "I can't wait!"
    
    # CHOICE
    menu:
        "Quick question - did you finish Day 30 of season 2? It's fine if you didn't!"
        "I didn't finish season 2":
            "Do you want to answer some questions to customize your story, or just jump straight in?"
            # SUB-CHOICE
            menu:
                s2_wedding_mc "I want to…"
                "Customise my story":
                    "OK! Let's set this up."
                    jump customize_my_story
                
                "Jump straight in!":
                    # uses save data from s2 for who you're coupled up with, name, and what you look like, auto fills in other questions
                    "Woah! Before you start, what do you want to be called?"
                    # input name
                    "Perfect! Now get ready… "
                    "For the wedding!"
        
        "I finished season 2":
            "Do you want to carry on your story from the end of Season 2, or customize some things?"
            # SUB-CHOICE
            menu:
                s2_wedding_mc "I'm going to…"
                "…continue my Season 2 story":

                "… customize my story":

    "OK! Let's set this up."
    "First, we'll create your character."
    (Character creation, display MC)
    N: Is this the look?
    -Yep! Nailed it! (Cont.) 
    -I want to try something else (back to creation)
    
    "What do you want to be called?"
    //Enter name//
    MC:Here I am!
 
"Next, we're going to ask you some questions to set up the story."
"You can answer these questions however you want. They will set up your relationships going into this mini-series."
"In the customised story, it is possible to set up some situations that weren't possible in the main game."

"Firstly, and most importantly, who do you want to marry?"
MC thought: I want to marry…
-Bobby, the boisterous booper
-Gary, the construction hunk
- Ibrahim, the gentle golfer
-Marisol, the hopeless romantic
-(next)
- Lucas, the charming daredevil
- Henrik, the Swedish outdoorsman
- Jakub, the muscular hustler
-Arjun, the cheeky charmer
- (next)
- Kassam, the quiet DJ
- Felix, the party animal
- Elijah, the suave sophisticate
- (next)
-Carl, the successful scientist
-   Elisa, the outrageous influencer
-  Noah, the luscious librarian
-(next) – restart from top


label customize_my_story:
    "First, we'll create your character."
    # character creator
    
    # CHOICE
    menu:
        "Is this the look?"
        "Yep! Nailed it!":
            pass
        "I want to try something else":
            jump customize_my_story

    "What do you want to be called?"
    # input name
    s2_wedding_mc "Here I am!"

    "Next, we're going to ask you some questions to set up your story."
    "You can answer these questions however you want. They will set up your relationships going into this mini-series."
    "In this customised story, it is possible to set up some situations that weren't possible in the main game."
    "Firstly, and most importantly, who do you want to marry?"

    label s2_wedding_choose_partner:
    # CHOICE
    # create screen with character's profile shots and arrows to hit next, showing 3-4 at a time
    # menu: 
#         "Bobby, the boisterous booper"
#         "Gary, the construction hunk"
#         "Ibrahim, the gentle golfer"
# "Marisol, the hopeless romantic"
# -(next)
# - Lucas, the charming daredevil
# - Henrik, the Swedish outdoorsman
# - Jakub, the muscular hustler
# -Arjun, the cheeky charmer
# - (next)
# - Kassam, the quiet DJ
# - Felix, the party animal
# - Elijah, the suave sophisticate
# - (next)
# -Carl, the successful scientist
# -   Elisa, the outrageous influencer
# -  Noah, the luscious librarian

    if s2_wedding_partner == "Bobby":
        # image of li
        bobby "I'm so lucky!"
    elif s2_wedding_partner == "Gary":
        # image of li
        gary "I'm so lucky!"
    elif s2_wedding_partner == "Ibrahim":
        # image of li
        ibrahim "I'm so lucky!"
    elif s2_wedding_partner == "Marisol":
        # image of li
        marisol "I'm so lucky!"
    elif s2_wedding_partner == "Lucas":
        # image of li
        lucas "I'm so lucky!"
    elif s2_wedding_partner == "Henrik":
        # image of li
        henrik "I'm so lucky!"
    elif s2_wedding_partner == "Jakub":
        # image of li
        jakub "I'm so lucky!"
    elif s2_wedding_partner == "Arjun":
        # image of li
        arjun "I'm so lucky!"
    elif s2_wedding_partner == "Kassam":
        # image of li
        kassam "I'm so lucky!"
    elif s2_wedding_partner == "Felix":
        # image of li
        felix "I'm so lucky!"
    elif s2_wedding_partner == "Elijah":
        # image of li
        elijah "I'm so lucky!"
    elif s2_wedding_partner == "Carl":
        # image of li
        carl "I'm so lucky!"
    elif s2_wedding_partner == "Noah":
        # image of li
        noah "I'm so lucky!"
    elif s2_wedding_partner == "Elisa":
        # image of li
        elisa "I'm so lucky!"

    # VERIFY CHOICE
    menu:
        "Am I sure I want to marry [s2_wedding_partner]?"
        "Of course!":
            pass
        "Let me choose again...":
            jump s2_wedding_choose_partner

    s02_wedding_mc "Nobody else has ever made me feel the way [s2_wedding_partner] makes me feel."

    "Are you and [s2_wedding_partner] living together?"
    
    # CHOICE
    menu:
        "Are [s2_wedding_partner] and I living together?"
        "Yep":
            $ s2_wedding_living_together = True
            "Happily cohabiting."
        "Nope":
            $ s2_wedding_living_together = False

    "The next few questions are about choices you could have made in the finale of Love Island. answer them however you like."
    "First - did you have a secret intimate moment with Lottie or Hannah, right before the series ended?"

    # CHOICE
    menu:
        "Did I have a secret moment with Lottie or Hannah?"
        "Yes, with Lottie":
            $ s2_wedding_secret_moment = "Lottie"
            s2_wedding_mc "I still think about it all the time..." 
        "Yes, with Hannah":
            $ s2_wedding_secret_moment = "Hannah"
            s2_wedding_mc "I still think about it all the time..." 
        "No, I didn't":
            $ s2_wedding_secret_moment = "No one"
            

    "Did you promise to go travelling with anyone?"

    # CHOICE
    menu:
        "Did I make travel plans with any of the Islanders?"
        "Yes, with Shannon":
            $ s2_wedding_travel_plans = "Shannon"
        "Yes, with Hope":
            $ s2_wedding_travel_plans = "Hope"
        "No, I didn't":
            $ s2_wedding_travel_plans = "No one"
            "I needed a bit of a break from everyone by then."
    
    "And finally, did you win Love Island?"
    
    # CHOICE
    menu:
        "Did I win?"
        "Totally":
            $ s2_wedding_win = True
            # SUB-CHOICE
            menu:
                "And I spent the prize money on..."
                "... travelling the world!":
                    $ s2_wedding_spent_prize_on = "Travel"
                "... a lot of clothes":
                    $ s2_wedding_spent_prize_on = "Clothes"
                "... helping people less well off than me":
                    $ s2_wedding_spent_prize_on = "Helping"
                "... a bit of this, a bit of that":
                    $ s2_wedding_spent_prize_on = "Random"
        "No, I didn't":
            $ s2_wedding_win = False
        
    




#############################################################################
## Wedding Part 2
#############################################################################



#############################################################################
## Wedding Part 3
#############################################################################