

define k = Character("Kim")
define you = Character("You")

# The game starts here.

label start:
    show bg mojave1

    "War... war never changes."
    "You are a time traveler from the year 2500."
    "You have been assigned a grave task..."
    "...one that will decide the fate of the planet Earth for centuries to come."
    show bg destroyed1
    show boss main:
        zoom 5.0
        xalign 0.5
        yalign 0.6
    k "Your task is to travel back to the year 2281, to the Mojave Wasteland."
    k "There, you will travel to New Vegas, and prevent Courier Six from killing Benny Gecko."
    k "If you fail, the chain of events resulting from his survival will cause the devastation that we see today."
    k "Do you accept this task?"
    menu:
        "Yes, I accept.":
            k "Then your journey begins now."
            jump saidyespath
        "No thanks, not for me.":
            k "Very well then, we'll find someone else to do it."
            hide boss main
            "GAME OVER"
    
    return
label saidyespath:
    show bg destroyed1
    show boss main:
        zoom 5.0
        xalign 0.5
        yalign 0.6
    k "We have no time to waste. We wish you luck."
    hide boss main
    "You step into the time machine and brace yourself for what lies ahead."
    show boss main:
        zoom 5.0
        xalign 0.5
        yalign 0.6
    k "Oh, one more thing, if you fail this mission, you're not allowed to come back."
    hide boss main
    "You feel comforted by your supportive employer."
    show bg mojave1
    with dissolve
    "Wow, this is it, the Mojave Wasteland."
    "I've heard so much about it."
    define s = Character("Sunny")
    show sunny main:
        zoom 5.0
        xalign 0.5
        yalign 0.6
    s "Who are you and what are you doing in my town?"
    "You're taken aback by her abruptness. Aren't westerners supposed to be nice?"
    "You notice the multitude of firearms that she's carrying."
    you "Umm... I'm looking for New Vegas."
    s "Ugh. All these damn tourists come through our town on the way to the Strip and trash the place."
    you "I'm not a tourist, I'm just here on business."
    s "You and that other guy that just came through."
    you "Other guy?"
    s "Yeah, some guy came out of Doc Mitchell's house asking about some guy in a checkered suit."
    you "Did he say where he was headed?"
    s "What's it to you?"
    you "I just have something really important I need to speak with him about."
    s "*Sigh*"
    s "He's headed for the Tops casino on the Vegas Strip."
    you "Can you please direct me to New Vegas?"
    s "Well..."
    s "You can either go down and around through Primm, Nipton, and Novac..."
    s "Or, you could go directly north through Quarry Junction."
    s "But I'd try to steer clear of the Deathclaws and Cazadores."
    menu:
        "Take the longer, safer path":
            s "Good call."
            hide sunny main
            jump longWay
        "Take the shorter, dangerous path":
            s "It's your funeral."
            hide sunny main
            jump quarryWay
            hide sunny main
label quarryWay:
    show bg black
    "You make quick progress towards the New Vegas strip."
    "However, you do not progress quickly enough."
    "First, you are stung by the giant venomous wasps they call Cazadores."
    "Then, in your dizziness, you stumble into Quarry Junction, the breeding ground for the giant reptilian Deathclaws."
    "I mean, do they really need a description? They're called DEATH-CLAWS."
    "While you face your tragic demise, you ask yourself--"
    you "Why didn't I just choose the long way?"
    "GAME OVER"
    return
define ncr = Character("NCR Agent")

label longWay:
    show bg mojave2
    "You make steady progress through the Mojave desert."
    show ncragent first:
        zoom 5.0
        xalign 0.5
        yalign 0.6
    ncr "Patrolling the Mojave almost makes you wish for a nuclear winter."
    you "Uh, haha yeah, I feel ya there."
    show ncragent first:
        zoom 6.0
        xalign 0.5
        yalign 0.6
    ncr "Patrolling the Mojave almost makes you wish for a nuclear winter."
    you "Umm, yep. I got it the first time you said it."
    show ncragent first:
        zoom 8.0
        xalign 0.5
        yalign 0.6
    ncr "Patrolling the Mojave almost makes you wish for a nuclear winter."
    hide ncragent first
    "You flee."
    show bg mojavenight1:
        zoom 3.0
    with dissolve
    "You spend hours walking through the Mojave desert."
    define guy = Character("Primm Resident")
    show primmguy main:
        zoom 5.0
        xalign 0.5
        yalign 0.6
    guy "Hey you! Stop!"
    you "Me?"
    guy "Yes you! It's dangerous to keep walking on this road alone."
    you "Why not?"
    guy "Further down this road are the powder gangers: a gang of dynamite slinging criminals who attack everyone they see."
    guy "It's not safe to go at night, you're better off staying at the Vicki and Vance casino here in Primm and waiting until morning."
    you "I'm kinda on a time crunch... deciding the fate of the world as we know it and stuff."
    you "Besides, I don't have much money on me..."
    guy "Listen, you can stay free of charge, no bottle caps necessary."
    guy "But you have to decide now, it's not safe for me to be out here."
    menu:
        "Spend the night in Primm":
            guy "Great, come with me."
            hide primmguy main
            jump stayinPrimm
        "Continue on through the night":
            you "I don't have time to waste!"
            hide primmguy main
            jump skipPrimm
label skipPrimm:
    show bg black
    "You push forward. The courier could already be at the Tops casino by now!"
    you "I see nothing on this road I need to worry about. I think that guy just wanted me to spend money in his casino."
    "But, you spoke too soon."
    "BOOM!!! EXPLOSION!!!"
    "You were no match for the firepower of the powder gangers."
    you "Why didn't I just choose the obviously correct path?!?!?"
    "GAME OVER"
    return
label stayinPrimm:
    show bg black
    "You play a little bit of blackjack and end up with 1000 caps! With that, you retire to your room."
    "In your bed, you sleep soundly through the night, almost forgetting the existential horror of your situation."
    you "ZZZZZZZZZZZZ"
    show boss main:
        zoom 5.0
        xalign 0.5
        yalign 0.6
    k "It's Kim! I'm contacting you through your dream!"
    k "We can't believe you're still alive! I mean, obviously I never doubted you for a second, haha."
    k "Listen, you need to hurry. You only have a limited window of time in which the return travel works."
    k "We can't have you dilly-dallying at casinos!!!"
    k "Alright bye, and good luck, because you know what happens if you fail your mission!"
    hide boss main
    show bg mojave1
    with dissolve
    you "Geez, what a weird dream."
    you "I wonder if she's serious, that I actually won't be allowed back if I fail."
    "With that in mind, you make your way out of Primm, and towards your next stop, Nipton."
    define legion = Character("Legion Member")
    show legion first:
        zoom 5.0
        xalign 0.5
        yalign 0.6
    legion "HALT, STRANGER!"
    "You are confronted by a man wearing what seems to be a bicycle helmet with a broom on top."
    "He is adorned in football gear spray painted to look gold."
    you "What a dork!"
    legion "State your business in Legion territory."
    "You try your best to match his cadence."
    you "Uhhh... I come in peace. I am a traveler new to the area."
    legion "Not satisfactory. State your allegiance to the Legion."
    you "Well, could you at least tell me what I'm pledging allegiance to?"
    you "Like, what does the Legion even do? What are its values."
    legion "Of course. The Legion is a military group run by Caesar."
    legion "We believe in enslaving women, murdering innocent people, and ruling the Mojave with an iron fist."
    legion "So, would you like to join?"
    menu:
        "Wow, that sounds awesome! Sign me up.":
            hide legion first
            jump joinCL
        "No way! I'm not joining that!":
            hide legion first
            jump dontJoinCL
label joinCL:
    show bg black
    "Wow, you really chose the Legion? Really?"
    "I mean, I thought people who supported the Legion were just trolling..."
    "Like, you were presented with the option to participate in slavery and murder,"
    "And you just... did it? Without a second thought?"
    "Anyways, back to the story."
    "You join the Legion and are sentenced to a life of slavery and suffering."
    "Because, like, that was obviously the Bad Choice."
    "GAME OVER"
    ">:("
    return
label dontJoinCL:
    show bg mojave1
    "You flee, because you are obviously not joining that group."
    you "Haha, wow. Only a psychopath would support the Legion!"
    "Finally, after a long day of traveling, you see it. The Vegas strip!"
    define lee = Character("Lee")
    show indialee main:
        zoom 5.0
        xalign 0.5
        yalign 0.6
    you "Excuse me ma'am, how can I get into the Vegas strip from here?"
    lee "The easiest way is to go right up to the gate with your passport."
    you "But I don't have a passport! I'm not from around here."
    lee "Well... I can think of a few things you could try."
    lee "You could either take the MonoRail in Camp McCarran, the NCR military base."
    lee "Or, you could go into Freeside and get a passport. But it's going to cost you."
    lee "Finally, you could try a bit of a hail mary, and just rush past the guards at the gate."
    lee "But, I don't recommend that last option. The guards will destroy anyone who tries."
    menu:
        "Go through Camp McCarran":
            hide indialee main
            jump campMc
        "Try to get a passport":
            hide indialee main
            jump passport
        "Go in guns blazing!":
            hide indialee main
            jump hailMary
label hailMary:
    show bg black
    you "Alright... I got this! Just rush past the guards!"
    "What the friendly bystander neglected to mention to you was that the guards were huge robots with lasers."
    "Need I say more?"
    "GAME OVER"
    return
label campMc:
    show bg black
    "You sneak through the NCR military base and make your way to the train."
    "The MonoRail ride quickly transports you to the New Vegas strip."
    "How come everyone doesn't use public transportation?"
    jump onTheStrip
label passport:
    show bg black
    "In Freeside, you spend the 1000 bottle caps you gained from the casino in Primm to purchase a counterfeit passport."
    you "Wow, gambling really did help me out! I should do it more often!"
    "Your passport works without issue, and you make your way to the strip."
    jump onTheStrip
label onTheStrip:
    show bg vegasnight
    you "Wow... fabulous New Vegas!"
    "You want to admire the scantily clad women walking around, but you have no time to waste."
    "You rush to the Tops casino, where you meet the two objects of your quest."
    define co = Character("Courier")
    define b = Character("Benny")
    define cob = Character("Courier and Benny")
    show bg tops
    show benny main:
        zoom 5.0
        xalign 0.2
        yalign 0.6
    show courier main:
        zoom 5.0
        xalign 0.7
        yalign 0.6
    you "WAIT!!! Courier six, don't kill Benny!"
    "You burst into the doors right as the Courier is drawing his handgun."
    cob "Who the hell are you?"
    you "Please, I know it sounds crazy, but I'm a time traveler from the future."
    you "Courier Six, what you're about to do will doom not just the Mojave, but the entire world."
    co "Yeah right. Time travel isn't real."
    b "Uhhhh.... I for one think you should hear them out!"
    co "Well of course you do."
    co "So, why shouldn't I kill this guy who already tried to kill me?"
    co "Like, what will happen if he dies?"
    you "Um... I'm not quite sure actually. My boss didn't really tell me."
    you "I just know that the fate of the world depends on you not killing Benny!"
    co "Real compelling argument. Do you have anything else to say before I do the exact opposite of what you want me to do?"
    b "AHHHHHHH"
    you "Listen, I just do what my boss tells me to. If I don't stop you from killing Benny, I won't be allowed back to the future."
    co "Doesn't sound like a very nice boss."
    co "Is that really the person you want to take orders from?"
    you "..."
    co "You know what? Here."
    "The Courier hands you his gun."
    co "Do what you think is right."
    b "Please please please don't kill me!!!"
    b "Kill him!!!"
    "Your journey has led you to a difficult decision."
    "What will you do? Will you follow your original orders, and kill the Courier?"
    "Or, will you stray from your path and kill Benny, knowing you won't be allowed home?"
    menu:
        "Kill Benny":
            hide courier main
            jump killBenny
        "Kill Courier":
            hide benny main
            jump killCourier
label killBenny:
    hide benny main
    show bg tops
    show courier main:
        zoom 5.0
        xalign 0.5
        yalign 0.6
    co "I knew you'd make the right choice."
    you "But... I won't be able to go home."
    co "Listen kid..."
    co "I hate to be the bearer of bad news, but did you really think they were ever intending on letting you go home?"
    co "I've learned a lot in my days of being a courier, and one thing I haven't forgotten is that people will do anything to make you do what they want."
    you "You know what... maybe you're right. But I still don't understand why they wanted me to kill you in the first place."
    co "I think I know."
    co "My journey, exploring the epic Fallout ... here in New Vegas, it was so good that society expected the future of the nuclear Fallout to be just as good."
    co "But, in comparison to my epic journey, the future of the nuclear Fallout falls flat in comparison."
    co "My existence probably makes your world look bad in comparison."
    you "But... President Todd Howard says that our world just works!"
    co "I'm sorry to hear that."
    co "But there is a good side to this."
    you "Oh yeah? What?"
    co "Because you chose to save my life, you get to spend the rest of your life exploring the Mojave with me."
    co "Only if you want to of course."
    you "Yes!"
    hide courier main
    show bg black
    "The End"
    return
label killCourier:
    hide courier main
    show bg tops
    show benny main:
        zoom 5.0
        xalign 0.5
        yalign 0.6
    b "Phew! Thanks kid! I thought I was a goner!"
    b "Welp, see ya!"
    hide benny main
    "Benny disappears. Hm. He seems a little unappreciative considering you basically just saved his life."
    you "Oh well, it's time to go home!"
    you "Hey Kim!!! I'm ready to go home."
    "You hear Kim's voice in your earpiece."
    k "Haha, this is awkward!"
    k "Sooo... thanks for everything you've done to help us out in the future!"
    k "However, I have some bad news. Bad for you at least, I don't really care."
    k "You can't come back. In fact, you never could have come back."
    you "What?"
    k "Yeah, like I said, awkwarddddd!"
    k "We only told you that so you'd be more motivated to carry out the job."
    k "You really thought we had the technology to bring people back?"
    you "Well, I mean, you have the technology to send people to the past so, yeah."
    k "I say, just enjoy the nice desert weather. Maybe get a tan. I don't care!"
    k "Byeee!"
    you "And just like that, you were destined to live out the rest of your life in the Mojave wasteland."
    show bg black
    "The End"
    return