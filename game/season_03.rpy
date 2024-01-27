#########################################################################
## Episode 1, Part 1
#########################################################################
label s3e1p1:
    scene edited_sandy_intro

    "Finding love can be tough..."
    "Daily life is nothing but work, sleep, and repeat..."
    "How are you supposed to have time to search for that special someone?"
    "It's time to get off social media, and find love the old-fashioned way..."
    "On a reality TV show!"
    "You've been invited to a place where everything is different..."
    "A place where all you have to do all day is meet beautiful people, couple up, and fall in love..."
    "A place called Love Island."

    scene s3-outside-villa-wide-shot-day
    with dissolve
    "We've taken a gorgeous Villa in a hot country and filled it with sexy singles."

    scene s3-lounge
    with dissolve
    "To stay in the Villa, they'll have to get together, and stay together."

    scene s3-bedroom-day
    with dissolve
    "And if they do find love, one lucky couple will also pocket fifty thousand pounds,"

    scene s3-hideaway-night
    with dissolve
    "But it won't be easy. We're going to throw in twists, turns, and challenges to see if their love can survive."

    scene s3-firepit-night
    with dissolve
    "Who will find eternal bliss, and who will find themselves on a plane home?"
    "Let there be love."

    # MC Customizer Here
    scene s3-outside-villa-entrance
    with dissolve

    "Your heel click on the driveway as you stride up to the Villa."

    thought "It's gorgeous!"
    thought "I can't believe this is going to be my home for the next two weeks!"
    thought "Unless I go home early."
    thought "I wonder where everybody is?"

    "A girl peeks her head out of the entrance."
    "She yells in excitement when she sees you."

    show elladine at npc_center

    elladine "Hey! You made it!"
    elladine "It's so nice to meet you! I'm Elladine."

    $ s3_character_profile = "Elladine"
    window hide
    show screen s3_character_profile with Pause(3)
    hide screen s3_character_profile with dissolve


    # solo portrait shot of elladine
    "{i}Elladine\n
    -25, from Cardiff\n
    -Glassblower\n
    -Heard every 'blowing' joke a hundred times already{/i}"

    s3_mc "I'm [s3_mc_name]"

    # CHOICE
    menu:
        "What should I say to Elladine?"
        "It's nice to meet you too":
            $ s3e1p1_warning_here_to_win = False
            $ s3_amount_npcs_like_mc["Elladine"] += 5
            $ s3_mc_attr['Sweet'] += 1
            s3_mc "I think we're the first ones here!"
            elladine "Amazing. This is one of those moments you remember forever, isn't it?"
            s3_mc "I think so!"
            elladine "I know we will."

        "Wow, I love your outfit":
            $ s3e1p1_warning_here_to_win = False
            $ s3_amount_npcs_like_mc["Elladine"] += 5
            $ s3_mc_attr['Sweet'] += 1
            s3_mc "It's stunning!"
            elladine "Babes, I was about to say the same to you!"
            elladine "Seriously. You've already set the bar super high."
            elladine "The boys are going to freak when they see us."

        "Warning, I'm here to win":
            $ s3e1p1_warning_here_to_win = True
            $ s3_amount_npcs_like_mc["Elladine"] -= 5
            $ s3_mc_attr['Bold'] += 1
            s3_mc "Before we go getting too friendly, you need to know one thing about me."
            s3_mc "I'm here to find love, and I don't care how many toes I have to tread on to get it."
            s3_mc "So if you're tempted to cross me at some point while we're here..."
            s3_mc "Don't."
            s3_mc "Understood?"
            elladine "Um, sure. Understood."

    elladine "I've been feeling well nervous ever since I got here."
    elladine "I mean it's exciting, but it's also a lot of pressure, isn't it?"

    # CHOICE
    menu:
        "How am I feeling?"
        "So nervous":
            $ s3_mc_attr['Sweet'] += 1
            $ s3e1p1_feeling_hungry = False
            s3_mc "I've never done anything like this before. It's a bit scary."
            elladine "At least we're all in the same boat!"

        "Just excited":
            $ s3_mc_attr['Bold'] += 1
            $ s3e1p1_feeling_hungry = False
            s3_mc "I'm really excited to meet everyone!"

        "Kinda hungry":
            $ s3_mc_attr['Funny'] += 1
            $ s3e1p1_feeling_hungry = True
            elladine "You mean, like...hungry for love, or..?"
            s3_mc "Nope. Just hungry."
            elladine "Sounds like you need a snack."
            elladine "I hope there are some snacks lined up for us outside!"
            s3_mc "Why would there be snacks outside?"
            elladine "I mean like hot guys when you see someone hot and you say 'he's a snack'."
            s3_mc "That's not what I meant, though. I'm just hungry."
            s3_mc "I wish I had a banana or something."
            "Elladine looks like she's about to make another joke, but then decides against it."

    s3_mc "Are there any other girls here yet?"
    elladine "Only one. We've been waiting in the bedroom."
    elladine "Come on. I'll introduce you."

    scene s3-bedroom-day

    show elladine at npc_left
    show aj at npc_right

    "Elladine leads you into the bedroom, where another girl is waiting."
    "Her jaw drops when you walk in."

    aj "Are you the new arrival?"
    aj "Man, I knew everyone here was gonna be gorgeous, but I wasn't prepared..."
    elladine "Stop staring and introduce yourself!"
    aj "Sorry, sorry!"
    aj "My name's AJ. It's nice to meet you."

    # solo portrait shot of aj
    $ s3_character_profile = "AJ"
    window hide
    show screen s3_character_profile with Pause(3)
    hide screen s3_character_profile with dissolve

    "{i}AJ\n
    -21, from Bath\n
    -Professional hockey player\n
    -Knows how to handle a stick{/i}"

    s3_mc "I'm [s3_mc_name]"
    if s3e1p1_warning_here_to_win == True:
        elladine "She, um.. she definitely means business."
    else:
        elladine "We were just talking outside. She's really nice."

    aj "I hope everyone's going to be cool. I don't want to get sucked into a load of drama."
    aj "I mean, we're all here to have fun, right?"

    # CHOICE
    menu:
        "AJ's here to have fun, not to get into drama.."
        "Me too! Let's keep it chill and friendly":
            $ s3_amount_npcs_like_mc["AJ"] += 5
            $ s3_mc_attr['Sweet'] += 1
            s3_mc "Trust me, we're gonna have a great time."
            s3_mc "You're my girls now, and I don't let my girls turn on each other."
            aj "Yes! I'm so glad you said that."

        "But there's no fun without drama":
            $ s3_mc_attr['Bold'] += 1
            s3_mc "It's so exciting when someone does something totally shocking, and you just know the fallout is gonna be huge."
            s3_mc "I can't wait to stir up some trouble around here."
            aj "Fair play! I guess we just have different priorities."
            aj "Friendship is really important to me."

        "I don't care, as long as I get what I want":
            $ s3_amount_npcs_like_mc["AJ"] -= 2
            $ s3_mc_attr['Bold'] += 1
            s3_mc "I don't set out to create drama. But I will if I have to."
            s3_mc "At the end of the day, it's not called Friend Island."
            aj "Fair play! I guess we just have different priorities."
            aj "Friendship is really important to me."

    aj "That's what I love about my teammates back home."
    aj "We never mess around arguing about who passed the ball to who, or whatever. We just get on with it."
    aj "I want you all to be like my new teammates while we're here."


    # CHOICE (assigns your job)
    menu:
        elladine "What do you do on the outside, MC?"

        "Model":
            $ s3_mc_attr['Job'] = 'Model'
            aj "I knew it! As soon as you walked in, I was like, I bet she's a model."
            elladine "Yeah, I can't say I'm surprised either."
        "Scientist":
            $ s3_mc_attr['Job'] = 'Scientist'
            aj "Oh wow, that's really cool!"
            aj "It's not fair that someone as pretty as you gets to be smart as well."
        "Musician":
            $ s3_mc_attr['Job'] = 'Musician'
            elladine "I love musicians. If I find out one of the boys is in a band, I'm going to make a beeline straight for him."
        "Athlete":
            $ s3_mc_attr['Job'] = 'Athlete'
            aj "Snap!"
            aj "I knew I felt a connection with you as soon as you walked in here."


    "Suddenly, you hear a beeping noise."
    s3_mc "What was that?"
    elladine "It sounded like a text..."
    "AJ checks her phone and gasps."
    aj "Oh, it's me!"
    
    text "Girls, it's time to start meeting the boys. AJ, please make your way to the lawn and choose a boy to couple up with. Elladine and [s3_mc_name], stand by in the bedroom. You'll be up next! #girlmeetsboy #getthepartystarted"

    aj "I've got a text!"

    aj "What? But the other girls still haven't arrived yet!"
    elladine " I guess they'll be coming in later?"
    aj "I'd better go, then."
    aj "I'll see you out there, guys."
    elladine "Good luck!"

    show aj at npc_exit
    show elladine at npc_center

    "AJ races out of the bedroom. Her heels clack all the way to the lawn."
    
    elladine "She's got a lot of energy, hasn't she?"
    elladine "I guess it's hard not to be excited when you know you're picking first."
    s3_mc "I wonder what the boys will be like?"
    elladine "I want a guy who's been around the block a bit, you know?"
    elladine "Someone who knows what he's about and takes it seriously."
    elladine "What about you? What's your type?"

    # CHOICE
    menu:
        "My type is..."
        "Funny and cute":
            $ s3_li_like_mc['Harry'] += 1
            $ s3_li_like_mc['Bill'] += 1
            s3_mc "I just want a boy to make me smile."
            elladine "Aw, I hope you find him, babes."

        "Smart and mature":
            $ s3_li_like_mc['Camilo'] += 1
            s3_mc "I agree with you. I need a guy with a good head on his shoulders."
            elladine "Aw, I hope you find him, babes."

        "Whatever, as long as they're hot":
            s3_mc "Personality will never be as important as looks for me."
            elladine "Ha, lucky for you!"

    elladine "We won't have much time to chat before we choose, so we'll mostly be going off looks."
    elladine "And speaking of boys..."
    "She gestures to a box of condoms on a nearby table and giggles."
    elladine "I guess we'll be needing a lot of those in the house, won't we?"


    # CHOICE
    menu:
        "Am I going to need the condoms?"
        "I'm not planning to have sex in here":
            $ s3e1p1_grab_some_condoms = False
            s3_mc "Don't get me wrong, I love having sex...but not on TV!"
            s3_mc "I don't want all my family and friends to see me!"
            elladine "Good point."

        "I'll take one now, just in case":
            $ s3e1p1_grab_some_condoms = False
            "You take a single condom and hide it in your bikini for later."
            "Elladine giggles again."
            elladine "You go, girl!"

        "Grab a whole handful":
            $ s3_mc_attr['Funny'] += 1
            $ s3e1p1_grab_some_condoms = True
            "You take a fistful of condoms and stuff them down your top."
            "Elladine giggles again."
            elladine "You go, girl!"

    elladine "I'm going to hold off for now."
    elladine "I probably won't do any big bits right away..."
    elladine "Unless the right guy comes along, obvs."
    elladine "Text! I think that means it's my turn!"
    "She gives you a quick hug before heading to the door."
    elladine "Good luck, [s3_mc_name]. I'll see you down there."

    show elladine at npc_exit

    "She hurries towards the lawn, leaving you alone."
    "There's still only three girls here!"
    "I wonder when the others will be arriving?"
    "You sit down on one of the beds. It's soft and springy."


    # CHOICE
    menu:
        "These beds are really comfy..."
        "Perfect for snuggling":
            $ s3_mc_attr['Sweet'] += 1
            thought "I can't wait till find someone to cuddle up to."
        
        "Perfect for doing bits":
            $ s3_mc_attr['Bold'] += 1
            thought "I'm gonna have so much fun, the whole Villa will shake."
        
        "Maybe I'll take a nap...":
            $ s3_mc_attr['Funny'] += 1
            $ s3e1p1_took_a_nap = True
            thought "Just a little one couldn't hurt..."
            "You lay your head on the pillow and close your eyes."
            "Maybe my Prince Charming will come and wake me with a kiss."
            "You drift off for a few minutes, but then..."

    "Your phone beeps."
    thought "Wait, is it my turn already?"

    "[s3_mc_name], come down to the lawn and couple up! The boys are waiting..."

    thought "Alright, let's do this!"

    scene s3-lawn-day

    "You step out into the brilliant sunshine."
    "Waiting on the lawn are three boys, standing in a line."
    "Elladine and AJ are off to the side, already paired up with their boys."

    show elladine at npc_left
    show aj at npc_right

    "Elladine shoots you an encouraging smile, and AJ gives you a thumbs up."

    show elladine at npc_exit
    show aj at npc_exit

    "Those two have already picked their boys..."
    "Which leaves these three for me to choose from."
    thought "I wonder which one I should pick?"

    show bill at npc_center

    "The first boy steps forward with a cheeky smile."

    # Meeting Bill
    bill "Alright, beautiful? I'm Bill."

    # solo portrait shot of bill
    $ s3_character_profile = "Bill"
    window hide
    show screen s3_character_profile with Pause(3)
    hide screen s3_character_profile with dissolve

    "{i}Bill\n
    -24, from Surrey\n
    -Roofer\n
    -Strong opinions about sandwiches{/i}"

    bill "I'm gonna come right out and say it. You look like a bit of me."

    # CHOICE
    menu:
        "Bill says I'm a bit of him..."
        "Smile politely":
            "You smile at Bill, trying not to give too much away."
            "I'm definitely in there."
        
        "Wink at him":
            $ s3_li_like_mc['Bill'] += 5
            "You shoot a wink in Bill's direction and his face lights up."
        
        "Roll your eyes":
            $ s3_li_like_mc['Bill'] -= 5
            "You roll your eyes at Bill and his face falls."

    show bill at npc_exit

    "You look down the line to the next boy."

    show camilo at npc_center

    camilo "Hola chica. Welcome to the Villa. Amazing, isn't it?"
    s3_mc " Is it?"
    camilo "Well, it is now you're here."

    # solo portrait shot of camilo
    $ s3_character_profile = "Camilo"
    window hide
    show screen s3_character_profile with Pause(3)
    hide screen s3_character_profile with dissolve

    "{i}Camilo\n
    -23, from Romford\n
    -Runs the family shop\n
    -A blackbelt in grafting (and Brazilian jiu-jitsu){/i}"

    camilo "Sorry. That was really cheesy."
    camilo "It's just, I think me and Bill had the exact same reaction..."
    camilo "So I thought I should try and fancy it up a bit."

    # CHOICE
    menu:
        "Camilo definitely likes me..."
        "The feeling is mutual":
            $ s3_li_like_mc['Camilo'] += 5
            "You give Camilo a dazzlinig smile and feel the chemistry crackling between you two."
            "I can't wait to get to know this one better."
        
        "It's too early to say":
            "You shrug and look away."
        
        "More like Camil-no":
            $ s3_li_like_mc['Camilo'] -= 5
            "Camilo deflates a little when he sees you're not into him."
            camilo "Oh..."

    show camilo at npc_exit

    "The third and final boy in the line seems nervous."
    "You raise your eyebrows at him and he smiles, trying to puff out his chest a bit."

    show harry at npc_center

    harry "Hey, I'm Harry."

    # solo portrait shot of harry
    $ s3_character_profile = "Harry"
    window hide
    show screen s3_character_profile with Pause(3)
    hide screen s3_character_profile with dissolve

    "{i}Harry\n
    -21, from York\n
    -Business student\n
    -Usually wears a tie with his swimsuit{/i}"

    harry "For what it's worth, I'm just as gobsmacked as these other two."
    harry "But I won't try to sway you. You've got to listen to your gut."
    harry "Or your heart. Or, like whatever part of your body you trust to make these decisions."

    # CHOICE
    menu:
        "I think Harry's trying to flirt with me, too..."
        "It's working!":
            $ s3_li_like_mc['Harry'] += 5
            "You give Harry a flirty smile. He blushes hard."
            "He's definitely got my attention."
        
        "Bless his heart":
            "Cute, but I'm not sure he knows what he's doing."
        
        "Ugh, no thanks":
            $ s3_li_like_mc['Harry'] -= 5
            "You frown, leaving Harry looking embarrassed."

    show bill at npc_left
    show camilo at npc_right

    "Alright, so these three guys are my options for now."
    "It seems like they're all keen."
    "It's so tough to pick a boy when you know so little about them!"
    "I know more boys might come in later in the series, and I'll get chances to change who I'm coupled up with..."
    "...but for now, whoever I pick is the person I'm probably going to spend the most time with early on."
    "I hope they're all as good as they seem!"

    # CHOICE (appends who you're coupled up with to list)
    # add screen that shows the 3 guys lined up, full body profile shot, and you click on the one you want
    menu:
        "Who should I couple up with?"
        "Bill":
            $ s3_coupled_up_with.append("Bill")
            $ s3_li_like_mc['Bill'] += 5
            s3_mc "The boy I want to couple up with is... Bill!"
            show camilo at npc_exit
            show harry at npc_exit
            show bill at npc_center
            "You stride over to Bill."
            "He grins like he can't hardly believe his luck."
            bill "Nice one."

        "Camilo":
            $ s3_coupled_up_with.append("Camilo")
            $ s3_li_like_mc['Camilo'] += 5
            s3_mc "The boy I want to couple up with is... Camilo!"
            show bill at npc_exit
            show harry at npc_exit
            show camilo at npc_center
            "You stride over to Camilo."
            "He grins like he can't hardly believe his luck."
            camilo "Nice one."

        "Harry":
            $ s3_coupled_up_with.append("Harry")
            $ s3_li_like_mc['Harry'] += 5
            s3_mc "The boy I want to couple up with is... Harry!"
            show camilo at npc_exit
            show bill at npc_exit
            show harry at npc_center
            "You stride over to Harry."
            "He grins like he can't hardly believe his luck."
            harry "Nice one."
    $ s3_current_partner = s3_coupled_up_with[0]
    $ s3_3rd_girl = s3_3rd_girl_options[s3_current_partner]
    menu:
        "Me and [s3_current_partner] are officially coupled up..."
        "Hug him":
            $ s3_li_like_mc[s3_current_partner] += 1
            "As you reach him, you throw your arms around his shoulders."
            "He hugs you back firmly. His hands are warm on the small of your back."

        "Kiss his cheek":
            $ s3_li_like_mc[s3_current_partner] += 1
            "As you reach him, you plant a kiss on his cheek, being careful not to smudge your lipstick."
        
        "Hands off for now":
            "You stand politely at his side, just close enough for your elbows to brush."

    # IF STATEMENT
    if s3_current_partner == "Bill":
        bill "I'm so glad you picked me."
        s3_mc " Did I make the right decision?"
        bill "Definitely. But I would say that, wouldn't I?"
    elif s3_current_partner == "Camilo":
        camilo "I'm so glad you picked me."
        s3_mc " Did I make the right decision?"
        camilo "Definitely. But I would say that, wouldn't I?"
    else:
        harry "I'm so glad you picked me."
        s3_mc "Did I make the right decision?"
        harry "Definitely. But I would say that, wouldn't I?"

    "The two of you go to stand next to the other couples."
    
    show bill at npc_exit
    show camilo at npc_exit
    show harry at npc_exit
    show elladine at npc_center

    elladine "Hey girl! Congratulations!"
    elladine "You really  bagged yourself a hottie there."
    elladine "Um, no offence, Nicky."

    show elladine at npc_left
    show nicky at npc_right

    nicky "None taken."
    nicky "Hi, by the way."
    nicky "I'm Nicky. I'm the lucky guy who's coupled up with Elladine."

    # solo portrait shot of nicky
    $ s3_character_profile = "Nicky"
    window hide
    show screen s3_character_profile with Pause(3)
    hide screen s3_character_profile with dissolve

    "{i}Nicky\n
    -24, from Newcastle\n
    -Music tutor\n
    -Oldest sibling energy{/i}"

    elladine "As soon as I found out he was a musician, I was hooked."
    elladine "I've already got a really good feeling about this one."

    show nicky at npc_exit
    show aj at npc_right

    aj "Er, yeah. Me too."
    "AJ doesn't sound so convinced about her guy..."

    show elladine at npc_exit
    show seb at npc_left

    seb "Alright? My name's Seb. I'm coupled up with AJ."

    # solo portrait shot of seb
    $ s3_character_profile = "Seb"
    window hide
    show screen s3_character_profile with Pause(3)
    hide screen s3_character_profile with dissolve

    "{i}Seb\n
    -28, from Liverpool\n
    -Runs a music shop\n
    -Owns 52 t-shirts and 1 shirt{/1}"

    aj "I coupled up with a musician, too!"
    seb "Well, no. I'm a shopkeeper."
    aj "But you must know about instruments to sell them, right?"
    seb "It's not that kind of music shop. I sell records."
    seb "You know, CDs and vinyl and stuff. There's a coffee shop, too."
    aj "Oh! With you now, sorry."

    "{i}You can't date Nicky or Seb in this season of Love Island The Game, but that doesn't mean you can't be friends! And don't worry - all the other boys, and some of the girls, are options.{/i}"

    aj "This is so nice, you guys! We're already learning so much about each other!"

    show seb at npc_exit
    show nicky at npc_left

    nicky "Whoa there."
    nicky "We're still waiting on two more new girls, right?"

    show aj at npc_exit
    show elladine at npc_right

    elladine " Yeah. I wonder what they'll be like?"

    # CHOICE
    menu:
        "The last two girls..."
        "I can't wait to meet them":
            $ s3_mc_attr['Sweet'] += 1
            s3_mc "We're not a complete Villa crew until everyone's here."

            show elladine at npc_exit
            show aj at npc_right

            aj "Right! I'm so excited for them to get here!"
            nicky "You're not the only ones."
            "Nicky looks over at the two remaining single boys."

        "They better stay away from [s3_current_partner]":
            $ s3_mc_attr['Bold'] += 1
            $ s3_li_like_mc[s3_current_partner] += 1
            nicky "Wow! So committed already, huh?"

            show elladine at npc_exit

            # IF STATEMENT
            if s3_current_partner == "Bill":
                show bill at npc_right

                bill "I kinda like it."
                bill "It's nice to know [s3_mc_name] is feeling it so strongly."
                bill "I mean, if another boy came in right now and tried to couple up with her, I'd have a thing or two to say about it, as well."
            elif s3_current_partner == "Camilo":
                show camilo at npc_right

                camilo "I kinda like it."
                camilo "It's nice to know [s3_mc_name] is feeling it so strongly."
                camilo "I mean, if another boy came in right now and tried to couple up with her, I'd have a thing or two to say about it, as well."
            elif s3_current_partner == "Harry":
                show harry at npc_right
                
                harry "I kinda like it."
                harry "It's nice to know [s3_mc_name] is feeling it so strongly."
                harry "I mean, if another boy came in right now and tried to couple up with her, I'd have a thing or two to say about it, as well."

        "Maybe they got lost on the way here":
            $ s3_mc_attr['Funny'] += 1
            s3_mc "This place isn't exactly well signposted."
            nicky "Bad news for the leftover boys if you're right."

    show aj at npc_exit

    # IF STATEMENT
    if s3_current_partner == "Bill":
        show bill at npc_right
        bill "I wonder if they'd be open to coupling up with each other."
    elif s3_current_partner == "Camilo":
        show camilo at npc_right
        camilo "I wonder if they'd be open to coupling up with each other."
    elif s3_current_partner == "Harry":
        show harry at npc_right
        harry "I wonder if they'd be open to coupling up with each other."

    "[s3_current_partner] looks over at the two remaining single boys."

    # IF STATEMENT
    if s3_current_partner == "Bill":
        "Camilo's smile is still dazzling, but it looks a little more nervous now."
        "Harry stands up straight, trying to look confident."
    elif s3_current_partner == "Camilo":
        "Bill is masking his disappointment by concentrating on the grass between his toes."
        "Harry stands up straight, trying to look confident."
    elif s3_current_partner == "Harry":
        "Bill is masking his disappointment by concentrating on the grass between his toes."
        "Camilo's smile is still dazzling, but it looks a little more nervous now."

    show nicky at npc_exit
    show aj at npc_left

    aj "I feel bad for them. Nobody wants to get picked last."

    show bill at npc_exit
    show camilo at npc_exit
    show harry at npc_exit
    show elladine at npc_right

    elladine "Yeah, and it's pretty obvious they both wanted to get picked by [s3_mc_name]..."
    aj "Well, maybe their perfect soulmates are about to walk out of that door any second."

    show aj at npc_exit
    show seb at npc_left

    seb "Let's not kid ourselves. That kind of thing never happens in the real world."

    show elladine at npc_exit
    show nicky at npc_right

    nicky "Alright, but this isn't exactly a normal situation, is it?"
    nicky "It's Love Island. Where dreams come true."
    seb "Wow, corny."
    nicky "Come on, mate. The magic only works if you believe in it."
    seb "Maybe that's why nothing magical ever happens to me."


    # CHOICE
    menu:
        "Do dreams come true in the Villa?"
        "Nicky's got it right!":
            $ s3_amount_npcs_like_mc['Nicky'] += 2
            s3_mc "I can't wait for whatever's on the horizon!"
            nicky "That's the spirit."
        
        "I don't believe in magic":
            $ s3_amount_npcs_like_mc['Seb'] += 2
            s3_mc "If we're gonna have fun in the Villa, it won't be from magic."
            s3_mc "It'll be from hard grafting."
            seb "You've got that right."
        
        "My dreams are too weird":
            s3_mc "If they manage to make my dreams come true, I'll be impressed."
            s3_mc "Could they even fit a T-Rex in here?"

    "Everyone falls silent as a new girl emerges from the Villa."

    # IF STATEMENT (which women show up in villa first)
    if s3_current_partner == "Harry":
        $ s3_amount_npcs_like_mc["Miki"] = 15
        call s3e1p1_meet_miki
        show miki at npc_exit
        $ s3_amount_npcs_like_mc["Iona"] = 15
        call s3e1p1_meet_iona
    elif s3_current_partner == "Bill":
        $ s3_amount_npcs_like_mc["Iona"] = 15
        call s3e1p1_meet_iona
        show iona at npc_exit
        $ s3_amount_npcs_like_mc["Genevieve"] = 15
        call s3e1p1_meet_genevieve
    elif s3_current_partner == "Camilo":
        $ s3_amount_npcs_like_mc["Miki"] = 15
        call s3e1p1_meet_miki
        show miki at npc_exit
        $ s3_amount_npcs_like_mc["Genevieve"] = 15
        call s3e1p1_meet_genevieve

    # CHOICE
    menu:
        "They've made an impression on each other already..."
        "It's really cute":
            $ s3_mc_attr['Sweet'] += 1
            thought "I hope me and [s3_current_partner] get on as well as they do!"
        
        "It's probably not real":
            $ s3_mc_attr['Bold'] += 1
            thought "It's not like they really know each other..."
            thought "They're probably just showing off."
        
        "I'd be the filling in that sandwich":
            $ s3_mc_attr['Funny'] += 1
            thought "They make such a hot couple!"

    show miki at npc_exit
    show iona at npc_exit
    show genevieve at npc_exit
    show elladine at npc_left

    elladine "I think that's everyone."

    show camilo at npc_exit
    show harry at npc_exit
    show bill at npc_right

    bill "Five great ladies, five great gents, five great couples. Makes sense to me."

    show elladine at npc_exit
    show aj at npc_left

    aj " Don't you think it's a bit early to say whether our couples are great or not?"

    # IF STATEMENT
    if s3_current_partner == "Bill":
        bill "I dunno. I've already got a pretty great feeling about this one."
        iona "Well, it's not a competition."
    elif s3_current_partner == "Camilo":
        camilo "I dunno. I've already got a pretty great feeling about this one."
        miki "Well, it's not a competition."
    elif s3_current_partner = "Harry":
        harry "I dunno. I've already got a pretty great feeling about this one."
        miki "Well, it's not a competition."

    nicky "It sort of is, though. Only the strongest couple can win the fifty grand."

    # CHOICE
    menu:
        "Based on first impressions, I think the strongest couple here will be..."
        "Me and [s3_current_partner]":
            $ s3e1p1_strongest_couple = "MC"
            # IF STATEMENT
            if s3_current_partner == "Bill":
                $ s3_li_like_mc['Bill'] += 1
                bill "Not to bang my own drum or anything, but hard agree."
            elif s3_current_partner == "Camilo":
                $ s3_li_like_mc['Camilo'] += 1
                camilo "Not to bang my own drum or anything, but hard agree."
            elif s3_current_partner = "Harry":
                $ s3_li_like_mc['Harry'] += 1
                harry "Not to bang my own drum or anything, but hard agree."

            show aj at npc_exit
            show elladine at npc_left

            elladine " I can't lie, you two do look super cute together."

        "Miki and Bill" if s3_current_partner == 'Camilo' or s3_current_partner == 'Harry':
            $ s3e1p1_strongest_couple = "Miki and Bill"

        "Iona and Camilo" if s3_current_partner == 'Bill' or s3_current_partner == 'Harry':
            $ s3e1p1_strongest_couple = "Iona and Camilo"

        "Genevieve and Harry" if s3_current_partner == 'Camilo' or s3_current_partner == 'Bill':
            $ s3e1p1_strongest_couple = "Genevieve and Harry"

        "Elladine and Nicky":
            $ s3e1p1_strongest_couple = "Elladine and Nicky"
            $ s3_amount_npcs_like_mc['Elladine'] += 1
            $ s3_amount_npcs_like_mc['Nicky'] += 1

            show aj at npc_exit
            show elladine at npc_left
            elladine "Aw, babes."
        
        "AJ and Seb":
            $ s3e1p1_strongest_couple = "AJ and Seb"
            $ s3_amount_npcs_like_mc['AJ'] += 1
            $ s3_amount_npcs_like_mc['Seb'] += 1

            aj "Wow, really?"
            show aj at npc_exit
            show seb at npc_left
            seb "That's, um... sweet of you to say."

    # IF STATEMENT
    if s3e1p1_strongest_couple == "Miki and Bill" or s3e1p1_strongest_couple == "Iona and Camilo" or s3e1p1_strongest_couple == "Genevieve and Harry":
        if s3_current_partner == "Bill":
            $ s3_li_like_mc['Bill'] -= 1
            bill "Stronger than you and me?"
        elif s3_current_partner == "Camilo":
            $ s3_li_like_mc['Camilo'] -= 1
            camilo "Stronger than you and me?"
        elif s3_current_partner == "Harry":
            $ s3_li_like_mc['Harry'] -= 1
            harry "Stronger than you and me?"

        s3_mc "I'm just being honest."

    show aj at npc_exit
    show elladine at npc_exit
    show seb at npc_exit
    # IF STATEMENT
    if s3_current_partner == "Bill":
        show iona at npc_left
        iona "All I meant was, it might be a competition, but it doesn't really matter who wins."
        iona "We're all just here to find love, right?"
    elif s3_current_partner == "Camilo" or s3_current_partner == "Harry":
        show miki at npc_left
        miki "All I meant was, it might be a competition, but it doesn't really matter who wins."
        miki "We're all just here to find love, right?"


    # CHOICE
    menu:
        "I'm here..."
        "To win the game":
            $ s3_mc_attr['Bold'] += 1
            s3_mc "Don't get me wrong, we all want to find someone..."
            s3_mc "But that doesn't change the fact that this is a competition."
            s3_mc "There will be a winner."
            s3_mc "And that winner will be me."
            # IF STATEMENT
            if s3_current_partner == "Bill":
                bill "Wow. Love that confidence."
            elif s3_current_partner == "Camilo":
                camilo "Wow. Love that confidence."
            elif s3_current_partner == "Harry":
                harry "Wow. Love that confidence."

        "To fall in love":
            $ s3_mc_attr['Sweet'] += 1
            s3_mc "She's right. At the end of the day, all that matters is finding the right person for you."
            s3_mc "That's the only prize worth winning, really."
            # IF STATEMENT
            if s3_current_partner == "Bill":
                $ s3_amount_npcs_like_mc['Iona'] += 1
                iona "Wow, yes. [s3_mc_name] just said it better than I ever could."
            elif s3_current_partner == "Camilo" or s3_current_partner == "Harry":
                $ s3_amount_npcs_like_mc['Miki'] += 1
                miki "Wow, yes. [s3_mc_name] just said it better than I ever could."

        "To have fun":
            $ s3_mc_attr['Funny'] += 1
            $ s3_amount_npcs_like_mc['AJ'] += 1
            s3_mc "This is the holiday of a lifetime."
            s3_mc "Love is great and winning is fine, but why put so much pressure on it?"
            s3_mc "If all I get from this is a few cool new friends, I'll count myself a winner."

            show miki at npc_exit
            show iona at npc_exit
            show aj at npc_left

            aj "Wow, yes. [s3_mc_name] just said it better than I ever could."

    show bill at npc_exit
    show camilo at npc_exit
    show harry at npc_exit
    # IF STATEMENT
    if s3_current_partner == "Harry":
        show iona at npc_right
        iona "Oh my days, you guys!"
        iona "I've got a text!"
    elif s3_current_partner == "Camilo" or s3_current_partner == "Bill":
        show genevieve at npc_right
        genevieve "Oh my days, you guys!"
        genevieve "I've got a text!"

    text "Islanders, it's time to get to know each other a little better. Please make your way to the challenge platform and get ready to unpack some secrets about your fellow Islanders! #excessbaggage #gettingtoknowyou"

    show aj at npc_exit
    show seb at npc_left

    seb "We've only just got here and we're already being challenged?"
    seb "I was hoping we could get a nap first."

    # IF STATEMENT
    if s3e1p1_took_a_nap:
        s3_mc "I had a little nap just before I came out!"
        seb "Oh mate, I wish I'd thought of that. Such a good move."
        seb "A little nap would be just the ticket."
    elif s3e1p1_feeling_hungry:
        seb "I'm a little peckish too."
        s3_mc "Me too! I was saying to Elladine, I'd love some kind of snack."
        show iona at npc_exit
        show genevieve at npc_exit
        if s3_current_partner == "Bill":
            show bill at npc_right
            bill "Maybe I'm the kind of snack you're after."
        elif s3_current_partner == "Camilo":
            show camilo at npc_right
            camilo "Maybe I'm the kind of snack you're after."
        elif s3_current_partner == "Harry":
            show harry at npc_right
            harry "Maybe I'm the kind of snack you're after."
        s3_mc "That's not the kind of snack I mean."

    show seb at npc_exit
    show nicky at npc_left

    nicky "I hate to sound like a stuck record, but it's Love Island."
    nicky "You have seen this show before, right? You didn't just get off at the wrong bus stop and end up here by mistake?"
    nicky "Because if that's what happened, the sooner you admit it, the less awkward it's going to be."

    show bill at npc_exit
    show camilo at npc_exit
    show harry at npc_exit
    show elladine at npc_right

    elladine "Aw, stop teasing him. He just needs a bit of time to get used to it, that's all."

    show nicky at npc_exit
    show camilo at npc_left

    camilo "The challenges are just a bit of fun! It'll help us all get closer as a group."

    show elladine at npc_exit
    show bill at npc_right

    bill "More importantly, we'll find out everyone's saucy secrets."
    camilo "Well, that too, I guess..."
    bill "Don't get me wrong. I've got nothing to hide."
    bill "But I'm excited to find out what the rest of you are holding back."

    show camilo at npc_exit
    show harry at npc_left

    harry "That's true, but we're not just here to mess around and relax, or dig up gossip on each other."
    
    show bill at npc_exit
    show aj at npc_right

    aj "We're not?"
    harry "No! We're here on an important mission! To find someone we love. It's serious business."
    harry "The challenge will focus our minds and get us ready for the road ahead."


    # CHOICE
    menu:
        "Doing the challenge is mostly about..."
        "Getting closer as a group":
            $ s3_mc_attr['Sweet'] += 1
            $ s3_li_like_mc["Camilo"] += 1
            s3_mc "Camilo's right. This challenge sounds like a great way to get to know each other."
            s3_mc "This is what it's all about! I bet it's going to be a right laugh."
        
        "Uncovering everyone's secrets":
            $ s3_mc_attr['Bold'] += 1
            $ s3_li_like_mc["Bill"] += 1
            s3_mc "Bill's right. This is a great chance to expose all our best and worst stories."
            s3_mc "I bet we've all got some really juicy ones, too."
        
        "Bringing out my competitive side":
            $ s3_mc_attr['Bold'] += 1
            $ s3_li_like_mc["Harry"] += 1
            s3_mc "Harry's right. We've all got to be on the ball if we want to make the most of our time here."
            s3_mc "This challenge sounds like a great way to get into the right mindset."

    show harry at npc_exit
    show elladine at npc_left

    elladine "Well, there's only one way to find out."

    show aj at npc_exit
    # IF STATEMENT
    if s3_current_partner == "Harry":
        show iona at npc_right
        iona "Let's go."
    elif s3_current_partner == "Camilo" or s3_current_partner == "Bill":
        show genevieve at npc_right
        genevieve "Let's go."

    show elladine at npc_exit
    if s3_current_partner == "Bill":
        show iona at npc_left
        iona "Woo! I can't wait!"
    elif s3_current_partner == "Camilo" or s3_current_partner == "Harry":
        show miki at npc_left
        miki "Woo! I can't wait!"

    show miki at npc_exit
    show genevieve at npc_exit
    show iona at npc_exit

    "Chattering and laughing, the Islanders head towards the challenge platform."
    "Before you can follow, [s3_current_partner] quietly takes you to one side."

    # IF STATEMENT
    if s3_current_partner == "Bill":
        show bill at npc_center
        bill "Hey, [s3_mc_name]. Sorry to hang back like this."
        bill "I just wanted to have a quick chat with you in private before the challenge, if that's OK."
    elif s3_current_partner == "Camilo":
        show camilo at npc_center
        camilo "Hey, [s3_mc_name]. Sorry to hang back like this."
        camilo "I just wanted to have a quick chat with you in private before the challenge, if that's OK."
    elif s3_current_partner == "Harry":
        show harry at npc_center
        harry "Hey, [s3_mc_name]. Sorry to hang back like this."
        harry "I just wanted to have a quick chat with you in private before the challenge, if that's OK."

    # CHOICE
    menu:
        "[s3_current_partner] wants a chat..."
        "I thought you'd never ask":
            $ s3e1p1_li_wants_chat_response = "Positive"
            $ s3_li_like_mc[s3_current_partner] += 1
            jump s3e1p1_cheeky_snog_before_game

        "Sure, what's up.":
            $ s3e1p1_li_wants_chat_response = "Neutral"
            jump s3e1p1_cheeky_snog_before_game

        "I'd rather just get going.":
            $ s3_li_like_mc[s3_current_partner] -= 1
            $ s3e1p1_li_wants_chat_response = "Negative"
            jump s3e1p1_cheeky_snog_before_game

    label s3e1p1_cheeky_snog_before_game:
        # IF STATEMENT
        # Bill LI
        if s3_current_partner == "Bill":
            if s3e1p1_li_wants_chat_response == "Positive":
                bill "Well, I'm asking now."
            elif s3e1p1_li_wants_chat_response == "Negative":
                bill "Sorry, I'll try to make it quick."
            else:
                bill "Well..."

            bill "I just wanted to say thank you for choosing me."
            bill "You could probably see it on my face, but you absolutely made my day."
            bill "You're blatantly the best-looking girl here."
            bill "And I'm no expert, but even I can see you're the best-dressed, too."

            # CHOICE
            menu:
                "This would be the perfect opportunity.."
                "Go in for a cheeky snog":
                    $ s3e1p1_cheeky_snog = True
                    $ s3_li_like_mc["Bill"] += 1
                    "You bet your eyelashes and tilt your face towards his."
                    "His eyes go wide. His gaze flickers down to your lips, then back up to your eyes."
                    "His voice is suddenly low and breathy."
                    bill "Are you sure?"
                    s3_mc "No time like the present."
                    "He bites his lip."
                    bill "I can't argue with that."
                    "He smiles as your lips meet."
                    "His rough, calloused hands rest firmly on your hips."
                    "Something about his hands seems to fit, as if the two of you have been doing this for years."
                    "Finally, you both break away at the same time."
                    bill "Cor."
                    bill "I didn't see that coming."
                    bill "Did you like it?"
                    bill "Did I like it? Did I like it? [s3_mc_name]..."
                    bill "I loved it."
                    bill "Do you think we could do it again? Like, right now?"
                    s3_mc "All in good time, babe."

                "Maybe later":
                    $ s3e1p1_cheeky_snog = False
                    "There's no rush. I only just got here."

            bill "You seem like a girl who says what's on her mind, and I really admire that."
            bill "I don't do subtlety, see. Whether I like someone or I don't like someone, I come right out and say so."
            bill "So, yeah."
            bill "Obviously I won't try anything on if you're not interested, but I didn't want today to go any further without saying..."
            bill "I'm excited to start getting to know you."

            # CHOICE
            menu:
                "Bill wants to get to know me..."
                "I'm excited to get to know you too":
                    $ s3_li_like_mc['Bill'] += 1
                    s3_mc "I picked you for a reason. I can't wait to see where it leads us."
                    bill "I'm glad you said that."

                "I'm not really interested, sorry":
                    $ s3_li_like_mc['Bill'] -= 2
                    s3_mc "Look, no offence..."
                    s3_mc "But just because I liked you better than the other two, that doesn't mean I actually like you."
                    bill "Oh... OK. I'm sorry."
                    bill "I just assumed..."
                    bill "I'll try to keep that in mind."

                "Let's wait and see how this goes":
                    s3_mc " It's still early days."
                    bill "Yeah, of course."
            
                "Show him the condoms" if s3e1p1_grab_some_condoms:
                    $ s3_mc_attr['Funny'] += 1
                    "You pull your bikini top out a bit and nod."
                    s3_mc " Check this out."
                    bill "Uh, alright...?"
                    "Tentatively, he peers down inside."
                    "He lets out a sharp laugh when he sees the stash of condoms there."
                    bill "That's certainly not what I was expecting to see."
                    bill "Are you trying to send me a message?"
                    bill "Because I already told you, I don't do subtlety."
                    s3_mc "I'm not trying to say anything."
                    s3_mc "I'm just a girl with a top full of condoms, and I thought you ought to know."
                    s3_mc "Seeing as we're being honest with each other right now."
                    bill "Amazing."

            bill "Well, I guess the others must be wondering where we've got to."
            bill "Let's head over for the challenge!"

        # Camilo LI
        elif s3_current_partner == "Camilo":
            if s3e1p1_li_wants_chat_response == "Positive":
                camilo "Well, I'm asking now."
            elif s3e1p1_li_wants_chat_response == "Negative":
                camilo "Sorry, I'll try to make it quick."
            else:
                camilo "Well..."

            camilo "I just wanted to say thank you for choosing me."
            camilo "You could probably see it on my face, but you absolutely made my day."
            camilo "You're blatantly the best-looking girl here."
            camilo "And I'm no expert, but even I can see you're the best-dressed, too."

            # CHOICE
            menu:
                "This would be the perfect opportunity.."
                "Go in for a cheeky snog":
                    $ s3e1p1_cheeky_snog = True
                    $ s3_li_like_mc["Camilo"] += 1
                    "You bet your eyelashes and tilt your face towards his."
                    "His eyes go wide. His gaze flickers down to your lips, then back up to your eyes."
                    "His voice is suddenly low and breathy."
                    camilo "Are you sure?"
                    s3_mc "No time like the present."
                    "He bites his lip."
                    camilo "I can't argue with that."
                    "He draws you into a slow, sensual kiss."
                    "His Hands tangle gently in your hair, stirring up goosebumps on the back of your neck."
                    "Finally, you both break away at the same time."
                    camilo "Blimey."
                    camilo "I didn't see that coming."
                    camilo "Did you like it?"
                    camilo "Did I like it? Did I like it? [s3_mc_name]..."
                    camilo "I loved it."
                    camilo "Do you think we could do it again? Like, right now?"
                    s3_mc "All in good time, babe."

                "Maybe later":
                    $ s3e1p1_cheeky_snog = False
                    "There's no rush. I only just got here."

            camilo "And I don't just mean looks-wise. I think we've got that spark, you know?"
            camilo "It makes me wanna know everything there is to know about you."
            camilo "So, yeah."
            camilo "Obviously I won't try anything on if you're not interested, but I didn't want today to go any further without saying..."
            camilo "I'm excited to start getting to know you."

            # CHOICE
            menu:
                "Camilo wants to get to know me..."
                "I'm excited to get to know you too":
                    $ s3_li_like_mc['Camilo'] += 1
                    s3_mc "I picked you for a reason. I can't wait to see where it leads us."
                    camilo "I'm glad you said that."

                "I'm not really interested, sorry":
                    $ s3_li_like_mc['Camilo'] -= 2
                    s3_mc "Look, no offence..."
                    s3_mc "But just because I liked you better than the other two, that doesn't mean I actually like you."
                    camilo "Oh... OK. I'm sorry."
                    camilo "I just assumed..."
                    camilo "I'll try to keep that in mind."

                "Let's wait and see how this goes":
                    s3_mc " It's still early days."
                    camilo "Yeah, of course."

                "Show him the condoms" if s3e1p1_grab_some_condoms:
                    $ s3_mc_attr['Funny'] += 1
                    "You pull your bikini top out a bit and nod."
                    s3_mc " Check this out."
                    camilo "Uh, alright...?"
                    "Tentatively, he peers down inside."
                    "He lets out a sharp laugh when he sees the stash of condoms there."
                    camilo "That's certainly not what I was expecting to see."
                    camilo "Are you trying to send me a message?"
                    s3_mc "I'm not trying to say anything."
                    s3_mc "I'm just a girl with a top full of condoms, and I thought you ought to know."
                    s3_mc "Seeing as we're being honest with each other right now."
                    camilo "Amazing."

            camilo "Well, I guess the others must be wondering where we've got to."
            camilo "Let's head over for the challenge!"

        # Harry LI
        elif s3_current_partner == "Harry":
            if s3e1p1_li_wants_chat_response == "Positive":
                harry "Well, I'm asking now."
            elif s3e1p1_li_wants_chat_response == "Negative":
                harry "Sorry, I'll try to make it quick."
            else:
                harry "Well..."

            harry "I just wanted to say thank you for choosing me."
            harry "You could probably see it on my face, but you absolutely made my day."
            harry "You're blatantly the best-looking girl here."
            harry "And I'm no expert, but even I can see you're the best-dressed, too."

            # CHOICE
            menu:
                "This would be the perfect opportunity.."
                "Go in for a cheeky snog":
                    $ s3e1p1_cheeky_snog = True
                    $ s3_li_like_mc["Harry"] += 1
                    "You bet your eyelashes and tilt your face towards his."
                    "His eyes go wide. His gaze flickers down to your lips, then back up to your eyes."
                    "His voice is suddenly low and breathy."
                    harry "Are you sure?"
                    s3_mc "No time like the present."
                    "He bites his lip."
                    harry "I can't argue with that."
                    "He looks nervous and excited as you gently press your lips to his."
                    "His hands tentatively come to rest on your lower back."
                    "As the kiss goes on, he becomes more confident, pulling you close against him."
                    "Finally, you both break away at the same time."
                    harry "Gosh."
                    harry "I didn't see that coming."
                    s3_mc "Did you like it?"
                    harry "Did I like it? Did I like it? [s3_mc_name]..."
                    harry "I loved it."
                    harry "Do you think we could do it again? Like, right now?"
                    s3_mc "All in good time, babe."

                "Maybe later":
                    $ s3e1p1_cheeky_snog = False
                    "There's no rush. I only just got here."

            harry "Well..."
            harry "Obviously we've only really got a first impression to go on at the moment."
            harry "But I already feel like you're exactly my type on paper."
            harry "I'm over here trying to act all manly and confident, and then you walk in, and it all just... melts away."
            harry "And the weird thing is, I don't even mind."
            harry "So, yeah."
            harry "Obviously I won't try anything on if you're not interested, but I didn't want today to go any further without saying..."
            harry "I'm excited to start getting to know you."

            # CHOICE
            menu:
                "Harry wants to get to know me..."
                "I'm excited to get to know you too":
                    $ s3_li_like_mc['Harry'] += 1
                    s3_mc "I picked you for a reason. I can't wait to see where it leads us."
                    harry "I'm glad you said that."

                "I'm not really interested, sorry":
                    $ s3_li_like_mc['Harry'] -= 2
                    s3_mc "Look, no offence..."
                    s3_mc "But just because I liked you better than the other two, that doesn't mean I actually like you."
                    harry "Oh...OK. I'm sorry."
                    harry "I just assumed..."
                    harry "I'll try to keep that in mind."

                "Let's wait and see how this goes":
                    s3_mc "It's still early days."
                    harry "Yeah, of course."

                "Show him the condoms" if s3e1p1_grab_some_condoms:
                    $ s3_mc_attr['Funny'] += 1
                    "You pull your bikini top out a bit and nod."
                    s3_mc "Check this out."
                    harry "Uh, alright...?"
                    "Tentatively, he peers down inside."
                    "He lets out a sharp laugh when he sees the stash of condoms there."
                    harry "That's certainly not what I was expecting to see."
                    harry "Are you trying to send me a message?"
                    s3_mc "I'm not trying to say anything."
                    s3_mc "I'm just a girl with a top full of condoms, and I thought you ought to know."
                    s3_mc "Seeing as we're being honest with each other right now."
                    harry "Amazing."

            harry "Well, I guess the others must be wondering where we've got to."
            harry "Let's head over for the challenge!"

    # CHOICE
    menu:
        "We should go and meet the others at the challenge platform..."
        "Yep, let's go":
            s3_mc "I hope they haven't started without us!"
            show bill at npc_exit
            show camilo at npc_exit
            show harry at npc_exit

        "Race you!":
            $ s3_mc_attr['Funny'] += 1
            s3_mc "Last one there has to clean the pool!"
            # IF STATEMENT
            if s3_current_partner == "Bill":
                bill "Wait, wh..."
                show bill at npc_exit
            elif s3_current_partner == "Camilo":
                camilo "Wait, wh..."
                show camilo at npc_exit
            elif s3_current_partner == "Harry":
                harry "Wait, wh..."
                show harry at npc_exit
            "You're already off and running."
            "Seconds later, you hear him laugh, then the sound of his bare feet on the grass as he gives chase."

        "Why don't you carry me?":
            $ s3_mc_attr['Bold'] += 1
            # IF STATEMENT
            if s3_current_partner == "Bill":
                bill "Carry you?"
                s3_mc "That's what I said."
                s3_mc "You can do it, right? Or are these muscles just for show?"
                bill "He smirks and flexes his impressives arms."
                bill "Of course I can do it. Just watch."
                bill "He puts one hand on your back, scoops the other under your legs, and effortlessly sweeps you off your feet."
                bill "To the challenge platform, m'lady?"
                s3_mc " To the challenge platform at once!"
                "He sets off, carrying you bridal-style across the lawn."
                show bill at npc_exit
            elif s3_current_partner == "Camilo":
                bill "Carry you?"
                s3_mc "That's what I said."
                s3_mc "You can do it, right? Or are these muscles just for show?"
                camilo "He smirks and flexes his impressives arms."
                camilo "Of course I can do it. Just watch."
                camilo "He puts one hand on your back, scoops the other under your legs, and effortlessly sweeps you off your feet."
                camilo "To the challenge platform, m'lady?"
                s3_mc " To the challenge platform at once!"
                "He sets off, carrying you bridal-style across the lawn."
                show camilo at npc exit
            elif s3_current_partner == "Harry":
                harry "Carry you?"
                s3_mc "That's what I said."
                s3_mc "You can do it, right? Or are these muscles just for show?"
                harry "Muscles?"
                "He looks down at his arms and gives them an optimistic flex."
                harry "Of course I can do it. Just watch."
                harry "He stretches a bit more, positions himself carefully, then scoops you up in his arms."
                harry "He's stronger than he looks."
                harry "To the challenge platform, m'lady?"
                s3_mc "To the challenge platform at once!"
                "He sets off, carrying you bridal-style across the lawn."
                show harry at npc_exit

    scene edited_sandy_intro

    "It's only day 1, and [s3_mc_name] is already turning heads all over the Villa!"
    # IF STATEMENT
    if s3e1p1_cheeky_snog == True:
        "I think that snog might be one for the record books."
        "Five minutes from first sight to first kiss?"
        "The other girls will never catch up!"
    "She's coupled up with [s3_current_partner] for now, but who knows what could happen at this afternoon's challenge?"

    show elladine at npc_center
    elladine "We've got to kiss the boy we think the clue is about."
    show elladine at npc_exit

    # IF STATEMENT
    if s3_current_partner == "Bill":
        show genevieve at npc_center
        genevieve "I can't believe how big that is..."
        show genevieve at npc_exit
    elif s3_current_partner == "Camilo" or s3_current_partner == "Harry":
        show miki at npc_center
        miki "I can't believe how big that is..."
        show miki at npc_exit

    # CHOICE
    menu:
        "Do you want to contine to next part or go back to the main menu?"
        "Next Part":
            jump s3e1p2
        "Main Menu":
            jump start

# LABELS FOR s3e1p1
label s3e1p1_meet_miki:
    show seb at npc_exit
    show miki at npc_left

    miki "Hi everyone! It's so exciting to be here!"

    # solo profile shot of miki
    $ s3_character_profile = "Miki"
    window hide
    show screen s3_character_profile with Pause(3)
    hide screen s3_character_profile with dissolve

    "{i}Miki\n
    -21, from Cambringe\n
    -Lifestyle vlogger\n
    -Loves it when you smash that subscribe button{/i}"

    miki "I mean, this is Love Island, where dreams come true, right?"
    nicky "Told you so."
    miki "At first I was like, what happens if I totally don't like any of the boys who are left?"
    miki "But now I see the two beautiful boys you've left for me to choose from..."
    miki "I don't know why I was worried."
    "Her eyes linger on Bill."
    miki "What's your name, handsome?"

    show nicky at npc_exit
    show harry at npc_exit
    show camilo at npc_exit
    show bill at npc_right

    bill "I'm Bill. Pleased to meet you, love."
    miki "You seem like a rugged, down-to-earth kind of guy, Bill."
    miki "And they say opposites attract."
    miki "Fancy being coupled up with an offbeat, creative type like me?"
    bill "I'm not exactly going to say no, am I?"
    bill "Beautiful girl asks if you want to couple up, you say yes. Basic common sense, isn't it."
    "She laughs."
    miki "I'll take that as a yes."
    "She takes his hand. Together, they walk back to you and the others."

    return

label s3e1p1_meet_iona:
    show seb at npc_exit
    show iona at npc_left

    "A new girl emerges from the Villa. Everyone falls silent."
    iona "Good morning, Love Island!"
    iona "I don't know about the rest of you, but I'm about ready to do something wild."

    # solo profile shot of iona
    $ s3_character_profile = "Iona"
    window hide
    show screen s3_character_profile with Pause(3)
    hide screen s3_character_profile with dissolve

    "{i}Iona\n
    -23, from Aberdeen\n
    -Apprentice pylon rigger\n
    -Spends all day making sparks fly{/i}"

    show nicky at npc_exit
    show bill at npc_exit
    show harry at npc_exit
    show camilo at npc_right

    camilo "You don't mess around, do you?"
    iona "I certainly don't, babe."
    iona "Is that going to be a problem?"
    camilo "Not at all."
    camilo "In fact, I think it's going to be the opposite of a problem."
    iona "Well, now I just have to couple up with you, don't I?"
    "Iona smirks and walks over to him."
    "He gives her a little salsa-style spin and she laughs."
    "They stride over to stand beside you."

    return

label s3e1p1_meet_genevieve:
    show seb at npc_exit
    show genevieve at npc_left
    "The door opens one last time, and everyone turns to look as another girl struts out onto the lawn."
    genevieve " Hello, darlings."
    genevieve "How are we all doing?"

    # solo profile shot of genevieve
    $ s3_character_profile = "Genevieve"
    window hide
    show screen s3_character_profile with Pause(3)
    hide screen s3_character_profile with dissolve

    "{i}Genevieve\n
    -26, from Gastonbury\n
    -Junior doctor\n
    -Wants to crowd surf into your heart{/i}"

    "Seeing the rest of the Islanders already in their couples, she realises Harry is the only single boy left."
    "She looks him over and smiles."
    genevieve "What's your name, sweetie?"

    show nicky at npc_exit
    show bill at npc_exit
    show camilo at npc_exit
    show harry at npc_right

    harry "Sweetie."
    harry "Er, I mean..."
    harry "Harry. It's Harry."
    genevieve "Lovely to meet you, Harry."
    genevieve "How lucky am I that nobody got to you before me?"
    "She goes over to give him a hug."
    "The two of them come to stand with you, Camilo and the other couples."

    return



#########################################################################
## Episode 1, Part 2
#########################################################################
label s3e1p2:
    scene edited_sandy_intro

    "Last time on this brand spanking new season of Love Island..."
    "The Islander checked out what the Villa has to offer..."
    "...but it wasn't just the immaculately tucked sheets getting a once over."
    "Everyone met each other and hit it off!"

    # IF STATEMENT
    if s3_current_partner == "Bill":
        show bill at npc_center
        bill "Obviously we've only really got a first impression to go on at the moment."
        bill "But I already feel like you're exactly my type on paper."
        show bill at npc_exit
    elif s3_current_partner == "Camilo":
        show camilo at npc_center
        camilo "Obviously we've only really got a first impression to go on at the moment."
        camilo "But I already feel like you're exactly my type on paper."
        show camilo at npc_exit
    elif s3_current_partner == "Harry":
        show harry at npc_center
        harry "Obviously we've only really got a first impression to go on at the moment."
        harry "But I already feel like you're exactly my type on paper."
        show harry at npc_exit

    "Well, almost everyone."
    show aj at npc_center
    aj "Don't you think it's a bit early to say whether our couples are great or not?"
    show aj at npc_exit
    "It's early days, AJ, early days."
    "But you know what they say..."
    "The early bird catches the worm."

    # IF STATEMENT
    if s3e1p1_cheeky_snog:
        "Or in this case, [s3_mc_name] and [s3_current_partner] get smooching!"
        if s3_current_partner == "Bill":
            show bill at npc_center
            bill "Cor"
            show bill at npc_exit
        elif s3_current_partner == "Camilo":
            show camilo at npc_center
            camilo "Blimey"
            show camilo at npc_exit
        elif s3_current_partner == "Harry":
            show harry at npc_center
            harry "Gosh"
            show harry at npc_exit
        "Well said, [s3_current_partner]."

    "Coming up..."
    "The Islander get hands-on with each other's excess baggage."
    show aj at npc_center
    aj "What gave it away?"
    show aj at npc_exit
    "And one clue doesn't add up..."
    show bill at npc_center
    bill "I have no idea who this is about."
    show bill at npc_exit

    scene s3-platform-excess-baggage
    "You and [s3_current_partner] make your way over to the platform where the other Islanders have already gathered."

    show elladine at npc_center
    elladine "There you are..."

    # IF STATEMENT
    if s3e1p1_cheeky_snog:
        "Elladine points at your lips."
        elladine "You've smudged your lipstick, hun. It's on your cheek."
        "You quickly wipe at your cheek. [s3_current_partner] laughs a little."
        show elladine at npc_left
        if s3_current_partner == "Bill":
            show bill at npc_right
            bill "Cheeky."
        elif s3_current_partner == "Camilo":
            show camilo at npc_right
            camilo "Cheeky."
        elif s3_current_partner == "Harry":
            show harry at npc_right
            harry "Cheeky."

    "Everyone is standing around some suitcase on a carousel."
    show harry at npc_exit
    show camilo at npc_exit
    show bill at npc_right
    bill "Those spinny things make me feel dizzy at airports."
    show bill at npc_exit
    show harry at npc_right
    harry "I always want to lie on them and just go round and round."
    harry "They look kinda comfy and you're always exhausted by the time you get to them."
    elladine "I got a text."
    elladine "Ooh, it's the rules of the challenge!"
    elladine "We're starting first."
    elladine "In each suitcase we'll find a secret clue about one of the guys..."
    elladine "Then we kiss the guy who we think the clue's about!"
    elladine "The guy who matches the clue steps forward and we'll see if we snogged the right person."
    elladine "Then it'll be the guys' turn."
    
    show harry at npc_exit
    # IF STATEMENT
    if s3_current_partner == "Harry":
        show miki at npc_right
        miki "So, do we actually have to kiss who we think the clue is about?"
        miki "Or can we just use this as a way to kiss someone we think is hot?"
        elladine "Well, you wouldn't win the game..."
        miki "But you'd get to snog someone you like."
    elif s3_current_partner == "Camilo" or s3_current_partner == "Bill":
        show genevieve at npc_right
        genevieve "So, do we actually have to kiss who we think the clue is about?"
        genevieve "Or can we just use this as a way to kiss someone we think is hot?"
        elladine "Well, you wouldn't win the game..."
        genevieve "But you'd get to snog someone you like."
    
    thought "Whoa, so much could be revealed today..."

    # CHOICE
    menu:
        "I wonder if any of the clues will be about my secret..."
        "sexual attraction to thunder":
            $ s3e1p2_mc_secret = "Thunder"
            thought "The way those clouds rumble when the storms are rolling."
            thought "It is so tantalising."
            thought "It just makes my body tingle..."
        "naughty adventure on a rollercoaster":
            $ s3e1p2_mc_secret = "Rollercoaster"
            thought "That was a ride and a half..."
        "tendency to get too excited by dimples":
            $ s3e1p2_mc_secret = "Dimples"
            thought "I just can't help it, they're just so cute."
            thought "I want to stick my finer in them and fall into a never ending dimple..."
        "fan fiction I wrote when I was younger":
            $ s3e1p2_mc_secret = "Fan Fiction"
            thought "There were some saucy times..."

    thought "It would be funny if that came out on the first day!"
    "[s3_current_partner] coughs, looking at you."
    show elladine at npc_exit
    # IF STATEMENT
    if s3_current_partner == "Bill":
        show bill at npc_left
        bill "You alright, [s3_mc_name]?"
    elif s3_current_partner == "Camilo":
        show camilo at npc_left
        camilo "You alright, [s3_mc_name]?"
    elif s3_current_partner == "Harry":
        show harry at npc_left
        harry "You alright, [s3_mc_name]?"

    show miki at npc_exit
    show genevieve at npc_exit
    show elladine at npc_left
    elladine "Yeah, you look a little farway."
    thought "Oops, I just got lost in thought."
    s3_mc "It's nothing."

# work work work work work

    # CHOICE
    menu:
        "I can't wait to..."
        "Find out the gossip about the boys":
            aj "Same, we've got to find out all the dirt."
        "Win this challenge!":
            elladine "There are no losers or winners in this challenge!"
            elladine "We're just getting to know each other"
            "You and Harry groan."
            harry "What's the point in that then?"

            # IF STATEMENT
            if s3_current_partner == "Bill" or s3_current_partner == "Harry":
                iona "You might get a lot of kisses."
            elif s3_current_partner == "Camilo":
                genevieve "You might get a lot of kisses."
            harry "Oh, OK."
            harry "That doesn't sound too bad."
        "Just kiss some dudes":
            # IF STATEMENT
            if s3_current_partner == "Bill":
                genevieve "I feel you hun."
                genevieve "Can't wait to get some action in here!"
            elif s3_current_partner == "Harry" or s3_current_partner == "Camilo":
                miki "I feel you hun."
                miki "Can't wait to get some action in here!"

    # IF STATEMENT
    if s3_current_partner == "Bill":
        genevieve "I'm just going to kiss whoever I think is the fittest."
        elladine "Right, let's get started!"
        elladine "Iona, can you do the honours?"
        "Iona rushes to the conveyor belt and grabs a suitcase."
        "She wheels it over to the girls and quickly unzips it."
        iona "OK, the clue is..."
        iona "'This boy once woke up spooning a badger...'"
        "The boys look at each other puzzled while the girls huddle closer together."
        aj "That sounds adorable!"
        elladine "It sounds scary! Badgers will mess you up."
        iona "How do you even end up in that situation?"
        genevieve "I bet it was a prank by his mates."
    elif s3_current_partner == "Camilo":
        genevieve "I'm just going to kiss whoever I think is the fittest."
        elladine "Right, let's get started!"
        elladine "Miki, can you do the honours?"
        "Miki rushes to the conveyor belt and grabs a suitcase."
        "She wheels it over to the girls and quickly unzips it."
        genevieve "OK, the clue is..."
        genevieve "'This boy once woke up spooning a badger...'"
        "The boys look at each other puzzled while the girls huddle closer together."
        aj "That sounds adorable!"
        elladine "It sounds scary! Badgers will mess you up."
        genevieve "How do you even end up in that situation?"
        miki "I bet it was a prank by his mates."
    elif s3_current_partner == "Harry":
        miki "I'm just going to kiss whoever I think is the fittest."
        elladine "Right, let's get started!"
        elladine "Iona, can you do the honours?"
        "Iona rushes to the conveyor belt and grabs a suitcase."
        "She wheels it over to the girls and quickly unzips it."
        iona "OK, the clue is..."
        iona "'This boy once woke up spooning a badger...'"
        "The boys look at each other puzzled while the girls huddle closer together."
        aj "That sounds adorable!"
        elladine "It sounds scary! Badgers will mess you up."
        iona "How do you even end up in that situation?"
        miki "I bet it was a prank by his mates."

    elladine "That's a terrible idea all round."
    aj "But which one of these guys do you think it is?"

    # CHOICE
    menu:
        "Who do I think woke up spooning a badger?"
        "Camilo":
            $ s3e1p2_spooned_a_badger = "Camilo"
        "Bill":
            $ s3e1p2_spooned_a_badger = "Bill"
        "Harry":
            $ s3e1p2_spooned_a_badger = "Harry"
        "Nicky":
            $ s3e1p2_spooned_a_badger = "Nicky"
        "Seb":
            $ s3e1p2_spooned_a_badger = "Seb"

    # IF STATEMENT
    if s3_current_partner == "Bill" or s3_current_partner == "Camilo":
        genevieve "I agree with [s3_mc_name]."
        genevieve "There's something about [s3e1p2_spooned_a_badger] that makes me imagine him waking up next to a badger."
    elif s3_current_partner == "Harry":
        miki "I agree with [s3_mc_name]."
        miki "There's something about [s3e1p2_spooned_a_badger] that makes me imagine him waking up next to a badger."

    elladine "So, we've decided it's [s3e1p2_spooned_a_badger]?"
    s3_mc "I think so, yeah."
    aj "So who wants to go kiss him?"

    # IF STATEMENT
    if s3e1p2_spooned_a_badger == "Nicky" or s3e1p2_spooned_a_badger == "Seb":
        elladine "Yeah, go on. I will."
        "Elladine kisses [s3e1p2_spooned_a_badger] on the lips. She leans in for a deep and romantic kiss."
    else:
        # CHOICE
        menu:
            "Should I volunteer to kiss [s3e1p2_spooned_a_badger]?"
            "No thanks, he's not my type":
                $ s3e1p2_challenge_kiss = False
                s3_mc "He's not for me."
                # IF STATEMENT
                if s3_current_partner == "Bill" or s3_current_partner == "Camilo":
                    elladine "Genevieve, you should kiss [s3e1p2_spooned_a_badger]."
                    aj "Yeah, you've dealt with these types before."
                    genevieve "Sure, sure."
                    "Genevieve kisses [s3e1p2_spooned_a_badger] on the lips."
                else:
                    elladine "I'll take one for the team."
                    "She kisses him."
            "Go on then, it's only a game":
                $ s3e1p2_challenge_kiss = True
                s3_mc "I'll do it."
                s3_mc "I'll kiss him."
                # IF STATEMENT
                if s3_current_partner == "Bill" or s3_current_partner == "Harry":
                    iona "Go on, MC!"
                elif s3_current_partner == "Camilo":
                    genevieve "Go on, MC!"
                "You wander over to [s3e1p2_spooned_a_badger]."
                # IF STATEMENT
                if s3e1p2_spooned_a_badger == "Bill":
                    bill "Alright?"
                elif s3e1p2_spooned_a_badger == "Camilo":
                    camilo "Alright?"
                elif s3e1p2_spooned_a_badger == "Harry":
                    harry "Alright?"
                "You kiss [s3e1p2_spooned_a_badger] firmly on the lips."
                "It's tender yet urgent."
                "As you pull away he whispers in your ear."
                # IF STATEMENT
                if s3e1p2_spooned_a_badger == "Bill":
                    bill "You're a really good kisser."
                elif s3e1p2_spooned_a_badger == "Camilo":
                    camilo "You're a really good kisser."
                elif s3e1p2_spooned_a_badger == "Harry":
                    harry "You're a really good kisser."
                "You blush a little and go back to the girls."
            "Do I have to stop at kissing him?":
                $ s3e1p2_challenge_kiss = True
                s3_mc "Let me at him."
                "You stride over to [s3e1p2_spooned_a_badger] and kiss him hard on his lips. You grind your body against his."
                # IF STATEMENT
                if s3e1p2_spooned_a_badger == "Bill":
                    bill "Woah!"
                    genevieve "Woop! Go girl."
                    "You finally pull away. He looks stunned as he wipes his brow."
                    bill "You're seriously a hot kisser."
                elif s3e1p2_spooned_a_badger == "Camilo":
                    camilo "Woah!"
                    miki "Woop! Go girl."
                    "You finally pull away. He looks stunned as he wipes his brow."
                    camilo "You're seriously a hot kisser."
                elif s3e1p2_spooned_a_badger == "Harry":
                    harry "Woah!"
                    miki "Woop! Go girl."
                    "You finally pull away. He looks stunned as he wipes his brow."
                    harry "You're seriously a hot kisser."
                s3_mc "Thanks, babe."
                "You stride back over to the girls."
                aj "Go [s3_mc_name]!"
                elladine "Now that's how you go from G to D."

    elladine "Ok, so whoever woke up to a terrifying bed companion..."
    elladine "Please step forward!"
    "The boys all look at each other."
    "Nicky steps forward."
    genevieve "Nicky!"

    # IF STATEMENT
    if s3e1p2_spooned_a_badger == "Nicky":
        nicky "How'd you know it was me?"
    else:
        aj "Argh, Nicky? I wouldn't have known."
        nicky "I mean, there's not much of a giveaway for that."
        # IF STATEMENT
        if s3e1p2_spooned_a_badger == "Bill":
            bill "Why'd you think it was me?"
        elif s3e1p2_spooned_a_badger == "Camilo":
            camilo "Why'd you think it was me?"
        elif s3e1p2_spooned_a_badger == "Harry":
            harry "Why'd you think it was me?"
        elif s3e1p2_spooned_a_badger == "Seb":
            seb "Why'd you think it was me?"
        aj "I don't know! I could just see you spooning a badger is all."

    bill "Mate, how'd you end up with a badger?"
    nicky "OK, so first off, it was a baby badger that had clearly got lost."
    nicky "It had been a really cold night, so it must have somehow got into my flat and found something warm to cuddle up to."
    nicky "Me."
    aj "So what did you do?"
    nicky "Handed it over to a local animal charity who would try to reunite it with its parents."
    nicky "Though it didn't stop clinging to me until they arrived..."
    camilo "Cute!"

    # IF STATEMENT
    if s3_current_partner == "Bill" or s3_current_partner == "Harry":
        iona "Adorable, but moving on..."
        iona "[s3_mc_name], why don't you go and get the next suitcase?"
    elif s3_current_partner == "Camilo":
        miki "Adorable, but moving on..."
        miki "[s3_mc_name], why don't you go and get the next suitcase?"


    "You head over to the carousel where suitcases are going round and round, and grab one."
    aj "Bring it over, [s3_mc_name]!"
    "You pop the case open. Inside is a label which says..."

    # IF STATEMENT
    if s3_current_partner == "Bill":
        s3_mc "'This boy got caught having sex in his mum's wardrobe.'"
        aj "Woah."
        genevieve "Filthy."
    elif s3_current_partner == "Camilo":
        s3_mc "'This boy got caught having sex at work.'"
        aj "Woah."
        genevieve "Filthy."
    elif s3_current_partner == "Harry":
        s3_mc "'This boy got caught having sex on a roof by someone flying a drone.'"
        aj "Woah."
        miki "Filthy."
        
    elladine "I reckon that's something Seb would do."
    aj "Or maybe it's [s3_current_partner]..."

    # CHOICE
    menu:
        "Which boy is the clue about?"
        "Camilo":
            $ s3e1p2_caught_having_sex = "Camilo"
        "Bill":
            $ s3e1p2_caught_having_sex = "Bill"
        "Harry":
            $ s3e1p2_caught_having_sex = "Harry"
        "Nicky":
            $ s3e1p2_caught_having_sex = "Nicky"
        "Seb":
            $ s3e1p2_caught_having_sex = "Seb"

    # IF STATEMENT
    if s3e1p2_caught_having_sex == "Seb":
        if s3_current_partner == "Bill" or s3_current_partner == "Harry":
            iona "OK, I'll go and kiss them."
            "Iona saunters over plants a kiss on his lips."
            seb "Thank you for that."
            "Iona smiles."
            iona "Any day"
        elif s3_current_partner == "Camilo":
            genevieve "OK, I'll go and kiss them."
            "Genevieve saunters over plants a kiss on his lips."
            seb "Thank you for that."
            "Genevieve smiles."
            genevieve "Any day"
    elif s3e1p2_caught_having_sex == "Nicky":
        if s3_current_partner == "Bill" or s3_current_partner == "Harry":
            iona "OK, I'll go and kiss them."
            "Iona saunters over plants a kiss on his lips."
            nicky "Thank you for that."
            "Iona smiles."
            iona "Any day"
        elif s3_current_partner == "Camilo":
            genevieve "OK, I'll go and kiss them."
            "Genevieve saunters over plants a kiss on his lips."
            nicky "Thank you for that."
            "Genevieve smiles."
            genevieve "Any day"
    else:
        # CHOICES
        menu:
            "Should I go and kiss him?"
            "Yes! Get in there with [s3e1p2_caught_having_sex]":
                $ s3e1p2_challenge_kiss = True
                "You rush over to [s3e1p2_caught_having_sex] and plant a kiss on his lips."
                "[s3e1p2_caught_having_sex] blushes at your touch."
                "You wink at him as you walk back to the girls."
                # IF STATEMENT
                if s3e1p2_first_clue_kiss:
                    if s3_current_partner == "Bill" or s3_current_partner == "Harry":
                        iona "Check out [s3_mc_name] getting all the kisses..."
                        iona "You go, babe."
                    elif s3_current_partner == "Camilo":
                        genevieve "Check out [s3_mc_name] getting all the kisses..."
                        genevieve "You go, babe."
                    s3_mc "Thanks hun!"
                    "You blow all the girls a kiss. They all laugh."
            "Nah, let one of the other girls":
                # IF STATMENT
                if s3_current_partner == "Bill":
                    genevieve "I'll kiss him!"
                    "Genevieve walks over and kisses [s3e1p2_caught_having_sex] quickly."
                    genevieve "Thank you, next!"
                elif s3_current_partner == "Camilo" or s3_current_partner == "Harry":
                    miki "I'll kiss him!"
                    "Miki walks over and kisses [s3e1p2_caught_having_sex] quickly."
                    miki "Thank you, next!"

    iona "Would the guy getting sweaty and sexy in the weird places please come forward?"
    s3_mc "Did I get it right?"
    "[s3_current_partner] steps forward."

    # IF STATEMENT
    if s3_current_partner == "Bill" and s3e1p2_caught_having_sex == "Bill":
        bill "Yeah, you did, hun."
    elif s3_current_partner == "Camilo" and s3e1p2_caught_having_sex == "Camilo":
        camilo "Yeah, you did, hun."
    elif s3_current_partner == "Harry" and s3e1p2_caught_having_sex == "Harry":
        harry "Yeah, you did, hun."
    elif s3_current_partner != s3e1p2_caught_having_sex:
        if s3_current_partner == "Bill":
            bill "Nope. It was me."
        elif s3_current_partner == "Camilo":
            camilo "Nope. It was me."
        elif s3_current_partner == "Harry":
            harry "Nope. It was me."
        
        s3_mc "Aw, I didn't get it right!"

        if s3e1p2_caught_having_sex == "Bill":
            bill "I can't believe you thought it was me."
        elif s3e1p2_caught_having_sex == "Camilo":
            camilo "I can't believe you thought it was me."
        elif s3e1p2_caught_having_sex == "Harry":
            harry "I can't believe you thought it was me."
        elif s3e1p2_caught_having_sex == "Nicky":
            nicky "I can't believe you thought it was me."
        elif s3e1p2_caught_having_sex == "Seb":
            seb "I can't believe you thought it was me."

    # IF STATEMENT
    if s3_current_partner == "Bill":
        aj "Why did you have sex in the wardrobe?"
        aj "Aren't there like coat hangers and stuff?"
        bill "I was having a house party and there was zero privacy."
        aj "Please say your mum didn't catch you."
        bill "No, no."
        bill "She actually has no idea that it happened."
        genevieve "Until now."
        bill "Oh yeah..."
        bill "Awks..."
    elif s3_current_partner == "Camilo":
        camilo "It was closed, OK? And like, I work at my parents' shop so it's basically my shop so it's basically my second house. It would have been fine..."
        camilo "But my dad still believes in getting milk in glass bottles, you know, to save the planet."
        camilo "And, like, after closing up me and this girl decided to get down and dirty on these boxes..."
        camilo "Heat of the moment, like..."
        camilo "But then the next thing I know a whole crate of these milk bottles have smashed and there is milk everywhere."
        harry "Remind me never to buy anything from your shop, like, ever."
    elif s3_current_partner == "Harry":
        harry "We were up on the roof, getting into it, and then I hear this buzzing sound..."
        harry "And there's this drone up there!"
        harry "So I threw my shoe at it."
        aj "Wait, what about the pilot? You could have hurt someone!"
        harry "Drones don't have pilots, AJ. They're only small."
        aj "Oh, right..."
        harry "And besides, it was breaking the law!"
        harry "You shouldn't fly them around built up areas."
        elladine "Right, speaking of laws, what were you doing up on a roof?"
        harry "Just checking out the sights of the city from a different angle."

    # IF STATEMENT
    if s3_current_partner == "Bill" or s3_current_partner == "Camilo":
        genevieve "Moving swiftly on..."
        genevieve "I'll go next."
        "Genevieve grabs another suitcase and reads out the clue."
        genevieve "'This boy rescued a cat from a burning tree.'"
    elif s3_current_partner == "Harry":
        miki "Moving swiftly on..."
        miki "I'll go next."
        "Miki grabs another suitcase and reads out the clue."
        miki "'This boy rescued a cat from a burning tree.'"

    aj "Woah, how many cats get stuck up burning trees?"

    # CHOICE
    menu:
        "Who would rescue a cat?"
        "Camilo":
            $ s3e1p2_rescue_cat = "Camilo"
        "Bill":
            $ s3e1p2_rescue_cat = "Bill"
        "Harry":
            $ s3e1p2_rescue_cat = "Harry"
        "Nicky":
            $ s3e1p2_rescue_cat = "Nicky"
        "Seb":
            $ s3e1p2_rescue_cat = "Seb"

    s3_mc "I reckon it's [s3e1p2_rescue_cat]."

    # IF STATEMENT
    if s3e1p2_rescue_cat == "Seb" or s3e1p2_rescue_cat == "Nicky":
        aj "Yeah, me too."
        aj "I'll take this one."
        "AJ jogs over to [s3e1p2_rescue_cat] and kisses him, stroking his hair a little."
        aj "Meow."
    else:
        # CHOICE
        menu:
            "Should I go and kiss [s3e1p2_rescue_cat]?"
            "Yes! Kiss him all over":
                "You rush over to [s3e1p2_rescue_cat] and smother him in kisses all over his body."
                s3_mc "You're just so kissable."
                "The girls and guys all cheer."
                camilo "Woah."
                # IF STATEMENT
                if s3e1p2_challenge_kiss:
                    if s3_current_partner == "Bill":
                        genevieve "[s3_mc_name] is at it again!"
                    elif s3_current_partner == "Camilo" or s3_current_partner == "Harry":
                        miki "[s3_mc_name] is at it again!"

            "Nah, I don't want to":
                if s3_current_partner == "Bill" or s3_current_partner == "Harry":
                    iona "I think it's Seb."
                    iona "I'm kissing him."
                    "Iona runs over to Seb and kisses him."
                    iona "Am I right?"
                elif s3_current_partner == "Camilo":
                    genevieve "I think it's Seb."
                    genevieve "I'm kissing him."
                    "Genevieve runs over to Seb and kisses him."
                    genevieve "Am I right?"

            "Just a quick peck will do":
                "You walk over to [s3e1p2_rescue_cat] and gently kiss him."
                if s3e1p2_challenge_kiss:
                    if s3_current_partner == "Bill":
                        genevieve "[s3_mc_name] is at it again!"
                    elif s3_current_partner == "Camilo" or s3_current_partner == "Harry":
                        miki "[s3_mc_name] is at it again!"

    # IF STATEMENT
    if s3_current_partner == "Bill" or s3_current_partner == "Camilo":
        genevieve "OK, can the man who risked his nine lives for a cat please come forward!"
    elif s3_current_partner == "Harry":
        iona "OK, can the man who risked his nine lives for a cat please come forward!"

    "Seb steps forward."
    seb "Yeah, it was me. I saved the cat."

    # IF STATEMENT
    if s3e1p2_rescue_cat == "Seb":
        seb "[s3_mc_name] and AJ were right."

    elladine "That's so brave of you Seb."
    seb "We were camping in the middle of nowhere and had just built our campfire."
    seb "A stray cat climbed the tree next to us."
    seb "Then suddenly the wind picked up and the tree caught fire!"
    seb "So I climbed up and caught the cat."

    # CHOICE
    menu:
        "Whoa, Seb saved a cat from a burning tree!"
        "That's so brave":
            s3_mc "That's so brave, Seb!"
            seb "Thanks, [s3_mc_name]."
        "He's foolish":
            thought "He could have gotten hurt!"
            s3_mc "He should have waited for the emergency services."
        "Seb clearly loves cats":
            s3_mc "Oh, you must love cats then to risk your life for them."
            seb "Yeah, cats are pretty awesome."

    aj "Once there was a fire in my dad's kitchen and we were all panicking and trying to find the cats to make sure they were safe..."
    aj "And we found them just stretching out on the floor in my bedroom, directly above where the fire was."
    seb "Cats are always proper dedicated to finding a warm spot."

    # IF STATEMENT
    if s3_current_partner == "Bill":
        genevieve "Or..."
        genevieve "They started the fire to create the warm spot..."
        iona "OK, OK, enough cat talk."
        iona "Final clue girls. Then it's the boy's turn to do the kissing."
        "The boys cheer excitedly."
        iona "[s3_mc_name], you can go and pick another one."
    elif s3_current_partner == "Camilo":
        genevieve "Or..."
        genevieve "They started the fire to create the warm spot..."
        miki "OK, OK, enough cat talk."
        miki "Final clue girls. Then it's the boy's turn to do the kissing."
        "The boys cheer excitedly."
        miki "[s3_mc_name], you can go and pick another one."
    elif s3_current_partner == "Harry":
        miki "Or..."
        miki "They started the fire to create the warm spot..."
        iona "OK, OK, enough cat talk."
        iona "Final clue girls. Then it's the boy's turn to do the kissing."
        "The boys cheer excitedly."
        iona "[s3_mc_name], you can go and pick another one."

    "You run over to the suitcases and grab one."
    aj "What's the clue, MC?"

    # IF STATEMENT
    if s3_current_partner == "Bill":
        s3_mc "'This boy asked a girl out by making her a plate of heart shaped sandwiches!'"
        aj "Aw, that's actually a really sweet one."
    elif s3_current_partner == "Camilo":
        s3_mc "'This boy once flew a date to Rome!'"
        aj "Wow, that's so exciting!"
    elif s3_current_partner == "Harry":
        s3_mc "'This boy once serenaded a girl with a ukulele wearing nothing but a tie.'"
        aj "Aw, that's actually kinda hilarious and sweet all rolled into one."

    # CHOICE
    menu:
        "Which boy would do that?"
        "Camilo":
            $ s3e1p2_asked_girl_out = "Camilo"
        "Bill":
            $ s3e1p2_asked_girl_out = "Bill"
        "Harry":
            $ s3e1p2_asked_girl_out = "Harry"
        "Nicky":
            $ s3e1p2_asked_girl_out = "Nicky"
        "Seb":
            $ s3e1p2_asked_girl_out = "Seb"

    s3_mc "I reckon it's [s3e1p2_asked_girl_out]."

    # IF STATEMENT
    if s3_current_partner == "Bill" or s3_current_partner == "Harry":
        iona "Aw, yeah."
        iona "He's a cutie."
    elif s3_current_partner == "Camilo":
        miki "Aw, yeah."
        miki "He's a cutie."

    # IF STATEMENT
    if s3e1p2_asked_girl_out == "Nicky" or s3e1p2_asked_girl_out == "Seb":
        if s3_current_partner == "Bill" or s3_current_partner == "Harry":
            iona "I'll kiss [s3e1p2_asked_girl_out]!"
            "Iona kisses [s3e1p2_asked_girl_out] on the nose."
            iona "Such a cutie."
        elif s3_current_partner == "Camilo":
            genevieve "I'll kiss [s3e1p2_asked_girl_out]!"
            "Genevieve kisses [s3e1p2_asked_girl_out] on the nose."
            genevieve "Such a cutie."
    else:
        # CHOICE
        menu:
            "Should I go and kiss [s3e1p2_asked_girl_out]?"
            "Why not?":
                "[s3e1p2_asked_girl_out] smiles as you walk over to him."
                s3_mc "Come here, you."
                "You smooch, hands all over each other."
                "Everyone cheers."
            "Yeah, he's a cutie":
                "[s3e1p2_asked_girl_out] smiles as you walk over to him."
                s3_mc "Come here, you."
                "You smooch, hands all over each other."
                "Everyone cheers."
            "Nah, [s3e1p2_asked_girl_out] isn't for me.":
                if s3_current_partner == "Bill" or s3_current_partner == "Harry":
                    iona "I'll kiss [s3e1p2_asked_girl_out]!"
                    "Iona kisses [s3e1p2_asked_girl_out] on the nose."
                    iona "Such a cutie."
                elif s3_current_partner == "Camilo":
                    genevieve "I'll kiss [s3e1p2_asked_girl_out]!"
                    "Genevieve kisses [s3e1p2_asked_girl_out] on the nose."
                    genevieve "Such a cutie."

    # IF STATEMENT
    if s3_current_partner == "Bill":
        iona "Will the hopeless romantic please step forward?"
        "Bill steps forward."
        iona "It's Bill!"
        # IF STATEMENT
        if s3e1p2_asked_girl_out == "Bill":
            thought "I guessed that right!"
        else:
            nicky "That's so sweet, man."
        bill "You can never go wrong with a good sandwich."
        bill "Only problem is that she hated mayo and I had put it in every one."
        bill "I had them for my lunch in the end."
        nicky "Nothing says love like mayo, to be fair."
    elif s3_current_partner == "Camilo":
        genevieve "Will the hopeless romantic please step forward?"
        "Camilo steps forward."
        genevieve "It's Bill!"
        # IF STATEMENT
        if s3e1p2_asked_girl_out == "Camilo":
            camilo "[s3_mc_name] knows me so well already."
        else:
            harry "That's so sweet, man."
            miki "Yeah, you're a real cutie."
    elif s3_current_partner == "Harry":
        iona "Will the hopeless romantic please step forward?"
        "Harry steps forward."
        iona "It's Harry!"
        # IF STATEMENT
        if s3e1p2_asked_girl_out == "Harry":
            thought "I knew it!"
        else:
            elladine "Harry! That's hilarious."
        harry "Yeah, I really can't even play the uke very well but I thought, like, why not."
        bill "And the tie was essential?"
        seb "But the clothes weren't..."
        harry "You've got to look smart, even in the nude."

    elladine "Right now, it's the boys' turn to find out some secrets about the girls!"
    elladine "Everyone switch sides."
    "The girls all line up. Seb runs up and grabs a suitcase."
    seb "OK..."
    seb "'This girl once cooked breakfast in bed for a guy she had just met..."
    seb "...and set his kitchen on fire.'"
    camilo "Oh, wow."
    seb "'...And then didn't call him back.'"

    # CHOICE
    menu:
        "Have I ever set fire to a boy's kitchen and not called him back?"
        "No! That's terrible":
            $ s3e1p2_set_fire = False
        "Oops, yeah, that's about me!":
            $ s3e1p2_set_fire = True

    seb "I reckon, that's..."

    # IF STATEMENT
    if s3_current_partner == "Bill" or s3_current_partner == "Harry":
        seb "Iona."
        "Seb jogs over and kisses her."
        seb "She seems like the fire starting type."
        "Iona crosses her arms and rolls her eyes."
        iona "Mate, part of my job is avoiding fires."
        bill "Is that even a type that, like, people have?"
        aj "It wouldn't work on paper."
        iona "Can the fire starter please step forward..."
    elif s3_current_partner == "Camilo":
        seb "Elladine."
        "Seb jogs over and kisses her."
        seb "She seems like the fire starting type."
        "Elladine gasps."
        camilo "Is that even a type that, like, people have?"
        genevieve "Can the fire starter please step forward..."


    # IF STATEMENT
    if s3e1p2_set_fire:
        "You step forward."
        if s3_current_partner == "Bill" or s3_current_partner == "Harry":
            iona "[s3_mc_name]!"
        elif s3_current_partner == "Camilo":
            genevieve "[s3_mc_name]!"
        aj "Woah, [s3_mc_name]. That's intense."
        s3_mc "Yeah, it was so embarrassing. All I wanted to do was make him breakfast in bed."
        s3_mc "No one got hurt."
        s3_mc "Just my pride..."
        s3_mc "And his kitchen cupboards."
    else:
        "Elladine steps forward."
        genevieve "Elladine!"
        elladine "Yeah, it was an accident, obviously. I was trying to make him a nice fry up."
        elladine "I knocked this kitchen roll off the top shelf and it got caught in the toaster."
        elladine "No one got hurt thankfully, but yeah, I never called him back after that."
        elladine "I was way too embarrassed."

    # IF STATEMENT
    if s3_current_partner == "Bill" or s3_current_partner == "Harry":
        iona "OK boys, next clue."
    elif s3_current_partner == "Camilo":
        genevieve "OK boys, next clue."

    "Nicky picks up a suitcase."
    nicky "Let's see what we've got here."
    "He unzips the case."
    nicky "'This girl hooked up with the chief bridesmaid at a cousin's wedding.'"
    thought "That secret's not about me, but..."

    # CHOICE
    menu:
        "In general would I be interested in being with girls while on Love Island?"
        "Yeah, I'd be interested in dating girls!":
            $ s3_mc_attr['Bisexual'] = True
            thought "If it felt right and I met the right person, I could imagine getting with a girl in here, for sure!"
        "No, I'm going to stick with boys.":
            $ s3_mc_attr['Bisexual'] = False

    nicky "I've got a sneaky suspicion that this secret is about..."
    "He walks over to AJ and kisses her on the lips."
    "As he walks back, AJ grins."
    aj "What gave it away?"
    nicky "I'm not sure, but I definitely get a vibe."
    nicky "I've got a good feel for these things."
    genevieve "Surely you can't tell someone's relationship history just from looking at them."
    aj "You'd be surprised."
    
    # IF STATEMENT
    if s3_mc_attr['Bisexual'] == True:
        "AJ winks at you."
        if s3_current_partner == "Bill":
            genevieve "Wait, what was that?"
        elif s3_current_partner == "Camilo" or s3_current_partner == "Harry":
            miki "Wait, what was that?"
        s3_mc "A code for girls who like girls."
        s3_mc "It's like a secret handshake that we have."
        aj "There's a secret handshake? Why wasn't I told?"
        if s3_current_partner == "Bill":
            s3_mc "Ssh, don't give away that it's fake. We've got to keep Genevieve on her toes."
        elif s3_current_partner == "Camilo" or s3_current_partner == "Harry":
            s3_mc "Ssh, don't give away that it's fake. We've got to keep Miki on her toes."

    # IF STATEMENT
    if s3_current_partner == "Bill" or s3_current_partner == "Harry":
        iona "Good guess, Nicky."
    elif s3_current_partner == "Camilo":
        genevieve "Good guess, Nicky."

    elladine "Next boy, grab a case!"
    "Camilo runs over and picks up a case."

    # IF STATEMENT
    if s3_current_partner == "Bill":
        camilo "'This girl took a job as a waitress to escape a blind date.'"
        thought "Have I taken a job as a waitress to escape a blind date?"
    elif s3_current_partner == "Camilo" or s3_current_partner == "Harry":
        camilo "'This girl did a sexy birthday striptease for a guy...'"
        camilo "'Only to be interrupted by his family, who had flown in to surprise him!'"
        thought "Have I ever gotten interrupted during a sexy dance?"

    # CHOICE
    menu:
        "Is that clue about me?"
        "Yeah, that's about me":
            $ s3e1p2_camilos_clue = True
            thought "I wonder if Camilo will get it right..."
        "No, I've never done that":
            $ s3e1p2_camilos_clue = False
            thought "I wonder who did that..."

    # IF STATEMENT
    if s3_current_partner == "Bill" or s3_current_partner == "Harry":
        camilo "I reckon this is..."
        camilo "Elladine!"
        "He goes over to Elladine and kisses her."
    elif s3_current_partner == "Camilo":
        camilo "I reckon this is..."
        camilo "[s3_mc_name]!"
        "He runs over to you."
        camilo "Mind if I kiss you, [s3_mc_name]?"
        # CHOICE
        menu:
            "Do I mind if Camilo kisses me?"
            "Sure, go for it":
                "He puts a hand behind your head and draws you in close."
                "He tenderly kisses the bottom of your lip."
            "Nah, I'd rather you didn't":
                camilo "That's fine! But just so everyone knows, I think this is about MC!"
                "He walks back to the others."

    elladine "Would the girl please step forward!"
    
    # IF STATEMENT
    if s3e1p2_camilos_clue:
        "You step forward."
        if s3_current_partner == "Bill":
            "Genevieve also steps forward."
            genevieve "Aw! Babe, what a coincidence!"
        elif s3_current_partner == "Camilo" or s3_current_partner == "Harry":
            "Miki also steps forward."
            miki "Oh my god, hun! We're so similar."
        s3_mc "Ha! Yeah..."
        s3_mc "I guess it could happen to anyone."
        if s3_current_partner == "Bill" or s3_current_partner == "Harry":
            camilo "I got that so wrong."
    else:
        if s3_current_partner == "Bill":
            "Genevieve steps forward."
        elif s3_current_partner == "Camilo" or s3_current_partner == "Harry":
            "Miki steps forward."
        camilo "Damn, I got that so wrong."

    # IF STATEMENT
    "Harry goes and picks up a suitcase."
    harry "'This girl...'"
    # IF STATEMENT
    if s3e1p2_mc_secret == "Thunder":
        harry "'...is sexually attracted to the rumble of thunder!'"
    elif s3e1p2_mc_secret == "Rollercoaster":
        harry "'...had a naughty adventure on a rollercoaster!'"
    elif s3e1p2_mc_secret == "Dimples":
        harry "'...has a tendency to get too excited by dimples!'"
    elif s3e1p2_mc_secret == "Fan Fiction":
        harry "'...wrote fan fiction when she was younger!'"
    
    thought "Oh no! This is about me."
    thought "I wonder if Harry can guess who that's about."

    # IF STATEMENT
    if s3_current_partner == "Bill" or s3_current_partner == "Camilo":
        harry "I reckon it's Genevieve."
        "He strides over and kisses Genevieve, accidentally bumping against her nose."
        genevieve "Don't worry. I didn't need my nose..."
        harry "Did I get it right?"
        genevieve "Nope!"
    elif s3_current_partner == "Harry":
        harry "I reckon it's [s3_mc_name]."
        "He walks over to you."
        harry "I've got a hunch it was you because you kinda look guilty..."
        harry "But I also just really want to kiss you."
        harry "You up for that?"

        # CHOICE
        menu:
            "Do I mind if Harry kisses me?"
            "Yeah, sure!":
                "He closes his eyes and leans in for a kiss."
                "He leans the wrong way and bumps against your nose."
                harry "Oops."
                harry "Let me try that again."
                "Your lips touch and you feel him stumble forward a little. He gains his balance and draws you closer."
            "I'd rather you didn't.":
                harry "That's fine! But just so everyone knows, I think this is about [s3_mc_name]!"
                "He walks back to the others."

        harry "Did I get it right?"

    # CHOICE
    menu:
        "The clue was about me! I'd better step forward..."
        "Proudly own it":
            "You leap forward with your hand on your hips."
            s3_mc "It's me!"
            # IF STATEMENT
            if s3e1p2_mc_secret == "Thunder":
                s3_mc "The thunder lover."
            elif s3e1p2_mc_secret == "Rollercoaster":
                s3_mc "The theme park exhibitionist."
            elif s3e1p2_mc_secret == "Dimples":
                s3_mc "The dimple lover."
            elif s3e1p2_mc_secret == "Fan Fiction":
                s3_mc "The smutty dirty lovely fan fiction writer."
        "Shamefully scuffle forward":
            "You step forward slowly, trying not to make any eye contact by looking at the ground."
            s3_mc "Yeah, that's about me."
        "Blame it on someone else":
            s3_mc "Um..."
            s3_mc "How do we know that clue isn't actually about you, Harry?"
            s3_mc "Whoever smelt it dealt it is a motto I live by."
            harry "Er, that's not how the game works."
            seb "Yeah, it's about one of you girls."
            "You shuffle your feet awkwardly."
            seb "It's about you. Isn't it, [s3_mc_name]?"
            s3_mc "Yeah... yeah it is."

    # IF STATEMENT
    if s3_current_partner == "Bill" or s3_current_partner == "Camilo":
        harry "[s3_mc_name]?"
        s3_mc "Yeah."
        harry "Woah, I was well off."
        harry "Ah, sorry, Genevieve."
        genevieve "You have got to tell us more about that later, hun."
    elif s3_current_partner == "Harry":
        harry "Yes! I got it right."
        miki "You have got to tell us more about that later, hun."

    # IF STATEMENT
    if s3_current_partner == "Bill":
        bill "Yeah, I need details."
    elif s3_current_partner == "Camilo":
        camilo "Yeah, I need details."
    elif s3_current_partner == "Harry":
        harry "Yeah, I need details."
    
    # CHOICE
    menu:
        "Everyone wants to hear more about my secret..."
        "Maybe another day...":
            s3_mc "I've got an air of mystery to keep up, haven't I?"
            s3_mc "Maybe I'll reveal more another time."    
        "No way, this is enough already":
            s3_mc "You know too much already and we hardly know each other!"
            s3_mc "I've got a reputation to keep up."
        "This wasn't the half of it":
            s3_mc "I've got even more laundry that needs airing."
            s3_mc "If you want to have a rummage..."

    "Elladine coughs pointedly."

    # IF STATEMENT
    if s3_current_partner == "Bill" or s3_current_partner == "Harry":
        bill "Right, my turn!"
        "Bill goes up and grabs another case."
        bill "'This girl accidentally ordered sex toys to her work address.'"
        # CHOICE
        menu:
            "Have I ever accidentally ordered sex toys to my work?"
            "Yes, how did the suitcase know?":
                $ s3e1p2_ordered_sex_toys = True
                thought "Mysterious, all-seeing suitcase..."
            "Nah, I've never done that.":
                $ s3e1p2_ordered_sex_toys = False
                thought "How embarrassing..."
                thought "I'm glad that's not about me!"

        bill "I reckon this is..."

        # IF STATEMENT
        if s3_current_partner == "Bill":
            bill "[s3_mc_name]?"
            bill "I think it's you, babes."
            "He walks over to you."
            bill "Mind if I kiss you?"
            # CHOICE
            menu:
                "Do I mind if Bill kisses me?"
                "Go for it, babes":
                    "He kisses you softly, His hand rests on your back, drawing you in closer."
                "Nah, I'd rather you didn't":
                    bill "That's fine! But just so everyone knows, I think this is about MC!"
                    "He walks back to the others."

        elif s3_current_partner == "Harry":
            bill "Iona?"
            "He walks over and kisses Iona."

        # IF STATEMENT
        if s3_current_partner == "Bill":
            genevieve "Would the girl with the multiple packages please step forward?"
        elif s3_current_partner == "Harry":
            miki "Would the girl with the multiple packages please step forward?"
        
        # IF STATEMENT
        if s3e1p2_ordered_sex_toys:
            "You and Iona both step forward."
            bill "I got it right!"
            iona "No way."
            iona "That's hilarious."
            iona "You've done that too?"
            s3_mc "Yeah!"
        else:
            "Iona steps forward."
            if s3_current_partner == "Bill":
                bill "Damn, I got it wrong!"
                s3_mc "Can't believe you thought that was me! "
                "He winks at you."
                bill "Maybe I just wanted an excuse to kiss you."
                s3_mc "Cheeky."
            else:
                "Iona steps forward."
                bill "Booyah. I got it right!"
                iona "Booyah?"
                "She winks."
                iona "Boo you more like."

        nicky "Woah, girl."
        nicky "That's like, so embarrassing."
        iona "To be honest, I wasn't embarrassed at all."
        iona "It was just a faff to get all the boxes home on the train."
        harry "Boxes plural? As in more than one?"
        iona "Bulk order discount, babe. "
        "Bill whistles."
        bill "Wow."
        # IF STATEMENT
        if s3_current_partner == "Bill":
            genevieve "Yeah! You go, sister."
        elif s3_current_partner == "Harry":
            miki "Yeah! You go, sister."

    # IF STATEMENT
    if s3e1p1_cheeky_snog:
        if s3_current_partner == "Bill":
            bill "Can I go again?"
            iona "Sure!"
            camilo "I'll go next."
            "He smiles at you as he walks over, hoisting a case over his toned shoulders."
            bill "OK, this girl..."
            "He looks up at you and smiles."
            bill "'This girl has already kissed a boy since we got into the Villa!'"
            iona "We'll all have by the end of this challenge."
            "He turns the piece of paper over."
            bill "'Before the challenge started!'"
            "Everyone laughs."
            genevieve "OK, I have no idea who that was."
            bill "I think I do..."
            "He strides up to you and gently places his palm on your cheek."
            bill "Fancy a round two?"
            # CHOICE
            menu:
                "Do I want Bill to kiss me again?"
                "Yes!":
                    "He leans in and kisses you softly on the lips."
                    genevieve "[s3_mc_name] is getting all the action today!"
                "Nah, you can kiss someone else":
                    bill "OK, suit yourself."
                    bill "I'll give AJ a quick kiss then."
                    "He kisses AJ on the cheek."
                "Go on then, Bill":
                    "He leans in and kisses you softly on the lips."
                    genevieve "[s3_mc_name] is getting all the action today!"
            iona "The answer was, of course..."
            "You step forward."
            iona "[s3_mc_name]!"
            bill "Knew it."
            iona "Oh, you guys!"
            elladine "Such cuties."
            iona "OK..."
            iona "Next round."

            bill "Can I go again?"
            "The other boys cheer him on."
        elif s3_current_partner == "Harry":
            harry "Can I go again?"
            iona "Sure!"
            camilo "I'll go next."
            "He smiles at you as he walks over, hoisting a case over his toned shoulders."
            harry "OK, this girl..."
            "He looks up at you and smiles."
            harry "'This girl has already kissed a boy since we got into the Villa!'"
            iona "We'll all have by the end of this challenge."
            "He turns the piece of paper over."
            harry "'Before the challenge started!'"
            "Everyone laughs."
            miki "OK, I have no idea who that was."
            harry "I think I do..."
            "He strides up to you and gently places his palm on your cheek."
            harry "Fancy a round two?"
            # CHOICE
            menu:
                "Do I want Bill to kiss me again?"
                "Yes!":
                    "He leans in and kisses you softly on the lips."
                    miki "[s3_mc_name] is getting all the action today!"
                "Nah, you can kiss someone else":
                    harry "OK, suit yourself."
                    harry "I'll give AJ a quick kiss then."
                    "He kisses AJ on the cheek."
                "Go on then, Bill":
                    "He leans in and kisses you softly on the lips."
                    miki "[s3_mc_name] is getting all the action today!"
            iona "The answer was, of course..."
            "You step forward."
            iona "[s3_mc_name]!"
            harry "Knew it."
            iona "Oh, you guys!"
            elladine "Such cuties."
            iona "OK..."
            iona "Next round."

            harry "Can I go again?"
            "The other boys cheer him on."
        elif s3_current_partner == "Camilo":
            camilo "I'll go next"
            "He smiles at you as he walks over, hoisting a case over his toned shoulders."
            camilo "OK, this girl..."
            "He looks up at you and smiles."
            camilo "'This girl has already kissed a boy since we got into the Villa!'"
            genevieve "We'll all have by the end of this challenge."
            "He turns the piece of paper over."
            camilo "'Before the challenge started!'"
            "Everyone laughs."
            miki "OK, I have no idea who that was."
            camilo "I think I do..."
            "He strides up to you and gently places his palm on your cheek."
            camilo "Fancy a round two?"
            # CHOICE
            menu:
                "Do I want Bill to kiss me again?"
                "Yes!":
                    "He leans in and kisses you softly on the lips."
                    miki "[s3_mc_name] is getting all the action today!"
                "Nah, you can kiss someone else":
                    camilo "OK, suit yourself."
                    camilo "I'll give AJ a quick kiss then."
                    "He kisses AJ on the cheek."
                "Go on then, Bill":
                    "He leans in and kisses you softly on the lips."
                    miki "[s3_mc_name] is getting all the action today!"
            genevieve "The answer was, of course..."
            "You step forward."
            genevieve "[s3_mc_name]!"
            camilo "Knew it."
            genevieve "Oh, you guys!"
            elladine "Such cuties."
            genevieve "OK..."
            genevieve "Next round."

            camilo "Can I go again?"
            "The other boys cheer him on."
    else:
        if s3_current_partner == "Bill":
            bill "I'll go"
        elif s3_current_partner == "Camilo":
            camilo "I'll go"
        elif s3_current_partner == "Harry":
            harry "I'll go"
    
    "He grabs a case and looks at the clue."
    s3_mc "Just read the secret, hun."

    # IF STATEMENT
    if s3_current_partner == "Bill":
        bill "'This girl has only ever had sex while on the water.'"
    elif s3_current_partner == "Camilo":
        camilo "'This girl has been proposed to six times...'"
    elif s3_current_partner == "Harry":
        harry "'This girl has never had sex with the lights off.'"

    "The boys go into a huddle."
    elladine "Oh my gosh, which of you is this about?"
    "You look around the group. Nobody says anything."
    aj "Come on, girls. It has to be one of us."
    "It quickly becomes clear that the clue isn't about any of you."

    # IF STATEMENT
    if s3_current_partner == "Bill":
        genevieve "I don't get it. Who could it be?"
        iona "It's got to be one of us."
        "A clatter and rattle of wheels grabs everyone's attention as a large suitcase wheels out onto the platform."
        aj "Oh, wow."
        aj "That's one huge suitcase."
        genevieve "I've never seen one that big before..."
        bill "I got a text!"
    elif s3_current_partner == "Camilo":
        genevieve "I don't get it. Who could it be?"
        miki "It's got to be one of us."
        "A clatter and rattle of wheels grabs everyone's attention as a large suitcase wheels out onto the platform."
        aj "Oh, wow."
        aj "That's one huge suitcase."
        genevieve "I've never seen one that big before..."
        camilo "I got a text!"
    elif s3_current_partner == "Harry":
        miki "I don't get it. Who could it be?"
        iona "It's got to be one of us."
        "A clatter and rattle of wheels grabs everyone's attention as a large suitcase wheels out onto the platform."
        aj "Oh, wow."
        aj "That's one huge suitcase."
        miki "I've never seen one that big before..."
        harry "I got a text!"
    
    text "Islanders, there is an unexpected item in your bagging area. [s3_current_partner], please unzip the case."

    elladine "Oh my gosh, [s3_current_partner]! Open up the case already!"
    "[s3_current_partner] tentatively unzips the suitcase."
    "A stunning woman steps out."

    # IF STATEMENT
    if s3_current_partner == "Bill":
        miki "Hey, you lot. I'm Miki."

        # Profile shot of Miki
        "Miki\n
        -21, from Cambridge\n
        -Lifestyle vlogger\n
        -Loves it when you smash the subscribe button"

        "She nods at Bill."
        miki "Thanks for getting me out of there, Bill."
        "Genevieve splutters in shock."
        genevieve "Wait... what? But..."
        iona "It's a new girl!"
        "Elladine and Iona run over to hug Miki."
        elladine "Welcome to the Villa, hun."
        nicky "Yeah, hey. I hope you weren't stuck in there for long, babe."
        miki "Nah, just a few minutes."
    elif s3_current_partner == "Camilo":
        Iona "Hey, you lot. I'm Iona."

        # Profile shot of Iona
        "Iona\n
        -23, from Aberdeen\n
        -Apprentice pylon rigger\n
        -Spends all day making sparks fly"

        "She nods at Camilo."
        iona "Thanks for getting me out of there, Camilo."
        "miki splutters in shock."
        miki "Wait... what? But..."
        genevieve "It's a new girl!"
        "Elladine and Genevieve run over to hug Iona."
        elladine "Welcome to the Villa, hun."
        nicky "Yeah, hey. I hope you weren't stuck in there for long, babe."
        iona "Nah, just a few minutes."
    elif s3_current_partner == "Harry":
        genevieve "Hey, you lot. I'm Genevieve."

        # Profile shot of Genevieve
        "Genevieve\n
        -26, from Gastonbury\n
        -Junior doctor\n
        -Wants to crowd surf into your heart"

        "She nods at Harry."
        genevieve "Thanks for getting me out of there, Harry."
        "Miki splutters in shock."
        miki "Wait... what? But..."
        iona "It's a new girl!"
        "Elladine and Iona run over to hug Genevieve."
        elladine "Welcome to the Villa, hun."
        nicky "Yeah, hey. I hope you weren't stuck in there for long, babe."
        genevieve "Nah, just a few minutes."

    # CHOICE
    menu:
        "There's a new girl in the Villa..."
        "Welcome her with a hug":
            if s3_current_partner == "Bill":
                "You walk over and hug Miki."
                miki "Aw, thanks girls!"
                miki "It's so nice to be so welcomed."
            elif s3_current_partner == "Camilo":
                "You walk over and hug Iona."
                iona "Aw, thanks girls!"
                iona "It's so nice to be so welcomed."
            elif s3_current_partner == "Harry":
                "You walk over and hug Genevieve."
                genevieve "Aw, thanks girls!"
                genevieve "It's so nice to be so welcomed."
            
        "Try and get in the suitcase":
            if s3_current_partner == "Bill":
                "You run past Miki and attempt to clamber into the large suitcase. You fit perfectly, even standing upright."
                s3_mc "Woah, this thing is huge."
                aj "Yeah, how did they get you on the plane in that thing?"
                miki "I didn't ride in it on the plane, hun. I only just got in it."
                aj "Oh right. Yeah, of course."
            elif s3_current_partner == "Camilo":
                "You run past Iona and attempt to clamber into the large suitcase. You fit perfectly, even standing upright."
                s3_mc "Woah, this thing is huge."
                aj "Yeah, how did they get you on the plane in that thing?"
                iona "I didn't ride in it on the plane, hun. I only just got in it."
                aj "Oh right. Yeah, of course."
            elif s3_current_partner == "Harry":
                "You run past Genevieve and attempt to clamber into the large suitcase. You fit perfectly, even standing upright."
                s3_mc "Woah, this thing is huge."
                aj "Yeah, how did they get you on the plane in that thing?"
                genevieve "I didn't ride in it on the plane, hun. I only just got in it."
                aj "Oh right. Yeah, of course."

        "Roll your eyes and ignore her":
            "You roll your eyes. "
            thought "I totally didn't see that coming."
            "You stare at the ground as the other girls crowd around her."

    # IF STATEMENT
    if s3_current_partner == "Bill":
        aj "Wait, we just had a clue, right? Miki, was it about you?"
        aj "Have you really only ever had sex on water?"
        genevieve "How does that even work?"
        "Miki smiles."
        miki "I guess we'll have to wait for the boys to guess before we find out, won't we?"
        bill "Well, I think I can guess who to kiss now..."
        "He takes a step toward her."
        # CHOICE
        menu:
            "Miki and Bill are going to kiss"
            "Cheer them on":
                s3_mc "Woo! Get in there, [s3_current_partner]."
                "He smiles at you."
            "Scream internally, but pretend to be fine":
                thought "..."
                thought "This is a disaster!"
                "Bill walks over to Miki."
                thought "Why me?"
                iona "You OK hun? You look like you're gritting your teeth a bit..."
                s3_mc "I'm fine! Totally fine."
            "Give her the stink eye":
                "You glare at Miki with menacing eyes."
                bill "Chill out, [s3_mc_name]."
                bill "It's just a kiss."

        # IF STATEMENT
        if s3e1p1_cheeky_snog:
            "Bill quickly walks over to Miki and kisses her on the lips tentatively."
            seb "How was it, mate?"
            bill "I'd say that was...maybe the third best kiss I've had today?"
            seb "Wow. You're really cracking on, huh."
        else:
            "Bill and Miki kiss. It feels like it lasts forever."
            "They finally pull away."

        elladine "So, was he right?"
        miki "Yeah, it's true."
        miki "I love the water."
        miki "Oh, I got a text! That was quick."

        text "Islanders, that's the end of the challenge. Hopefully you've all learnt a little bit more about your fellow Islanders. Now all the dirt is dished, it's time for Miki to go and get to know you all."

        miki "Alright! Let's go, huns!"
    elif s3_current_partner == "Camilo":
        aj "Wait, we just had a clue, right? Iona, was it about you?"
        aj "Did you really get proposed six times?"
        miki "Juicy!"
        "Iona smiles."
        iona "I guess we'll have to wait for the boys to guess before we find out, won't we?"
        camilo "Well, I think I can guess who to kiss now..."
        "He takes a step toward her."
        # CHOICE
        menu:
            "Iona and Camilo are going to kiss"
            "Cheer them on":
                s3_mc "Woo! Get in there, [s3_current_partner]."
                "He smiles at you."
            "Scream internally, but pretend to be fine":
                thought "..."
                thought "This is a disaster!"
                "Camilo walks over to Iona."
                thought "Why me?"
                genevieve "You OK hun? You look like you're gritting your teeth a bit..."
                s3_mc "I'm fine! Totally fine."
            "Give her the stink eye":
                "You glare at Iona with menacing eyes."
                camilo "Chill out, [s3_mc_name]."
                camilo "It's just a kiss."
        # IF STATEMENT
        if s3e1p1_cheeky_snog:
            "Camilo quickly walks over to Iona and kisses her on the lips tentatively."
            seb "How was it, mate?"
            camilo "I'd say that was...maybe the third best kiss I've had today?"
            seb "Wow. You're really cracking on, huh."
        else:
            "Camilo and Iona kiss. It feels like it lasts forever."
            "They finally pull away."
        elladine "So, was he right?"
        iona "Yeah, it's true."
        iona "I can't help it, people just always seem to want to marry me."
        iona "Oh, I got a text! That was quick."

        text "Islanders, that's the end of the challenge. Hopefully you've all learnt a little bit more about your fellow Islanders. Now all the dirt is dished, it's time for Iona to go and get to know you all."

        iona "Alright! Let's go, huns!"
    elif s3_current_partner == "Harry":
        aj "Wait, we just had a clue, right? Miki, was it about you?"
        aj "Have you really never ever had sex with the lights off?"
        aj "Do you only do it in the day or something?"
        "Genevieve smiles."
        genevieve "I guess we'll have to wait for the boys to guess before we find out, won't we?"
        harry "Well, I think I can guess who to kiss now..."
        "He takes a step toward her."
        # CHOICE
        menu:
            "Genevieve and Harry are going to kiss"
            "Cheer them on":
                s3_mc "Woo! Get in there, [s3_current_partner]."
                "He smiles at you."
            "Scream internally, but pretend to be fine":
                thought "..."
                thought "This is a disaster!"
                "Harry walks over to Genevieve."
                thought "Why me?"
                iona "You OK hun? You look like you're gritting your teeth a bit..."
                s3_mc "I'm fine! Totally fine."
            "Give her the stink eye":
                "You glare at Genevieve with menacing eyes."
                harry "Chill out, [s3_mc_name]."
                harry "It's just a kiss."

        # IF STATEMENT
        if s3e1p1_cheeky_snog:
            "Harry quickly walks over to Genevieve and kisses her on the lips tentatively."
            seb "How was it, mate?"
            harry "I'd say that was...maybe the third best kiss I've had today?"
            seb "Wow. You're really cracking on, huh."
        else:
            "Harry and Genevieve kiss. It feels like it lasts forever."
            "They finally pull away."
        elladine "So, was he right?"
        genevieve "Yeah, it's true."
        genevieve "What can I say."
        genevieve "I like to be able to see the action..."
        genevieve "Oh, I got a text! That was quick."
    
        text "Islanders, that's the end of the challenge. Hopefully you've all learnt a little bit more about your fellow Islanders. Now all the dirt is dished, it's time for Genevieve to go and get to know you all."
        
        genevieve "Alright! Let's go, huns!"

    "[s3_3rd_girl] struts off towards the Villa, and everyone else follows."
    thought "So, now this [s3_3rd_girl] person is in the mix."
    thought "I should think about how I want to play things with her."
    thought "Do I want to get in her good books early?"
    thought "Or find out her priorities?"
    thought "Maybe I should get to her before the other Islanders do, and get the gossip."
    
    # CHOICE
    menu:
        "Should I get [s3_3rd_girl] over for a private chat?"
        "Spend some time with the new girl":
            $ s3e1p2_talk_to_new_girl = True
            call s3e1p2_talk_to_new_girl
        "Don't talk to her":
            $ s3e1p2_talk_to_new_girl = False
            "You watch her walk off with the others."
            thought "Nah, I'm not bothered."
            thought "I'll just get to know her with the others."

    "You and the other Islanders are lounging by the pool."
    # IF STATEMENT
    if s3_current_outfit in s3_npc_preferred_outfits:
        if s3_current_partner == "Bill":
            bill "By the way. I never got the chance to say it earlier, but I absolutely love the swimsuit."
            bill "It looks so good on you."
        elif s3_current_partner == "Camilo":
            camilo "By the way. I never got the chance to say it earlier, but I absolutely love the swimsuit."
            camilo "It looks so good on you."
        elif s3_current_partner == "Harry":
            harry "By the way. I never got the chance to say it earlier, but I absolutely love the swimsuit."
            harry "It looks so good on you."
    else:
        if s3_current_partner == "Bill":
            bill "Call me shallow, but I love how good you look, [s3_mc_name]."
            bill "Even in your lowkey getup."
        elif s3_current_partner == "Camilo":
            camilo "Call me shallow, but I love how good you look, [s3_mc_name]."
            camilo "Even in your lowkey getup."
        elif s3_current_partner == "Harry":
            harry "Call me shallow, but I love how good you look, [s3_mc_name]."
            harry "Even in your lowkey getup."

    s3_mc "Thanks!"

    # IF STATEMENT
    if s3_current_partner == "Bill" or s3_current_partner == "Harry":
        iona "So, everyone's dirties are out now..."
        iona "And now [s3_3rd_girl] is here."
    elif s3_current_partner == "Camilo":
        genevieve "So, everyone's dirties are out now..."
        genevieve "And now [s3_3rd_girl] is here."

    "[s3_3rd_girl] does a little wave."

    # IF STATEMENT
    if s3_current_partner == "Bill":
        miki "Yeah, it's me."
    elif s3_current_partner == "Camilo":
        iona "Yeah, it's me."
    elif s3_current_partner == "Harry":
        genevieve "Yeah, it's me."

    harry "So much has happened, in so little time!"
    harry "I feel like we're already a solid group."

    # IF STATEMENT
    if s3_current_partner == "Bill":
        iona "I know, right? It's all going down."
        iona "Pretending to be a waitress..."
        if s3e1p2_camilos_clue:
            "She winks at you and Genevieve."
    elif s3_current_partner == "Camilo" or s3_current_partner == "Harry":
        genevieve "I know, right? It's all going down."
        genevieve "Embarrassing sexy dances..."
        if s3e1p2_camilos_clue:
            "She winks at you and Miki."

    # IF STATEMENT
    if s3_current_partner == "Bill":
        nicky "I can't believe Miki's secret."
        bill "Yeah, did you, like, live on a boat or something?"
        miki "Yeah, I do actually."
        bill "Oh, woah. That makes more sense now."
    elif s3_current_partner == "Camilo":
        nicky "I can't believe Iona's secret."
        camilo "You must have seen, like, all the cheesy proposals."
        iona "Yeah, I've seen them all."
        iona "One guy even flew a plane with a message on a banner."
        camilo "Oh, wow."
        "She shrugs."
        iona "He flew the wrong way."
        iona "So my name read 'ANOI'. He was so embarrassed."
    elif s3_current_partner == "Harry":
        nicky "I can't believe Genevieve's secret."
        harry "Yeah, like you've never turned off the lights?"
        genevieve "Nope... never."
        genevieve "I like to be able to see what's happening."
        
    nicky "I thought it was a great clue."
    seb "Yeah, same."
    seb "Shows you've got good life experiences and all that."

    # CHOICE
    menu:
        "What do I think about [s3_3rd_girl]'s clue?"
        "I can't wait to get to know [s3_3rd_girl]!":
            s3_mc "You sound right up my street, [s3_3rd_girl]."
            s3_mc "I can't wait to get to know you!"
            if s3_current_partner == "Bill":
                miki "Aw, thanks, [s3_mc_name]."
            elif s3_current_partner == "Camilo":
                iona "Aw, thanks, [s3_mc_name]."
            elif s3_current_partner == "Harry":
                genevieve "Aw, thanks, [s3_mc_name]."
        "It doesn't say much about her":
            s3_mc "Is it, like, the best reflection of your personality?"
            if s3_current_partner == "Bill":
                miki "Um... no, probably not."
            elif s3_current_partner == "Camilo":
                iona "Um... no, probably not."
            elif s3_current_partner == "Harry":
                genevieve "Um... no, probably not."
            nicky "I think it's a proper funny place to start though."
        "I don't believe [s3_3rd_girl] at all":
            s3_mc "I don't believe you, [s3_3rd_girl]."
            nicky "Why would she make that up?"
            "You shrug."
            s3_mc "It's a game."
            if s3_current_partner == "Bill":
                genevieve "Yeah you've got to stand out."
            elif s3_current_partner == "Camilo" or s3_current_partner == "Harry":
                miki "Yeah you've got to stand out."
            nicky "Yeah, authentically."
            if s3_current_partner == "Bill":
                miki "It's also a bit of a specific thing to lie about..."
            elif s3_current_partner == "Camilo":
                iona "It's also a bit of a specific thing to lie about..."
            elif s3_current_partner == "Harry":
                genevieve "It's also a bit of a specific thing to lie about..."
            s3_mc "Hmm..."

    # IF STATEMENT
    if s3_current_partner == "Bill":
        iona "For real though Miki, you definitely made an entrance."
        iona "Maybe we should all arrive in suitcases next time!"
        miki "Yeah, I thought it was a bit out there at first but it was actually really fun."
        miki "I can't believe all this."
        "She gestures to the Villa."
        miki "It's amazing, isn't it?"
    elif s3_current_partner == "Camilo":
        genevieve "For real though Miki, you definitely made an entrance."
        genevieve "Maybe we should all arrive in suitcases next time!"
        iona "Yeah, I thought it was a bit out there at first but it was actually really fun."
        iona "This place is bigger than I thought it would be!"
    elif s3_current_partner == "Harry":
        iona "For real though Miki, you definitely made an entrance."
        iona "Maybe we should all arrive in suitcases next time!"
        genevieve "It worked really well."
        genevieve "It's so cool to be finally here."
        genevieve "I really needed a holiday."

    aj "Yeah, I'm still getting used to all this."
    elladine "We'll all settle in soon enough."
    camilo "Once we have, like, proper meal together."
    camilo "Then it'll feel like home."
    camilo "Food is the way to my heart..."
    aj "As long as I haven't cooked it, then a good meal is exactly what we need."

    if s3e1p2_set_fire:
        genevieve "Yeah, and hopefully [s3_mc_name] doesn't burn the kitchen down!"
    else:
        genevieve "Yeah, and hopefully Elladine doesn't burn the kitchen down!"

    # CHOICE
    menu:
        "Is food the way to my heart?"
        "Of course! Food makes the heart grow fonder":
            harry "I'm pretty sure it's absence makes the heart fonder."
            bill "Come on, [s3_mc_name] is right."
            bill "Food is the real key to it."
        "Nah, I'm more of a drinks gal":
            s3_mc "Give me a good bottle and I'm happy."
            bill "Nah, you can't beat a good piece of toast."
        "As long as I'm eating it off [s3_current_partner]'s body":
            elladine "Woah, [s3_mc_name]!"
            thought "Did I say that out loud?"
            if s3_current_partner == "Bill":
                "Bill blushes, but grins excitedly."
                bill "You sure did..."
            elif s3_current_partner == "Camilo":
                "Camilo blushes, but grins excitedly."
                camilo "You sure did..."
            elif s3_current_partner == "Harry":
                "Harry blushes, but grins excitedly."
                harry "You sure did..."

    # IF STATEMENT
    if s3_current_partner == "Bill":
        miki "Oh, that's mine."
    elif s3_current_partner == "Camilo":
        iona "Oh, that's mine."
    elif s3_current_partner == "Harry":
        genevieve "Oh, that's mine."
    
    text "[s3_3rd_girl], it's time for you to decide who to couple up with. All Islanders, please gather at the fire pit for the recoupling. #chooseyourmatch #dontlookback"
    
    "[s3_3rd_girl] looks around the group with a cheeky glint in her eye."
    elladine "Who are you going to choose?"

    "Who knows, Elladine?"
    "Who knows...?"
    if s3e1p2_talk_to_new_girl:
        "Well, I guess [s3_mc_name] does."
    else:
        "Well, I guess [s3_3rd_girl] does."
    "Remind me not to let those lot in the kitchen."
    if s3e1p2_set_fire:
        "Especially that [s3_mc_name] and AJ. They're fire hazards."
    else:
        "Especially that Elladine and AJ. They're fire hazards."
    "I don't know how I'd actually stop them. I can't leave this shed."
    "Maybe if I shout loud enough."
    "Coming up..."
    "The Islanders get their graft on."
    if s3_current_partner == "Bill":
        genevieve "Single and ready to mingle, eh?"
        iona "Guess we'll need to keep a close eye on you."
        "And the power is in Miki's hands."
        miki "But, ultimately, I do have to make a choice and so..."
    elif s3_current_partner == "Camilo":
        miki "Single and ready to mingle, eh?"
        genevieve "Guess we'll need to keep a close eye on you."
        "And the power is in Miki's hands."
        iona "But, ultimately, I do have to make a choice and so..."
    elif s3_current_partner == "Harry":
        miki "Single and ready to mingle, eh?"
        iona "Guess we'll need to keep a close eye on you."
        "And the power is in Miki's hands."
        genevieve "But, ultimately, I do have to make a choice and so..."

    # CHOICE
    menu:
        "Do you want to contine to next part or go back to the main menu?"
        "Next Part":
            jump s3e1p3
        "Main Menu":
            jump start

label s3e1p2_talk_to_new_girl:
    thought "Yeah, I'll call her over for a chat."
    s3_mc "Hey [s3_3rd_girl]."
    "She peels away from the others and walks over to you."
    if s3_current_partner == "Bill":
        miki "Hey, hun."
        miki "You all right?"
        s3_mc "Yeah, I thought I'd see if you wanted to have a chat?"
        s3_mc "Girl to girl."
        miki "I'd love to."
        miki "Roof terrace? I've been dying to check it out."
        s3_mc "Great idea."
        "You and [s3_3rd_girl] sit beside each other on the roof."
        miki "Thanks for this."
        miki "Like, I was so worried coming in later."
        miki "Because everyone else has had a chance to couple up and meet each other first."
        # CHOICE
        menu:
            "[s3_3rd_girl] was worried about coming in late..."
            "You don't need to worry":
                s3_mc "Everyone seems pretty chill."
                s3_mc "Plus, we've only been here for a few hours!"
                miki "That's true, yeah."
                miki "You're so right."
            "I've got your back":
                miki "Really?"
                s3_mc "Always."
            "I would have been terrified":
                miki "I was proper worried."

        miki "I literally live on a boat, but when I got out of that suitcase I felt so unsteady on my legs."
        s3_mc "Yeah, it's a pretty surreal experience."
        s3_mc "But it'll be fun, you'll see."
        miki "For sure."
        miki "I'm so glad you called me over."
        miki "I wanted to talk to you about who I'm crushing on right now."
        s3_mc "Oh, yeah?"
        miki "Yeah, you see..."
        "She looks down, then up again."
        miki "I'm actually really attracted to Bill."
        
        # CHOICE
        menu:
            "[s3_3rd_girl] is into [s3_current_partner]!"
            "I totally saw that coming":
                miki "You did?"
                s3_mc "Yeah, I had a hunch."
            "Yeah, I don't blame you! He's gorgeous":
                miki "He is, isn't he?"
                miki "And a sweetheart as well."
            "But I'm with him!":
                miki "I know, I know."

        miki "That's why I wanted to talk to you."
        miki "Right now, if I had to couple up with someone, I'd for sure pick Camilo/Harry/Bill."
        miki "I've got to choose someone so I wanted to be super upfront with you about it."
        miki "I know it's early days..."
        s3_mc "It's only been a few hours."
        miki "...but feelings get so magnified in here."

        # CHOICE
        menu:
            "How do I feel about the idea of [s3_3rd_girl] picking [s3_current_partner]?"
            "I'd be OK about it":
                miki "Really?"
                s3_mc "Yeah, like you said, early days."
            "At least you told me":
                miki "I thought it was the best thing to do."
            "I'd be annoyed":
                miki "Oh, really?"
                s3_mc "Yeah."
                miki "Well, I'm sorry you feel like that."
                miki "I hope we can move past, like, whatever happens."
                miki "If it happens."

        miki "I've got no clue whatsoever how he feels about me."
        miki "But I really wanted to talk to you about it."
        miki "So, thank you for taking the time to talk to me..."
        miki "It means a lot."
        miki "We should get back to the others."
        "You both head down from the roof terrace."
    elif s3_current_partner == "Camilo":
        iona "Hey, hun."
        iona "You all right?"
        s3_mc "Yeah, I thought I'd see if you wanted to have a chat?"
        s3_mc "Girl to girl."
        iona "I'd love to."
        iona "Roof terrace? I've been dying to check it out."
        s3_mc "Great idea."
        "You and [s3_3rd_girl] sit beside each other on the roof."
        iona "Thanks for this."
        iona "Like, I was so worried coming in later."
        iona "Because everyone else has had a chance to couple up and meet each other first."
        # CHOICE
        menu:
            "[s3_3rd_girl] was worried about coming in late..."
            "You don't need to worry":
                s3_mc "Everyone seems pretty chill."
                s3_mc "Plus, we've only been here for a few hours!"
                iona "That's true, yeah."
                iona "You're so right."
            "I've got your back":
                iona "Really?"
                s3_mc "Always."
            "I would have been terrified":
                iona "I was proper worried."

        iona "I work on pylons, like, they're proper high and it can get kinda windy."
        iona "But that doesn't scare me."
        iona "But coming onto this..."
        iona "Mate, I was terrified."
        s3_mc "Yeah, it's a pretty surreal experience."
        s3_mc "But it'll be fun, you'll see."
        iona "For sure."
        iona "I'm so glad you called me over."
        iona "I actually really wanted to chat with you about who I'm keen on."
        s3_mc "Oh, yeah?"
        iona "Yeah, you see..."
        "She looks down, then up again."
        iona "When I look at the boys, the one who really makes me go 'he's my type' is Camilo."
        iona "He's banging."
        
        # CHOICE
        menu:
            "[s3_3rd_girl] is into [s3_current_partner]!"
            "I totally saw that coming":
                iona "You did?"
                s3_mc "Yeah, I had a hunch."
            "Yeah, I don't blame you! He's gorgeous":
                iona "He is, isn't he?"
                iona "And a sweetheart as well."
            "But I'm with him!":
                iona "I know, I know."

        iona "That's why I wanted to talk to you."
        iona "Right now, if I had to couple up with someone, I'd for sure pick Camilo/Harry/Bill."
        iona "I've got to choose someone so I wanted to be super upfront with you about it."
        iona "I know it's early days..."
        s3_mc "It's only been a few hours."
        iona "...but feelings get so magnified in here."

        # CHOICE
        menu:
            "How do I feel about the idea of [s3_3rd_girl] picking [s3_current_partner]?"
            "I'd be OK about it":
                iona "Really?"
                s3_mc "Yeah, like you said, early days."
            "At least you told me":
                iona "I thought it was the best thing to do."
            "I'd be annoyed":
                iona "Oh, really?"
                s3_mc "Yeah."
                iona "Well, I'm sorry you feel like that."
                iona "I hope we can move past, like, whatever happens."
                iona "If it happens."

        iona "And also, I don't know if he likes me the same way."
        iona "But I really wanted to talk to you about it."
        iona "So, thank you for taking the time to talk to me..."
        iona "It means a lot."
        iona "We should get back to the others."
        "You both head down from the roof terrace."
    elif s3_current_partner == "Harry":
        genevieve "Hey, hun."
        genevieve "You all right?"
        s3_mc "Yeah, I thought I'd see if you wanted to have a chat?"
        s3_mc "Girl to girl."
        genevieve "I'd love to."
        genevieve "Roof terrace? I've been dying to check it out."
        s3_mc "Great idea."
        "You and [s3_3rd_girl] sit beside each other on the roof."
        genevieve "Thanks for this."
        genevieve "Like, I was so worried coming in later."
        genevieve "Because everyone else has had a chance to couple up and meet each other first."
        # CHOICE
        menu:
            "[s3_3rd_girl] was worried about coming in late..."
            "You don't need to worry":
                s3_mc "Everyone seems pretty chill."
                s3_mc "Plus, we've only been here for a few hours!"
                genevieve "That's true, yeah."
                genevieve "You're so right."
            "I've got your back":
                genevieve "Really?"
                s3_mc "Always."
            "I would have been terrified":
                genevieve "I was proper worried."

        
        genevieve "I mean, I'm used to huge crowds and dealing with sick people and all this intense stuff, from work."
        genevieve "But this was so beyond that."
        genevieve "Also that suitcase was kinda dark which freaked me out a bit."
        genevieve "Luckily I wasn't in there for long."
        s3_mc "Yeah, it's a pretty surreal experience."
        s3_mc "But it'll be fun, you'll see."
        genevieve "For sure."
        genevieve "I'm so glad you called me over."
        genevieve "I wanted to say, I'm actually low-key into someone already."
        s3_mc "Oh, yeah?"
        genevieve "Yeah, you see..."
        "She looks down, then up again."
        genevieve "Harry is definitely a bit of me."
    
        # CHOICE
        menu:
            "[s3_3rd_girl] is into [s3_current_partner]!"
            "I totally saw that coming":
                genevieve "You did?"
                s3_mc "Yeah, I had a hunch."
            "Yeah, I don't blame you! He's gorgeous":
                genevieve "He is, isn't he?"
                genevieve "And a sweetheart as well."
            "But I'm with him!":
                genevieve "I know, I know."

        genevieve "That's why I wanted to talk to you."
        genevieve "Right now, if I had to couple up with someone, I'd for sure pick Camilo/Harry/Bill."
        genevieve "I've got to choose someone so I wanted to be super upfront with you about it."
        genevieve "I know it's early days..."
        s3_mc "It's only been a few hours."
        genevieve "...but feelings get so magnified in here."

        # CHOICE
        menu:
            "How do I feel about the idea of [s3_3rd_girl] picking [s3_current_partner]?"
            "I'd be OK about it":
                genevieve "Really?"
                s3_mc "Yeah, like you said, early days."
            "At least you told me":
                genevieve "I thought it was the best thing to do."
            "I'd be annoyed":
                genevieve "Oh, really?"
                s3_mc "Yeah."
                genevieve "Well, I'm sorry you feel like that."
                genevieve "I hope we can move past, like, whatever happens."
                genevieve "If it happens."

        genevieve "I've no idea how he feels, like."
        genevieve "But I really wanted to talk to you about it."
        genevieve "So, thank you for taking the time to talk to me..."
        genevieve "It means a lot."
        genevieve "We should get back to the others."
        "You both head down from the roof terrace."



#########################################################################
## Episode 1, Part 3
#########################################################################
label s3e1p3:
    "Welcome back..."
    "To Love Island!"
    "In an absolutely shocking twist that literally no one could have predicted..."
    "Another girl has already entered the Villa!"
    if s3_current_partner == "Bill":
        miki "Hey, you lot. I'm Miki."
        miki "Thanks for getting me out of there."
    elif s3_current_partner == "Camilo":
        iona "Hey, you lot. I'm Iona."
        iona "Thanks for getting me out of there."
    elif s3_current_partner == "Harry":
        genevieve "Hey, you lot. I'm Genevieve."
        genevieve "Thanks for getting me out of there."
    "Ladies, hide your men, this one's coming for them..."
    "Though it'll be hard to hide them in a Villa covered in cameras..."
    "Maybe if they put the sheets over their heads and pretend to be ghosts?"
    "Or stand really still and pretend to be statues?"
    "I don't know. I've never played a game of Hide and Seek in my life."
    "Coming up!"
    "Bill gets cheesy..."
    bill "I don't know about the rest of you, but I'm cream-crackered."
    if s3_current_partner == "Bill":
        "And Miki takes her pick..."
        miki "The guy I'd like to couple up with is..."
    elif s3_current_partner == "Camilo":
        "And Iona takes her pick..."
        iona "The guy I'd like to couple up with is..."
    elif s3_current_partner == "Harry":
        "And Genevieve takes her pick..."
        genevieve "The guy I'd like to couple up with is..."

    "The dressing room is a flurry of activity as the girls ready themselves for [s3_3rd_girl]'s decision."
    # IF STATEMENT
    if s3_current_partner == "Bill" or s3_current_partner == "Harry":
        iona "It's so weird knowing that [s3_3rd_girl]'s just stood by the firepit waiting for us."
    elif s3_current_partner == "Camilo":
        genevieve "It's so weird knowing that [s3_3rd_girl]'s just stood by the firepit waiting for us."
    
    if s3_current_partner == "Bill":
        genevieve "Waiting for the guys more like."
        elladine "Yeah. It really didn't take long for the drama to start."
        genevieve "Tell me about it! I thought we'd at least have a day or something."
    elif s3_current_partner == "Camilo" or s3_current_partner == "Harry":
        miki "Waiting for the guys more like."
        elladine "Yeah. It really didn't take long for the drama to start."
        miki "Tell me about it! I thought we'd at least have a day or something."

    if s3_current_partner == "Bill" or s3_current_partner == "Harry":
        iona "Well, we kind of did."
    elif s3_current_partner == "Camilo":
        genevieve "Well, we kind of did."
    
    aj "Can you pass me my lipstick, Ella, babes."
    elladine "Of course hun."
    aj "Thanks! [s3_3rd_girl]'s super fit, don't you think?"

    # CHOICE
    menu:
        "[s3_3rd_girl] is..."
        "Almost too good looking":
            elladine "Yeah..."
        "Not really all that":
            elladine "I don't know how you can say that?"
        "Not as fit as me":
            elladine "You're both gorgeous."

    elladine "She's definitely some fierce competition."
    aj "That's why I want to make a special effort."
    thought "Everyone's going all out. I guess if there was a night for it, now's the time..."

    # IF STATEMENT
    if s3e1p1_grab_some_condom:
        "You absent-mindedly undo your bra, then hear the telltale sound of plastic wrappers hitting the floor."
        s3_mc "The condoms!"
        "Different coloured wrappers indicating flavours spill across the room. Cherry red, banana yellow, and wheatgrass green."
        aj "Woah, [s3_mc_name]!"
        s3_mc "Whoops..."
        aj "Someone's looking to get busy."
        s3_mc "Better to be safe than sorry."
        elladine "Damn right."

    # Evening wear outfit selector
    # change all npcs to evening wear

    # IF STATEMENT
    if s3_current_outfit in s3_npc_preferred_outfits["Elladine"]:
        thought "Oh yeah, this is going to blow some minds."
        "Elladine looks over to you. Her eyes go wide."
        elladine "Damn! [s3_mc_name], you're a real heart-stealer in that!"
        s3_mc "That's the idea."
    else:
        s3_mc "Or, I could just wear this I guess..."
        elladine "Not going to push the boat out a bit? You must be confident."


    if s3_current_partner == "Bill" or s3_current_partner == "Harry":
        "Iona turns to you."
        iona "Are you worried about tonight, babe?"
    elif s3_current_partner == "Camilo":
        "Genevieve turns to you."
        genevieve "Are you worried about tonight, babe?"

    # CHOICE
    menu:
        "Am I worried about who Miki will pick?"
        "I'd be lying if I said no":
            if s3_current_partner == "Bill" or s3_current_partner == "Harry":
                iona "Yeah, I know what you mean."
                iona "Why am I so nervous?"
            elif s3_current_partner == "Camilo":
                genevieve "Yeah, I know what you mean."
                genevieve "Why am I so nervous?"
        "No, of course I'm not":
            if s3_current_partner == "Bill" or s3_current_partner == "Harry":
                iona "Yeah..."
                iona "I don't know. I feel surprisingly nervous myself."
            elif s3_current_partner == "Camilo":
                genevieve "Yeah..."
                genevieve "I don't know. I feel surprisingly nervous myself."
        "How could I when I look this good?":
            elladine "Wow, hun. I wish I had your confidence!"
            aj "She's not wrong, though."
            if s3_current_partner == "Bill" or s3_current_partner == "Harry":
                iona "Hearing that actually made me feel a little better myself."
            elif s3_current_partner == "Camilo":
                genevieve "Hearing that actually made me feel a little better myself."
        "Actually, I know she's going to pick [ss3_current_partner]." if s3e1p2_talk_to_new_girl == True:
            if s3_current_partner == "Bill" or s3_current_partner == "Harry":
                iona "Really? How?"
                s3_mc "She told me."
                iona "Oh..."
            elif s3_current_partner == "Camilo":
                genevieve "Really? How?"
                s3_mc "She told me."
                genevieve "Oh..."
            elladine "At least she was honest, I guess?"

    if s3_current_partner == "Bill":
        "Genevieve takes a deep breath, and gives herself one last look-over in the mirror."
        genevieve "Well, girls, I guess this is it..."
    elif s3_current_partner == "Camilo" or s3_current_partner == "Harry":
        "Miki takes a deep breath, and gives herself one last look-over in the mirror."
        miki "Well, girls, I guess this is it..."

    "[s3_3rd_girl] stands in front of the Islanders sat around the firepit."

    # CHOICE
    menu:
        "We only just arrived and already I might get separated from [s3_current_partner]..."
        "Hold his hand":
            if s3_current_partner == "Bill":
                "You reach over and take a hold of [s3_current_partner]'s hand. He turns and smiles at you."
                bill "Your hands are so soft."
                "You blush"
                bill "Seriously, it's like holding a warm loaf of bread or something..."
                s3_mc "Huh?"
                bill "...I don't know. Ignore me. My mind's all over the place."
                "He shifts in his seat."
            elif s3_current_partner == "Camilo":
                "You reach over and take a hold of [s3_current_partner]'s hand. He turns and smiles at you."
                camilo "Your hands are so soft."
                "You blush"
                camilo "Seriously, it's like holding a warm loaf of bread or something..."
                s3_mc "Huh?"
                camilo "...I don't know. Ignore me. My mind's all over the place."
                "He shifts in his seat."
            elif s3_current_partner == "Harry":
                "You reach over and take a hold of [s3_current_partner]'s hand. He turns and smiles at you."
                harry "Your hands are so soft."
                "You blush"
                harry "Seriously, it's like holding a warm loaf of bread or something..."
                s3_mc "Huh?"
                harry "...I don't know. Ignore me. My mind's all over the place."
                "He shifts in his seat."

        "Glare at [s3_3rd_girl]":
            "You frown at [s3_3rd_girl]. She doesn't look at you."
            s3_mc "Dammit, she didn't see me!"
            "You squint harder and lean in closer."
            thought "She has to notice me now."
            "Just then, you hear [s3_current_partner]'s voice whispering in your ear."
            if s3_current_partner == "Bill":
                bill "Um, what are you doing?"
                s3_mc "Huh?"
                bill "Do you need glasses or something?"
            elif s3_current_partner == "Camilo":
                camilo "Um, what are you doing?"
                s3_mc "Huh?"
                camilo "Do you need glasses or something?"
            elif s3_current_partner == "Harry":
                harry "Um, what are you doing?"
                s3_mc "Huh?"
                harry "Do you need glasses or something?"
            s3_mc "No..."

        "Look at the other Islanders":
            "You look around to see how the others are handling [s3_3rd_girl]'s arrival."
            thought "If those girls are nervous, they're doing a banging job of hiding it."
            "The only one who seems a little off is Elladine, who occasionally glances at her hands."
            "The boys seem calm, too. But you look harder, you notice that Seb's chewing his cheek."
            if s3_current_partner == "Bill":
                "Harry can't keep his eyes off of Miki."
                "Camilo's eyes are fixed on Genevieve's face. He bites his lips."
            elif s3_current_partner == "Camilo":
                "Harry can't keep his eyes off of Miki."
            elif s3_current_partner == "Harry":
                "Camilo's eyes are fixed on Genevieve's face. He bites his lips."
            thought "Any of these guys would probably jump at the chance to be with [s3_3rd_girl]..."

    "[s3_3rd_girl] clears her throat, then speaks."

    if s3_current_partner == "Bill":
        miki "I didn't know how to feel on the way here."
        miki "I was excited, obviously, but I knew I'd be taking a guy away from another girl."
        miki "I thought I'd be OK with that as you've only been together since this morning..."
        miki "But looking at you all now, you already seem like such cute couples."
        miki "But at first glance, this boy seems like my type on paper."
        miki "He's smart, funny, and just dreamy."
        miki "And although I don't want to break a promising couple up so early on..."
        miki "I'm here to make a choice and so..."
        "Everyone tenses."

        if s3e1p2_talk_to_new_girl:
            thought "Here she goes. About to pick [s3_current_partner]..."
        else:
            thought "She better not pick [s3_current_partner]."
        miki "The boy I'd like to couple up with is..."
        thought "Maybe she won't?"
        miki "[s3_current_partner]."
    elif s3_current_partner == "Camilo":
        iona "I didn't know how to feel on the way here."
        iona "I was excited, obviously, but I knew I'd be taking a guy away from another girl."
        iona "I thought I'd be OK with that as you've only been together since this morning..."
        iona "But looking at you all now, you already seem like such cute couples."
        iona "But at first glance, this boy seems like my type on paper."
        iona "He's smart, funny, and just dreamy."
        iona "And although I don't want to break a promising couple up so early on..."
        iona "I'm here to make a choice and so..."
        "Everyone tenses."
        if s3e1p2_talk_to_new_girl:
            thought "Here she goes. About to pick [s3_current_partner]..."
        else:
            thought "She better not pick [s3_current_partner]."
        iona "The boy I'd like to couple up with is..."
        thought "Maybe she won't?"
        iona "[s3_current_partner]."
    elif s3_current_partner == "Harry":
        genevieve "I didn't know how to feel on the way here."
        genevieve "I was excited, obviously, but I knew I'd be taking a guy away from another girl."
        genevieve "I thought I'd be OK with that as you've only been together since this morning..."
        genevieve "But looking at you all now, you already seem like such cute couples."
        genevieve "But at first glance, this boy seems like my type on paper."
        genevieve "He's smart, funny, and just dreamy."
        genevieve "And although I don't want to break a promising couple up so early on..."
        genevieve "I'm here to make a choice and so..."
        "Everyone tenses."
        if s3e1p2_talk_to_new_girl:
            thought "Here she goes. About to pick [s3_current_partner]..."
        else:
            thought "She better not pick [s3_current_partner]."
        genevieve "The boy I'd like to couple up with is..."
        thought "Maybe she won't?"
        genevieve "[s3_current_partner]."

    # CHOICE
    menu:
        "Miki picked Bill!"
        "I called it" if s3e1p2_talk_to_new_girl == True:
            pass
        "At least she told me" if s3e1p2_talk_to_new_girl == False:
            pass
        "No, dammit!":
            pass
        "Well, this sucks":
            pass

    if s3_current_partner == "Harry":
        "Genevieve looks at you apologetically."
        genevieve "I'm so sorry, babe."
    "You hear sighs of relief and murmurs coming from the others."
    elladine "Oh no! Poor [s3_mc_name]..."
    seb "Wow, that's brutal."
    nicky "Yeah, that's rough, man."

    # CHOICE
    menu:
        "[s3_3rd_girl]'s taken my guy..."
        "It is what it is":
            if s3_current_partner == "Bill":
                "Miki smiles."
                miki "Thanks for understanding, [s3_mc_name]."
            elif s3_current_partner == "Camilo":
                "Iona smiles."
                iona "Thanks for understanding, [s3_mc_name]."
            elif s3_current_partner == "Harry":
                "Genevieve smiles."
                genevieve "Thanks for understanding, [s3_mc_name]."
        "How could you?":
            if s3_current_partner == "Bill":
                "Miki's face drops."
                miki "It was a really hard decision, babe. I didn't want to make it..."
            elif s3_current_partner == "Camilo":
                "Iona's face drops."
                iona "It was a really hard decision, babe. I didn't want to make it..."
            elif s3_current_partner == "Harry":
                "Genevieve's face drops."
                genevieve "It was a really hard decision, babe. I didn't want to make it..."
        "I'll be coming for him":
            if s3_current_partner == "Bill":
                miki "Good."
                miki "I'm looking forward to the competition."
            elif s3_current_partner == "Camilo":
                iona "Good."
                iona "I'm looking forward to the competition."
            elif s3_current_partner == "Harry":
                genevieve "Good."
                genevieve "I'm looking forward to the competition."
        "At least you told me " if s3e1p2_talk_to_new_girl == True:
            if s3_current_partner == "Bill":
                miki "I really didn't want it to be a surprise for you..."
            elif s3_current_partner == "Camilo":
                iona "I really didn't want it to be a surprise for you..."
            elif s3_current_partner == "Harry":
                genevieve "I really didn't want it to be a surprise for you..."

    if s3_current_partner == "Harry":
        "Harry puts a hand on your back."
    else:
        "[s3_current_partner] puts a hand on your back."

    if s3_current_partner == "Bill":
        bill "I can't believe this."
        bill "I was blown away when you picked me. It's like I'd won the jackpot."
        bill "And now we're not a couple, less than a day after that..."
    elif s3_current_partner == "Camilo":
        camilo "I can't believe this."
        camilo "I was blown away when you picked me. It's like I'd won the jackpot."
        camilo "And now we're not a couple, less than a day after that..."
    elif s3_current_partner == "Harry":
        harry "I can't believe this."
        harry "I was blown away when you picked me. It's like I'd won the jackpot."
        harry "And now we're not a couple, less than a day after that..."
    "He stands to walk over to [s3_3rd_girl]."

    # CHOICE
    menu:
        "Bill's getting up to leave..."
        "Squeeze his hand":
            if s3_current_partner == "Bill":
                "You reach out, grab his hand, and give it a gentle squeeze. He stops in his tracks and turns back to you."
                bill "Don't worry. I'll only be over there."
                s3_mc "But that's not here."
                bill "Yeah..."
                "He sighs, then continues over to [s3_3rd_girl]."
            elif s3_current_partner == "Camilo":
                "You reach out, grab his hand, and give it a gentle squeeze. He stops in his tracks and turns back to you."
                camilo "Don't worry. I'll only be over there."
                s3_mc "But that's not here."
                camilo "Yeah..."
                "He sighs, then continues over to [s3_3rd_girl]."
            elif s3_current_partner == "Harry":
                "You reach out, grab his hand, and give it a gentle squeeze. He stops in his tracks and turns back to you."
                harry "Don't worry. I'll only be over there."
                s3_mc "But that's not here."
                harry "Yeah..."
                "He sighs, then continues over to [s3_3rd_girl]."
        "Drag him back":
            if s3_current_partner == "Bill":
                "You reach out, wrap your fingers around his arm, and pull."
                bill "Agh!"
                "He lurches back, loses his balance and falls hard onto the seat."
                "Seb and Nicky let out a laugh. Elladine raises an eyebrow at you."
                bill "Ow, my bum!"
                bill "These cushions are weirdly firm."
                "He looks at you with a puzzled expression."
                s3_mc "Sorry…"
                bill "Don't worry. Look, I'm only going to be over there."
                s3_mc "But that's not here."
                "He gets back up and makes his way over to [s3_3rd_girl]."
            elif s3_current_partner == "Camilo":
                "You reach out, wrap your fingers around his arm, and pull."
                iona "Agh!"
                "He lurches back, loses his balance and falls hard onto the seat."
                "Seb and Nicky let out a laugh. Elladine raises an eyebrow at you."
                iona "Ow, my bum!"
                iona "These cushions are weirdly firm."
                "He looks at you with a puzzled expression."
                s3_mc "Sorry…"
                iona "Don't worry. Look, I'm only going to be over there."
                s3_mc "But that's not here."
                "He gets back up and makes his way over to [s3_3rd_girl]."
            elif s3_current_partner == "Harry":
                "You reach out, wrap your fingers around his arm, and pull."
                harry "Agh!"
                "He lurches back, loses his balance and falls hard onto the seat."
                "Seb and Nicky let out a laugh. Elladine raises an eyebrow at you."
                harry "Ow, my bum!"
                harry "These cushions are weirdly firm."
                "He looks at you with a puzzled expression."
                s3_mc "Sorry…"
                harry "Don't worry. Look, I'm only going to be over there."
                s3_mc "But that's not here."
                "He gets back up and makes his way over to [s3_3rd_girl]."
        "Wave goodbye":
            "You slowly wave at [s3_current_partner] as he makes his way over to [s3_3rd_girl]."
            "He turns, sees you, and does a small, reassuring wink."
            thought "There he goes…"
            "[s3_current_partner] nods at [s3_3rd_girl]."

    if s3_current_partner == "Bill":
        bill "Alright, girl?"
        miki "I'm good, you?"
    elif s3_current_partner == "Camilo":
        camilo "Hiya, you alright?"
        iona "I'm good, you?"
    elif s3_current_partner == "Harry":
        harry "Hey! How are you doing?"
        genevieve "I'm good, you?"

    "[s3_current_partner] shrugs. He and [s3_3rd_girl] share a clumsy hug."
    s3_mc "I got a text..."
    s3_mc "I swear, if this is me getting dumped already I'm gonna be livid."
    aj "That wouldn't happen already, right?"
    seb "It isn't unheard of."
    elladine "Read it out, hun."

    text "[s3_mc_name], [s3_3rd_girl] has taken your partner, leaving you single..."

    s3_mc "Ugh."

    text "...so get ready to mingle. #getthatgrafton #the singlelife"

    aj "What's that all mean?"
    s3_mc "I'm...safe?"
    elladine "Phew! Not gonna lie but that would have been proper cruel."

    # IF STATEMENT
    if s3_mc_attr["Bisexual"] == True:
        aj "Yay!"
        aj "Single and ready to mingle, eh?"
        aj "Guess we'll need to keep a close eye on you."
    else:
        aj "Ooh..."
        genevieve "Single and ready to mingle, eh?"
        genevieve "Guess we'll need to keep a close eye on you."

    "Nicky gets up and stretches."
    nicky "I don't know about you lot, but my bum's gone numb."
    "He makes his way over to [s3_3rd_girl]."

    # CHOICE
    menu:
        "Should I go and talk to [s3_3rd_girl]?"
        "Walk over to [s3_3rd_girl]":
            if s3_current_partner == "Bill":
                "You make your way over to [s3_3rd_girl] along with Nicky, Genevieve and Iona."
                genevieve "Hey, girl!"
                miki "Hi!"
                nicky "Thought we'd come over and chat properly."
                "Iona gives you a sympathetic look before turning to [s3_3rd_girl]."
                iona "I hope you're alright. That was a tough decision for anyone to make."
                genevieve "Yeah, I'm so glad it wasn't me doing it."
                "[s3_3rd_girl] goes to speak, but looks at you instead."
                miki "Sorry, all. Can I have a quick word with [s3_mc_name] first?"
            elif s3_current_partner == "Camilo":
                "You make your way over to [s3_3rd_girl] along with Nicky, Miki and Genevieve."
                miki "Hey, girl!"
                iona "Hi!"
                nicky "Thought we'd come over and chat properly."
                "Genevieve gives you a sympathetic look before turning to [s3_3rd_girl]."
                genevieve "I hope you're alright. That was a tough decision for anyone to make."
                miki "Yeah, I'm so glad it wasn't me doing it."
                "[s3_3rd_girl] goes to speak, but looks at you instead."
                iona "Sorry, all. Can I have a quick word with [s3_mc_name] first?"
            elif s3_current_partner == "Harry":
                "You make your way over to [s3_3rd_girl] along with Nicky, Miki and Iona."
                miki "Hey, girl!"
                genevieve "Hi!"
                nicky "Thought we'd come over and chat properly."
                "Iona gives you a sympathetic look before turning to [s3_3rd_girl]."
                iona "I hope you're alright. That was a tough decision for anyone to make."
                miki "Yeah, I'm so glad it wasn't me doing it."
                "[s3_3rd_girl] goes to speak, but looks at you instead."
                genevieve "Sorry, all. Can I have a quick word with [s3_mc_name] first?"
            nicky "Oh yeah, no problem."
            "Nicky winks at you as he ushers the others away… including [s3_current_partner]."
        "Stay where you are":
            "You stay back while everyone around you gets up and goes off in their own little groups."
            "The flames of the fire flicker and twirl. You soon find yourself lost in thought."
            # CHOICE
            menu:
                "I can't stop thinking about…"
                "How I'm single again":
                    thought "Like, I literally came here to stop being single!"
                "All the mingling I'm going to do":
                    thought "This is a blessing. It means I'll get to do as much grafting as I want."
                "Chinstrap penguins…":
                    thought "They're just so silly! It's like they're wearing helmets all the time."
            "Just then, a voice snaps you out of your thoughts."
            # IF STATEMENT
            if s3_current_partner == "Bill":
                miki "[s3_mc_name]?"
                s3_mc "Huh?"
            elif s3_current_partner == "Camilo":
                iona "[s3_mc_name]?"
                s3_mc "Huh?"
            elif s3_current_partner == "Harry":
                genevieve "[s3_mc_name]?"
                s3_mc "Huh?"
        "Walk away from the others":
            "You get up, leaving the rest of the Islanders to form their own little groups."
            "The night is surprisingly chilly. You rub your arms for some warmth."
            "The sound of laughter drifts over from the other Islanders."
            # IF STATEMENT
            if s3_current_partner == "Bill":
                miki "Cold?"
                "You turn and see Miki standing in front of you. A concerned look on her face."
                miki "Me too. And I thought Cambridge could get chilly!"
                miki "Sometimes the boat's little heater isn't enough, you know?"
                "She rubs her arm."
            elif s3_current_partner == "Camilo":
                iona "Cold?"
                "You turn and see Iona standing in front of you. A concerned look on her face."
                "She rubs her arm."
            elif s3_current_partner == "Harry":
                genevieve "Cold?"
                "You turn and see Genevieve standing in front of you. A concerned look on her face."
                genevieve "I nearly forgot to pack a cardigan for the colder evenings."
                "She rubs her arm."

    if s3_current_partner == "Bill":
        miki "Um, I'd like to clear the air with you."
        s3_mc "Sure...let's talk."
        miki "Thanks."
        miki "I want you to know that it wasn't anything personal. I mean, obviously, I've only just met you."
        if s3e1p2_talk_to_new_girl:
            miki "That's why I told you earlier who I was going to pick, so it wasn't a shock."
        else:
            miki "I wanted to tell you earlier, but we didn't get any time to chat."
            miki "I didn't want it to come as a shock."
        miki "At the end of the day, I had to pick someone."
        miki "But I actually think this puts you in a really strong position. You're now free to chat and flirt with whoever you want."
        miki "Even if that person is Bill. Like, all's fair. I won't make a fuss."
        miki "Early days and all that."
        "She pauses."
        miki "So...friends?"
    elif s3_current_partner == "Camilo":
        iona "Um, I'd like to clear the air with you."
        s3_mc "Sure...let's talk."
        iona "Thanks."
        iona "I want you to know that it wasn't anything personal. I mean, obviously, I've only just met you."
        if s3e1p2_talk_to_new_girl:
            iona "That's why I told you earlier who I was going to pick, so it wasn't a shock."
        else:
            iona "I wanted to tell you earlier, but we didn't get any time to chat."
            iona "I didn't want it to come as a shock."
        iona "At the end of the day, I had to pick someone."
        iona "But I actually think this puts you in a really strong position. You're now free to chat and flirt with whoever you want."
        iona "Even if that person is Camilo. Like, all's fair. I won't make a fuss."
        iona "Early days and all that."
        "She pauses."
        iona "So...friends?"
    elif s3_current_partner == "Harry":
        genevieve "Um, I'd like to clear the air with you."
        s3_mc "Sure...let's talk."
        genevieve "Thanks."
        genevieve "I want you to know that it wasn't anything personal. I mean, obviously, I've only just met you."
        if s3e1p2_talk_to_new_girl:
            genevieve "That's why I told you earlier who I was going to pick, so it wasn't a shock."
        else:
            genevieve "I wanted to tell you earlier, but we didn't get any time to chat."
            genevieve "I didn't want it to come as a shock."
        genevieve "At the end of the day, I had to pick someone."
        genevieve "But I actually think this puts you in a really strong position. You're now free to chat and flirt with whoever you want."
        genevieve "Even if that person is Harry. Like, all's fair. I won't make a fuss."
        genevieve "Early days and all that."
        "She pauses."
        genevieve "So... friends?"

    # CHOICE
    menu:
        "Should I forgive [s3_3rd_girl] for choosing [s3_current_partner]?"
        "Hey, it's fine. It was a tough call":
            "[s3_3rd_girl]'s shoulders relax with relief."
            if s3_current_partner == "Bill":
                miki "Thanks, babe! You have no idea how awkward I was feeling."
                miki "You're so understanding."
                "She squeezes your arm lightly."
                miki "Come on, then. We should get back to the others."
            elif s3_current_partner == "Camilo":
                iona "Thanks, babe! You have no idea how awkward I was feeling."
                iona "You're so understanding."
                "She squeezes your arm lightly."
                iona "Come on, then. We should get back to the others."
            elif s3_current_partner == "Harry":
                genevieve "Thanks, babe! You have no idea how awkward I was feeling."
                genevieve "You're so understanding."
                "She squeezes your arm lightly."
                genevieve "Come on, then. We should get back to the others."
            "You walk back together."
        "I'm sorry, but I need some time":
            "[s3_3rd_girl] gaze falls to the ground. She lets out a heavy sigh."
            if s3_current_partner == "Bill":
                miki "I understand…"
                miki "Look, I hope we can still be friends someday, you know?"
                s3_mc "Hmm."
                "She looks back at the others."
                miki "Alright, I guess I should get back over there."
            elif s3_current_partner == "Camilo":
                iona "I understand…"
                iona "Look, I hope we can still be friends someday, you know?"
                s3_mc "Hmm."
                "She looks back at the others."
                iona "Alright, I guess I should get back over there."
            elif s3_current_partner == "Harry":
                genevieve "I understand…"
                genevieve "Look, I hope we can still be friends someday, you know?"
                s3_mc "Hmm."
                "She looks back at the others."
                genevieve "Alright, I guess I should get back over there."
            "[s3_3rd_girl] walks back on her own."
        "Relax, girl! I'd known him for two minutes":
            if s3_current_partner == "Bill":
                miki "Hah!"
                "She tries to stop herself from laughing."
                miki "Ah, I'm sorry…"
                miki "I'm just relieved."
                miki "I really hate the idea of getting on the wrong side of someone in here."
                miki "Especially on the first day!"
                "A burst of laughter from the other group makes her turn her head."
                miki "Sounds like they're having fun. Come on, let's get back there."
            elif s3_current_partner == "Camilo":
                iona "Hah!"
                "She tries to stop herself from laughing."
                iona "Ah, I'm sorry…"
                iona "I'm just relieved."
                iona "I really hate the idea of getting on the wrong side of someone in here."
                iona "Especially on the first day!"
                "A burst of laughter from the other group makes her turn her head."
                iona "Sounds like they're having fun. Come on, let's get back there."
            elif s3_current_partner == "Harry":
                genevieve "Hah!"
                "She tries to stop herself from laughing."
                genevieve "Ah, I'm sorry…"
                genevieve "I'm just relieved."
                genevieve "I really hate the idea of getting on the wrong side of someone in here."
                genevieve "Especially on the first day!"
                "A burst of laughter from the other group makes her turn her head."
                genevieve "Sounds like they're having fun. Come on, let's get back there."
            "The two of you make your way to the others."

    "Seb, Nicky, Elladine and Genevieve are sat around the firepit chatting"
    thought "I could do with someone to talk to."

    # GAME POP-UP
    "Love Island isn't just about romance. It's also about the friendships you form along the way. One of these four Islanders is going to be a close friend for the rest of your time in the Villa."

    thought "People can get attached pretty quickly in this Villa. I should think about who I want to be friends with..."
    thought "I don't think I've ever met anyone as positive as Elladine."
    thought "I feel like she's the kind of person that always has a funny story to share or a comfortable shoulder to cry on."
    if s3_current_partner == "Harry":
        thought "Genevieve did just pick Harry, but she was in a tough position…"
        thought "And she actually seems kinda lovely… I feel like she's used to dealing with people and understands how to navigate tricky issues…"
    else:
        thought "I feel like Genevieve is used to dealing with people and understands how to navigate tricky issues..."
        thought "Plus, she just seems lovely."
    thought "I don't get romantic vibes off Seb and Nicky. I definitely see them more as friends than romantic partners."
    thought "Nicky already strikes me as a proper joker. He's got an 'older bro' vibe to him."
    thought "Seb's got this darker side to him. Like, he's got the most life experience here and will just say things how they are..."

    # CHOICE
    menu:
        "Who should I speak to?"
        "Elladine":
            $ s3_best_friend = "Elladine"
        "Genevieve":
            $ s3_best_friend = "Genevieve"
        "Nicky":
            $ s3_best_friend = "Nicky"
        "Seb":
            $ s3_best_friend = "Seb"


# "You make your way over to where [s3_best_friend] is sitting with the others."
# elladine "Hey, [s3_mc_name]!"
# if s3_current_partner = "Harry":
#     genevieve "Join us! We're staying close to the fire for warmth."
#     seb "Yeah, right? I thought it'd be baking."
#     seb "Didn't realise I'd need a fluffy onesie at night"

# s3_mc "Hey, [s3_best_friend]..."



# Choiceseb "Who do I want to scare?"
# -Harry 
# -Camilo
# -Bill 
# -AJ

# You dive under Bill's bed and wait for him to get within grabbing range.
# Bill, Camilo, and Harry enter the room.
# bill "...so yeah, sorry if I don't want dust powder with fake 'cream' in the middle, but no thanks."
# harry "But they're the best!"
# bill "I've literally just explained to you why that isn't the case."
# camilo "I still can't believe you dunk pink wafers in your tea, bruv."
# bill "They're a biscuit! Biscuits are meant to be dunked. That's like saying you shouldn't drink  beer with a curry."
# bill "It's just common sense, yeah?"
# camilo "But don't they just get soggy?"
# bill "Well yeah, that's why you have a dunking hierarchy, ranked from hardest to weakest."
# harry "I don't think I've ever thought about biscuits so much in my life."
# aj "And I don't think I ever want to again."
# elladine "It's been very..."
# elladine "...enlightening."
# nicky "That's a word. Not sure the one I'd for this conversation, but definitely a word."
# From your hiding spot, you see Bill making his way over to you.
# bill "Anyone seen MC?"
# genevieve "No?"
# bill "Weird. Maybe she's gone to sleep on the daybeds?"
# Genevieve lowers her voice into a harsh whisper.
# genevieve "Or maybe a ghost got her..."
# She wiggles her fingers dramatically.
# iona "Woah! Hey, guys, look at the moon."
# miki "It looks massive."
# genevieve "Come out onto the terrace with me. Let's get a proper look."
# You hear the others leave.
# bill "I'll be out there in a second!"
# Bill stops in front of you...

# Choiceseb "This is it! How should I scare him?"
# -Call out his name
# You start with a whisper...
# s3_mc "Bill..."
# bill "Huh?"
# s3_mc "Bill."
# bill "...Hello?"
# s3_mc "Bill!"
# The force from your sudden shout makes Bill jump.
# bill "What the hell? (you get 😱 with Bill)"
# You crawl out from under the bed, crackling wildly.
# bill "Nice one. (you get 😍 with Bill)"

# -Jump out at him

# -Grab his ankle

# bill "Maybe I'll get you back by hiding in your bed?"

# Choiceseb "Bill hiding in my bed..."
# -Sounds more like a dream come true

# -You in my bed would be terrifying

# -Is that an invitation?
# bill "It can be if you want... (you get 😏 with Bill)"
# bill "You realise I have to get you back for this, right?"
# s3_mc "I'd like to see you try..."

# Before he can say anything else, the rest of the Islanders reappear, laughing.
# iona "Genevieve told us what you were up to, MC."
# nicky "It sounds like it worked."
# miki "Just never spook me, yeah? I hate jump scares..."

# They start to get ready for bed.
# thought "That's enough excitement for one night. I'm going to go and get changed."

# thought "Right, first night in the Villa and I'm single. It's worth going all out tonight."
# thought "I want the others to see who they're dealing with..."
# MC outfit change to sleepwear
# thought "This outfit is beyond cute."

# You squeeze some toothpaste onto your brush and begin to clear your teeth.
# You hear the bathroom door open and close. You turn to see AJ standing there, towel in hand.
# aj "Oh, sorry! I should have knocked."
# s3_mc "Thawt's oclay, garl."
# She laughs.
# aj "What?"
# You try to speak again but a dribble of toothpaste makes it's way down your chin instead.
# You quickly wipe it away.
# s3_mc "Whurlps!"
# aj "Hah! Gross."
# aj "Don't mind me, hun. I'm just going to brush my teeth as well."
# She looks you up and down quickly.
# aj "I didn't think pyjamas could look so good. You're making me jealous. (you get 🤩 with AJ)"
# She picks up her brush and begins to vigorously clean her teeth.
# thought "I've never seen someone brush their teeth so hard and fast..."
# aj "Schwo, howsh shings?"
# s3_mc "Hmm?"
# She chuckles and leans in towards the sink.
# The two of you go to use it at the same time and gently bump into each other.
# AJ giggles.
# She gestures to the sink. You quickly rinse your mouth.
# s3_mc "Thanks."
# AJ does the same.
# aj "No problem."
# She grins at you as she wipes her mouth with her towel.
# aj "Ahh, minty fresh."
# aj "I asked how's things?"


# Choiceseb "Things are..."
# -Great!

# -All a bit much
# aj "Aw, sorry, babes."

# -What they are

# AJ slowly plays with the towel in her hands.
# aj "So, you got your eye on any of the guys here?"

# Choiceseb "Which guy do I have my eye on?"
# -Harry

# -Camilo

# -Bill
# aj "Hah! Really? (you get 😲 with AJ)"
# aj "Sorry, that was well rude."
# aj "It's just, he's got an opinion on everything!"
# aj "Though, he's kinda funny, I'll give you that."
# aj "It sucks that you don't get to spend your first night here with him."

# -Nobody so far...

# A knock on the door breaks you both out of your conversation.
# seb "Hey, you done yet?"
# seb "There's half a dozen people out here waiting to use the loo."
# seb "Some are in more desperate need than others!"
# s3_mc "Whoops."
# AJ chuckles again.
# aj "I guess we should go."

# "Don't fret, MC! So, you've lost Bill, but at least you've got a bed!"
# "I don't even have a sleeping bag! All the budget's gone on biscuits for the Islanders to argue over."
# "Not that they appreciate my sacrifice!"
# "Next time on Love Island..."
# "Seb says something appalling at breakfast..."
# seb "I really want some black pudding."
# "Eww!"
# "And MC gets grafting..."
# s3_mc "Let me ride you..."
# "And we've got a whole bunch of other surprises lined up for you."
# "It's a whole new series! I can't wait to see what's going to happen."


label s3e1p3_best_friend_chat:
    if s3_best_friend == "Elladine":
        elladine "Yeah?"
        s3_mc "Could I speak to you in private?"
        elladine "Of course, babes!"
        elladine "Roof terrace?"
        s3_mc "Sounds good!"
        "The two of you make your way upstairs."
    elif s3_best_friend == "Genevieve":
        genevieve "Yeah?"
        s3_mc "Could I speak to you in private?"
        genevieve "Of course, babes!"
        genevieve "Roof terrace?"
        s3_mc "Sounds good!"
        "The two of you make your way upstairs."
    elif s3_best_friend == "Nicky":
        nicky "Yeah?"
        s3_mc "Could I speak to you in private?"
        nicky "Of course!"
        nicky "Roof terrace?"
        s3_mc "Sounds good!"
        "The two of you make your way upstairs."
    elif s3_best_friend == "Seb":
        seb "Yeah?"
        s3_mc "Could I speak to you in private?"
        seb "Of course!"
        seb "Roof terrace?"
        s3_mc "Sounds good!"
        "The two of you make your way upstairs."

    # IF STATEMENT
    if s3_best_friend == "Genevieve" and s3_current_partner == "Harry":
        "After having Harry taken from her by Genevieve, [s3_mc_name]'s made the interesting decision to confide in her."
        "Could this be the start of a beautifully awkward friendship?"
    else:
        "After having [s3_current_partner] taken from her, [s3_mc_name] and [s3_best_friend] have come to the terrace to talk it over."
        "I get the feeling that this could be the start of a beautiful friendship..."
    "You and [s3_best_friend] make your way to the nearest sofa and take a seat that overlooks the rest of the Villa."
    "There's a splash, then AJ emerges from the pool. She runs around to the other side, then cannonballs in again."

    if s3_best_friend == "Elladine":
        elladine "I bet that girl's never been tired in her life..."
    elif s3_best_friend == "Genevieve":
        genevieve "I bet that girl's never been tired in her life..."
    elif s3_best_friend == "Nicky":
        nicky "I bet that girl's never been tired in her life..."
    elif s3_best_friend == "Seb":
        seb "I bet that girl's never been tired in her life..."

    # CHOICE
    menu:
        "AJ seems to be bursting with energy..."
        "I wish I was more like that":
            if s3_best_friend == "Elladine":
                elladine "Right?"
                elladine "I just don't get how some people can be so active. I'm useless without two coffees in the morning."
            elif s3_best_friend == "Genevieve":
                genevieve "Right?"
                genevieve "I just don't get how some people can be so active. I'm useless without two coffees in the morning."
            elif s3_best_friend == "Nicky":
                nicky "Right?"
                nicky "I just don't get how some people can be so active. I'm useless without two coffees in the morning."
            elif s3_best_friend == "Seb":
                seb "Right?"
                seb "I just don't get how some people can be so active. I'm useless without two coffees in the morning."
        "I get tired just watching her":
            if s3_best_friend == "Elladine":
                elladine "Right?"
                elladine "I just don't get how some people can be so active. I'm useless without two coffees in the morning."
            elif s3_best_friend == "Genevieve":
                genevieve "Right?"
                genevieve "I just don't get how some people can be so active. I'm useless without two coffees in the morning."
            elif s3_best_friend == "Nicky":
                nicky "Right?"
                nicky "I just don't get how some people can be so active. I'm useless without two coffees in the morning."
            elif s3_best_friend == "Seb":
                seb "Right?"
                seb "I just don't get how some people can be so active. I'm useless without two coffees in the morning."

        "Maybe she'll keep me on my toes...":
            if s3_best_friend == "Elladine":
                "Empty"
                # NEED TO FILL
            elif s3_best_friend == "Genevieve":
                genevieve "She seems like a dynamo. Maybe the two of you should work out together."
                genevieve "Exercise releases endorphins, which can help you feel happy."
                s3_mc "Wow, am I getting medical advice from Doctor Viv?"
                genevieve "My full title is actually Doctor Aliu, but I like Doctor Viv."
            elif s3_best_friend == "Nicky":
                "Empty"
                # NEED TO FILL
            elif s3_best_friend == "Seb":
                seb "She seems like a dynamo. Maybe the two of you should work out together."
                seb "Get the old heart rate going."
            
    if s3_best_friend == "Genevieve" and s3_current_partner == "Harry":
        genevieve "Thanks again for accepting my apology earlier."
        genevieve "I really didn't want there to be any bad feelings between us."
    "There's a moment of silence as the two of you watch the other Islanders roam around the Villa."

    if s3_best_friend == "Elladine":
        elladine "So, how are you doing?"
        elladine "Tonight must have been tough..."
    elif s3_best_friend == "Genevieve":
        genevieve "So, how are you doing?"
        genevieve "Tonight must have been tough..."
    elif s3_best_friend == "Nicky":
        nicky "So, how are you doing?"
        nicky "Tonight must have been tough..."
    elif s3_best_friend == "Seb":
        seb "So, how are you doing?"
        seb "Tonight must have been tough..."

# CHOICE
menu:
    "I'm doing..."
    "Pretty good, all things considered":
        s3_mc "I'm OK. Anyway, it's only the first day, still."
        if s3_best_friend == "Elladine":
            elladine "Exactly! You're thinking smart here."
        elif s3_best_friend == "Genevieve":
            genevieve "Exactly! You're thinking smart here."
        elif s3_best_friend == "Nicky":
            nicky "Exactly! You're thinking smart here."
        elif s3_best_friend == "Seb":
            seb "Exactly! You're thinking smart here."
    "Meh, my head's all over the place":
        if s3_best_friend == "Elladine":
            elladine "That's understandable. You've already been through a dumping and it's only the first day."
        elif s3_best_friend == "Genevieve":
            genevieve "That's understandable. You've already been through a dumping and it's only the first day."
        elif s3_best_friend == "Nicky":
            nicky "That's understandable. You've already been through a dumping and it's only the first day."
        elif s3_best_friend == "Seb":
            seb "That's understandable. You've already been through a dumping and it's only the first day."

    "Great! I'm single and ready to mingle!":
        s3_mc "…again."
        s3_mc "As everyone keeps saying."
        "Genevieve/Seb laughs."
#         G/S: "Good to see it hasn't dampened your spirit. (you get 😏 with Genevieve/Seb)"

# Genevieve smiles at you.
# Seb coughs and tucks his hair behind his ear
# genevieve "Want to know what I think?"
# S: So, um, I've been thinking about your situation…

# s3_mc "Go on."
# genevieve "The way I see it, you're actually in one of the best positions in the Villa."
# genevieve "You can graft on whoever you want to now, and no one can really have a problem with you for it."
# genevieve "You can get to know everyone before the next recoupling!"
# genevieve "I'd say that's better than pairing up with a stranger straight away."

# Choiceseb "Genevieve thinks that being single at the start is better..."
# -You make a good point

# -But what if I already like Bill?
# genevieve "Then go out and get him back!"
# G: Well, there's nothing wrong with a bit of healthy competition, is there? (if couple harry)

# genevieve "Tomorrow is when the real grafting starts. You've just gotta keep your eyes on the prize."

# -I'm going to graft so hard

# Genevieve looks out thoughtfully at the view.
# genevieve "It's well dark already, isn't it?"
# s3_mc "Yeah, it is actually."
# genevieve "I can't believe we're in here looking for love."
# genevieve "Such a weird, like, concept, isn't it?"
# genevieve "We're on an Island doing some kind of treasure hunting or something..."
# genevieve "And the prize is that you might fall in love."

# Choiceseb "Genevieve thinks we're on a treasure hunt for love!"
# -Yeah, and I've lost my treasure already
# genevieve "Girl, you've got nothing to worry about."
# genevieve "Miki has got nothing on you."
# genevieve "I'm sure you're still in with a chance to win him back!"

# -Don't forget about the prize money

# -But sex marks the spot

# Genevieve bites her thumbnail absentmindedly.
# genevieve "I'm like, such a night warrior and a worrier."
# s3_mc "A worrying night warrior."
# genevieve "Yeah, that should be my superhero name at work or something."
# s3_mc "What is it that you do again?"
# genevieve "Junior doctor."
# genevieve "I always get hyper sensitive when it gets dark."
# genevieve "Which means three things..."
# She counts them off on her fingers as she goes along.
# genevieve "One, I'm good at working night shifts because I am rarely able to sleep."
# genevieve "Two, when I'm not working, I'm freaking out because work is, like, such a good distraction."
# genevieve "I'm mostly working on site for festivals at the moment."

# Choiceseb "Working as a doctor at a festival sounds..."
# -Really hard work
# genevieve "Yeah, it can be."

# -Like my absolute dream job

# -Rubbish! I thought you didn't like the dark?

# genevieve "Being a model must have its moments, though. (depends on your job)"
# genevieve "Every job has its bad habits."
# genevieve "I love that I'm surrounded by people."
# genevieve "It's literally constant when you're working as a doctor at a festival."
# genevieve "Can't stand how quiet and dark hospitals can get."
# genevieve "I bet this place will be a bit spooky, like, late at night."
# genevieve "It'd be easier if there were more people."
# s3_mc "What was the third thing?"
# Genevieve looks puzzled.
# genevieve "You know what?"
# genevieve "For the life of me I can't remember."
# genevieve "It's because it's getting late."
# genevieve "I'm just getting restless."

# Choiceseb "Genevieve struggles settling down at night."
# -Don't worry, I'll look out for you!
# genevieve "Awh, really?"
# genevieve "Means a lot, I'm not going to lie. (you get 😍 with Genevieve)"

# -I'll be out like a log soon

# -I can never get to sleep either

# The sound of the other Islanders draws your attention away from Genevieve.
# bill "Right, I don't know about the rest of you, but I'm cream-crackered."
# miki "You're a cream cracker?"
# camilo "Hah! He is now. That's brilliant."
# bill "What? No. I'm knackered."
# miki "Oh!"
# miki "You mumble too much."
# iona "Who even likes cream crackers?"
# camilo "They're gross. Chocolate bourbons all the way, you get me?"
# bill "Wait, a cream cracker isn't a biscuit."
# camilo "Isn't it one of those square ones with custard cream in the middle?"
# bill "That's a custard cream, mate, and they're way better than bourbons."
# The door to the Villa closes.
# genevieve "Sounds like everyone's going to bed."
# s3_mc "Guess I'll be sleeping alone."
# Genevieve rubs her chin.
# genevieve "You know what?"
# genevieve "I think you should find a way to show that you're totally not fazed by this."
# genevieve "Some way to show the Villa that you're still here to have a good time, just like everyone else."
# She thinks about it for a moment.
# genevieve "What about a prank?"
# s3_mc "Do you have anything in mind?"
# genevieve "Well, if we want to do it before bed, it's got to be something simple and classic."
# genevieve "What about if you hide somewhere and jump out at someone?"
# genevieve "I can keep them distracted while you get ready. What do you say?"
# thought "Do I want to make one of the other Islanders jump? It could be a cute start to my single gal mischief..."

# Choiceseb "It might be a good chance to get some alone time with someone, too..."
# -That sounds hilarious! Let's do it (gem choice)

# -As fun as that sounds, I don't think so
# genevieve "That's fair. It's been a big day already. Another time, maybe."
# genevieve "Although, are you sure? Last chance..."
# Choiceseb "I bet it'd be really fun to make someone jump..."
# -Actually, let's do it (gem choice)
# -Nah, not right now

# Gem choice:
# genevieve "Yes! This'll be so fun. (you get 😍 with Genevieve)"


# You both stand up.
# genevieve "Hey, before we head back in, I just want to say that I'm really glad we had this chat."
# genevieve "If you ever need to talk again, just come and see me, yeah?"
# genevieve "Come on, then. Let's go."
# The two of you head inside.

# Continuation of gem choice:
# You and Genevieve head into the bedroom. You can hear the others approaching.
# genevieve "Alright, go time! You hide. I'll go and keep them busy."
# Genevieve dashes out of the other door. You hear her talking to the others.


#########################################################################
## Episode 2, Part 1
#########################################################################

#########################################################################
## Episode 2, Part 2
#########################################################################

#########################################################################
## Episode 2, Part 3
#########################################################################

#########################################################################
## Episode 3, Part 1
#########################################################################

#########################################################################
## Episode 3, Part 2
#########################################################################

#########################################################################
## Episode 3, Part 3
#########################################################################