#########################################################################
## Episode 1, Part 1
#########################################################################
label s3e1p1:
    "Finding love can be tough..."
    "Daily life is nothing but work, sleep, and repeat..."
    "How are you supposed to have time to search for that special someone?"
    "It's time to get off social media, and find love the old-fashioned way..."
    "On a reality TV show!"
    "You've been invited to a place where everything is different..."
    "A place where all you have to do all day is meet beautiful people, couple up, and fall in love..."
    "A place called Love Island."
    "We've taken a gorgeous Villa in a hot country and filled it with sexy singles."
    "To stay in the Villa, they'll have to get together, and stay together."
    "And if they do find love, one lucky couple will also pocket fifty thousand pounds,"
    "But it won't be easy. We're going to throw in twists, turns, and challenges to see if their love can survive."
    "Who will find eternal bliss, and who will find themselves on a plane home?"
    "Let there be love."
    # MC Customizer Here

    "Your heel click on the driveway as you stride up to the Villa."

    "It's gorgeous!"
    "I can't believe this is going to be my home for the next two weeks!"
    "Unless I go home early."
    "I wonder where everybody is?"

    "A girl peeks her head out of the entrance."
    "She yells in excitement when she sees you."

    elladine "Hey! You made it!"
    elladine "It's so nice to meet you! I'm Elladine."

    # solo portrait shot of elladine
    "Elladine\n
    -25, from Cardiff\n
    -Glassblower\n
    -Heard every 'blowing' joke a hundred times already"

    s03_mc "I'm [s03_mc_name]"

    # CHOICE
    menu:
        "What should I say to Elladine?"
        "It's nice to meet you too":
            $ s3e1p1_warning_here_to_win = False
            $ s3_amount_npcs_like_mc["Elladine"] += 5
            $ s3_mc_attr['Sweet'] += 1
            s03_mc "I think we're the first ones here!"
            elladine "Amazing. This is one of those moments you remember forever, isn't it?"
            s03_mc "I think so!"
            elladine "I know we will."

        "Wow, I love your outfit":
            $ s3e1p1_warning_here_to_win = False
            $ s3_amount_npcs_like_mc["Elladine"] += 5
            $ s3_mc_attr['Sweet'] += 1
            s03_mc "It's stunning!"
            elladine "Babes, I was about to say the same to you!"
            elladine "Seriously. You've already set the bar super high."
            elladine "The boys are going to freak when they see us."

        "Warning, I'm here to win":
            $ s3e1p1_warning_here_to_win = True
            $ s3_amount_npcs_like_mc["Elladine"] -= 5
            $ s3_mc_attr['Bold'] += 1
            s03_mc "Before we go getting too friendly, you need to know one thing about me."
            s03_mc "I'm here to find love, and I don't care how many toes I have to tread on to get it."
            s03_mc "So if you're tempted to cross me at some point while we're here..."
            s03_mc "Don't."
            s03_mc "Understood?"
            elladine "Um, sure. Understood."

    elladine "I've been feeling well nervous ever since I got here."
    elladine "I mean it's exciting, but it's also a lot of pressure, isn't it?"

    # CHOICE
    menu:
        "How am I feeling?"
        "So nervous":
            $ s3_mc_attr['Sweet'] += 1
            $ s3e1p1_feeling_hungry = False
            s03_mc "I've never done anything like this before. It's a bit scary."
            elladine "At least we're all in the same boat!"

        "Just excited":
            $ s3_mc_attr['Bold'] += 1
            $ s3e1p1_feeling_hungry = False
            s03_mc "I'm really excited to meet everyone!"

        "Kinda hungry":
            $ s3_mc_attr['Funny'] += 1
            $ s3e1p1_feeling_hungry = True
            elladine "You mean, like...hungry for love, or..?"
            s03_mc "Nope. Just hungry."
            elladine "Sounds like you need a snack."
            elladine "I hope there are some snacks lined up for us outside!"
            s03_mc "Why would there be snacks outside?"
            elladine "I mean like hot guys when you see someone hot and you say 'he's a snack'."
            s03_mc "That's not what I meant, though. I'm just hungry."
            s03_mc "I wish I had a banana or something."
            "Elladine looks like she's about to make another joke, but then decides against it."

    s03_mc "Are there any other girls here yet?"
    elladine "Only one. We've been waiting in the bedroom."
    elladine "Come on. I'll introduce you."

    "Elladine leads you into the bedroom, where another girl is waiting."
    "Her jaw drops when you walk in."

    aj "Are you the new arrival?"
    aj "Man, I knew everyone here was gonna be gorgeous, but I wasn't prepared..."
    elladine "Stop staring and introduce yourself!"
    aj "Sorry, sorry!"
    aj "My name's AJ. It's nice to meet you."

    # solo portrait shot of aj
    "AJ\n
    -21, from Bath\n
    -Professional hockey player\n
    -Knows how to handle a stick"

    s03_mc "I'm [s03_mc_name]"
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
            s03_mc "Trust me, we're gonna have a great time."
            s03_mc "You're my girls now, and I don't let my girls turn on each other."
            aj "Yes! I'm so glad you said that."

        "But there's no fun without drama":
            $ s3_mc_attr['Bold'] += 1
            s03_mc "It's so exciting when someone does something totally shocking, and you just know the fallout is gonna be huge."
            s03_mc "I can't wait to stir up some trouble around here."
            aj "Fair play! I guess we just have different priorities."
            aj "Friendship is really important to me."

        "I don't care, as long as I get what I want":
            $ s3_amount_npcs_like_mc["AJ"] -= 2
            $ s3_mc_attr['Bold'] += 1
            s03_mc "I don't set out to create drama. But I will if I have to."
            s03_mc "At the end of the day, it's not called Friend Island."
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
    s03_mc "What was that?"
    elladine "It sounded like a text..."
    "AJ checks her phone and gasps."
    aj "Oh, it's me!"
    
    $ renpy.show_screen("s3e1p1_text_message", layer='top')

    aj "I've got a text!"
    $ renpy.hide_screen("s3e1p1_text_message")
    # Text Message
    # use screen s3e1p1_text_message
    

    aj "What? But the other girls still haven't arrived yet!"
    elladine " I guess they'll be coming in later?"
    aj "I'd better go, then."
    aj "I'll see you out there, guys."
    elladine "Good luck!"

    "AJ races out of the bedroom. Her heels clack all the way to the lawn."

    elladine "She's got a lot of energy, hasn't she?"
    elladine "I guess it's hard not to be excited when you know you're picking first."
    s03_mc "I wonder what the boys will be like?"
    elladine "I want a guy who's been around the block a bit, you know?"
    elladine "Someone who knows what he's about and takes it seriously."
    elladine "What about you? What's your type?"

    # CHOICE
    menu:
        "My type is..."
        "Funny and cute":
            $ s3_li_like_mc['Harry'] += 1
            $ s3_li_like_mc['Bill'] += 1
            s03_mc "I just want a boy to make me smile."
            elladine "Aw, I hope you find him, babes."

        "Smart and mature":
            $ s3_li_like_mc['Camilo'] += 1
            s03_mc "I agree with you. I need a guy with a good head on his shoulders."
            elladine "Aw, I hope you find him, babes."

        "Whatever, as long as they're hot":
            s03_mc "Personality will never be as important as looks for me."
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
            s03_mc "Don't get me wrong, I love having sex...but not on TV!"
            s03_mc "I don't want all my family and friends to see me!"
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
    elladine "Good luck, [s03_mc_name]. I'll see you down there."

    "She hurries towards the lawn, leaving you alone."
    "There's still only three girls here!"
    "I wonder when the others will be arriving?"
    "You sit down on one of the beds. It's soft and springy."


    # CHOICE
    menu:
        "These beds are really comfy..."
        "Perfect for snuggling":
            $ s3_mc_attr['Sweet'] += 1
            "I can't wait till find someone to cuddle up to."
        
        "Perfect for doing bits":
            $ s3_mc_attr['Bold'] += 1
            "I'm gonna have so much fun, the whole Villa will shake."
        
        "Maybe I'll take a nap...":
            $ s3_mc_attr['Funny'] += 1
            $ s3e1p1_took_a_nap = True
            "Just a little one couldn't hurt..."
            "You lay your head on the pillow and close your eyes."
            "Maybe my Prince Charming will come and wake me with a kiss."
            "You drift off for a few minutes, but then..."

    "Your phone beeps."
    "Wait, is it my turn already?"

    # Text Message
    "[s03_mc_name], come down to the lawn and couple up! The boys are waiting..."

    "Alright, let's do this!"
    "You step out into the brilliant sunshine."
    "Waiting on the lawn are three boys, standing in a line."
    "Elladine and AJ are off to the side, already paired up with their boys."
    "Elladine shoots you an encouraging smile, and AJ gives you a thumbs up."

    "Those two have already picked their boys..."
    "Which leaves these three for me to choose from."
    "I wonder which one I should pick?"

    "The first boy steps forward with a cheeky smile."

    # Meeting Bill
    bill "Alright, beautiful? I'm Bill."

    # solo portrait shot of bill
    "Bill\n
    -24, from Surrey\n
    -Roofer\n
    -Strong opinions about sandwiches"

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

    "You look down the line to the next boy."
    camilo "Hola chica. Welcome to the Villa. Amazing, isn't it?"
    s03_mc " Is it?"
    camilo "Well, it is now you're here."

    # solo portrait shot of camilo
    "Camilo\n
    -23, from Romford\n
    -Runs the family shop\n
    -A blackbelt in grafting (and Brazilian jiu-jitsu)"

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

    "The third and final boy in the line seems nervous."
    "You raise your eyebrows at him and he smiles, trying to puff out his chest a bit."
    harry "Hey, I'm Harry."

    # solo portrait shot of harry
    "Harry\n
    -21, from York\n
    -Business student\n
    -Usually wears a tie with his swimsuit"

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
            s03_mc "The boy I want to couple up with is... Bill!"
            "You stride over to Bill."
            "He grins like he can't hardly believe his luck."
            bill "Nice one."

        "Camilo":
            $ s3_coupled_up_with.append("Camilo")
            $ s3_li_like_mc['Camilo'] += 5
            s03_mc "The boy I want to couple up with is... Camilo!"
            "You stride over to Camilo."
            "He grins like he can't hardly believe his luck."
            camilo "Nice one."

        "Harry":
            $ s3_coupled_up_with.append("Harry")
            $ s3_li_like_mc['Harry'] += 5
            s03_mc "The boy I want to couple up with is... Harry!"
            "You stride over to Harry."
            "He grins like he can't hardly believe his luck."
            harry "Nice one."
    $ s3_current_partner = s3_coupled_up_with[-1]
    menu:
        "Me and [s3_current_partner] are officially coupled up..."
        "Hug him":
            $ s3_li_like_mc[s3_coupled_up_with[-1]] += 1
            "As you reach him, you throw your arms around his shoulders."
            "He hugs you back firmly. His hands are warm on the small of your back."

        "Kiss his cheek":
            $ s3_li_like_mc[s3_coupled_up_with[-1]] += 1
            "As you reach him, you plant a kiss on his cheek, being careful not to smudge your lipstick."
        
        "Hands off for now":
            "You stand politely at his side, just close enough for your elbows to brush."

    # IF STATEMENT
    if s3_coupled_up_with[-1] == "Bill":
        bill "I'm so glad you picked me."
        s03_mc " Did I make the right decision?"
        bill "Definitely. But I would say that, wouldn't I?"
    elif s3_coupled_up_with[-1] == "Camilo":
        camilo "I'm so glad you picked me."
        s03_mc " Did I make the right decision?"
        camilo "Definitely. But I would say that, wouldn't I?"
    else:
        harry "I'm so glad you picked me."
        s03_mc "Did I make the right decision?"
        harry "Definitely. But I would say that, wouldn't I?"

    "The two of you go to stand next to the other couples."
    elladine "Hey girl! Congratulations!"
    elladine "You really  bagged yourself a hottie there."
    elladine "Um, no offence, Nicky."
    nicky "None taken."
    nicky "Hi, by the way."
    nicky "I'm Nicky. I'm the lucky guy who's coupled up with Elladine."

    # solo portrait shot of nicky
    "Nicky\n
    -24, from Newcastle\n
    -Music tutor\n
    -Oldest sibling energy"

    elladine "As soon as I found out he was a musician, I was hooked."
    elladine "I've already got a really good feeling about this one."
    aj "Er, yeah. Me too."
    "AJ doesn't sound so convinced about her guy..."
    seb "Alright? My name's Seb. I'm coupled up with AJ."

    # solo portrait shot of seb
    "Seb\n
    -28, from Liverpool\n
    -Runs a music shop\n
    -Owns 52 t-shirts and 1 shirt"

    aj "I coupled up with a musician, too!"
    seb "Well, no. I'm a shopkeeper."
    aj "But you must know about instruments to sell them, right?"
    seb "It's not that kind of music shop. I sell records."
    seb "You know, CDs and vinyl and stuff. There's a coffee shop, too."
    aj "Oh! With you now, sorry."

    "You can't date Nicky or Seb in this season of Love Island The Game, but that doesn't mean you can't be friends! And don't worry - all the other boys, and some of the girls, are options."

    aj "This is so nice, you guys! We're already learning so much about each other!"
    nicky "Whoa there."
    nicky "We're still waiting on two more new girls, right?"
    elladine " Yeah. I wonder what they'll be like?"

    # CHOICE
    menu:
        "The last two girls..."
        "I can't wait to meet them":
            $ s3_mc_attr['Sweet'] += 1
            s03_mc "We're not a complete Villa crew until everyone's here."
            aj "Right! I'm so excited for them to get here!"
            nicky "You're not the only ones."
            "Nicky looks over at the two remaining single boys."

        "They better stay away from [s3_current_partner]":
            $ s3_mc_attr['Bold'] += 1
            $ s3_li_like_mc[s3_current_partner] += 1
            nicky "Wow! So committed already, huh?"
            # IF STATEMENT
            if s3_coupled_up_with[-1] == "Bill":
                bill "I kinda like it."
                bill "It's nice to know [s03_mc_name] is feeling it so strongly."
                bill "I mean, if another boy came in right now and tried to couple up with her, I'd have a thing or two to say about it, as well."
            elif s3_coupled_up_with[-1] == "Camilo":
                camilo "I kinda like it."
                camilo "It's nice to know [s03_mc_name] is feeling it so strongly."
                camilo "I mean, if another boy came in right now and tried to couple up with her, I'd have a thing or two to say about it, as well."
            elif s3_coupled_up_with[-1] == "Harry":
                harry "I kinda like it."
                harry "It's nice to know [s03_mc_name] is feeling it so strongly."
                harry "I mean, if another boy came in right now and tried to couple up with her, I'd have a thing or two to say about it, as well."

            "[s3_coupled_up_with] looks over at the two remaining single boys."

        "Maybe they got lost on the way here":
            $ s3_mc_attr['Funny'] += 1
            s03_mc "This place isn't exactly well signposted."
            nicky "Bad news for the leftover boys if you're right."

    # IF STATEMENT
    if s3_coupled_up_with[-1] == "Bill":
        bill "I wonder if they'd be open to coupling up with each other."
    elif s3_coupled_up_with[-1] == "Camilo":
        camilo "I wonder if they'd be open to coupling up with each other."
    elif s3_coupled_up_with[-1] == "Harry":
        harry "I wonder if they'd be open to coupling up with each other."

    "[s3_coupled_up_with[-1]] looks over at the two remaining single boys."

    # IF STATEMENT
    if s3_coupled_up_with[-1] == "Bill":
        "Camilo's smile is still dazzling, but it looks a little more nervous now."
        "Harry stands up straight, trying to look confident."
    elif s3_coupled_up_with[-1] == "Camilo":
        "Bill is masking his disappointment by concentrating on the grass between his toes."
        "Harry stands up straight, trying to look confident."
    elif s3_coupled_up_with[-1] == "Harry":
        "Bill is masking his disappointment by concentrating on the grass between his toes."
        "Camilo's smile is still dazzling, but it looks a little more nervous now."

    aj "I feel bad for them. Nobody wants to get picked last."
    elladine "Yeah, and it's pretty obvious they both wanted to get picked by MC..."
    aj "Well, maybe their perfect soulmates are about to walk out of that door any second."
    seb "Let's not kid ourselves. That kind of thing never happens in the real world."
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
            s03_mc "I can't wait for whatever's on the horizon!"
            nicky "That's the spirit."
        
        "I don't believe in magic":
            $ s3_amount_npcs_like_mc['Seb'] += 2
            s03_mc "If we're gonna have fun in the Villa, it won't be from magic."
            s03_mc "It'll be from hard grafting."
            seb "You've got that right."
        
        "My dreams are too weird":
            s03_mc "If they manage to make my dreams come true, I'll be impressed."
            s03_mc "Could they even fit a T-Rex in here?"

    "Everyone falls silent as a new girl emerges from the Villa."

    # IF STATEMENT (which women show up in villa first)
    if s3_coupled_up_with[-1] == "Harry":
        $ s3_amount_npcs_like_mc["Miki"] = 15
        call s3e1p1_meet_miki
        $ s3_amount_npcs_like_mc["Iona"] = 15
        call s3e1p1_meet_iona
    elif s3_coupled_up_with[-1] == "Bill":
        $ s3_amount_npcs_like_mc["Iona"] = 15
        call s3e1p1_meet_iona
        $ s3_amount_npcs_like_mc["Genevieve"] = 15
        call s3e1p1_meet_genevieve
    elif s3_coupled_up_with[-1] == "Camilo":
        $ s3_amount_npcs_like_mc["Miki"] = 15
        call s3e1p1_meet_miki
        $ s3_amount_npcs_like_mc["Genevieve"] = 15
        call s3e1p1_meet_genevieve

    # CHOICE
    menu:
        "They've made an impression on each other already..."
        "It's really cute":
            $ s3_mc_attr['Sweet'] += 1
            "I hope me and [s3_coupled_up_with[-1]] get on as well as they do!"
        
        "It's probably not real":
            $ s3_mc_attr['Bold'] += 1
            "It's not like they really know each other..."
            "They're probably just showing off."
        
        "I'd be the filling in that sandwich":
            $ s3_mc_attr['Funny'] += 1
            "They make such a hot couple!"

    elladine " I think that's everyone."
    bill "Five great ladies, five great gents, five great couples. Makes sense to me."
    aj " Don't you think it's a bit early to say whether our couples are great or not?"

    # IF STATEMENT
    if s3_coupled_up_with[-1] == "Bill":
        bill "I dunno. I've already got a pretty great feeling about this one."
        iona "Well, it's not a competition."
    elif s3_coupled_up_with[-1] == "Camilo":
        camilo "I dunno. I've already got a pretty great feeling about this one."
        miki "Well, it's not a competition."
    elif s3_coupled_up_with[-1] = "Harry":
        harry "I dunno. I've already got a pretty great feeling about this one."
        miki "Well, it's not a competition."

    nicky "It sort of is, though. Only the strongest couple can win the fifty grand."

    # CHOICE
    menu:
        "Based on first impressions, I think the strongest couple here will be..."
        "Me and [s3_coupled_up_with[-1]]":
            # IF STATEMENT
            if s3_coupled_up_with == "Bill":
                $ s3_amount_npcs_like_mc['Bill'] += 1
                bill "Not to bang my own drum or anything, but hard agree."
            elif s3_coupled_up_with[-1] == "Camilo":
                $ s3_amount_npcs_like_mc['Camilo'] += 1
                camilo "Not to bang my own drum or anything, but hard agree."
            elif s3_coupled_up_with[-1] = "Harry":
                $ s3_amount_npcs_like_mc['Harry'] += 1
                harry "Not to bang my own drum or anything, but hard agree."

            elladine " I can't lie, you two do look super cute together."

        "Miki and Bill" if 'Miki' in s3_amount_npcs_like_mc:
            $ s3e1p1_strongest_couple = "Miki and Bill"

        "Iona and Camilo" if 'Iona' in s3_amount_npcs_like_mc:
            $ s3e1p1_strongest_couple = "Iona and Camilo"

        "Genevieve and Harry" if 'Genevieve' in s3_amount_npcs_like_mc:
            $ s3e1p1_strongest_couple = "Genevieve and Harry"

        "Elladine and Nicky":
            $ s3_amount_npcs_like_mc['Elladine'] += 1
            $ s3_amount_npcs_like_mc['Nicky'] += 1
            elladine "Aw, babes."
        
        "AJ and Seb":
            $ s3_amount_npcs_like_mc['AJ'] += 1
            $ s3_amount_npcs_like_mc['Seb'] += 1
            aj "Wow, really?"
            seb "That's, um... sweet of you to say."

    # IF STATEMENT
    if s3e1p1_strongest_couple == "Miki and Bill" or s3e1p1_strongest_couple == "Iona and Camilo" or s3e1p1_strongest_couple == "Genevieve and Harry":
        if s3_coupled_up_with[-1] == "Bill":
            $ s3_li_like_mc['Bill'] -= 1
            bill "Stronger than you and me?"
        elif s3_coupled_up_with[-1] == "Camilo":
            $ s3_li_like_mc['Camilo'] -= 1
            camilo "Stronger than you and me?"
        elif s3_coupled_up_with[-1] == "Harry":
            $ s3_li_like_mc['Harry'] -= 1
            harry "Stronger than you and me?"

        s03_mc "I'm just being honest."

    # IF STATEMENT
    if s3_coupled_up_with[-1] == "Bill":
        iona "All I meant was, it might be a competition, but it doesn't really matter who wins."
        iona "We're all just here to find love, right?"
    elif s3_coupled_up_with[-1] == "Camilo" or s3_coupled_up_with[-1] == "Harry":
        miki "All I meant was, it might be a competition, but it doesn't really matter who wins."
        miki "We're all just here to find love, right?"


    # CHOICE
    menu:
        "I'm here..."
        "To win the game":
            $ s3_mc_attr['Bold'] += 1
            s03_mc "Don't get me wrong, we all want to find someone..."
            s03_mc "But that doesn't change the fact that this is a competition."
            s03_mc "There will be a winner."
            s03_mc "And that winner will be me."
            # IF STATEMENT
            if s3_coupled_up_with[-1] == "Bill":
                bill "Wow. Love that confidence."
            elif s3_coupled_up_with[-1] == "Camilo":
                camilo "Wow. Love that confidence."
            elif s3_coupled_up_with[-1] == "Harry":
                harry "Wow. Love that confidence."

        "To fall in love":
            $ s3_mc_attr['Sweet'] += 1
            s03_mc "She's right. At the end of the day, all that matters is finding the right person for you."
            s03_mc "That's the only prize worth winning, really."
            # IF STATEMENT
            if s3_coupled_up_with[-1] == "Bill":
                $ s3_amount_npcs_like_mc['Iona'] += 1
                iona "Wow, yes. MC just said it better than I ever could."
            elif s3_coupled_up_with[-1] == "Camilo" or s3_coupled_up_with[-1] == "Harry":
                $ s3_amount_npcs_like_mc['Miki'] += 1
                miki "Wow, yes. MC just said it better than I ever could."

        "To have fun":
            $ s3_mc_attr['Funny'] += 1
            $ s3_amount_npcs_like_mc['AJ'] += 1
            s03_mc "This is the holiday of a lifetime."
            s03_mc "Love is great and winning is fine, but why put so much pressure on it?"
            s03_mc "If all I get from this is a few cool new friends, I'll count myself a winner."
            aj "Wow, yes. MC just said it better than I ever could."

    # IF STATEMENT
    if s3_coupled_up_with[-1] == "Harry":
        iona "Oh my days, you guys!"
        iona "I've got a text!"
    elif s3_coupled_up_with[-1] == "Camilo" or s3_coupled_up_with[-1] == "Bill":
        genevieve "Oh my days, you guys!"
        genevieve "I've got a text!"

    # Text Message
    "Islanders, it's time to get to know each other a little better. Please make your way to the challenge platform and get ready to unpack some secrets about your fellow Islanders! #excessbaggage #gettingtoknowyou"

    seb "We've only just got here and we're already being challenged?"
    seb "I was hoping we could get a nap first."

    # IF STATEMENT
    if s3e1p1_took_a_nap:
        s01_mc "I had a little nap just before I came out!"
        seb "Oh mate, I wish I'd thought of that. Such a good move."
        seb "A little nap would be just the ticket."
    elif s3e1p1_feeling_hungry:
        seb "I'm a little peckish too."
        s03_mc "Me too! I was saying to Elladine, I'd love some kind of snack."
        if s3_coupled_up_with[-1] == "Bill":
            bill "Maybe I'm the kind of snack you're after."
        elif s3_coupled_up_with[-1] == "Camilo":
            camilo "Maybe I'm the kind of snack you're after."
        elif s3_coupled_up_with[-1] == "Harry":
            harry "Maybe I'm the kind of snack you're after."
        s03_mc "That's not the kind of snack I mean."

    nicky "I hate to sound like a stuck record, but it's Love Island."
    nicky "You have seen this show before, right? You didn't just get off at the wrong bus stop and end up here by mistake?"
    nicky "Because if that's what happened, the sooner you admit it, the less awkward it's going to be."
    elladine "Aw, stop teasing him. He just needs a bit of time to get used to it, that's all."
    camilo "The challenges are just a bit of fun! It'll help us all get closer as a group."
    bill "More importantly, we'll find out everyone's saucy secrets."
    camilo "Well, that too, I guess..."
    bill "Don't get me wrong. I've got nothing to hide."
    bill "But I'm excited to find out what the rest of you are holding back."
    harry "That's true, but we're not just here to mess around and relax, or dig up gossip on each other."
    aj "We're not?"
    harry "No! We're here on an important mission! To find someone we love. It's serious business."
    harry "The challenge will focus our minds and get us ready for the road ahead."


    # CHOICE
    menu:
        "Doing the challenge is mostly about..."
        "Getting closer as a group":
            $ s3_mc_attr['Sweet'] += 1
            $ s3_li_like_mc["Camilo"] += 1
            s03_mc "Camilo's right. This challenge sounds like a great way to get to know each other."
            s03_mc "This is what it's all about! I bet it's going to be a right laugh."
        
        "Uncovering everyone's secrets":
            $ s3_mc_attr['Bold'] += 1
            $ s3_li_like_mc["Bill"] += 1
            s03_mc "Bill's right. This is a great chance to expose all our best and worst stories."
            s03_mc "I bet we've all got some really juicy ones, too."
        
        "Bringing out my competitive side":
            $ s3_mc_attr['Bold'] += 1
            $ s3_li_like_mc["Harry"] += 1
            s03_mc "Harry's right. We've all got to be on the ball if we want to make the most of our time here."
            s03_mc "This challenge sounds like a great way to get into the right mindset."


    elladine "Well, there's only one way to find out."

    # IF STATEMENT
    if s3_coupled_up_with[-1] == "Harry":
        iona "Let's go."
    elif s3_coupled_up_with[-1] == "Camilo" or s3_coupled_up_with[-1] == "Bill":
        genevieve "Let's go."

    if s3_coupled_up_with[-1] == "Bill":
        iona "Woo! I can't wait!"
    elif s3_coupled_up_with[-1] == "Camilo" or s3_coupled_up_with[-1] == "Harry":
        miki "Woo! I can't wait!"

    "Chattering and laughing, the Islanders head towards the challenge platform."
    "Before you can follow, [s3_current_partner] quietly takes you to one side."

    # IF STATEMENT
    if s3_coupled_up_with[-1] == "Bill":
        bill "Hey, MC. Sorry to hang back like this."
        bill "I just wanted to have a quick chat with you in private before the challenge, if that's OK."
    elif s3_coupled_up_with[-1] == "Camilo":
        camilo "Hey, MC. Sorry to hang back like this."
        camilo "I just wanted to have a quick chat with you in private before the challenge, if that's OK."
    elif s3_coupled_up_with[-1] == "Harry":
        harry "Hey, MC. Sorry to hang back like this."
        harry "I just wanted to have a quick chat with you in private before the challenge, if that's OK."

    # CHOICE
    menu:
        "[s3_current_partner] wants a chat..."
        "I thought you'd never ask":
            $ s3e1p1_li_wants_chat_response = "Positive"
            $ s3_li_like_mc[s3_coupled_up_with[-1]] += 1
            jump s3e1p1_cheeky_snog_before_game

        "Sure, what's up.":
            jump s3e1p1_cheeky_snog_before_game

        "I'd rather just get going.":
            $ s3_li_like_mc[s3_coupled_up_with[-1]] -= 1
            $ s3e1p1_li_wants_chat_response = "Negative"
            jump s3e1p1_cheeky_snog_before_game

    label s3e1p1_cheeky_snog_before_game:
        # IF STATEMENT
        # Bill LI
        if s3_coupled_up_with[-1] == "Bill":
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
                    s03_mc "No time like the present."
                    "He bites his lip."
                    bill "I can't argue with that."
                    "He smiles as your lips meet."
                    "His rough, calloused hands rest firmly on your hips."
                    "Something about his hands seems to fit, as if the two of you have been doing this for years."
                    "Finally, you both break away at the same time."
                    bill "Cor."
                    bill "I didn't see that coming."
                    bill "Did you like it?"
                    bill "Did I like it? Did I like it? [s03_mc_name]..."
                    bill "I loved it."
                    bill "Do you think we could do it again? Like, right now?"
                    s03_mc "All in good time, babe."

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
                    s03_mc "I picked you for a reason. I can't wait to see where it leads us."
                    bill "I'm glad you said that."

                "I'm not really interested, sorry":
                    $ s3_li_like_mc['Bill'] -= 2
                    s03_mc "Look, no offence..."
                    s03_mc "But just because I liked you better than the other two, that doesn't mean I actually like you."
                    bill "Oh... OK. I'm sorry."
                    bill "I just assumed..."
                    bill "I'll try to keep that in mind."

                "Let's wait and see how this goes":
                    s03_mc " It's still early days."
                    bill "Yeah, of course."
            
                "Show him the condoms" if s3e1p1_grab_some_condoms:
                    $ s3_mc_attr['Funny'] += 1
                    "You pull your bikini top out a bit and nod."
                    s03_mc " Check this out."
                    bill "Uh, alright...?"
                    "Tentatively, he peers down inside."
                    "He lets out a sharp laugh when he sees the stash of condoms there."
                    bill "That's certainly not what I was expecting to see."
                    bill "Are you trying to send me a message?"
                    bill "Because I already told you, I don't do subtlety."
                    s03_mc "I'm not trying to say anything."
                    s03_mc "I'm just a girl with a top full of condoms, and I thought you ought to know."
                    s03_mc "Seeing as we're being honest with each other right now."
                    bill "Amazing."

            bill "Well, I guess the others must be wondering where we've got to."
            bill "Let's head over for the challenge!"

        # Camilo LI
        elif s3_coupled_up_with[-1] == "Camilo":
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
                    s03_mc "No time like the present."
                    "He bites his lip."
                    camilo "I can't argue with that."
                    "He draws you into a slow, sensual kiss."
                    "His Hands tangle gently in your hair, stirring up goosebumps on the back of your neck."
                    "Finally, you both break away at the same time."
                    camilo "Blimey."
                    camilo "I didn't see that coming."
                    camilo "Did you like it?"
                    camilo "Did I like it? Did I like it? [s03_mc_name]..."
                    camilo "I loved it."
                    camilo "Do you think we could do it again? Like, right now?"
                    s03_mc "All in good time, babe."

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
                    s03_mc "I picked you for a reason. I can't wait to see where it leads us."
                    camilo "I'm glad you said that."

                "I'm not really interested, sorry":
                    $ s3_li_like_mc['Camilo'] -= 2
                    s03_mc "Look, no offence..."
                    s03_mc "But just because I liked you better than the other two, that doesn't mean I actually like you."
                    camilo "Oh... OK. I'm sorry."
                    camilo "I just assumed..."
                    camilo "I'll try to keep that in mind."

                "Let's wait and see how this goes":
                    s03_mc " It's still early days."
                    camilo "Yeah, of course."

                "Show him the condoms" if s3e1p1_grab_some_condoms:
                    $ s3_mc_attr['Funny'] += 1
                    "You pull your bikini top out a bit and nod."
                    s03_mc " Check this out."
                    camilo "Uh, alright...?"
                    "Tentatively, he peers down inside."
                    "He lets out a sharp laugh when he sees the stash of condoms there."
                    camilo "That's certainly not what I was expecting to see."
                    camilo "Are you trying to send me a message?"
                    s03_mc "I'm not trying to say anything."
                    s03_mc "I'm just a girl with a top full of condoms, and I thought you ought to know."
                    s03_mc "Seeing as we're being honest with each other right now."
                    camilo "Amazing."

            camilo "Well, I guess the others must be wondering where we've got to."
            camilo "Let's head over for the challenge!"

        # Harry LI
        elif s3_coupled_up_with[-1] == "Harry":
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
                    s03_mc "No time like the present."
                    "He bites his lip."
                    harry "I can't argue with that."
                    "He looks nervous and excited as you gently press your lips to his."
                    "His hands tentatively come to rest on your lower back."
                    "As the kiss goes on, he becomes more confident, pulling you close against him."
                    "Finally, you both break away at the same time."
                    harry "Gosh."
                    harry "I didn't see that coming."
                    s03_mc "Did you like it?"
                    harry "Did I like it? Did I like it? [s03_mc_name]..."
                    harry "I loved it."
                    harry "Do you think we could do it again? Like, right now?"
                    s03_mc "All in good time, babe."

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
                    s03_mc "I picked you for a reason. I can't wait to see where it leads us."
                    harry "I'm glad you said that."

                "I'm not really interested, sorry":
                    $ s3_li_like_mc['Harry'] -= 2
                    s03_mc "Look, no offence..."
                    s03_mc "But just because I liked you better than the other two, that doesn't mean I actually like you."
                    harry "Oh...OK. I'm sorry."
                    harry "I just assumed..."
                    harry "I'll try to keep that in mind."

                "Let's wait and see how this goes":
                    s03_mc "It's still early days."
                    harry "Yeah, of course."

                "Show him the condoms" if s3e1p1_grab_some_condoms:
                    $ s3_mc_attr['Funny'] += 1
                    "You pull your bikini top out a bit and nod."
                    s03_mc "Check this out."
                    harry "Uh, alright...?"
                    "Tentatively, he peers down inside."
                    "He lets out a sharp laugh when he sees the stash of condoms there."
                    harry "That's certainly not what I was expecting to see."
                    harry "Are you trying to send me a message?"
                    s03_mc "I'm not trying to say anything."
                    s03_mc "I'm just a girl with a top full of condoms, and I thought you ought to know."
                    s03_mc "Seeing as we're being honest with each other right now."
                    harry "Amazing."

            harry "Well, I guess the others must be wondering where we've got to."
            harry "Let's head over for the challenge!"

    # CHOICE
    menu:
        "We should go and meet the others at the challenge platform..."
        "Yep, let's go":
            s03_mc "I hope they haven't started without us!"

        "Race you!":
            $ s3_mc_attr['Funny'] += 1
            s03_mc "Last one there has to clean the pool!"
            # IF STATEMENT
            if s3_coupled_up_with[-1] == "Bill":
                bill "Wait, wh..."
            elif s3_coupled_up_with[-1] == "Camilo":
                camilo "Wait, wh..."
            elif s3_coupled_up_with[-1] == "Harry":
                harry "Wait, wh..."
            "You're already off and running."
            "Seconds later, you hear him laugh, then the sound of his bare feet on the grass as he gives chase."

        "Why don't you carry me?":
            $ s3_mc_attr['Bold'] += 1
            # IF STATEMENT
            if s3_coupled_up_with[-1] == "Bill":
                bill "Carry you?"
                s03_mc "That's what I said."
                s03_mc "You can do it, right? Or are these muscles just for show?"
                bill "He smirks and flexes his impressives arms."
                bill "Of course I can do it. Just watch."
                bill "He puts one hand on your back, scoops the other under your legs, and effortlessly sweeps you off your feet."
                bill "To the challenge platform, m'lady?"
                s03_mc " To the challenge platform at once!"
                "He sets off, carrying you bridal-style across the lawn."
            elif s3_coupled_up_with[-1] == "Camilo":
                bill "Carry you?"
                s03_mc "That's what I said."
                s03_mc "You can do it, right? Or are these muscles just for show?"
                camilo "He smirks and flexes his impressives arms."
                camilo "Of course I can do it. Just watch."
                camilo "He puts one hand on your back, scoops the other under your legs, and effortlessly sweeps you off your feet."
                camilo "To the challenge platform, m'lady?"
                s03_mc " To the challenge platform at once!"
                "He sets off, carrying you bridal-style across the lawn."
            elif s3_coupled_up_with[-1] == "Harry":
                harry "Carry you?"
                s03_mc "That's what I said."
                s03_mc "You can do it, right? Or are these muscles just for show?"
                harry "Muscles?"
                "He looks down at his arms and gives them an optimistic flex."
                harry "Of course I can do it. Just watch."
                harry "He stretches a bit more, positions himself carefully, then scoops you up in his arms."
                harry "He's stronger than he looks."
                harry "To the challenge platform, m'lady?"
                s03_mc "To the challenge platform at once!"
                "He sets off, carrying you bridal-style across the lawn."

    "It's only day 1, and [s03_mc_name] is already turning heads all over the Villa!"
    # IF STATEMENT
    if s3e1p1_cheeky_snog == True:
        "I think that snog might be one for the record books."
        "Five minutes from first sight to first kiss?"
        "The other girls will never catch up!"
    "She's coupled up with [s3_coupled_up_with[-1]] for now, but who knows what could happen at this afternoon's challenge?"
    elladine "We've got to kiss the boy we think the clue is about."

    # IF STATEMENT
    if s3_coupled_up_with[-1] == "Bill":
        genevieve "I can't believe how big that is..."
    elif s3_coupled_up_with[-1] == "Camilo" or s3_coupled_up_with[-1] == "Harry":
        miki "I can't believe how big that is..."

    "This is how much people like you:"
    "NPCs [s3_amount_npcs_like_mc]\n"
    "Love Interests [s3_li_like_mc]\n"
    "Your attributes [s3_mc_attr]"

    # LABELS FOR s3e1p1
    label s3e1p1_meet_miki:
        miki "Hi everyone! It's so exciting to be here!"

        # solo profile shot of miki
        "Miki\n
        -21, from Cambringe\n
        -Lifestyle vlogger\n
        -Loves it when you smash that subscribe button"

        miki "I mean, this is Love Island, where dreams come true, right?"
        nicky "Told you so."
        miki "At first I was like, what happens if I totally don't like any of the boys who are left?"
        miki "But now I see the two beautiful boys you've left for me to choose from..."
        miki "I don't know why I was worried."
        "Her eyes linger on Bill."
        miki "What's your name, handsome?"
        bill "I'm Bill. Pleased to meet you, love."
        miki "You seem like a rugged, down-to-earth kind of guy, Bill."
        miki "And they say opposites attract."
        miki "Fancy being coupled up with an offbeat, creative type like me?"
        bill "I'm not exactly going to say no, am I?"
        bill "Beautiful girl asks if you want to couple up, you say yes. Basic common sense, isn't it."
        "She laughs."
        miki "I'll take that as a yes."
        "She takes his hand. Together, they walk back to you and the others."

    label s3e1p1_meet_iona:
        "A new girl emerges from the Villa. Everyone falls silent."
        iona "Good morning, Love Island!"
        iona "I don't know about the rest of you, but I'm about ready to do something wild."

        # solo profile shot of iona
        "Iona\n
        -23, from Aberdeen\n
        -Apprentice pylon rigger\n
        -Spends all day making sparks fly"

        camilo "You don't mess around, do you?"
        iona "I certainly don't, babe."
        iona "Is that going to be a problem?"
        camilo "Not at all."
        camilo "In fact, I think it's going to be the opposite of a problem."
        iona "Well, now I just have to couple up with you, don't I?"
        "Iona smirks and walks over to him."
        "He gives her a little salsa-style spin and she laughs."
        "They stride over to stand beside you."


    label s3e1p1_meet_genevieve:
        "The door opens one last time, and everyone turns to look as another girl struts out onto the lawn."
        genevieve " Hello, darlings."
        genevieve "How are we all doing?"

        # solo profile shot of genevieve
        "Genevieve\n
        -26, from Gastonbury\n
        -Junior doctor\n
        -Wants to crowd surf into your heart"

        "Seeing the rest of the Islanders already in their couples, she realises Harry is the only single boy left."
        "She looks him over and smiles."
        genevieve "What's your name, sweetie?"
        harry "Sweetie."
        harry "Er, I mean..."
        harry "Harry. It's Harry."
        genevieve "Lovely to meet you, Harry."
        genevieve "How lucky am I that nobody got to you before me?"
        "She goes over to give him a hug."
        "The two of them come to stand with you, Camilo and the other couples."



#########################################################################
## Episode 1, Part 2
#########################################################################
label s3e1p2:
    "Last time on this brand spanking new season of Love Island..."
    "The Islander checked out what the Villa has to offer..."
    "...but it wasn't just the immaculately tucked sheets getting a once over."
    "Everyone met each other and hit it off!"

    # IF STATEMENT
    if s3_coupled_up_with[-1] == "Bill":
    bill "Obviously we've only really got a first impression to go on at the moment."
    bill "But I already feel like you're exactly my type on paper."
    elif s3_coupled_up_with[-1] == "Camilo":
    camilo "Obviously we've only really got a first impression to go on at the moment."
    camilo "But I already feel like you're exactly my type on paper."
    elif s3_coupled_up_with[-1] == "Harry":
    harry "Obviously we've only really got a first impression to go on at the moment."
    harry "But I already feel like you're exactly my type on paper."

    "Well, almost everyone."
    aj "Don't you think it's a bit early to say whether our couples are great or not?"
    "It's early days, AJ, early days."
    "But you know what they say..."
    "The early bird catches the worm."

    # IF STATEMENT
    if s3e1p1_cheeky_snog:
        "Or in this case, [s3_mc_name] and [s3_current_partner] get smooching!"
        if s3_coupled_up_with[-1] == "Bill":
            bill "Cor"
        elif s3_coupled_up_with[-1] == "Camilo":
            camilo "Blimey"
        elif s3_coupled_up_with[-1] == "Harry":
            harry "Gosh"
        "Well said, [s3_current_partner]."

    "Coming up..."
    "The Islander get hands-on with each other's excess baggage."
    aj "What gave it away?"
    "And one clue doesn't add up..."
    bill "I have no idea who this is about."

    "You and [s3_current_partner] make your way over to the platform where the other Islanders have already gathered."

    elladine "There you are..."

    # IF STATEMENT
    if s3e1p1_cheeky_snog:
        "Elladine points at your lips."
        elladine "You've smudged your lipstick, hun. It's on your cheek."
        "You quickly wipe at your cheek. [s3_current_partner] laughs a little."
        if s3_coupled_up_with[-1] == "Bill":
            bill "Cheeky."
        elif s3_coupled_up_with[-1] == "Camilo":
            camilo "Cheeky."
        elif s3_coupled_up_with[-1] == "Harry":
            harry "Cheeky."

    "Everyone is standing around some suitcase on a carousel."
    bill "Those spinny things make me feel dizzy at airports."
    harry "I always want to lie on them and just go round and round."
    harry "They look kinda comfy and you're always exhausted by the time you get to them."
    elladine "I got a text."
    elladine "Ooh, it's the rules of the challenge!"
    elladine "We're starting first."
    elladine "In each suitcase we'll find a secret clue about one of the guys..."
    elladine "Then we kiss the guy who we think the clue's about!"
    elladine "The guy who matches the clue steps forward and we'll see if we snogged the right person."
    elladine "Then it'll be the guys' turn."
    
    # IF STATEMENT
    if s3_coupled_up_with[-1] == "Harry":
        miki "So, do we actually have to kiss who we think the clue is about?"
        miki "Or can we just use this as a way to kiss someone we think is hot?"
        elladine "Well, you wouldn't win the game..."
        miki "But you'd get to snog someone you like."
    elif s3_coupled_up_with[-1] == "Camilo" or s3_coupled_up_with[-1] == "Bill":  
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
    "Bill coughs, looking at you."
    # IF STATEMENT
    if s3_coupled_up_with[-1] == "Bill":
        bill "You alright, [s3_mc_name]?"
    elif s3_coupled_up_with[-1] == "Camilo":
        camilo "You alright, [s3_mc_name]?"
    elif s3_coupled_up_with[-1] == "Harry":
        harry "You alright, [s3_mc_name]?"

    elladine "Yeah, you look a little farway."
    thought "Oops, I just got lost in thought."
    s3_mc "It's nothing."

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
            if s3_coupled_up_with[-1] == "Bill" or s3_coupled_up_with[-1] == "Harry":
                iona "You might get a lot of kisses."
            elif s3_coupled_up_with[-1] == "Camilo":
                genevieve "You might get a lot of kisses."
            harry "Oh, OK."
            harry "That doesn't sound too bad."
        "Just kiss some dudes":
            # IF STATEMENT
            if s3_coupled_up_with[-1] == "Bill":
                genevieve "I feel you hun."
                genevieve "Can't wait to get some action in here!"
            elif s3_coupled_up_with[-1] == "Harry" or s3_coupled_up_with[-1] == "Camilo":
                miki "I feel you hun."
                miki "Can't wait to get some action in here!"

    # IF STATEMENT
    if s3_coupled_up_with[-1] == "Bill":
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
    elif s3_coupled_up_with[-1] == "Camilo":
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
    elif s3_coupled_up_with[-1] == "Harry":
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
    if s3_coupled_up_with[-1] == "Bill" or s3_coupled_up_with[-1] == "Camilo":
        genevieve "I agree with [s3_mc_name]."
        genevieve "There's something about [s3e1p2_spooned_a_badger] that makes me imagine him waking up next to a badger."
    elif s3_coupled_up_with[-1] == "Harry":
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
                s3_mc "He's not for me."
                # IF STATEMENT
                if s3_coupled_up_with[-1] == "Bill" or s3_coupled_up_with[-1] == "Camilo":
                    elladine "Genevieve, you should kiss [s3e1p2_spooned_a_badger]."
                    aj "Yeah, you've dealt with these types before."
                    genevieve "Sure, sure."
                    "Genevieve kisses [s3e1p2_spooned_a_badger] on the lips."
                else:
                    elladine "I'll take one for the team."
                    "She kisses him."
            "Go on then, it's only a game":
                s3_mc "I'll do it."
                s3_mc "I'll kiss him."
                # IF STATEMENT
                if s3_coupled_up_with[-1] == "Bill" or s3_coupled_up_with[-1] == "Harry":
                    iona "Go on, MC!"
                elif s3_coupled_up_with[-1] == "Camilo":
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
    if s3_coupled_up_with[-1] == "Bill" or s3_coupled_up_with[-1] == "Harry":
        iona "Adorable, but moving on..."
        iona "[s3_mc_name], why don't you go and get the next suitcase?"
    elif s3_coupled_up_with[-1] == "Camilo":
        miki "Adorable, but moving on..."
        miki "[s3_mc_name], why don't you go and get the next suitcase?"


    "You head over to the carousel where suitcases are going round and round, and grab one."
    aj "Bring it over, [s3_mc_name]!"
    "You pop the case open. Inside is a label which says..."

    # IF STATEMENT
    if s3_coupled_up_with[-1] == "Bill":
        s3_mc "'This boy got caught having sex in his mum's wardrobe.'"
        aj "Woah."
        genevieve "Filthy."
    elif s3_coupled_up_with[-1] == "Camilo":
        s3_mc "'This boy got caught having sex at work.'"
        aj "Woah."
        genevieve "Filthy."
    elif s3_coupled_up_with[-1] == "Harry":
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

    # CHOICES
    menu:
        "Should I go and kiss him?"
        "Yes! Get in there with [s3e1p2_caught_having_sex]":
            "You rush over to [s3e1p2_caught_having_sex] and plant a kiss on his lips."
            "[s3e1p2_caught_having_sex] blushes at your touch."
            "You wink at him as you walk back to the girls."
        "Nah, let one of the other girls":
            # IF STATMENT
            if s3_coupled_up_with[-1] == "Bill":
            elif s3_coupled_up_with[-1] == "Camilo":
            elif s3_coupled_up_with[-1] == "Harry":
            miki "I'll kiss him!"
            "Miki walks over and kisses Camilo quickly."
            miki "Thank you, next!"

# WORKING ON THIS SPOT HERE, WORKING HERE, WORK WORK WORK WORK WORK WORK

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

    # IF STATEMENT
    if s3e1p2_caught_having_sex == "Bill":
        aj "Why did you have sex in the wardrobe?"
        aj "Aren't there like coat hangers and stuff?"
        bill "I was having a house party and there was zero privacy."
        aj "Please say your mum didn't catch you."
        bill "No, no."
        bill "She actually has no idea that it happened."
        genevieve "Until now."
        bill "Oh yeah..."
        bill "Awks..."
    elif s3e1p2_caught_having_sex == "Camilo":
        # NEED TO FILL
        "EMPTY"
    elif s3e1p2_caught_having_sex == "Harry":
        # NEED TO FILL
        "EMPTY"

    # IF STATEMENT
    if s3_coupled_up_with[-1] == "Bill" or s3_coupled_up_with[-1] == "Camilo":
        genevieve "Moving swiftly on..."
        genevieve "I'll go next."
        "Genevieve grabs another suitcase and reads out the clue."
        genevieve "'This boy rescued a cat from a burning tree.'"
    elif s3_coupled_up_with[-1] == "Harry":
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
    aj "Yeah, me too."
    aj "I'll take this one."
    "AJ jogs over to [s3e1p2_rescue_cat] and kisses him, stroking his hair a little."
    aj "Meow."

    # IF STATEMENT
    if s3_coupled_up_with[-1] == "Bill" or s3_coupled_up_with[-1] == "Camilo":
        genevieve "OK, can the man who risked his nine lives for a cat please come forward!"
    elif s3_coupled_up_with[-1] == "Harry":
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
            # NEED TO FILL
            "EMPTY"
        "He's foolish":
            # NEED TO FILL
            "EMPTY"
        "Seb clearly loves cats":
            s3_mc "Oh, you must love cats then to risk your life for them."
            seb "Yeah, cats are pretty awesome."

    aj "Once there was a fire in my dad's kitchen and we were all panicking and trying to find the cats to make sure they were safe..."
    aj "And we found them just stretching out on the floor in my bedroom, directly above where the fire was."
    seb "Cats are always proper dedicated to finding a warm spot."

    # IF STATEMENT
    if s3_coupled_up_with[-1] == "Bill":
        genevieve "Or..."
        genevieve "They started the fire to create the warm spot..."
        iona "OK, OK, enough cat talk."
        iona "Final clue girls. Then it's the boy's turn to do the kissing."
        "The boys cheer excitedly."
        iona "[s3_mc_name], you can go and pick another one."
    elif s3_coupled_up_with[-1] == "Camilo":
        genevieve "Or..."
        genevieve "They started the fire to create the warm spot..."
        miki "OK, OK, enough cat talk."
        miki "Final clue girls. Then it's the boy's turn to do the kissing."
        "The boys cheer excitedly."
        miki "[s3_mc_name], you can go and pick another one."
    elif s3_coupled_up_with[-1] == "Harry":
        miki "Or..."
        miki "They started the fire to create the warm spot..."
        iona "OK, OK, enough cat talk."
        iona "Final clue girls. Then it's the boy's turn to do the kissing."
        "The boys cheer excitedly."
        iona "[s3_mc_name], you can go and pick another one."

    "You run over to the suitcases and grab one."
    aj "What's the clue, MC?"

    # IF STATEMENT
    if s3_coupled_up_with[-1] == "Bill":
        s3_mc "'This boy asked a girl out by making her a plate of heart shaped sandwiches!'"
    elif s3_coupled_up_with[-1] == "Camilo":
        # NEED TO FILL
        "EMPTY"
    elif s3_coupled_up_with[-1] == "Harry":
        # NEED TO FILL
        "EMPTY"

    aj "Aw, that's actually a really sweet one."

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
    if s3_coupled_up_with[-1] == "Bill" or s3_coupled_up_with[-1] == "Harry":
        iona "Aw, yeah."
        iona "He's a cutie."
    elif s3_coupled_up_with[-1] == "Camilo":
        miki "Aw, yeah."
        miki "He's a cutie."


    # CHOICE
    menu:
        "Should I go and kiss [s3e1p2_asked_girl_out]?"
        "Why not?":
            # NEED TO FILL
            "EMPTY"
        "Yeah, he's a cutie":
            "[s3e1p2_asked_girl_out] smiles as you walk over to him."
            s3_mc "Come here, you."
            "You smooch, hands all over each other."
            "Everyone cheers."
        "Nah, [s3e1p2_asked_girl_out] isn't for me.":
            # NEED TO FILL
            "EMPTY"

    # IF STATEMENT
    if s3_coupled_up_with[-1] == "Bill":
        iona "Will the hopeless romantic please step forward?"
        "Bill steps forward."
        iona "It's Bill!"

        # IF STATEMENT
        if s3e1p2_asked_girl_out == "Bill":
            thought "I guessed that right!"

        bill "You can never go wrong with a good sandwich."
        bill "Only problem is that she hated mayo and I had put it in every one."
        bill "I had them for my lunch in the end."
        nicky "Nothing says love like mayo, to be fair."
    elif s3_coupled_up_with[-1] == "Camilo":
        genevieve "Will the hopeless romantic please step forward?"
        "Camilo steps forward."
        genevieve "It's Bill!"

        # IF STATEMENT
        if s3e1p2_asked_girl_out == "Camilo":
            thought "I guessed that right!"
        # NEED TO FILL
        "EMPTY"
    elif s3_coupled_up_with[-1] == "Harry":
        iona "Will the hopeless romantic please step forward?"
        "Harry steps forward."
        iona "It's Harry!"

        # IF STATEMENT
        if s3e1p2_asked_girl_out == "Harry":
            thought "I guessed that right!"
        # NEED TO FILL
        "EMPTY"

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
    if s3_coupled_up_with[-1] == "Bill" or s3_coupled_up_with[-1] == "Harry":
        seb "Iona."
        "Seb jogs over and kisses her."
        seb "She seems like the fire starting type."
        "Iona crosses her arms and rolls her eyes."
        iona "Mate, part of my job is avoiding fires."
        bill "Is that even a type that, like, people have?"
        aj "It wouldn't work on paper."
        iona "Can the fire starter please step forward..."
        Elladine steps forward.
        iona "Elladine!"
    elif s3_coupled_up_with[-1] == "Camilo":
        seb "Genevieve."
        "Seb jogs over and kisses her."
        seb "She seems like the fire starting type."
        # NEED TO FILL
        "EMPTY"

        genevieve "Can the fire starter please step forward..."
        "Elladine steps forward."
        genevieve "Elladine!"

    elladine "Yeah, it was an accident, obviously. I was trying to make him a nice fry up."
    elladine "I knocked this kitchen roll off the top shelf and it got caught in the toaster."
    elladine "No one got hurt thankfully, but yeah, I never called him back after that."
    elladine "I was way too embarrassed."

    # IF STATEMENT
    if s3_coupled_up_with[-1] == "Bill" or s3_coupled_up_with[-1] == "Harry":
        iona "OK boys, next clue."
    elif s3_coupled_up_with[-1] == "Camilo":
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
        # NEED TO FILL
        "EMPTY"
    
    # IF STATEMENT
    if s3_coupled_up_with[-1] == "Bill" or s3_coupled_up_with[-1] == "Harry":
        iona "Good guess, Nicky."
    elif s3_coupled_up_with[-1] == "Camilo":
        genevieve "Good guess, Nicky."

    elladine "Next boy, grab a case!"
    
    
# GIRLS SECRET 1

    # IF STATEMENT
    if s3_coupled_up_with[-1] == "Bill":
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
        harry "I reckon it's Genevieve."
        "He strides over and kisses Genevieve, accidentally bumping against her nose."
        genevieve "Don't worry. I didn't need my nose..."
        harry "Did I get it right?"
        genevieve "Nope!"

        # CHOICE
        menu:
            "The clue was about me! I'd better step forward..."
            "Proudly own it":
                "You leap forward with your hand on your hips."
                s3_mc "It's me!"
            "Shamefully scuffle forward":
                "You shuffle your feet forward looking down at the floor."
                s3_mc "It's me."
            "Blame it on someone else":
                "You point at Elladine with an accusing finger"
                s3_mc "This is a set up! Elladine is clearly the one that secret is about!"
                "Everyone keeps staring at you and it's clear your pointed blame is not believed."
                s3_mc "Fine, it's me."

        # IF STATEMENT
        if s3e1p2_mc_secret == "Thunder":
            s3_mc "The thunder lover."
        elif s3e1p2_mc_secret == "Rollercoaster":
            s3_mc "The rollercoaster lover."
        elif s3e1p2_mc_secret == "Dimples":
            s3_mc "The dimple lover."
        elif s3e1p2_mc_secret == "Fan Fiction":
            s3_mc "The fan fiction lover."

        harry "[s3_mc_name]?"
        s3_mc "Yeah."
        harry "Woah, I was well off."
        harry "Ah, sorry, Genevieve."
        genevieve "You have got to tell us more about that later, hun."
        bill "Yeah, I need details."
    elif s3_coupled_up_with[-1] == "Camilo":
        "Bill goes and picks up a suitcase."
        bill "'This girl...'"
        # IF STATEMENT
        if s3e1p2_mc_secret == "Thunder":
            bill "'...is sexually attracted to the rumble of thunder!'"
        elif s3e1p2_mc_secret == "Rollercoaster":
            bill "'...had a naughty adventure on a rollercoaster!'"
        elif s3e1p2_mc_secret == "Dimples":
            bill "'...has a tendency to get too excited by dimples!'"
        elif s3e1p2_mc_secret == "Fan Fiction":
            bill "'...wrote fan fiction when she was younger!'"
        
        thought "Oh no! This is about me."
        thought "I wonder if Bill can guess who that's about."
        bill "I reckon it's Miki."
        "He strides over and kisses Miki."
        bill "Did I get it right?"
        miki "Nope!"

        # CHOICE
        menu:
            "The clue was about me! I'd better step forward..."
            "Proudly own it":
                "You leap forward with your hand on your hips."
                s3_mc "It's me!"
            "Shamefully scuffle forward":
                "You shuffle your feet forward looking down at the floor."
                s3_mc "It's me."
            "Blame it on someone else":
                "You point at Elladine with an accusing finger"
                s3_mc "This is a set up! Elladine is clearly the one that secret is about!"
                "Everyone keeps staring at you and it's clear your pointed blame is not believed."
                s3_mc "Fine, it's me."

        # IF STATEMENT
        if s3e1p2_mc_secret == "Thunder":
            s3_mc "The thunder lover."
        elif s3e1p2_mc_secret == "Rollercoaster":
            s3_mc "The rollercoaster lover."
        elif s3e1p2_mc_secret == "Dimples":
            s3_mc "The dimple lover."
        elif s3e1p2_mc_secret == "Fan Fiction":
            s3_mc "The fan fiction lover."

        bill "[s3_mc_name]?"
        s3_mc "Yeah."
        bill "Woah, I was well off."
        bill "Ah, sorry, Genevieve."
        miki "You have got to tell us more about that later, hun."
        camilo "Yeah, I need details."
    elif s3_coupled_up_with[-1] == "Harry":
        "Camilo goes and picks up a suitcase."
        camilo "'This girl...'"
        # IF STATEMENT
        if s3e1p2_mc_secret == "Thunder":
            camilo "'...is sexually attracted to the rumble of thunder!'"
        elif s3e1p2_mc_secret == "Rollercoaster":
            camilo "'...had a naughty adventure on a rollercoaster!'"
        elif s3e1p2_mc_secret == "Dimples":
            camilo "'...has a tendency to get too excited by dimples!'"
        elif s3e1p2_mc_secret == "Fan Fiction":
            camilo "'...wrote fan fiction when she was younger!'"
        
        thought "Oh no! This is about me."
        thought "I wonder if Camilo can guess who that's about."
        camilo "I reckon it's Iona."
        "He strides over and kisses Iona."
        camilo "Did I get it right?"
        iona "Nope!"

    # CHOICE
    menu:
        "The clue was about me! I'd better step forward..."
        "Proudly own it":
            "You leap forward with your hand on your hips."
            s3_mc "It's me!"
        "Shamefully scuffle forward":
            "You shuffle your feet forward looking down at the floor."
            s3_mc "It's me."
        "Blame it on someone else":
            "You point at Elladine with an accusing finger"
            s3_mc "This is a set up! Elladine is clearly the one that secret is about!"
            "Everyone keeps staring at you and it's clear your pointed blame is not believed."
            s3_mc "Fine, it's me."

    # IF STATEMENT
    if s3e1p2_mc_secret == "Thunder":
        s3_mc "The thunder lover."
    elif s3e1p2_mc_secret == "Rollercoaster":
        s3_mc "The rollercoaster lover."
    elif s3e1p2_mc_secret == "Dimples":
        s3_mc "The dimple lover."
    elif s3e1p2_mc_secret == "Fan Fiction":
        s3_mc "The fan fiction lover."

    camilo "[s3_mc_name]?"
    s3_mc "Yeah."
    camilo "Woah, I was well off."
    camilo "Ah, sorry, Genevieve."
    iona "You have got to tell us more about that later, hun."
    harry "Yeah, I need details."

Choiceseb "Everyone wants to hear more about my secret..."
-Maybe another day...
s3_mc "I've got an air of mystery to keep up, haven't I?"
s3_mc "Maybe I'll reveal more another time."

-No way, this is enough already
-This wasn't the half of it

Elladine coughs pointedly.

# GIRL SECRET 2

(If you kissed your partner in the first episode with the gem choice)
bill "Can I go again?"
iona "Sure!"
He smiles at you as he walks over, hoisting a case over his toned shoulders.
bill "OK, this girl..."
He looks up at you and smiles.
bill "'This girl has already kissed a boy since we got into the Villa!'"
iona "We'll all have by the end of this challenge."
He turns the piece of paper over.
bill "'Before the challenge started!'"
Everyone laughs.
genevieve "OK, I have no idea who that was."
bill "I think I do..."
He strides up to you and gently places his palm on your cheek.
bill "Fancy a round two?"
Choiceseb "Do I want Bill to kiss me again?"
-Yes!
He leans in and kisses you softly on the lips. (you get ❤️ with Bill)
genevieve "MC is getting all the action today!"

-Nah, you can kiss someone else
-Go on then, Bill

iona "The answer was, of course..."
You step forward.
iona "MC!"
bill "Knew it."
iona "Oh, you guys!"
elladine "Such cuties."


iona "OK..."
iona "Next round."

MC coupled with Bill
bill "Can I go again? "
The other boys cheer him on.
He grabs a case and looks at the clue.
s3_mc "Just read the secret, hun."
bill "'This girl has only ever had sex while on the water.'"
The boys go into a huddle.
elladine "Oh my gosh, which of you is this about?"
You look around the group. Nobody says anything.
aj "Come on, girls. It has to be one of us."
It quickly becomes clear that the clue isn't about any of you.
genevieve "I don't get it. Who could it be?"
iona "It's got to be one of us."
A clatter and rattle of wheels grabs everyone's attention as a large suitcase wheels out onto the platform.
aj "Oh, wow."
aj "That's one huge suitcase."
genevieve "I've never seen one that big before..."
bill "I got a text!"
Text: Islanders, there is an unexpected item in your bagging area. Bill, please unzip the case.
elladine "Oh my gosh, Bill! Open up the case already!"
Bill tentatively unzips the suitcase.
A stunning woman steps out.
M: Hey, you lot. I'm Miki.
Miki
-21, from Cambridge
-Lifestyle vlogger
-Loves it when you smash the subscribe button

She nods at Bill.
M: Thanks for getting me out of there, Bill.
Genevieve splutters in shock.
genevieve "Wait..what? But..."
iona "It's a new girl!"
Elladine and Iona run over to hug Miki.
elladine "Welcome to the Villa, hun."
nicky "Yeah, hey. I hope you weren't stuck in there for long, babe."
M: Nah, just a few minutes.

Choiceseb "There's a new girl in the Villa..."
-Welcome her with a hug

-Try and get in the suitcase
You run past Miki and attempt to clamber into the large suitcase. You fit perfectly, even standing upright.
s3_mc "Woah, this thing is huge."
aj "Yeah, how did they get you on the plane in that thing?"
Mikiona "I didn't ride in it on the plane, hun. I only just got in it."
aj "Oh right. Yeah, of course."

-Roll your eyes and ignore her

aj "Wait, we just had a clue, right? Miki, was it about you?"
aj "Have you really only ever had sex on water?"
genevieve "How does that even work?"
Miki smiles.
M: I guess we'll have to wait for the boys to guess before we find out, won't we?
bill "Well, I think I can guess who to kiss now..."
He takes a step toward her.

Choiceseb "Miki and Bill are going to kiss"
-Cheer them on

-Scream internally, but pretend to be fine
thought "..."
thought "This is a disaster!"
Bill walks over to Miki.
thought "Why me?"
iona "You OK hun? You look like you're gritting your teeth a bit..."
s3_mc "I'm fine! Totally fine."

-Give her the stink eye

Bill quickly walks over to Miki and kisses her on the lips tentatively.
seb "How was it, mate?"
bill "I'd say that was...maybe the third best kiss I've had today?"
seb "Wow. You're really cracking on, huh."
elladine "So, was he right?"
M: Yeah, it's true.
M: I love the water.
M: Oh, I got a text! That was quick.
Text: Islanders, that's the end of the challenge. Hopefully you've all learnt a little bit more about your fellow Islanders. Now all the dirt is dished, it's time for Miki to go and get to know you all.
M: Alright! Let's go, huns!
Miki struts off towards the Villa, and everyone else follows.
thought "So, now this Miki person is in the mix."
thought "I should think about how I want to play things with her."
thought "Do I want to get in her good books early?"
thought "Or find out her priorities?"
thought "Maybe I should get to her before the other Islanders do, and get the gossip."
Choiceseb "Should I get Miki over for a private chat?"
-Spend some time with the new girl (gem choice)

-Don't talk to her
You watch her walk off with the others.
thought "Am I sure about this? It might be my last chance..."
Choiceseb "Should I get to know Miki before the others do?"
-Spend some time with the new girl (gem choice)

-Don't talk to her
thought "Nah, I'm not bothered."
thought "I'll just get to know her with the others."

You and the other Islanders are lounging by the pool.
bill "By the way. I never got the chance to say it earlier, but I absolutely love the swimsuit. "
bill "It looks so good on you. (you get 🤩 with Bill)"
s3_mc "Thanks!"
iona "So, everyone's dirties are out now..."
iona "And now Miki is here."
Miki does a little wave.
M: Yeah, it's me.
harry "So much has happened, in so little time!"
harry "I feel like we're already a solid group."
iona "I know, right? It's all going down."
iona "Pretending to be a waitress..."
nicky "I can't believe Miki's secret."
bill "Yeah, did you, like, live on a boat or something?"
M: Yeah, I do actually.
bill "Oh, woah. That makes more sense now."
nicky "I thought it was a great clue."
seb "Yeah, same."
seb "Shows you've got good life experiences and all that."

Choiceseb "What do I think about Miki's clue?"
-I can't wait to get to know Miki!
s3_mc "You sound right up my street, Miki."
s3_mc "I can't wait to get to know you!"
M: Aw, thanks, MC.
-It doesn't say much about her
-I don't believe Miki at all

iona "For real though Miki, you definitely made an entrance."
iona "Maybe we should all arrive in suitcases next time!"
M: Yeah, I thought it was a bit out there at first but it was actually really fun.
genevieve "It worked really well."
M: I can't believe all this.
She gestures to the Villa.
M: It's amazing, isn't it?
aj "Yeah, I'm still getting used to all this."
elladine "We'll all settle in soon enough."
camilo "Once we have, like, proper meal together."
camilo "Then it'll feel like home."
camilo "Food is the way to my heart..."
aj "As long as I haven't cooked it, then a good meal is exactly what we need."
genevieve "Yeah, and hopefully Elladine doesn't burn the kitchen down!"

Choiceseb "Is food the way to my heart?"
-Of course! Food makes the heart grow fonder
-Nah, I'm more of a drinks gal

-As long as I'm eating it off Bill's body
elladine "Woha, MC!"
thought "Did I say that out loud?"
Bill blushes, but grins excitedly.
bill "You sure did..."
M: Oh, that's mine.
Text: Miki, it's time for you to decide who to couple up with. All Islanders, please gather at the fire pit for the recoupling.
#chooseyourmatch #dontlookback
Miki looks around the group with a cheeky glint in her eye.
elladine "Who are you going to choose?"

"Who knows, Elladine?"
"Who knows...?"
"Well, I guess Miki does."
"Remind me not to let those lot in the kitchen."
" Especially that Elladine and AJ. They're fire hazards."
"I don't know how I'd actually stop them. I can't leave this shed."
"Maybe if I shout loud enough."
"Coming up..."
"The Islanders get their graft on."
genevieve "Single and ready to mingle, eh?"
iona "Guess we'll need to keep a close eye on you."
"And the power is in Miki's hands."
M: But, ultimately, I do have to make a choice and so...



#########################################################################
## Episode 1, Part 3
#########################################################################
label s3e1p3:
Stick the Landing - New Rules  Day 1 Part  3/3
"Welcome back..."
"To Love Island!"
"In an absolutely shocking twist that literally no one could have predicted..."
"Another girl has already entered the Villa!"
M: Hey, you lot. I'm Miki.
M: Thanks for getting me out of there.
"Ladies, hide your men, this one's coming for them..."
"Though it'll be hard to hide them in a Villa covered in cameras..."
"Maybe if they put the sheets over their heads and pretend to be ghosts?"
"Or stand really still and pretend to be statues?"
"I don't know. I've never played a game of Hide and Seek in my life."
"Coming up!"
"Bill gets cheesy..."
bill "I don't know about the rest of you, but I'm cream-crackered."
"And Miki takes her pick..."
M: The guy I'd like to couple up with is...

The dressing room is a flurry of activity as the girls ready themselves for Miki's decision.
iona "It's so weird knowing that Miki's just stood by the firepit waiting for us."
genevieve "Waiting for the guys more like."
elladine "Yeah. It really didn't take long for the drama to start."
genevieve "Tell me about it! I thought we'd at least have a day or something."
iona "Well, we kind of did."
aj "Can you pass me my lipstick, Ella, babes."
elladine "Of course hun."
aj "Thanks! Miki's super fit, don't you think?"

Choiceseb "Miki is..."
-Almost too good looking
elladine "Yeah..."

-Not really all that

-Not as fit as me
elladine "You're both gorgeous."

elladine "She's definitely some fierce competition."
aj "That's why I want to make a special effort."
thought "Everyone's going all out. I guess if there was a night for it, now's the time..."
(If you chose 'grab a handful of condoms' in Episode 1:)
You absent-mindedly undo your bra, then hear the telltale sound of plastic wrappers hitting the floor.
s3_mc "The condoms!"
Different coloured wrappers indicating flavours spill across the room. Cherry red, banana yellow, and wheatgrass green.
aj "Woah, MC!"
s3_mc "Whoops..."
aj "Someone's looking to get busy."
s3_mc "Better to be safe than sorry."
elladine "Damn right."

MC outfit change to evening wear

thought "Oh yeah, this is going to blow some minds."
Elladine looks over to you. Her eyes go wide.
elladine "Damn! MC, you're a real heart-stealer in that! (you get 🤩 with Elladine)"
s3_mc "That's the idea."
Iona turns to you.
iona "Are you worried about tonight, babe?"

Choiceseb "Am I worried about who Miki will pick?"
-I'd be lying if I said no
iona "Yeah, I know what you mean."

-No, of course I'm not

-How could I when I look this good?

iona "Why am I so nervous?"
Genevieve takes a deep breath, and gives herself one last look-over in the mirror.
genevieve "Well, girls, I guess this is it..."

Miki stands in front of the Islanders sat around the firepit.

Choiceseb "We only just arrived and already I might get separated from Bill..."
-Hold his hand
You reach over and take a hold of Bill's hand. He turns and smiles at you.
bill "Your hands are so soft. (you get 😍 with Bill)"
You blush
bill "Seriously, it's like holding a warm loaf of bread or something..."
s3_mc "Huh?"
B:...I don't know. Ignore me. My mind's all over the place.
He shifts in his seat.

-Glare at Miki

-Look at the other Islanders

Miki clears her throat, then speaks.
M: I didn't know how to feel on the way here.
M: I was excited, obviously, but I knew I'd be taking a guy away from another girl.
M: I thought I'd be OK with that as you've only been together since this morning...
M: But looking at you all now, you already seem like such cute couples.
M: But at first glance, this boy seems like my type on paper.
M: He's smart, funny, and just dreamy.
M: And although I don't want to break a promising couple up so early on...
M: I'm here to make a choice and so...
Everyone tenses.
thought "She better not pick Bill."
M: The boy I'd like to couple up with is...
thought "Maybe she won't?"
M: Bill.

Choiceseb "Miki picked Bill!"
-I called it

-No, dammit!

-Well, this sucks (no further reaction)

You hear sighs of relief and murmurs coming from the others.
elladine "Oh no! Poor MC..."
seb "Wow, that's brutal."
nicky "Yeah, that's rough, man."

Choiceseb "Miki's taken my guy..."
-It is what it is

-How could you?

-I'll be coming for him
M: Good
M: I'm looking forward to the competition

Bill puts a hand on your back.
bill "I can't believe this."
bill "I was blown away when you picked me. It's like I'd won the jackpot."
bill "And now we're not a couple, less than a day after that..."
He stands to walk over to Miki.

Choiceseb "Bill's getting up to leave..."
-Squeeze his hand
You reach out, grab his hand, and give it a gentle squeeze. He stops in his tracks and turns back to you.
bill "Don't worry. I'll only be over there (you get 😍 with Bill)"
s3_mc "But that's not here."
bill "Yeah..."
He sighs, then continues over to Miki.

-Drag him back

-Wave goodbye

bill "Alright, girl?"
M: I'm good, you?
Bill shrugs. He and Miki share a clumsy hug.
s3_mc "I got a text..."
s3_mc "I swear, if this is me getting dumped already I'm gonna be livid."
aj "That wouldn't happen already, right?"
seb "It isn't unheard of."
elladine "Read it out, hun."
Text: MC, Miki has taken your partner, leaving you single...
s3_mc "Ugh."
Text: ...so get ready to mingle.
#getthatgrafton #the singlelife
aj "What's that all mean?"
s3_mc "I'm...safe?"
elladine "Phew! Not gonna lie but that would have been proper cruel."
aj "Yay!"
genevieve "Single and ready to mingle, eh?"
genevieve "Guess we'll need to keep a close eye on you."
Nicky gets up and stretches.
nicky "I don't know about you lot, but my bum's gone numb."
He makes his way over to Miki.

Choiceseb "Should I go and talk to Miki?"
-Walk over to Miki

-Stay where you are

-Walk away from the others
You get up, leaving the rest of the Islanders to form their own little groups.
The night is surprisingly chilly. You rub your arms for some warmth.
The sound of laughter drifts over from the other Islanders.
M: Cold?
You turn and see Miki standing in front of you. A concerned look on her face.
M: Me too. And I thought Cambridge could get chilly!
M: Sometimes the boat's little heater isn't enough, you know?
She rubs her arm.

M: Um, I'd like to clear the air with you.
s3_mc "Sure...let's talk."
M: Thanks.
M: I want you to know that it wasn't anything personal. I mean, obviously, I've only just met you.
M: I wanted to tell you earlier, but we didn't get any time to chat.
M: I didn't want it to come as a shock.
M: At the end of the day, I had to pick someone.
M: But I actually think this puts you in a really strong position. You're now free to chat and flirt with whoever you want.
M: Even if that person is Bill. Like, all's fair. I won't make a fuss.
M: Early days and all that.
She pauses.
M: So...friends?

Choiceseb "Should I forgive Miki for choosing Bill?"
-Hey, it's fine. It was a tough call
Miki's shoulders relax with relief. (you get 😍 with Miki)
M: Thanks, babe! You have no idea how awkward I was feeling.
M: You're so understanding.

-I'm sorry, but I need some time

-Relax, girl! I'd known him for two minutes

She squeezes your arm lightly.
M: Come on, then. We should get back to the others.
You walk back together.

Seb, Nicky, Elladine and Genevieve are sat around the firepit chatting
thought "I could do with someone to talk to."
Love Island isn't just about romance. It's also about the friendships you form along the way. One of these four Islanders is going to be a close friend for the rest of your time in the Villa.
thought "People can get attached pretty quickly in this Villa. I should think about who I want to be friends with..."
thought "I don't think I've ever met anyone as positive as Elladine."
thought "I feel like she's the kind of person that always has a funny story to share or a comfortable shoulder to cry on."
thought "I feel like Genevieve is used to dealing with people and understands how to navigate tricky issues..."
thought "Plus, she just seems lovely."
thought "I don't get romantic vibes off Seb and Nicky. I definitely see them more as friends than romantic partners."
thought "Nicky already strikes me as a proper joker. He's got an 'older bro' vibe to him."
thought "Seb's got this darker side to him. Like, he's got the most life experience here and will just say things how they are..."
Choiceseb "Who should I speak to?"
-Elladine
-Genevieve
-Nicky
-Seb

You make your way over to where Genevieve is sitting with the others.
elladine "Hey, MC!"
s3_mc "Hey, Genevieve..."
genevieve "Yeah?"
s3_mc "Could I speak to you in private?"
genevieve "Of course, babes!"
genevieve "Roof terrace?"
s3_mc "Sounds good!"
The two of you make your way upstairs.
"After having Bill taken from her, MC and Genevieve have come to the terrace to talk it over."
"I get the feeling that this could be the start of a beautiful friendship..."
You and Genevieve make your way to the nearest sofa and take a seat that overlooks the rest of the Villa.
There's a splash, then AJ emerges from the pool. She runs around to the other side, then cannonballs in again.
genevieve "I bet that girl's never been tired in her life..."

Choiceseb "AJ seems to be bursting with energy..."
-I wish I was more like that
genevieve "Right?"
genevieve "I just don't get how some people can be so active. I'm useless without two coffees in the morning."

-I get tired just watching her

-Maybe she'll keep me on my toes...

There's a moment of silence as the two of you watch the other Islanders roam around the Villa.
genevieve "So, how are you doing?"
genevieve "Tonight must have been tough..."

Choiceseb "I'm doing..."
-Pretty good, all things considered

-Meh, my head's all over the place
genevieve "That's understandable. You've already been through a dumping and it's only the first day."

-Great! I'm single and ready to mingle!

Genevieve smiles at you.
genevieve "Want to know what I think?"
s3_mc "Go on."
genevieve "The way I see it, you're actually in one of the best positions in the Villa."
genevieve "You can graft on whoever you want to now, and no one can really have a problem with you for it."
genevieve "You can get to know everyone before the next recoupling!"
genevieve "I'd say that's better than pairing up with a stranger straight away."

Choiceseb "Genevieve thinks that being single at the start is better..."
-You make a good point

-But what if I already like Bill?
genevieve "Then go out and get him back!"
genevieve "Tomorrow is when the real grafting starts. You've just gotta keep your eyes on the prize."

-I'm going to graft so hard

Genevieve looks out thoughtfully at the view.
genevieve "It's well dark already, isn't it?"
s3_mc "Yeah, it is actually."
genevieve "I can't believe we're in here looking for love."
genevieve "Such a weird, like, concept, isn't it?"
genevieve "We're on an Island doing some kind of treasure hunting or something..."
genevieve "And the prize is that you might fall in love."

Choiceseb "Genevieve thinks we're on a treasure hunt for love!"
-Yeah, and I've lost my treasure already
genevieve "Girl, you've got nothing to worry about."
genevieve "Miki has got nothing on you."
genevieve "I'm sure you're still in with a chance to win him back!"

-Don't forget about the prize money

-But sex marks the spot

Genevieve bites her thumbnail absentmindedly.
genevieve "I'm like, such a night warrior and a worrier."
s3_mc "A worrying night warrior."
genevieve "Yeah, that should be my superhero name at work or something."
s3_mc "What is it that you do again?"
genevieve "Junior doctor."
genevieve "I always get hyper sensitive when it gets dark."
genevieve "Which means three things..."
She counts them off on her fingers as she goes along.
genevieve "One, I'm good at working night shifts because I am rarely able to sleep."
genevieve "Two, when I'm not working, I'm freaking out because work is, like, such a good distraction."
genevieve "I'm mostly working on site for festivals at the moment."

Choiceseb "Working as a doctor at a festival sounds..."
-Really hard work
genevieve "Yeah, it can be."

-Like my absolute dream job

-Rubbish! I thought you didn't like the dark?

genevieve "Being a model must have its moments, though. (depends on your job)"
genevieve "Every job has its bad habits."
genevieve "I love that I'm surrounded by people."
genevieve "It's literally constant when you're working as a doctor at a festival."
genevieve "Can't stand how quiet and dark hospitals can get."
genevieve "I bet this place will be a bit spooky, like, late at night."
genevieve "It'd be easier if there were more people."
s3_mc "What was the third thing?"
Genevieve looks puzzled.
genevieve "You know what?"
genevieve "For the life of me I can't remember."
genevieve "It's because it's getting late."
genevieve "I'm just getting restless."

Choiceseb "Genevieve struggles settling down at night."
-Don't worry, I'll look out for you!
genevieve "Awh, really?"
genevieve "Means a lot, I'm not going to lie. (you get 😍 with Genevieve)"

-I'll be out like a log soon

-I can never get to sleep either

The sound of the other Islanders draws your attention away from Genevieve.
bill "Right, I don't know about the rest of you, but I'm cream-crackered."
M: You're a cream cracker?
camilo "Hah! He is now. That's brilliant."
bill "What? No. I'm knackered."
M: Oh!
M: You mumble too much.
iona "Who even likes cream crackers?"
camilo "They're gross. Chocolate bourbons all the way, you get me?"
bill "Wait, a cream cracker isn't a biscuit."
camilo "Isn't it one of those square ones with custard cream in the middle?"
bill "That's a custard cream, mate, and they're way better than bourbons."
The door to the Villa closes.
genevieve "Sounds like everyone's going to bed."
s3_mc "Guess I'll be sleeping alone."
Genevieve rubs her chin.
genevieve "You know what?"
genevieve "I think you should find a way to show that you're totally not fazed by this."
genevieve "Some way to show the Villa that you're still here to have a good time, just like everyone else."
She thinks about it for a moment.
genevieve "What about a prank?"
s3_mc "Do you have anything in mind?"
genevieve "Well, if we want to do it before bed, it's got to be something simple and classic."
genevieve "What about if you hide somewhere and jump out at someone?"
genevieve "I can keep them distracted while you get ready. What do you say?"
thought "Do I want to make one of the other Islanders jump? It could be a cute start to my single gal mischief..."

Choiceseb "It might be a good chance to get some alone time with someone, too..."
-That sounds hilarious! Let's do it (gem choice)

-As fun as that sounds, I don't think so
genevieve "That's fair. It's been a big day already. Another time, maybe."
genevieve "Although, are you sure? Last chance..."
Choiceseb "I bet it'd be really fun to make someone jump..."
-Actually, let's do it (gem choice)
-Nah, not right now

Gem choice:
genevieve "Yes! This'll be so fun. (you get 😍 with Genevieve)"


You both stand up.
genevieve "Hey, before we head back in, I just want to say that I'm really glad we had this chat."
genevieve "If you ever need to talk again, just come and see me, yeah?"
genevieve "Come on, then. Let's go."
The two of you head inside.

Continuation of gem choice:
You and Genevieve head into the bedroom. You can hear the others approaching.
genevieve "Alright, go time! You hide. I'll go and keep them busy."
Genevieve dashes out of the other door. You hear her talking to the others.

Choiceseb "Who do I want to scare?"
-Harry 
-Camilo
-Bill 
-AJ

You dive under Bill's bed and wait for him to get within grabbing range.
Bill, Camilo, and Harry enter the room.
bill "...so yeah, sorry if I don't want dust powder with fake 'cream' in the middle, but no thanks."
harry "But they're the best!"
bill "I've literally just explained to you why that isn't the case."
camilo "I still can't believe you dunk pink wafers in your tea, bruv."
bill "They're a biscuit! Biscuits are meant to be dunked. That's like saying you shouldn't drink  beer with a curry."
bill "It's just common sense, yeah?"
camilo "But don't they just get soggy?"
bill "Well yeah, that's why you have a dunking hierarchy, ranked from hardest to weakest."
harry "I don't think I've ever thought about biscuits so much in my life."
aj "And I don't think I ever want to again."
elladine "It's been very..."
elladine "...enlightening."
nicky "That's a word. Not sure the one I'd for this conversation, but definitely a word."
From your hiding spot, you see Bill making his way over to you.
bill "Anyone seen MC?"
genevieve "No?"
bill "Weird. Maybe she's gone to sleep on the daybeds?"
Genevieve lowers her voice into a harsh whisper.
genevieve "Or maybe a ghost got her..."
She wiggles her fingers dramatically.
iona "Woah! Hey, guys, look at the moon."
M: It looks massive.
genevieve "Come out onto the terrace with me. Let's get a proper look."
You hear the others leave.
bill "I'll be out there in a second!"
Bill stops in front of you...

Choiceseb "This is it! How should I scare him?"
-Call out his name
You start with a whisper...
s3_mc "Bill..."
bill "Huh?"
s3_mc "Bill."
bill "...Hello?"
s3_mc "Bill!"
The force from your sudden shout makes Bill jump.
bill "What the hell? (you get 😱 with Bill)"
You crawl out from under the bed, crackling wildly.
bill "Nice one. (you get 😍 with Bill)"

-Jump out at him

-Grab his ankle

bill "Maybe I'll get you back by hiding in your bed?"

Choiceseb "Bill hiding in my bed..."
-Sounds more like a dream come true

-You in my bed would be terrifying

-Is that an invitation?
bill "It can be if you want... (you get 😏 with Bill)"
bill "You realise I have to get you back for this, right?"
s3_mc "I'd like to see you try..."

Before he can say anything else, the rest of the Islanders reappear, laughing.
iona "Genevieve told us what you were up to, MC."
nicky "It sounds like it worked."
M: Just never spook me, yeah? I hate jump scares...

They start to get ready for bed.
thought "That's enough excitement for one night. I'm going to go and get changed."

thought "Right, first night in the Villa and I'm single. It's worth going all out tonight."
thought "I want the others to see who they're dealing with..."
MC outfit change to sleepwear
thought "This outfit is beyond cute."

You squeeze some toothpaste onto your brush and begin to clear your teeth.
You hear the bathroom door open and close. You turn to see AJ standing there, towel in hand.
aj "Oh, sorry! I should have knocked."
s3_mc "Thawt's oclay, garl."
She laughs.
aj "What?"
You try to speak again but a dribble of toothpaste makes it's way down your chin instead.
You quickly wipe it away.
s3_mc "Whurlps!"
aj "Hah! Gross."
aj "Don't mind me, hun. I'm just going to brush my teeth as well."
She looks you up and down quickly.
aj "I didn't think pyjamas could look so good. You're making me jealous. (you get 🤩 with AJ)"
She picks up her brush and begins to vigorously clean her teeth.
thought "I've never seen someone brush their teeth so hard and fast..."
aj "Schwo, howsh shings?"
s3_mc "Hmm?"
She chuckles and leans in towards the sink.
The two of you go to use it at the same time and gently bump into each other.
AJ giggles.
She gestures to the sink. You quickly rinse your mouth.
s3_mc "Thanks."
AJ does the same.
aj "No problem."
She grins at you as she wipes her mouth with her towel.
aj "Ahh, minty fresh."
aj "I asked how's things?"


Choiceseb "Things are..."
-Great!

-All a bit much
aj "Aw, sorry, babes."

-What they are

AJ slowly plays with the towel in her hands.
aj "So, you got your eye on any of the guys here?"

Choiceseb "Which guy do I have my eye on?"
-Harry

-Camilo

-Bill
aj "Hah! Really? (you get 😲 with AJ)"
aj "Sorry, that was well rude."
aj "It's just, he's got an opinion on everything!"
aj "Though, he's kinda funny, I'll give you that."
aj "It sucks that you don't get to spend your first night here with him."

-Nobody so far...

A knock on the door breaks you both out of your conversation.
seb "Hey, you done yet?"
seb "There's half a dozen people out here waiting to use the loo."
seb "Some are in more desperate need than others!"
s3_mc "Whoops."
AJ chuckles again.
aj "I guess we should go."

"Don't fret, MC! So, you've lost Bill, but at least you've got a bed!"
"I don't even have a sleeping bag! All the budget's gone on biscuits for the Islanders to argue over."
"Not that they appreciate my sacrifice!"
"Next time on Love Island..."
"Seb says something appalling at breakfast..."
seb "I really want some black pudding."
"Eww!"
"And MC gets grafting..."
s3_mc "Let me ride you..."
"And we've got a whole bunch of other surprises lined up for you."
"It's a whole new series! I can't wait to see what's going to happen."




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