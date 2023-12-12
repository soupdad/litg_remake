

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
        $ amount_npcs_like_mc["allegra"] += 1
        show allegra at little_hop
        allegra "That outfit is absolutely amazing, by the way."
        show s01_mc at little_hop
        s01_mc "Thanks."
        show allegra at little_hop
        allegra "I kind of wish I'd dressed up a bit more."
    else:
        $ amount_npcs_like_mc["allegra"] -= 1
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
            $ amount_npcs_like_mc["allegra"] += 2
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
            $ amount_npcs_like_mc["erikah"] += 2
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
            $ amount_npcs_like_mc["allegra"] += 1
            $ s1_what_are_you_here_for = "love"
            show allegra at little_hop
            allegra "Exactly."
            allegra "That's what it's all about."
            show erikah at little_hop
            erikah "Well don't forget to enjoy yourself."

        "To have fun":
            $ amount_npcs_like_mc["erikah"] += 1
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
            $ amount_npcs_like_mc["allegra"] -= 1
            $ amount_npcs_like_mc["erikah"] -= 1
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

    allegra "I should've realised what was going on. He was going to the gym loads but wasn't getting any fitter."
    talia "Ugh. Get rid."
    jen "What about you [s01_mc_name]? What kind of body does your ideal man have?"

    # CHOICE
    menu:
        s01_mc "My ideal body-type is… "
        "tall, dark and handsome":
            s01_mc "Someone with dark eyes, a strong jaw, and a body like a greek statue."
            talia "Ooh, yeah, I could go for a bit of that."

        "sun's out, guns out":
            s01_mc "Someone totally stacked. The kind of guy who hangs out at the beach."
            jen "Yeah, I like that. Someone with big, strong arms you can wrap around yourself."

        "cute, small, well put-together":
            s01_mc "Someone who's not too big. That's my preference." 
            jen "I'm not into skinny guys. I like them big."
            erikah "Yeah, big muscular dudes. That's my jam."
            s01_mc "All the more for me!"

        "not important as long as they make me laugh":
            s01_mc "I'm all about the person underneath. If they're funny and we get on, that's everything."
            talia "That's cute. I'm way shallow compared to that."
    jen "And what about personality?"

    # CHOICE
    menu:
        s01_mc "My ideal partner's personality is…"

        "intense and romantic":
            s01_mc "I want the kind of guy who's going to treat every day like it's Valentine's day."
            jen "Yeah, the kind of guy who only has eyes for me. I love that."
            erikah "That doesn't sound fun at all."
            allegra "Yeah, I want someone with a sense of humour."

        "one of the lads":
            s01_mc "I like a real boy's boy, you know. Someone blokey."
            erikah "I know what you mean."
            jen "Ew, no. I want my man to have eyes for nobody but me."
            jen "I don't want him running off to the pub all the time."

        "quiet and thoughtful":
            s01_mc "I like it when a guy is sensitive and considerate, you know."
            s01_mc "Someone who can listen well."
            jen "You and me both, hun."
            erikah "I think that sounds kind of dull…"

        "not important, as long as they're good in bed":
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
            "His cheeks flush red."
        "Look down at my feet":
            "You avoid his gaze."

    "Jake jogs down to the lawn as the next boy steps out."

    mason "Alright, ladies? I’m Mason. We’re going to have such an epic summer!"

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
                        erikah "Really? That's not who I was going to pick."
                        s01_mc "So, who are you into?"
                        erikah "Not telling!"
                        s01_mc "Fair enough. I wonder who's next?"
                    "Mason":
                        erikah "Really? That's not who I was going to pick."
                        s01_mc "So, who are you into?"
                        erikah "Not telling!"
                        s01_mc "Fair enough. I wonder who's next?"
                    "Miles":
                        # FILL
                        pass
            "Not telling!":
                s01_mc "I don't want to give my strategy away so quickly, babes!"
                erikah "Fair enough…"
                s01_mc "I wonder who's next?"

            "Nah, I'm not into any of them.":
                "Well, maybe one of the next guys will be the one for you."
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
            "He grins."
        "Ignore him":
            "He looks away, slightly disappointed."
    
    "The door opens again."
    "The next boy runs a hand through his hair as he swaggers out of the Villa."

    jasper "Hi darlings. I'm Jasper. I can't wait to get to know you all."

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
            "As you make eye contact, he raises his eyebrows slightly."
            "A tiny smile forms in the corners of his mouth."
        "Act like you're not bothered":
            "You look across towards the pool and stretch."

    # IF STATEMENT
    "The men size each other up."
    erikah "So there are six boys and only five girls?"
    erikah "Amazing!"
    # If you didn't react positively to any of the boys, you get the following instead 
    "While the boys are checking each other out, you catch Talia glancing at you."
    "She nods her head in the direction of the boys and rolls her eyes."
    # reacted positive to mason and neg to levi
    "While the boys are checking each other out, you catch Mason glancing up at you."
    s01_mc "Looks like my little smile worked. He already can’t keep his eyes off me!
    This would be the perfect time to say something to one of the boys, before all the grafting gets underway…"
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
                "Mason":
                    $ e1p1_boy_spoke_to = "Mason"
                "Jasper":
                    $ e1p1_boy_spoke_to = "Jasper"
                "Miles":
                    $ e1p1_boy_spoke_to = "Miles"
                "Tim":
                    $ e1p1_boy_spoke_to = "Tim"
                "Jake":
                    $ e1p1_boy_spoke_to = "Jake"

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
# Season 1, Episode 1, Part 3
# Season 1, Episode 1, Part 4
# Season 1, Episode 1, Part 5