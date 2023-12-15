#########################################################################
## Episode 1, Part 1
#########################################################################
label s3e1p1:
"Finding love can be tough…"
"Daily life is nothing but work, sleep, and repeat…"
"How are you supposed to have time to search for that special someone?"
"It's time to get off social media, and find love the old-fashioned way…"
"On a reality TV show!"
"You've been invited to a place where everything is different…"
"A place where all you have to do all day is meet beautiful people, couple up, and fall in love…"
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
"I can't believe this is going to be my home for the next two weeks! (We may add a bit more later but for now just focus on what we have.)"
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
s03_mc "I think we're the first ones here!"
elladine "Amazing. This is one of those moments you remember forever, isn't it?"
s03_mc "I think so!"
elladine "I know we will. (you get  with Elladine)"

"Wow, I love your outfit":
s03_mc "It's stunning!"
elladine "Babes, I was about to say the same to you! (you get  with Elladine)"
elladine "Seriously. You've already set the bar super high."
elladine "The boys are going to freak when they see us."

"Warning, I'm here to win":
s03_mc "Before we go getting too friendly, you need to know one thing about me."
s03_mc "I'm here to find love, and I don't care how many toes I have to tread on to get it."
s03_mc "So if you're tempted to cross me at some point while we're here…"
s03_mc "Don't."
s03_mc "Understood?"
elladine "Um, sure. Understood ( you get 🙁 with Elladine)"

elladine "I've been feeling well nervous ever since I got here."
elladine "I mean it's exciting, but it's also a lot of pressure, isn't it?"

# CHOICE
menu:
"How am I feeling?"
"So nervous":
s03_mc "I've never done anything like this before. It's a bit scary."
elladine "At least we're all in the same boat!"

"Just excited":
s03_mc "I'm really excited to meet everyone!"

"Kinda hungry":
$ s3e1p1_feeling_hungry = True
elladine "You mean, like…hungry for love, or..?"
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
aj "Man, I knew everyone here was gonna be gorgeous, but I wasn't prepared…"
elladine "Stop staring and introduce yourself!"
aj "Sorry, sorry!"
aj "My name's AJ. It's nice to meet you."

# solo portrait shot of aj
"AJ\n
-21, from Bath\n
-Professional hockey player\n
-Knows how to handle a stick"

s03_mc "I'm [s03_mc_name]"
elladine "We were just talking outside. She's really nice. (after Wow, I love your outfit or it's nice to meet you too) Or We were just talking outside. She, um.. she definitely means business. (after Warning, I'm here to win)"
aj "I hope everyone's going to be cool. I don't want to get sucked into a load of drama."
aj "I mean, we're all here to have fun, right?"

# CHOICE
menu:
"AJ's here to have fun, not to get into drama.."

"Me too! Let's keep it chill and friendly":
s03_mc "Trust me, we're gonna have a great time."
s03_mc "You're my girls now, and I don't let my girls turn on each other. (you get  with AJ)"
aj "Yes! I'm so glad you said that."

"But there's no fun without drama":
s03_mc "It's so exciting when someone does something totally shocking, and you just know the fallout is gonna be huge."
s03_mc "I can't wait to stir up some trouble around here."
aj "Fair play! I guess we just have different priorities."
aj "Friendship is really important to me."

"I don't care, as long as I get what I want":
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
aj "I knew it! As soon as you walked in, I was like, I bet she's a model."
elladine "Yeah, I can't say I'm surprised either."
"Scientist":
aj "Oh wow, that's really cool!"
aj "It's not fair that someone as pretty as you gets to be smart as well."
"Musician":
elladine "I love musicians. If I find out one of the boys is in a band, I'm going to make a beeline straight for him."
"Athlete":
aj "Snap!"
aj "I knew I felt a connection with you as soon as you walked in here."


"Suddenly, you hear a beeping noise."
s03_mc "What was that?"
elladine "It sounded like a text…"
"AJ checks her phone and gasps."
aj "Oh, it's me!"
aj "I've got a text!"

# Text Message
"Girls, it's time to start meeting the boys.\n AJ, please make your way to the lawn and choose a boy to couple up with. Elladine and MC, stand by in the bedroom.\n You'll be up next! #girlmeetsboy #getthepartystarted"

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
"My type is…"
"Funny and cute":
s03_mc "I just want a boy to make me smile."
elladine "Aw, I hope you find him, babes."

"Smart and mature":
s03_mc "I agree with you. I need a guy with a good head on his shoulders."
elladine "Aw, I hope you find him, babes."

"Whatever, as long as they're hot":
s03_mc "Personality will never be as important as looks for me."
elladine "Ha, lucky for you!"

elladine "We won't have much time to chat before we choose, so we'll mostly be going off looks."
elladine "And speaking of boys…"
"She gestures to a box of condoms on a nearby table and giggles."
elladine "I guess we'll be needing a lot of those in the house, won't we?"


# CHOICE
menu:
"Am I going to need the condoms?"

"I'm not planning to have sex in here":
s03_mc "Don't get me wrong, I love having sex…but not on TV!"
s03_mc "I don't want all my family and friends to see me!"
elladine "Good point."
"I'll take one now, just in case":
"You take a single condom and hide it in your bikini for later."
"Elladine giggles again."
elladine "You go, girl!"
"Grab a whole handful":
"You take a fistful of condoms and stuff them down your top."
"Elladine giggles again."
elladine "You go, girl!"

elladine "I'm going to hold off for now."
elladine "I probably won't do any big bits right away…"
elladine "Unless the right guy comes along, obvs."
elladine "Text! I think that means it's my turn!"
"She gives you a quick hug before heading to the door."
elladine "Good luck, MC. I'll see you down there."
"She hurries towards the lawn, leaving you alone."
"There's still only three girls here!"
"I wonder when the others will be arriving?"
"You sit down on one of the beds. It's soft and springy."


# CHOICE
menu:
"These beds are really comfy…"

"Perfect for snuggling":
"I can't wait till find someone to cuddle up to."
"Perfect for doing bits":
"I'm gonna have so much fun, the whole Villa will shake."
"Maybe I'll take a nap…":
$ s3e1p1_took_a_nap = True
"Just a little one couldn't hurt…"
"You lay your head on the pillow and close your eyes."
"Maybe my Prince Charming will come and wake me with a kiss."
"You drift off for a few minutes, but then…"

"Your phone beeps."
"Wait, is it my turn already?"

"MC, come down to the lawn and couple up! The boys are waiting…"

"Alright, let's do this!"

"You step out into the brilliant sunshine."
"Waiting on the lawn are three boys, standing in a line."
"Elladine and AJ are off to the side, already paired up with their boys."
"Elladine shoots you an encouraging smile, and AJ gives you a thumbs up."

"Those two have already picked their boys…"
"Which leaves these three for me to choose from."
"I wonder which one I should pick?"

"The first boy steps forward with a cheeky smile."
bill "Alright, beautiful? I'm Bill."

# solo portrait shot of bill
"Bill\n
-24, from Surrey\n
-Roofer\n
-Strong opinions about sandwiches"

bill "I'm gonna come right out and say it. You look like a bit of me."


# CHOICE
menu:
"Bill says I'm a bit of him…"
"Smile politely":
"You smile at Bill, trying not to give too much away."
"I'm definitely in there."
"Wink at him":
"You shoot a wink in Bill's direction and his face lights up."
"Roll your eyes":
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
camilo "It's just, I think me and Bill had the exact same reaction…"
camilo "So I thought I should try and fancy it up a bit."

# CHOICE
menu:
"Camilo definitely likes me…"

"The feeling is mutual":
"You give Camilo a dazzlinig smile and feel the chemistry crackling between you two."
"I can't wait to get to know this one better."
"It's too early to say":
"You shrug and look away."
"More like Camil-no"
"Camilo deflates a little when he sees you're not into him."
camilo "Oh…"

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
"I think Harry's trying to flirt with me, too…"

"It's working!":
"You give Harry a flirty smile. He blushes hard."
"He's definitely got my attention."
"Bless his heart":
"Cute, but I'm not sure he knows what he's doing."
"Ugh, no thanks":
"You frown, leaving Harry looking embarrassed."

"Alright, so these three guys are my options for now."
"It seems like they're all keen."
"It's so tough to pick a boy when you know so little about them!"
"I know more boys might come in later in the series, and I'll get chances to change who I'm coupled up with…"
"…but for now, whoever I pick is the person I'm probably going to spend the most time with early on."
"I hope they're all as good as they seem!"

# CHOICE (appends who you're coupled up with to list)
# add screen that shows the 3 guys lined up, full body profile shot, and you click on the one you want
menu:
"Who should I couple up with?"

"Bill":
$ s3_coupled_up_with.append("Bill")
s03_mc " The boy I want to couple up with is… Bill!"
"You stride over to Bill."
"He grins like he can't hardly believe his luck."
bill "Nice one."

"Camilo":
$ s3_coupled_up_with.append("Camilo")
s03_mc " The boy I want to couple up with is… Camilo!"
"You stride over to Camilo."
"He grins like he can't hardly believe his luck."
camilo "Nice one."

"Harry":
$ s3_coupled_up_with.append("Harry")
s03_mc " The boy I want to couple up with is… Harry!"
"You stride over to Harry."
"He grins like he can't hardly believe his luck."
harry "Nice one."

menu:
"Me and [s3_coupled_up_with[-1]] are officially coupled up…"

"Hug him":
"As you reach him, you throw your arms around his shoulders."
"He hugs you back firmly. His hands are warm on the small of your back."
"Kiss his cheek":
"As you reach him, you plant a kiss on his cheek, being careful not to smudge your lipstick."
"Hands off for now"
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
"AJ doesn't sound so convinced about her guy…"
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
"The last two girls…"
"I can't wait to meet them":
s03_mc " We're not a complete Villa crew until everyone's here."
aj " Right! I'm so excited for them to get here!"
nicky "You're not the only ones."
"Nicky looks over at the two remaining single boys."

"They better stay away from [s3_coupled_up_with[-1]]":
nicky "Wow! So committed already, huh?"
# IF STATEMENT
if s3_coupled_up_with[-1] == "Bill":
bill "I kinda like it."
bill "It's nice to know MC is feeling it so strongly."
bill "I mean, if another boy came in right now and tried to couple up with her, I'd have a thing or two to say about it, as well."
elif s3_coupled_up_with[-1] == "Camilo":
camilo "I kinda like it."
camilo "It's nice to know MC is feeling it so strongly."
camilo "I mean, if another boy came in right now and tried to couple up with her, I'd have a thing or two to say about it, as well."
elif s3_coupled_up_with[-1] == "Harry":
harry "I kinda like it."
harry "It's nice to know MC is feeling it so strongly."
harry "I mean, if another boy came in right now and tried to couple up with her, I'd have a thing or two to say about it, as well."

"[s3_coupled_up_with] looks over at the two remaining single boys."

"Maybe they got lost on the way here":
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

aj " I feel bad for them. Nobody wants to get picked last."
elladine " Yeah, and it's pretty obvious they both wanted to get picked by MC…"
aj " Well, maybe their perfect soulmates are about to walk out of that door any second."
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
s03_mc " I can't wait for whatever's on the horizon!"
nicky "That's the spirit."
"I don't believe in magic":
s03_mc " If we're gonna have fun in the Villa, it won't be from magic."
s03_mc " It'll be from hard grafting."
seb "You've got that right."
"My dreams are too weird":
s03_mc " If they manage to make my dreams come true, I'll be impressed. (you get  with Nicky and Seb)"
s03_mc " Could they even fit a T-Rex in here?"

"Everyone falls silent as a new girl emerges from the Villa."

# miki bill
# iona camilo
# genevieve harry

# IF STATEMENT
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
miki "But now I see the two beautiful boys you've left for me to choose from…"
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
harry "Er, I mean…"
harry "Harry. It's Harry."
genevieve "Lovely to meet you, Harry."
genevieve "How lucky am I that nobody got to you before me?"
"She goes over to give him a hug."
"The two of them come to stand with you, Camilo and the other couples."


# CHOICE
menu:
"They've made an impression on each other already…"

"It's really cute":
"I hope me and [s3_coupled_up_with[-1]] get on as well as they do!"
"It's probably not real":
"It's not like they really know each other…"
"They're probably just showing off."
"I'd be the filling in that sandwich":
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
"Based on first impressions, I think the strongest couple here will be…"

"Me and [s3_coupled_up_with[-1]]":
# IF STATEMENT
if s3_coupled_up_with == "Bill":
bill "Not to bang my own drum or anything, but hard agree."
elif s3_coupled_up_with[-1] == "Camilo":
camilo "Not to bang my own drum or anything, but hard agree."
elif s3_coupled_up_with[-1] = "Harry":
harry "Not to bang my own drum or anything, but hard agree."

elladine " I can't lie, you two do look super cute together."

"Miki and Bill" if "Miki" in s3_amount_npcs_like_mc:
$ s3e1p1_strongest_couple = "Miki and Bill"
"Iona and Camilo" if "Iona" in s3_amount_npcs_like_mc:
$ s3e1p1_strongest_couple = "Iona and Camilo"
"Genevieve and Harry" if "Genevieve" in s3_amount_npcs_like_mc:
$ s3e1p1_strongest_couple = "Genevieve and Harry"
"Elladine and Nicky":
elladine " Aw, babes."
"AJ and Seb":
aj " Wow, really? (you get  with AJ)"
seb "That's, um… sweet of you to say."

# IF STATEMENT
if s3e1p1_strongest_couple == "Miki and Bill" or s3e1p1_strongest_couple == "Iona and Camilo" or s3e1p1_strongest_couple == "Genevieve and Harry":

if s3_coupled_up_with[-1] == "Bill":
bill "Stronger than you and me?"
elif s3_coupled_up_with[-1] == "Camilo":
camilo "Stronger than you and me?"
elif s3_coupled_up_with[-1] == "Harry":
harry "Stronger than you and me?"

s03_mc " I'm just being honest."

# IF STATEMENT
if s3_coupled_up_with[-1] == "Bill":
iona "All I meant was, it might be a competition, but it doesn't really matter who wins."
iona "We're all just here to find love, right?"
elif s3_coupled_up_with[-1] == "Camilo" or s3_coupled_up_with[-1] == "Harry":
miki "All I meant was, it might be a competition, but it doesn't really matter who wins."
miki "We're all just here to find love, right?"


# CHOICE
menu:
"I'm here…"
"To win the game":
s03_mc "Don't get me wrong, we all want to find someone…"
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
s03_mc "She's right. At the end of the day, all that matters is finding the right person for you."
s03_mc "That's the only prize worth winning, really."

# IF STATEMENT
if s3_coupled_up_with[-1] == "Bill":
iona "Wow, yes. MC just said it better than I ever could."
elif s3_coupled_up_with[-1] == "Camilo" or s3_coupled_up_with[-1] == "Harry":
miki "Wow, yes. MC just said it better than I ever could."

-To have fun
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
camilo "Well, that too, I guess…"
bill "Don't get me wrong. I've got nothing to hide."
bill "But I'm excited to find out what the rest of you are holding back."
harry "That's true, but we're not just here to mess around and relax, or dig up gossip on each other."
aj "We're not?"
harry "No! We're here on an important mission! To find someone we love. It's serious business."
harry "The challenge will focus our minds and get us ready for the road ahead."


# CHOICE
menu:
"Doing the challenge is mostly about…"

"Getting closer as a group":
$ s3_amount_npcs_like_mc["Camilo"] += 1
s03_mc "Camilo's right. This challenge sounds like a great way to get to know each other."
s03_mc "This is what it's all about! I bet it's going to be a right laugh."
"Uncovering everyone's secrets":
$ s3_amount_npcs_like_mc["Bill"] += 1
s03_mc "Bill's right. This is a great chance to expose all our best and worst stories."
s03_mc "I bet we've all got some really juicy ones, too."
"Bringing out my competitive side":
$ s3_amount_npcs_like_mc["Harry"] += 1
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
"Before you can follow, [s3_coupled_up_with[-1]] quietly takes you to one side."

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
"[s3_coupled_up_with[-1]] wants a chat…"

"I thought you'd never ask":
$ s3e1p1_li_wants_chat_response = "Positive"
call s3e1p1_cheeky_snog_before_game

"Sure, what's up.":
call s3e1p1_cheeky_snog_before_game

"I'd rather just get going.":
$ s3e1p1_li_wants_chat_response = "Negative"
call s3e1p1_cheeky_snog_before_game

label s3e1p1_cheeky_snog_before_game:
# IF STATEMENT
# Bill LI
if s3_coupled_up_with[-1] == "Bill":
if s3e1p1_li_wants_chat_response == "Positive":
$ s3_amount_npcs_like_mc["Bill"] += 1
bill "Well, I'm asking now."
elif s3e1p1_li_wants_chat_response == "Negative":
$ s3_amount_npcs_like_mc["Bill"] -= 1
bill "Sorry, I'll try to make it quick."
else:
bill "Well…"

bill "I just wanted to say thank you for choosing me."
bill "You could probably see it on my face, but you absolutely made my day."
bill "You're blatantly the best-looking girl here."
bill "And I'm no expert, but even I can see you're the best-dressed, too."

# CHOICE
menu:
"This would be the perfect opportunity.."
"Go in for a cheeky snog":
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
bill "Did I like it? Did I like it? MC…"
bill "I loved it."
bill "Do you think we could do it again? Like, right now?"
s03_mc "All in good time, babe."

"Maybe later":
"There's no rush. I only just got here."

bill "You seem like a girl who says what's on her mind, and I really admire that."
bill "I don't do subtlety, see. Whether I like someone or I don't like someone, I come right out and say so."

# Camilo LI
elif s3_coupled_up_with[-1] == "Camilo":
if s3e1p1_li_wants_chat_response == "Positive":
$ s3_amount_npcs_like_mc["Camilo"] += 1
camilo "Well, I'm asking now."
elif s3e1p1_li_wants_chat_response == "Negative":
$ s3_amount_npcs_like_mc["Camilo"] -= 1
camilo "Sorry, I'll try to make it quick."
else:
camilo "Well…"

camilo "I just wanted to say thank you for choosing me."
camilo "You could probably see it on my face, but you absolutely made my day."
camilo "You're blatantly the best-looking girl here."
camilo "And I'm no expert, but even I can see you're the best-dressed, too."

# CHOICE
menu:
"This would be the perfect opportunity.."
"Go in for a cheeky snog":
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
camilo "Did I like it? Did I like it? MC…"
camilo "I loved it."
camilo "Do you think we could do it again? Like, right now?"
s03_mc "All in good time, babe."

camilo "And I don't just mean looks-wise. I think we've got that spark, you know?"
camilo "It makes me wanna know everything there is to know about you."

# Harry LI
elif s3_coupled_up_with[-1] == "Harry":
if s3e1p1_li_wants_chat_response == "Positive":
$ s3_amount_npcs_like_mc["Harry"] += 1
harry "Well, I'm asking now."
elif s3e1p1_li_wants_chat_response == "Negative":
$ s3_amount_npcs_like_mc["Harry"] -= 1
harry "Sorry, I'll try to make it quick."
else:
harry "Well…"

harry "I just wanted to say thank you for choosing me."
harry "You could probably see it on my face, but you absolutely made my day."
harry "You're blatantly the best-looking girl here."
harry "And I'm no expert, but even I can see you're the best-dressed, too."

# CHOICE
menu:
"This would be the perfect opportunity.."
"Go in for a cheeky snog":
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
harry "Did you like it?"
harry "Did I like it? Did I like it? MC…"
harry "I loved it."
harry "Do you think we could do it again? Like, right now?"
s03_mc "All in good time, babe."


harry "Well…"
harry "Obviously we've only really got a first impression to go on at the moment."
harry "But I already feel like you're exactly my type on paper."
harry "I'm over here trying to act all manly and confident, and then you walk in, and it all just…melts away."
harry "And the weird thing is, I don't even mind."


## left off here

H/B/camilo "So, yeah."
H/B/camilo "Obviously I won't try anything on if you're not interested, but I didn't want today to go any further without saying…"
H/B/camilo "I'm excited to start getting to know you."
Choiceseb "Harry/Bill/Camilo wants to get to know me…"
-I'm excited to get to know you, too
s03_mc " I picked you for a reason. I can't wait to see where it leads us. (you get 😍 with Harry/Bill/Camilo)"
H/B/camilo "I'm glad you said that."

-I'm not really interested, sorry
s03_mc " Look, no offence…"
s03_mc " But just because I liked you better than the other two, that doesn't mean I actually like you. (you get 🙁 with Harry/Bill/Camilo)"
H/B/camilo "Oh…OK. I'm sorry."
H/B/camilo "I just assumed…"
H/B/camilo "I'll try to keep that in mind."

-Let's wait and see how this goes
s03_mc " It's still early days."
H/B/camilo "Yeah, of course."

If you picked `Grab a whole handful' (condoms) in the bedroom there is a fourth choicelladine ""
-Show him the condoms
You pull your bikini top out a bit and nod.
s03_mc " Check this out."
H/B/camilo "Uh, alright…?"
Tentatively, he peers down inside.
He lets out a sharp laugh when he sees the stash of condoms there. (you get 😂 with Harry/Bill/Camilo)
H/B/camilo "That's certainly not what I was expecting to see."
H/B/camilo "Are you trying to send me a message?"
Only bill "Because I already told you, I don't do subtlety."
s03_mc " I'm not trying to say anything."
s03_mc " I'm just a girl with a top full of condoms, and I thought you ought to know."
s03_mc " Seeing as we're being honest with each other right now."
H/B/camilo "Amazing."

H/B/camilo "Well, I guess the others must be wondering where we've got to."
H/B/camilo "Let's head over for the challenge!"

Choiceseb "We should go and meet the others at the challenge platform…"
-Yep, let's go
s03_mc " I hope they haven't started without us!"

-Race you!
s03_mc " Last one there has to clean the pool!"
H/B/camilo "Wait, wh…"
You're already off and running.
Seconds later, you hear him laugh, then the sound of his bare feet on the grass as he gives chase.

-Why don't you carry me?
H/B/camilo "Carry you?"
s03_mc " That's what I said."
s03_mc " You can do it, right? Or are these muscles just for show?"
(Only B/Cam)He smirks and flexes his impressives arms.
(Only Harry): Muscles?
(Harry) He looks down at his arms and gives them an optimistic flex.
H/B/camilo "Of course I can do it. Just watch."
(Only Harry) He stretches a bit more, positions himself carefully, then scoops you up in his arms.
(Only Harry) He's stronger than he looks.
(Only B/Cam) He puts one hand on your back, scoops the other under your legs, and effortlessly sweeps you off your feet.
H/B/camilo "To the challenge platform, m'lady?"
s03_mc " To the challenge platform at once!"
He sets off, carrying you bridal-style across the lawn.

" It's only day 1, and MC is already turning heads all over the Villa!"
(If you choose the gem choice to kiss your partner)
" I think that snog might be one for the record books."
" Five minutes from first sight to first kiss?"
" The other girls will never catch up!"
" She's coupled up with Harry/Bill/Camilo for now, but who knows what could happen at this afternoon's challenge?"
elladine " We've got to kiss the boy we think the clue is about."
M (MC coupled with Harry/Camilo)/ G (MC coupled with Bill): I can't believe how big that is…




#########################################################################
## Episode 1, Part 2
#########################################################################

#########################################################################
## Episode 1, Part 3
#########################################################################

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