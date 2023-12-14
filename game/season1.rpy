

label testing:
    scene black

    "Hi, You are testing out something. That's cool"

    show allegra at center

    show allegra at little_hop

    "im allegra and im doing something lol"
    return


    


# Season 1, Episode 1, Part 1
label s1e1p1:
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

    show s01_mc at mc_spot

    show allegra at npc_1

    show s01_mc at little_hop
    s01_mc "Hi I'm [s01_mc_name]"

    show allegra at little_hop
    allegra "I'm {b}Allegra{/b}. It's so good to meet you!"

    # Profile shot of Allegra
    "Allegra\n 
    -24, from Swansea\n
    -Cocktail Entrepreneur\n
    -We don't know what that means either"

    $ likes_outfit = check_if_like_outfit(allegra_liked_outfits)
    if likes_outfit:
        $ amount_npcs_like_mc["Allegra"] += 1
        show allegra at little_hop
        allegra "That outfit is absolutely amazing, by the way."
        show s01_mc at little_hop
        s01_mc "Thanks."
        show allegra at little_hop
        allegra "I kind of wish I'd dressed up a bit more."
    else:
        $ amount_npcs_like_mc["Allegra"] -= 1
        show allegra at little_hop
        allegra "Oh wow, interesting outfit choice, by the way."
        allegra "Good luck making a splash wearing that."

    "Another girl walks in as Allegra finishes speaking."

    show erikah at npc_3

    erikah "Hi My name's {b}Erikah{/b}."

    # Profile shot of Erikah
    "Erikah\n
    -20, from Norwich\n 
    - Jobbing Actor\n
    - Has made over a 100 makeup tutorials"

    "She totters towards you and embraces you warmly."
    erikah "So happy to meet you both."

    # CHOICE 1
    menu:
        "What do you do next?"
        "Talk about yourself":
            s01_mc "So in the outside world I'm a [s01_mc_job]."
            show allegra at little_hop
            allegra "Wow, we're just getting your whole life story, huh?"

            if s01_mc_job == "Social Media Influencer":
                show erikah at little_hop
                erikah "Like, on social media? That's such a cool job!"
                erikah "Like, everyone thinks they'd be really good at it, but they don't get how hard it actually is."
                
            elif s01_mc_job == "Trainee Heart Surgeon":
                show allegra at little_hop
                allegra "That is amazing, though." 
                show erikah at little_hop
                erikah "Do you dream about being that person that stands up on a plane when they ask for a doctor?"
                show allegra at little_hop
                allegra "I'll never be that person..."

            elif s01_mc_job == "Runway Model":
                show allegra at little_hop
                allegra "I actually used to date a boy who worked on the catwalk."
                allegra "He was, like, the most extra person I've ever met."
                "She launches into a lengthy description of her ex."
                allegra "But that's in the past. We're here to find someone new!"

            elif s01_mc_job == "Conceptual Artist":
                show allegra at little_hop
                allegra "What does that even mean?"
                show s01_mc at little_hop
                s01_mc "I make art, but it's more like… about the idea of art."
                show allegra at little_hop
                allegra "I think I have an artistic soul, but, like, I'm very results-oriented."
                allegra "I love that we've got someone creative in the Villa, though."

            show allegra at little_hop
            allegra "So, what are you guys hoping to get out of the Villa?"

        "Ask about Allegra":
            $ amount_npcs_like_mc["Allegra"] += 1
            s01_mc "Allegra, what kind of person are you looking for, in here?"
            show allegra at little_hop
            allegra "I don't know. I think my type is 'not my ex'."
            show s01_mc at little_hop
            s01_mc "Totally. It's all about new beginnings."
            show allegra at little_hop
            allegra "New beginnings! This is going to be the best summer of our lives."
            show erikah at little_hop
            erikah "What about you, [s01_mc_name]? What are you after from the Villa?"

        "Ask about Erikah":
            $ amount_npcs_like_mc["Erikah"] += 1
            s01_mc "So Erikah, what kind of guy do you want to find in here?"
            show erikah at little_hop
            erikah "I don't really have a type on paper. I guess I want to be surprised."
            erikah "But he has to be fun."
            erikah "It has to be someone I can have a laugh with, even if we're just sitting on the sofa watching TV."
            show allegra at little_hop
            allegra "Yeah, I absolutely agree."
            show erikah at little_hop
            erikah "What about you, [s01_mc_name]? What are you after from the Villa?"
                
                
    # CHOICE 2
    menu:
        "What are you after from the Villa?"

        "To find love":
            $ amount_npcs_like_mc["Allegra"] += 1
            $ s1_what_are_you_here_for = "love"
            show allegra at little_hop
            allegra "Exactly."
            allegra "That's what it's all about."
            show erikah at little_hop
            erikah "Well don't forget to enjoy yourself."

        "To have fun":
            $ amount_npcs_like_mc["Erikah"] += 1
            $ s1_what_are_you_here_for = "fun"
            show erikah at little_hop
            erikah "Yeah! All about the good times."
            erikah "A whole summer full of banter, with a load of hot dudes, chilling by the pool?"
            erikah "Yes Please!"
            show allegra at little_hop
            allegra "For me it's all about finding love. Does that sound really cheesy?"
            show s01_mc at little_hop
            s01_mc "Not at all!"
                    
        "For the prize money":
            $ amount_npcs_like_mc["Allegra"] -= 1
            $ amount_npcs_like_mc["Erikah"] -= 1
            $ s1_what_are_you_here_for = "money"
            show allegra at little_hop
            allegra "What, for real?"
            allegra "That's, like, so not the point for me."
            show erikah at little_hop
            erikah "Me neither."

    show allegra at little_hop
    allegra "For me, it's all about the new beginnings."
    allegra "I've just come out of this really intense breakup, and I need to get a fresh start."
    show s01_mc at little_hop
    s01_mc "What happened?"
    show allegra at little_hop
    allegra "Well, I realised he was cheating on me with his personal trainer, and…"
    
    "Erikah raises her eyebrows at you."

    allegra "Oh, check it out, another girl!"
    
    "Allegra points across the lawn."

    show jen at npc_2

    jen "Hey girls! I'm Jen."

    "Jen walks elegantly towards the group, tossing her hair over her shoulder as she embraces you."

    # Profile shot of Jen
    "Jen\n
    -22, from London\n
    -Fashion Blogger\n
    -Says she has 'mega resting bitch face'"

    jen "We're all looking for love right?"

    menu:
        "Are you looking for love?"
        "Yeah, of course":
            if s1_what_are_you_here_for == "money":
                $ amount_npcs_like_mc["Allegra"] -= 1
                $ amount_npcs_like_mc["Erikah"] -= 1
                $ amount_npcs_like_mc["Jen"] -= 1
                erikah "That's not what you said just now!"
                erikah "What's changed?"
            else:
                erikah "That's the name of the game!"
                erikah "We were just talking about it and we all said the same thing."
            
        "Not exactly":
            if s1_what_are_you_here_for == "love" or s1_what_are_you_here_for == "fun":
                $ amount_npcs_like_mc["Allegra"] -= 1
                $ amount_npcs_like_mc["Erikah"] -= 1
                $ amount_npcs_like_mc["Jen"] -= 1
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

    # Profile shot of Talia
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
            $ amount_npcs_like_mc["Allegra"] -= 1
            allegra "Oh my god, you guys haven't been paying attention to anything I've been saying!"
            allegra "She was his personal trainer."
            jen "Come on, ladies. We're all getting to know each other."
            allegra "Hmph."
        "Personal trainer":
            $ amount_npcs_like_mc["Allegra"] += 1
            allegra "It's so sweet that you were listening, I can't wait to get to know you guys."
        "Next-door neighbour":
            $ amount_npcs_like_mc["Allegra"] -= 1
            allegra "Oh my god, you guys haven't been paying attention to anything I've been saying!"
            allegra "She was his personal trainer."
            jen "Come on, ladies. We're all getting to know each other."
            allegra "Hmph."

    allegra "I should've realised what was going on. He was going to the gym loads but wasn't getting any fitter."
    talia "Ugh. Get rid."
    jen "What about you [s01_mc_name]? What kind of body does your ideal man have?"

    # CHOICE
    menu:
        s01_mc "My ideal body-type is… "
        "tall, dark and handsome":
            $ amount_npcs_like_mc["Jake"] += 1
            $ amount_npcs_like_mc["Jasper"] += 1
            s01_mc "Someone with dark eyes, a strong jaw, and a body like a greek statue."
            talia "Ooh, yeah, I could go for a bit of that."

        "sun's out, guns out":
            $ amount_npcs_like_mc["Levi"] += 1
            $ amount_npcs_like_mc["Mason"] += 1
            s01_mc "Someone totally stacked. The kind of guy who hangs out at the beach."
            jen "Yeah, I like that. Someone with big, strong arms you can wrap around yourself."

        "cute, small, well put-together":
            $ amount_npcs_like_mc["Miles"] += 1
            s01_mc "Someone who's not too big. That's my preference." 
            jen "I'm not into skinny guys. I like them big."
            erikah "Yeah, big muscular dudes. That's my jam."
            s01_mc "All the more for me!"

        "not important as long as they make me laugh":
            $ amount_npcs_like_mc["Tim"] += 1
            s01_mc "I'm all about the person underneath. If they're funny and we get on, that's everything."
            talia "That's cute. I'm way shallow compared to that."

    jen "And what about personality?"

    # CHOICE
    menu:
        s01_mc "My ideal partner's personality is…"

        "intense and romantic":
            $ amount_npcs_like_mc["Jasper"] += 1
            $ amount_npcs_like_mc["Miles"] += 1
            s01_mc "I want the kind of guy who's going to treat every day like it's Valentine's day."
            jen "Yeah, the kind of guy who only has eyes for me. I love that."
            erikah "That doesn't sound fun at all."
            allegra "Yeah, I want someone with a sense of humour."

        "one of the lads":
            $ amount_npcs_like_mc["Mason"] += 1
            $ amount_npcs_like_mc["Levi"] += 1
            $ amount_npcs_like_mc["Tim"] += 1
            s01_mc "I like a real boy's boy, you know. Someone blokey."
            erikah "I know what you mean."
            jen "Ew, no. I want my man to have eyes for nobody but me."
            jen "I don't want him running off to the pub all the time."

        "quiet and thoughtful":
            $ amount_npcs_like_mc["Jake"] += 1
            s01_mc "I like it when a guy is sensitive and considerate, you know."
            s01_mc "Someone who can listen well."
            jen "You and me both, hun."
            erikah "I think that sounds kind of dull…"

        "not important, as long as they're good in bed":
            $ amount_npcs_like_mc["Erikah"] += 1
            s01_mc "If he knows his way around the bedroom, nothing else really matters."
            erikah "Ha! Yes. Right answer."

    talia "Can I ask you guys something?"

    # CHOICES
    menu:
        talia "Like, are you going to actually… get intimate in here? You don't mind if it's on TV?"
        "I'm into it":
            erikah "Yeah, for sure. How else will I know if I've found the one?"
            s01_mc "Exactly."
        "Depends on the person":
            allegra "That's how I feel,too."
            s01_mc "If the right man comes along, though…"
            erikah "But the whole point is to hook up with hot guys!"
            talia "I think there's a little bit more to it than that."
        "No chance":
            jen "So you're not going to hook up for the whole summer, Talia?"
            talia "I haven't really decided, to be honest."
            talia "You know that fifty thousand people applied to be on the show this year?"

    "Before the conversation can continue, Jen's phone beeps."

    jen "Oh, what's this?"
    jen "I get the first one. Awesome."

    "She clears her throat."

    jen "Guys! I got a text!"
    jen "I've been looking forward to that way too much."

    # Text Message
    "Hello, girls, and welcome to Love Island! Please gather on the lawn. It's time to meet the boys. #thewaitisover #boyparade"

    talia "Amazing!"
    jen "Finally!"

    "The girls stand on the lawn and look towards the entrance."
    "The door to the Villa bursts open."

    jake "How are you doing, girls? I'm Jake."

    # Profile shot of Jake
    "Jake\n
    - 29, from Preston\n
    - Chef\n
    - Has known heartbreak"
    "Jake stands with his shoulders square, and his hands clasped together."
    "For a moment, he doesn't move."

    talia "A little nervous there, Jake?"
    jake "No, just overwhelmed by all these beautiful people!"

    # CHOICE
    menu:
        "Jake looks…"

        "like a film star!":
            thought "He's old-school handsome. I love it."
        "really intense":
            thought "I like how serious his expression is."
        "kind of scared…":
            thought "I think I want someone a little more chipper."
            
    # CHOICE
    menu:
        "He's looking right at me."

        "Wink at him":
            $ e1p1_cracking_onto_boys += 1
            $ amount_npcs_like_mc["Jake"] += 1
            $ e1p1_initial_meeting_likes.append("Jake")
            "His cheeks flush red."
        "Look down at my feet":
            "You avoid his gaze."

    "Jake jogs down to the lawn as the next boy steps out."

    mason "Alright, ladies? I'm Mason. We're going to have such an epic summer!"

    # Profile shot of Mason
    "Mason\n
    -24, from Romford\n
    - Musician and underwear model\n
    - Favourite food: Love Hearts"

    "Mason shields his eyes from the sun as he steps forward, radiating confidence."
    "He catches your eye and smiles at you."

    # CHOICE
    menu:
        "Mason, huh?"

        "I like his vibe!":
            thought "He seems way more exciting than the last guy."
        "I like his abs!":
            thought "You could grate cheese on those things."
        "Meh…":
            thought "He's trying too hard."

    "He looks at you and nods hello."

    mason "'Sup?"

    # CHOICE
    menu:
        "Mason's giving me the eye…"

        "Smile back":
            $ e1p1_cracking_onto_boys += 1
            $ amount_npcs_like_mc["Mason"] += 1
            $ e1p1_initial_meeting_likes.append("Mason")
            "He grins."
        "Look away":
            "You break eye contact first. He doesn't seem bothered."

    "Mason takes his place next to Jake, grinning widely."
    "The next boy is close behind."

    miles "Alright, everybody? I'm Miles."

    # Profile shot of Miles
    "Miles\n
    - 22, from Glasgow\n
    - Carpenter\n
    - Life goal: build a house with his bare hands\n"

    "Miles catches your eye and throws you a cheeky wink."

    # CHOICE
    menu:
        "Miles seems…"

        "totally extra":
            thought "That wink was ridiculous. This guy's totally over the top."
        "my type on paper":
            thought "He's totally built! Love it."
        "pretty good-looking":
            thought "He's got the looks, but will he have the banter?"

    "He strikes a strongman pose."

    # CHOICE
    menu:
        "Miles is trying to show off his muscles."

        "Cheer":
            $ e1p1_cracking_onto_boys += 1
            $ amount_npcs_like_mc["Miles"] += 1
            $ e1p1_initial_meeting_likes.append("Miles")
            s01_mc "Woo! Awesome!"
            "Miles bows and blows a kiss at you."
            # IF STATEMENT
            if e1p1_cracking_onto_boys == 3:
                erikah "Wow, you're cracking on to all the boys, huh?"
                s01_mc "First impressions are everything, hun."
                s01_mc "I wonder who's going to be next?"
            call e1p1_see_anyone_you_like_choice

        "Don't encourage him":
            "Some of the other girls clap, but it's clear he's not really impressing anyone."
            # IF STATEMENT
            if e1p1_cracking_onto_boys == 0:
                erikah "Wow, you're not giving an inch, huh?"
                s01_mc "What do you mean?"
                erikah "The boys keep nodding at you and winking and stuff, and you're just stonewalling them!"
                s01_mc "Well, treat 'em mean, keep 'em keen, right?"
                erikah"That's totally not my attitude, but you do you, hun."
                s01_mc "Maybe I'm just not into any of the guys we've seen so far?"
            else:
                call e1p1_see_anyone_you_like_choice

    label e1p1_see_anyone_you_like_choice:
        # From "Miles is trying to show off his muscles."
        erikah "See anybody you like yet?"
        # CHOICE
        menu:
            "Erikah wants to know if I see any boys I like so far."

            "Yeah!":
                s01_mc "There's totally someone I like the look of."
                erikah "Nice, which one?"
                # SUB-CHOICE
                menu:
                    s01_mc"I like the look of…"

                    "Jake":
                        $ amount_npcs_like_mc["Jake"] += 1
                        erikah "Really? That's not who I was going to pick."
                        s01_mc "So, who are you into?"
                        erikah "Not telling!"
                        s01_mc "Fair enough. I wonder who's next?"
                    "Mason":
                        $ amount_npcs_like_mc["Mason"] += 1
                        erikah "Really? That's not who I was going to pick."
                        s01_mc "So, who are you into?"
                        erikah "Not telling!"
                        s01_mc "Fair enough. I wonder who's next?"
                    "Miles":
                        $ amount_npcs_like_mc["Miles"] += 1
                        erikah "Really? That's not who I was going to pick."
                        s01_mc "So, who are you into?"
                        erikah "Not telling!"
                        s01_mc "Fair enough. I wonder who's next?"
            "Not telling!":
                s01_mc "I don't want to give my strategy away so quickly, babes!"
                erikah "Fair enough…"
                s01_mc "I wonder who's next?"

            "Nah, I'm not into any of them.":
                erikah "Well, maybe one of the next guys will be the one for you."
                s01_mc "I hope so!"
    
    "Just as you say that, the next boy walks out."

    tim "Wow, everyone's so fit!"
    tim "I'm Tim, by the way."

    # Profile shot of Tim
    "Tim\n
    - 23, from Truro\n
    - DJ\n
    - Describes himself as 'a genius'\n"

    "He mimes fanning himself, and walks straight into Miles."

    talia "Ha! This guy's hilarious."


    # CHOICES
    menu:
        "Tim looks like…"

        "He's got banter":
            "Banter is everything, after all."
        "He's full of himself":
            "I'm not about that, to be honest."
        "A handful":
            "I wonder if he's this full-on all the time?"


    "He grins at you and makes a call-me gesture with his hand."
    s01_mc "Come on, really?"

    # CHOICES
    menu:
        "What do you do?"

        "Flutter your eyelashes at him":
            $ amount_npcs_like_mc["Tim"] += 1
            $ e1p1_initial_meeting_likes.append("Tim")
            "He grins."
        "Ignore him":
            "He looks away, slightly disappointed."
    
    "The door opens again."
    "The next boy runs a hand through his hair as he swaggers out of the Villa."

    jasper "Hi darlings, I'm Jasper. I can't wait to get to know you all."

    # Profile shot of Jasper
    "Jasper\n
    - 26, from Kingston\n
    - Financial advisor\n
    - Likes fine dining, classic cars, Instagram stalking"

    # CHOICE
    menu:
        "Jasper seems like…"

        "He'd be a good kisser.":
            thought "He seems really confident. That's a good sign."
        "He needs a haircut.":
            thought "Come on, mate. You look ridiculous."
        "A total snob":
            thought "I'm not about these cocky London boys."

    "He stands with his arms folded and looks at the girls."

    # CHOICE
    "What kind of impression do I want to make with Jasper?"

    menu:
        "Make bedroom eyes":
            $ amount_npcs_like_mc["Jasper"] += 1
            $ e1p1_initial_meeting_likes.append("Jasper")
            "Jasper notices you looking at him and raises an eyebrow."
        "Look at your nails":
            "Jasper notices you checking your nails, shrugs, and walks over to join the other boys."

    talia "Five boys and five girls. Is that everyone?"
    "As if in response to her question, the door opens one more time."

    "One more guy walks out, grinning."

    levi "Hello ladies! I'm Levi."

    # Profile shot of Levi
    "Levi
    - 26, from Manchester
    - Professional water polo player
    - Friends call him 'Romeo'"

    jen "Hello."

    # CHOICE
    menu:
        "Levi…"

        "He's a dreamboat":
            thought "That is what a proper man looks like."
        "Those shorts make a statement!!":
            thought "I can't tear my eyes away!"
        "Not sure about his hair…":
            thought "I wonder what he puts in it to make it stick up like that?"

    "He looks confident but not too over-the-top as he surveys the other Islanders."

    # CHOICE
    menu:
        "Levi's checking everyone out."

        "Catch his eye":
            $ amount_npcs_like_mc["Levi"] += 1
            $ e1p1_initial_meeting_likes.append("Levi")
            "As you make eye contact, he raises his eyebrows slightly."
            "A tiny smile forms in the corners of his mouth."
        "Act like you're not bothered":
            "You look across towards the pool and stretch."

    
    "The men size each other up."
    erikah "So there are six boys and only five girls?"
    erikah "Amazing!"

    # IF STATEMENT
    # If you didn't react positively to any of the boys, you get the following instead
    if e1p1_cracking_onto_boys == 0:
        "While the boys are checking each other out, you catch Talia glancing at you."
        "She nods her head in the direction of the boys and rolls her eyes."
    elif "Levi" in e1p1_initial_meeting_likes and "Mason" not in e1p1_initial_meeting_likes: 
        # reacted positive to mason and neg to levi
        "While the boys are checking each other out, you catch Mason glancing up at you."
        s01_mc "Looks like my little smile worked. He already can't keep his eyes off me!"
        s01_mc "This would be the perfect time to say something to one of the boys, before all the grafting gets underway…"
    elif "Mason" in e1p1_initial_meeting_likes and "Levi" not in e1p1_initial_meeting_likes:
        # reacted positive to levi and neg to mason
        "While the boys are checking each other out, you catch Levi glancing up at you."
        s01_mc "Looks like I've caught his attention already."

    "Being upfront right now would give me a real headstart when it comes to getting the guy I want."

    # CHOICE
    menu:
        "Should I talk to one of the boys and give myself a head start?"

        "Yes, it's never too early to start grafting!":
            thought "Yes, now I can really stand out from the crowd."
            # SUB-CHOICE
            menu:
                "Which boy should I single out?"

                # dialog for Levi, Mason, Jasper, and Miles is the same
                "Levi":
                    $ e1p1_boy_spoke_to = "Levi"
                    $ amount_npcs_like_mc["Levi"] += 1
                "Mason":
                    $ e1p1_boy_spoke_to = "Mason"
                    $ amount_npcs_like_mc["Mason"] += 1
                "Jasper":
                    $ e1p1_boy_spoke_to = "Jasper"
                    $ amount_npcs_like_mc["Jasper"] += 1
                "Miles":
                    $ e1p1_boy_spoke_to = "Miles"
                    $ amount_npcs_like_mc["Miles"] += 1
                "Tim":
                    $ e1p1_boy_spoke_to = "Tim"
                    $ amount_npcs_like_mc["Tim"] += 1
                "Jake":
                    $ e1p1_boy_spoke_to = "Jake"
                    $ amount_npcs_like_mc["Jake"] += 1

            s01_mc "Hey [e1p1_boy_spoke_to], …I'm [s01_mc_name]. It's great to meet you."
            # IF STATEMENT
            if e1p1_boy_spoke_to == "Levi":
                levi "Hey, [s01_mc_name]. It's good to meet you, too."
                call e1p1_how_you_flirt_choice
                s01_mc "What's your type on paper, babe?"
                levi "Not to be too cheeky right off… But I'd say I'm looking at it."
                s01_mc "Noted."
                "He holds your gaze and smiles."
            elif e1p1_boy_spoke_to == "Mason":
                mason "Hey, [s01_mc_name]. It's good to meet you, too."
                call e1p1_how_you_flirt_choice
                s01_mc "What's your type on paper, babe?"
                mason "Not to be too cheeky right off… But I'd say I'm looking at it."
                s01_mc "Noted."
                "He holds your gaze and smiles."
            elif e1p1_boy_spoke_to == "Jasper":
                jasper "Hey, [s01_mc_name]. It's good to meet you, too."
                call e1p1_how_you_flirt_choice
                s01_mc "What's your type on paper, babe?"
                jasper "Not to be too cheeky right off… But I'd say I'm looking at it."
                s01_mc "Noted."
                "He holds your gaze and smiles."
            elif e1p1_boy_spoke_to == "Miles":
                miles "Hey, [s01_mc_name]. It's good to meet you, too."
                call e1p1_how_you_flirt_choice
                s01_mc "What's your type on paper, babe?"
                miles "Not to be too cheeky right off… But I'd say I'm looking at it."
                s01_mc "Noted."
                "He holds your gaze and smiles."
            elif e1p1_boy_spoke_to == "Tim":
                tim "Hey, [s01_mc_name]. It's good to meet you, too."
                call e1p1_how_you_flirt_choice
                s01_mc "What's your type on paper, babe?"
                tim "I need someone with enough banter to keep up with me!"
                tim "Which is why I'll always be single."
                s01_mc "Noted."
            elif e1p1_boy_spoke_to == "Jake":
                jake "Hey, [s01_mc_name]. It's good to meet you, too."
                call e1p1_how_you_flirt_choice
                s01_mc "What's your type on paper, babe?"
                jake "Oh well… (He looks shyly at you.) I'm a firm believer that I'll know it when I find it."
                s01_mc "Noted."
        
            label e1p1_how_you_flirt_choice:
                # CHOICE
                menu:
                    "I should"

                    "Smile sweetly at him":
                        "You give him your most winning, innocent smile."
                    "Play with my hair":
                        "You twirl a strand of hair around your finger and bite your lip."
                    "Blow him a kiss":
                        "You make a show of pressing a kiss to your hand and blowing it towards him. He catches it and laughs."

        "No, stay quiet":
            "I guess there'll be other chances."

    "Suddenly, Erikah's phone beeps."
    jen "Oh my god, what does it say? Read it out!"

    # Text Message
    "Islanders, you've got the rest of the day to get to know one another. You will couple up by the fire pit at sunset, when the girls will choose their partners.\n\n
    The boy that isn't chosen will be dumped from the island immediately.\n
    #getonthegraft #returnticket #girlsontop"

    "The girls all share a grin."
    "The boys look like they've been electrocuted!"
    "Except for Mason."

    mason "Fantastic."
    "There's an awkward moment as the two groups eye one another up."
    mason "Well boys, I guess we'd better crack on!"

    # Outro
    "Coming up next on Love Island"
    "Levi gets busy in the bedroom…"
    levi "Yeah, they're really bouncy. Love it."
    "Tim rubs Miles up the wrong way…"
    tim "I'll wind you up so hard you'll think you're a clock!"
    "And one of the boys is dumped from the island."
    "You won't want to miss it."

# Season 1, Episode 1, Part 2
label s1e1p2:
    "Our sexy singles have just met one another for the first time."
    "Now, it's time to let them loose in the Villa."
    "And with the islanders coupling up this evening, everybody's out to impress."
    "I haven't seen this much peacocking since the time I got lost in a zoo, but that's another story."
    "This evening, you will choose your first partner."
    "The girls will choose their new partners in random order, so you won't know which boys will be chosen before you get to make your choice."
    "The only way to avoid getting dumped in Love Island is to be in a couple. You need to get to know the boys to work out who you'll save in the recoupling."

    mason "Looks like the game starts here!"
    "Everybody laughs."
    talia "Let's split up and explore the Villa. I want to check out the roof terrace!"
    jake "Oh, yeah, I want to see that."
    "They exchange a look and hurry off."
    jen "Oh my god, let's check out the bedroom."
    "She leaves. Levi grins and follows."
    "Tim and Miles head off towards the pool. Allegra follows."
    "Jasper, Mason, and Erikah stay where they are."
    "Your time in the Villa will be shaped by the choices you make.\n One of the most important choices is who you spend time with."

    thought "Who shall I go with?"

    # villa overview shot with all options of who you can talk to
    # call (label that has this screen once made)
    call screen s1e1p2_select_who_to_talk_to

    # Allegra, Tim, and Miles at pool
    label s1e1p2_talk_to_allegra_tim_miles:
        $ e1p2_who_have_i_talked_to.append("Allegra", "Tim", "Miles")

        "Allegra, Tim, and Miles have wasted no time getting acquainted with the pool."
        "Allegra is sitting on the poolside, her legs in the water."
        "Tim and Miles are standing in the shallow end, the water up to their waists."
        allegra "[s01_mc_name]! Come and join us."
        tim "Hey. My name's Tim, you're [s01_mc_name], of course."
        miles "Tim reckons he's your future husband. My name's Miles, by the way."
        "Miles has a thick Scottish accent. Tim punches him on the arm."
        tim "So, have you decided who you're going to pick yet?"
        "Allegra splashes him."
        allegra "You can't ask that! She probably hasn't decided."
        tim "She might have."

        # IF STATEMENT
        if "Tim" in e1p1_initial_meeting_likes:
            # if you reacted positively to tim during introduction to boys
            tim "Me and her definitely had a bit of a look going on when we all came in."
        elif "Miles" in e1p1_initial_meeting_likes:
            # if you reacted positively to miles during introduction to boys
            miles "I thought [s01_mc_name] looked like my type straight away."

        allegra "I guess some people are moving pretty fast."
        s01_mc "I expect some of us made up our minds, like, as soon as we saw you guys come in."
        # if you interacted with Jen and Levi first 
        s01_mc "For sure. Jen's totally hitting it off with Levi."
        tim "Definitely. What about you, [s01_mc_name]?"
        tim "Anyone come onto you yet? Apart from me, obvs."

        # IF STATEMENT
        # CHOICE
        if "Mason" in e1p2_who_have_i_talked_to or "Levi" in e1p2_who_have_i_talked_to:
            if "Mason" in e1p2_who_have_i_talked_to and "Levi" in e1p2_who_have_i_talked_to:
                menu:
                    "I'm just trying to chat to everyone.":
                        s01_mc "I want to keep people guessing."
                        tim "Oh, come on!"
                        miles "Works for me. I like a challenge."
                    "Tell them about Mason and Levi":
                        s01_mc "Yeah, Mason and Levi both seem pretty keen."
                        s01_mc "But it's hard to know how real anyone is at this stage."
                        tim "Wow, check you out! Miss Popular over here."
                        miles "Well, you can see why. You're gorgeous."
                        s01_mc "Thanks, boys."
                    "I haven't had alone time with anyone yet.":
                        tim "You should be cracking on, then!"
                        tim "You don't want to get left behind."
                    "None of your business.":
                        s01_mc "I wouldn't tell you if they had! Cheeky."

            elif "Mason" in e1p2_who_have_i_talked_to:
                menu:
                    "I'm just trying to chat to everyone.":
                        s01_mc "I want to keep people guessing."
                        tim "Oh, come on!"
                        miles "Works for me. I like a challenge."
                    "Tell them about Mason":
                        s01_mc "Yeah, Mason seemed pretty keen."
                        s01_mc "But it's hard to know how real anyone is at this stage."
                    "I haven't had alone time with anyone yet.":
                        tim "You should be cracking on, then!"
                        tim "You don't want to get left behind."
                    "None of your business.":
                        s01_mc "I wouldn't tell you if they had! Cheeky."

            elif "Levi" in e1p2_who_have_i_talked_to:
                menu:
                    "I'm just trying to chat to everyone.":
                        s01_mc "I want to keep people guessing."
                        tim "Oh, come on!"
                        miles "Works for me. I like a challenge."
                    "Tell them about Levi":
                        s01_mc "I reckon Levi's into me. We had a little moment. Don't tell Jen, though."
                        allegra "Don't say 'don't tell Jen'! It's a small Villa!"
                    "I haven't had alone time with anyone yet.":
                        tim "You should be cracking on, then!"
                        tim "You don't want to get left behind."
                    "None of your business.":
                        s01_mc "I wouldn't tell you if they had! Cheeky."
            else:
                menu:
                    "I'm just trying to chat to everyone.":
                        s01_mc "I want to keep people guessing."
                        tim "Oh, come on!"
                        miles "Works for me. I like a challenge."
                    "I haven't had alone time with anyone yet.":
                        tim "You should be cracking on, then!"
                        tim "You don't want to get left behind."
                    "None of your business.":
                        s01_mc "I wouldn't tell you if they had! Cheeky."

        miles "I reckon most of the girls have probably made their minds up, you know."
        miles "I'm not going to make myself seem like a prat by desperately trying to impress everyone."
        tim "Thing is, mate, it's Love Island, right?"
        tim "You're used to being the only eight in a room full of sevens."
        tim "But here, everyone's an eight. No room for complacency."
        miles "Eight? I'm a ten, mate. Or, like, a nine point nine nine."
        "Tim laughs. Allegra raises her eyebrows."
        miles "Your problem, Tim, is that you're all mouth. You've got no chill."
        tim "Bollocks!"
        miles "Nah, it's true."
        miles "[s01_mc_name], what's more attractive? Someone cool and collected, or someone who won't stop chattering?"

        # CHOICE
        menu:
            "Do I prefer someone chill, like Miles, or someone with banter, like Tim?"
            "Someone chill.":
                $ amount_npcs_like_mc["Miles"] += 1
                miles "Exactly!"
                allegra "I disagree. I don't like that 'too cool for school' attitude some guys have."
                allegra "In my experience, it's covering up the fact that they're really dull and have no chat."
                tim "Oh! Shots fired!"
                miles "That's not... I'm not saying that…"
                allegra "Don't worry, babe. I'm not talking about you."
            "Someone with banter.":
                $ amount_npcs_like_mc["Tim"] += 1
                tim "Exactly! Can you imagine dating someone with no chat?"
                miles "Can you imagine dating a man who never shuts up for five seconds, though?"
                allegra "Sounds alright, to be honest. Good banter is everything."
                s01_mc "I just don't want to be with a guy who acts like I'm not even there, you know?"
            "I'm all about the looks.":
                $ amount_npcs_like_mc["Allegra"] += 1
                "Allegra laughs. Miles hesitates for a second, then joins in."
                allegra "The only thing that really matters. She's so right."
                "Miles laughs and slaps Tim on the back."
                miles "And I think we both know that I've got the edge there, mate."
                "He kisses his biceps."


        "Miles looks at Tim."
        miles "Look man, I'm just winding you up, yeah?"
        "Tim laughs."
        tim "You're winding me up? Mate, you've just declared war."
        tim "I'll wind you up so hard you'll think you're a clock."
        "Miles grins."
        miles "Alright, mate. You're on."
        "You and Allegra walk off before the bromance gets too much to bear."
        
        # checks to see if you have talked to everyone
        if len(e1p2_who_have_i_talked_to) == 10:
            jump s1e1p2_outro


    # Erikah, Jasper, and Mason on lawn
    label s1e1p2_talk_to_erikah_jasper_mason:
        $ e1p2_who_have_i_talked_to.append("Erikah", "Jasper", "Mason")
        "Erikah seems delighted to have two boys chatting her up. Let's see if [s01_mc_name] cramps her style."

        "Jasper sees you approaching and goes to shake your hand."
        jasper "Hi, my name's Jasper."
        s01_mc "Hi, I'm [s01_mc_name]."

        # CHOICE
        menu:
            "Shake his hand.":
                jasper "So good to meet you."

            "Hug him.":
                $ amount_npcs_like_mc["Jasper"] += 1
                "You look at his outstretched hand."
                s01_mc "A bit formal, isn't it?"
                "You give him a hug. "
                jasper "Oh! Right. Sorry."
                "He grins."

            "Ignore the handshake.":
                "You ignore his outstretched hand. He withdraws it, pretending to fix his hair."
                jasper "Yeah, good to meet you."

        "You turn to the other guy."
        s01_mc "And what's your name, again?"
        mason "I'm Mason."

        # IF STATEMENT
        if "Mason" in e1p1_initial_meeting_likes:
            # If you reacted positively to Mason upon meeting, these lines occur)
            "Without waiting, he gives you a massive bear hug."
            mason "Looks like I caught your eye earlier, yeah?"
        else:
            "Mason gives you a peck on the cheek."
            mason "Alright, darling?"

        mason "I can't believe we've got to wait until this evening to couple up."
        s01_mc "Yeah, the girls have all the power!"
        erikah "Oh my god, it's like a buffet table."
        s01_mc "So…"

        # CHOICE
        menu:
            "Ask about Mason":
                $ amount_npcs_like_mc["Mason"] += 1
                s01_mc "So, what do you do in the outside world, Mason?"
                mason "Well, I used to play drums in a band called Seventh Heaven…"
                erikah "Oh my god, I remember you guys! You had that song... how did it go?"
                erikah "I want to take you to the stars, find out who you really are... "
                mason "That's the one."
                s01_mc "Seventh Heaven broke up, right?"
                mason "Yeah, Frankie's still going strong as a solo artist and Dan and Lizzie are producers."
                mason "Mostly I'm a model these days. Underwear, designer stuff, that kind of thing…"
                s01_mc "A rock star turned underwear model? Are you bantering?"
                mason "Nah, it's true. "
                erikah "…"

            "Ask about Jasper":
                $ amount_npcs_like_mc["Jasper"] += 1
                s01_mc "So what's your job, Jasper?"
                jasper "Oh, I'm into finance."
                s01_mc "That's pretty intense."
                jasper "Well, you know what they say. Work hard, play hard."
                erikah "Does that mean you're loaded?"
                jasper "Um, well, I'm quite senior… I have some fairly prestigious clients…"
                s01_mc "You can't just ask people stuff like that!"
                erikah "Come on, you were all thinking it."

            "Ask about Erikah":
                s01_mc "What do you do, Erikah?"
                erikah "Thanks for asking!"
                erikah "I'm an actor."
                mason "Have you been in anything on telly?"
                erikah "Apart from this?"
                erikah "No, I've only just got out of drama school."
                jasper "Do you enjoy it?"
                erikah "God, no. I hate it. Actors are the worst."
                mason "Really?!"
                erikah "Nah, I'm joking. It's fun."
                jasper "Anyway, we should probably mingle with the others a little, don't you think?"
                mason "Yeah, you're probably right."
                
        erikah "Anybody want a drink?"

        # CHOICE
        menu:
            "Yes please.":
                jasper "Let me get you one. "
            "I'm OK.":
                jasper "Well, I won't say no."
            "I want to stay here.":
                jasper "Suit yourself."

        jasper "Let's make a round. I'll help."

        "Erikah and Jasper walk off towards the Villa. You take a few steps with them."
        "Mason hangs back on the lawn. As you look back at him, he catches your eye."
        "This is the perfect chance to chat to him in private."
        "He grins at you, and nods towards a more secluded corner of the garden."

        # CHOICE
        # choose whether to talk more with mason or not
        menu:
            "I should…"

            "Go back and talk to Mason.":
                "You walk back towards Mason, apologising to Erikah and Jasper."
                mason "Hey! I'm glad you came back."

                # SUB-CHOICE
                menu:
                    "I wanted to speak to you alone.":
                        $ amount_npcs_like_mc["Mason"] += 1
                        mason "I thought we had a little spark, actually."

                    "I didn't want to mingle anymore.":
                        mason "Yeah, it's nice to just chill for a second."

                    "Jasper's a bit of a nobhead.":
                        mason "Yeah, he's not really my type either."
                        mason "It's cool you wanted to hang out with me for a bit, though."

                mason "There won't be much alone time today, I reckon."
                mason "Which sucks, because I'm way better one-on-one."
                s01_mc "Is that right?"
                mason "Yeah, for sure!"
                mason "And I just wanted to say, like, you seem really cool."

                # SUB-CHOICE
                menu:
                    "Mason said he thinks I'm cool, what do I say back?"
                    "I'm glad you noticed":
                        "Mason laughs at you."
                        mason "Even if you do know it."
                    "Even in this heat?":
                        mason "Yeah. Ice cold."
                    "Is that the best you've got?":
                        mason "Nah, but I'm not giving you all my best lines right now."
                        mason "You've got to work for those."

                mason "I know it's only first impressions…"
                mason "But if you picked me later, I'd be really happy."

                # CHOICE
                menu:
                    s01_mc "Oh, I…"
                    "I'd like that too":
                        mason "Amazing!"
                        mason "This is getting off to a good start. I'm stoked."

                    "I'll think about it":
                        mason "Oh, no! Shot down."
                        "He makes a heart shape with his fingers and then breaks it apart."
                        mason "Can't blame a guy for asking, right?"
                        s01_mc "Yeah, of course ."

                    "I don't think you're my type":
                        mason "Oh, right, yeah. Of course. Early days."
                        s01_mc "I think Erikah might have the hots for you, though."
                        mason "Really? Interesting."
                        "He rubs his chin."
                        mason "I still reckon you're more my type on paper, though."
                
                "He grins, and walks off towards the Villa."    
                s01_mc "Hmmm. I've definitely got a shot with him."

            # choose whether to talk more with mason or not
            "Walk off.":
                "You look up at the Villa."
        
        # checks to see if you have talked to everyone
        if len(e1p2_who_have_i_talked_to) == 10:
            jump s1e1p2_outro


    # Jen and Levi in bedroom
    label s1e1p2_talk_to_jen_levi:
        "In the bedroom Levi and Jen are having their ups and downs. Or at least Levi is…"
        "Levi is bouncing up and down on one of the beds. Jen is leaning against a wall watching him."
        levi "Yeah, they're really bouncy. Love it."
        "He notices you, and jumps off the bed."
        levi "Alright?"
        levi "I wasn't sure if you'd noticed me when I walked in. "
        if "Levi" in e1p1_initial_meeting_likes:
            # If you react positively upon meeting levi
            levi "Alright?"
            levi "I'm glad you came over. You and Jen caught my eye as soon as I walked in."

        # CHOICE
        menu:
            "Levi seems interested in me, how do I respond?"
            
            "I can't wait to get to know you.":
                $ amount_npcs_like_mc["Levi"] += 1
                levi "Yeah, likewise."
            "Hi, I'm [s01_mc_name].":
                levi "And I'm Levi."
                s01_mc "Yeah, you already said that."
                levi "Oh, yeah!"
            "Levi's a weird name.":
                "There's an awkward pause. Jen clears her throat."
                jen "Um, this is [s01_mc_name]."

        levi "Had a good look around yet?"
        jen "Not really, it's such a big house, though! I wonder who lives here normally? Probably, like, Kim Kardashian."
        levi "I have a couple of mates with holiday places out here. The houses are just ridiculous."

        # CHOICE
        menu:
            "What do you do?":
                pass
            "So, you clearly work out a lot.":
                jen "He does. Just wait until he tells you why."
                s01_mc "Why?"
            "Have you seen the pool yet?":
                levi "Can't exactly miss it, can you?"
                levi "Actually, I wouldn't be able to come here if there wasn't a pool."
                s01_mc "Oh yeah? Why not?"


        levi "I play waterpolo"
        s01_mc "What, like, professionally?"
        levi "Yeah."
        jen "He was in the Olympics."
        levi "I was."
        jen "You must be, like, amazingly fit."
        "He smiles and looks off to one side."
        levi "Uh, yeah, I guess I am."
        jen "I'm definitely going to pick you this evening."

        # CHOICE
        menu:
            "Jen said she's going to couple up with Levi tonight, what should I say?"
            "Not if I pick him first.":
                jen "All's fair in love and war, I guess..."
                "Levi looks awkwardly down at his feet."
                levi "So, um… What do you do, [s01_mc_name]?"
            "We don't know the order yet.":
                jen "But, like, if I get the chance…"
                jen "It sounds way less romantic when you say it like that."
                "Levi looks awkwardly down at his feet."
                levi "So, um… What do you do, [s01_mc_name]?"
            "Wink at Levi.":
                "He raises his eyebrows."
                levi "Sounds good, I've never dated anyone posh."
                jen "I'm not that posh... Not compared to Jasper!"
                levi "Well, where I come from, people would say you were posh."
                levi "What about you, [s01_mc_name]?"
                s01_mc "Well, I can't pick you if Jen already has!"
                levi "Oh no, I didn't mean. I meant like, what do you do?"

        # IF STATEMENT
        if s01_mc_job == "Runway Model":
            # If your profession is a runway model
            s01_mc "Oh, I'm a runway model."
            levi "What? That's amazing. Is that, like, one big party the whole time?"
            s01_mc "Yeah, there's a lot of that. And a lot of really dull photoshoots."

        elif s01_mc_job == "Social Media Influencer":
            # if you're a social media influencer
            s01_mc "Oh, I'm a social media influencer."
            levi "Mate, I don't even know what that is. Does that mean you've got like, a million Snapchat followers?"
            s01_mc "Pretty much."
        
        elif s01_mc_job == "Trainee Heart Surgeon":
            # if you're a trainee heart surgeon
            s01_mc "Oh, I'm a trainee heart surgeon."
            levi "Whoa! For real? That's so impressive."
            jen "Wow, that's amazing! I didn't know that about you. "
            levi "At least if you break someone's heart, you'll know how to fix it."

            # SUB-CHOICE FOR TRAINEE HEART SURGEON JOB
            menu:
                "People have been making this joke about you all year."

                "Pretend to laugh":
                    s01_mc "That's so funny!"
                "Are you a heartbreaker, Levi?":
                    levi "Guess so, yeah."
                "I'm only a trainee so let's hope it's not yours.":
                    levi "Yeah, me too!"

        elif s01_mc_job == "Conceptual Artist":
            # If your profession is a conceptual artist
            s01_mc "Oh, I'm a conceptual artist."
            levi "That's wild. I love conceptual art."
            levi "People think it's just unmade beds and cows cut in half."
            levi "But there's so much good stuff out there from unknown artists."
            s01_mc "Wow, this isn't a conversation I was expecting to have in here."
            levi "Nah, love it. Checking out some modern art is like my ideal Sunday, man."
            levi "Galleries, then down the pub. Mint."

        "Jen looks a bit left out."
        jen "Want some champagne? I need a top up too."
        levi "Yeah, thanks love."
        "She grabs Levi's glass and leaves."
        levi "I'm glad she's gone, actually."
        "Levi inches closer and looks you directly in the eye."
        levi "There's something I wanted to ask you…"

        # CHOICE
        # talk more with levi option
        menu:
            "This could be a valuable chance to get some alone time with Levi…"
            "Graft on Levi.":
                s01_mc "What is it?"
                levi "So, you know Jen?"

                # SUB-CHOICE
                menu:
                    "She seems really into you.":
                        levi "Yeah, yeah. She seems like a really nice girl."
                        levi "But I don't want to get into something too quick, you know?"
                        s01_mc "Yeah, of course. It's all just first impressions right now."

                    "She's out of your league.":
                        levi "Are you joking?"
                        levi "If she's out of my league, I dunno why I'm even bothering talking to you."
                        s01_mc "Nice line."

                    "I'm more your type.":
                        levi "You don't hold back, that's decent."
                        s01_mc "I just want you to know where I stand."


                levi "So, what I'm thinking is, you and me should like, get to know each other a bit."

                # SUB-CHOICE
                menu:
                    levi "So, what I'm thinking is, you and me should like, get to know each other a bit."

                    "I like the sound of that":
                        $ amount_npcs_like_mc["Levi"] += 1
                        levi "Sick."
                        levi "I don't know what's going to happen this evening, but, like, that's a plan."
                        s01_mc "You work quickly, huh?"
                        levi "Well, that's the game, isn't it?"
                        levi "Listen, I…"
                    "I bet you're saying that to all the girls":
                        levi "Ha! I don't know. Haven't really met everyone else yet."
                        levi "Probably not, though. "
                        levi "You're definitely my type on paper. I thought that as soon as I saw you."
                    "I think Jen's got her eye on you":
                        levi "Well, yeah. "
                        levi "Guess that means I won't get sent home this evening, anyway."
                        levi "But I get a say in the matter, too."
                        s01_mc "So you're not into her?"
                        levi "I don't know... We've only just met."
                        levi "But…"

                "It seems like he's got something on the tip of his tongue, but before he can say anything, Jen comes back in."

                jen "More bubbly!"
                s01_mc "So, he clearly fancies me."
                s01_mc "Good to know!"

            # talk to levi more option
            "Go and get a refill too.":
                s01_mc "Sorry, babes."
                "You smile at Levi as you follow Jen outside."

        # checks to see if you have talked to everyone
        if len(e1p2_who_have_i_talked_to) == 10:
            jump s1e1p2_outro

    # Talia and Jake on roof
    label s1e1p2_talk_to_talia_jake:
        $ e1p2_who_have_i_talked_to.append("Talia", "Jake")
        "Talia seems to have vanished off somewhere, leaving Jake alone on the roof."
        "Little tip, Jake - to win this game you actually have to talk to the girls!"
        "As you walk out onto the roof terrace, you practically walk straight into Jake."
        jake "Oh, hey. Sorry, my fault."
        s01_mc "No, it's all good."
        jake"I was hoping you would come up and talk to me."

        # IF STATEMENT
        if "Jake" in e1p1_initial_meeting_likes:
            # if you reacted positively to jake upon meeting him
            jake"I noticed you looking at me when we all came in."

        # CHOICE
        menu:
            "You look around for something to talk about."

            "The view's amazing, huh?":
                jake "Yeah, it's beautiful. I just came up here to check it out."
            "Aren't you handsome?":
                jake "Hah... Well, my mother always said so..."
            "I'm [s01_mc_name].":
                jake "I know."

        "There's a pause, Jake glances uncomfortably at a camera."
        s01_mc "Seven weeks in this place, huh?"
        "Jake laughs."
        jake "Well, for most of us. Someone only gets one day."

        # CHOICE
        menu:
            "You'll be fine.":
                jake "Oh, don't say that. Overconfidence is a killer."
            "I'd be worried.":
                jake "Well, they never said it was going to be easy."
            "Love don't come easy.":
                jake "If it did, it wouldn't be so valuable."

        jake "To be honest, it would be amazing to be chosen by any of you girls. You're all incredible."
        s01_mc "Oh, yeah. But the boys are all like superhuman levels of handsome, too."
        jake "Yeah, there's some fierce competition."
        "You're both quiet for a moment."
        "Jake doesn't really bring the chat. His eyes are intense, though."
        "Talia steals the moment by walking out onto the terrace."
        talia "Oh, hi guys. I'm not interrupting anything, am I?"

        # CHOICE
        menu:
            "Is Talia interrupting?"

            "Hah, a little, but it's OK.":
                talia "Sorry! Don't worry, you'll have other chances."
            "Not at all.":
                talia "Haha, awkward!"
            "Wait for Jake to reply.":
                "Jake catches your eye for a moment."
                jake "No, we were just chatting."

        talia "I just wanted to check out this view. It's amazing!"
        talia "Hey, Jake. Would you be a sweetheart and fetch me some champagne?"
        jake "Sure thing. Would you like some too, [s01_mc_name]?"
        s01_mc "Um, sure. Thanks!"
        "Jake takes your glass and walks off down to the garden."

        # CHOICE
        menu:
            "Isn't it mean to make him fetch your drink?":
                talia "Nah. Do you think?"
                talia "I reckon they're all anxious to get a chance to show off."
            "Get the men to work for you. I like it.":
                talia "Here's someone who gets it."
            "Wanted to get me by myself, did you?":
                talia "Maybe I did."
                talia "Nah, not really. Just making Jake work for it."

        talia "They've got to impress us today. Might as well enjoy it while it lasts."
        talia "By the way, we didn't really get to meet earlier. I'm Talia."
        "She gives you a kiss on both cheeks."
        s01_mc "I'm [s01_mc_name]."
        "Talia nods her head towards the door, the way Jake just went."
        talia "He seems cute."

        # CHOICE
        menu:
            s01_mc "Jake's got the looks, but personality-wise…"    

            "He's too quiet.":
                talia "I don't know. Maybe that means he's, like, a good listener or something?"
            "I like how eager to please he is.":
                talia "Yeah, that's completely necessary in a man."
            "It's going to take some effort to get to know him.":
                talia "Oh, I don't know. You just have to be direct. You'll see."
                talia "I'll get him talking about himself when he gets back."

        s01_mc "And he's certainly handsome. That heavy brow and those dark eyes."
        talia "Sounds ideal. I like someone a bit thoughtful, you know?"
        talia "Reckon you'll pick him this evening?"

        # CHOICE
        menu:
            "Am I going to pick Jake this evening?"

            "Yeah, maybe":
                talia "Hmm. Maybe we'll be rivals."
                "She smiles."
            "No, probably not.":
                talia "Cool. I might snap him up, in that case."
            "I don't know at this point.":
                talia "Cool. I might snap him up, in that case."
            "I've got my eye on someone else.":
                talia "Cool. I might snap him up, in that case."

        talia "I feel really bad for whoever gets sent home, anyway."
        "As if on cue, Jake reappears in the doorway with three champagne flutes."
        talia "So, Jake. Tell us about yourself."
        jake "Feels like an interview!"
        talia "Who said it wasn't?"
        "Talia winks at you. Jake shrugs and settles down onto a bench."
        jake "Well, I work in a restaurant…"
        talia "Waiter or chef?"
        jake "Chef. Actually, I'm head chef. It's not as big of a deal as it sounds."

        # CHOICE
        menu:
            "Jake's a head chef…"

            "That sounds impressive.":
                jake "I'm glad you think so, but I don't want to make a whole thing of it."
                jake "Being head chef basically just means I set the menu, and get in trouble when something goes wrong."
            "I love a man that can cook.":
                jake "Maybe I can show you something if I get the chance."
            "You must work all the time.":
                s01_mc "Sounds like you don't have too much time for relationships."
                jake "There's long nights, but I'm always up for a lunch date."

        jake "I love to get busy in the kitchen."
        jake "Being head chef basically just means I set the menu, and get in trouble when something goes wrong."
        talia "Oh my god, humblebrag."
        s01_mc "Don't they mind you missing the whole summer?"
        jake "Well, I might get sent back tonight, so I'm not that worried."
        talia "Boom!"
        jake "What about you? What do you do?"
        talia "Me? I'm a music journalist."
        talia "I get paid to hang around backstage at gigs and go to festivals all summer."
        talia "It's way cooler than being a chef."
        "Jake grins."
        thought "He's definitely shy. Can I be bothered to deal with that?"
        "Eventually, the three of you decide to mingle."
        "As you walk back down to the Villa, Jake catches your eye and nervously looks away, then looks back again to see if you're still looking."
        "This time, he winks."
        # checks to see if you have talked to everyone
        if len(e1p2_who_have_i_talked_to) == 10:
            jump s1e1p2_outro

    label s1e1p2_outro:
        "Someone's been grafting hard."
        "You've chatted to everyone! Time to see what happens next…"

        "You're checking out the kitchen bar when Talia wanders over to refill her glass."
        talia "Hey babes! Enjoying yourself so far?"

        # CHOICE
        menu:
            "Am I enjoying myself?"

            "I'm loving it!":
                talia "Oh my god, me too."
            "The Villa is amazing":
                talia "I know! I saw you taking a look around."
            "I'm still getting used to this.":
                talia "It's so different, isn't it?"
    
        talia "Sun, sea, and all these boys. What more do you want?"
        s01_mc "Sea?"
        talia "Well, there's a pool. That's close enough, I reckon."
        "Her phone beeps."
        talia "Guys! I got a text!"
        "Jasper jogs over."
        jasper "Is it a challenge?"
        talia "Looks like it!"
        jasper "Guys, get over here! It's a text!"
        "Everyone gathers around."
        miles "What does it say?"

        # Text Message
        "The girls only have a few hours left to size up the talent.\n 
        What better way to get to know each other than with a game of Never Have I Ever?\n
        Let's find out who your fellow Islanders really are…\n
        #firstimpressions #gotnosecrets #timetobereal"

        talia "Amazing. This will be so much fun!"

        # verify this is correct in all cases
        levi "I already know who's made a good impression on me…"
        "Levi winks at you."

        "Coming up next on Love Island…"
        "A game of Never Have I Ever gives our Islanders more than they bargained for…"
        "And our first coupling up leads to tears of joy, and tears of misery."
        "You wouldn't want to miss it"



# Season 1, Episode 1, Part 3
# Season 1, Episode 1, Part 4
# Season 1, Episode 1, Part 5