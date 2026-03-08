# ------------------------------------------------------------------------------
music = Sound("Fallen down cover piano.mp3")
keepPlaying = True
music.play()
scene = "BEGINNING"

while keepPlaying:
    if scene == "BEGINNING":
        clear()
        setConsoleSize(LARGE_SCREEN)
        clear()
        setTextColour(234, 245, 174)
        print(r'''
        ⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢀⣀⣀⣀⣀⣀⣀⣠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣄⣀⣀⣀⣀⣀⣀⡀⠀⠀
⠀⠀⢠⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⣤⡄⠀⠀
⠀⠀⣿⣿⣿⣿⣿⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⢹⣿⣿⣿⣿⡟⣿⣿⣿⣿⣿⠀⠀
⠀⠀⣿⣿⣿⣿⡟⢸⣿⣿⣿⣿⢹⣿⣿⣿⣿⡘⣿⣿⣿⣿⡇⢻⣿⣿⣿⣿⠀⠀
⠀⢀⣛⣛⣛⣛⠃⣛⣛⣛⣛⡋⠈⣛⣛⣛⣛⠁⢛⣛⣛⣛⣛⠘⣛⣛⣛⣛⡀⠀
⠀⠈⠻⠿⠿⠋⣀⠈⠻⠿⠟⢁⡀⠙⠿⠿⠋⢀⡈⠻⠿⠟⠁⣀⠙⠿⠿⠟⠁⠀
⠀⢸⣷⣦⣶⣿⣿⣿⣶⣤⣶⣿⣿⣷⣦⣴⣾⣿⣿⣶⣤⣶⣿⣿⣿⣶⣴⣾⡇⠀
⠀⢸⣿⡏⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⣉⡉⢹⣿⠉⣉⣉⣉⣉⣉⢹⣿⡇⠀
⠀⢸⣿⡇⣿⠉⢉⣩⣭⣽⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⠀⣿⣿⣿⣿⣿⢸⣿⡇⠀
⠀⢸⣿⡇⣿⢀⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⠀⠿⠿⠿⠿⠿⢸⣿⡇⠀
⠀⢸⣿⡇⣿⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢸⣿⠀⠶⠶⠶⠶⠶⢸⣿⡇⠀
⠀⢸⣿⡇⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⢸⣿⠀⣶⣶⣶⣶⣶⢸⣿⡇⠀
⠀⢸⣿⣷⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣾⣿⠀⣿⣿⣿⣿⣿⢸⣿⡇⠀
⠀⠈⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠉⠀⠉⠉⠉⠉⠉⠈⠉⠁⠀
         WELCOME TO IVY PETS!
        ''')
        setTextColour(WHITE)
        sleep(3)
        print("Welcome to Ivy's Pets")
        sleep(4)
        print("Here, you can adopt a variety of pets,")
        sleep(2)
        print("all in need of finding love and care in a new home!")
        sleep(4)
        input(" Press Enter Key to enter shop!")
        scene = "INSIDESHOP"
        continue

    elif scene == "INSIDESHOP":
        clear()
        setTextColour(211, 245, 174)
        print("You enter the shop to see the following pets:")
        setTextColour(WHITE)

        print("Option 1:")
        print(r'''     ╱|、
    (˚ˎ 。7  
    |、˜〵          
    じしˍ,)ノ 
    CAT
    ''')

        print("Option 2:")
        print(r'''
     ︵ 
  ૮(`ᴥ ⁻ 𑁬
   |    ⸝ 〵
   じしˍ,  )୭
    DOG''')

        print("Option 3:")
        print(r'''.         ⊹ ₊
    __  ♡
⊂⊂  • )  
/     | 
⊂_﹏u
RABBIT
    ''')

        print("Option 4:")
        print(r'''<￣｀ヽ　　              ／￣＞ 
　ゝ、　＼　 ／<>ヽ,ノ　 /´ 
    ゝ、　`꒰˶• ▾ •˶꒱ ／   
　　　　  　>　　 ノ  
          --''--''--
OWL
    ''')

        sleep(1)
        Pet = input(" Which option will you go with? (enter number only):  ").strip()

        if Pet == "1":
            scene = "CATCHOICE"
        elif Pet == "2":
            scene = "DOGCHOICE"
        elif Pet == "3":
            scene = "RABBITCHOICE"
        elif Pet == "4":
            scene = "OWLCHOICE"
        else:
            print("You can only continue if you say a number from 1-4!")
            setTextColour(GREEN)
            input("Press [ENTER] to continue.")
            setTextColour(WHITE)
        continue

    elif scene == "CATCHOICE":
        clear()
        setTextColour(CYAN)
        print("You've adopted your Cat")
        PetName = input("What will you name your cat? ").strip() or "Kitty"
        setTextColour(WHITE)
        print(f"\n{PetName} purrs happily. 🐱")

        input("What do you want to do with your cat? <press enter to continue>  ")
        ChoiceCatOne = input("Play (1) Walk (2) Feed (3) Pat (4): ").strip()

        if ChoiceCatOne == "1":
            print("Your Cat is joyful right now. Joy is 5/5 now.")
            print(r'''
          へ  ♡       
         ૮  >  <) 
         /  ⁻  ៸|                                                                                      
      乀(ˍ, ل ل   ''')
            sleep(2)
            print("Joy level: ♡ ♡ ♡ ♡ ♡ ")
            print("Hunger Level:🍗🍗🍗🦴🦴")

            HungerChoice = input(f"Oh no, {PetName} is hungry! Feed them (1) Ignore hunger (2): ").strip()

            if HungerChoice == "1":
                WhatFood = input("What will you give them? Dog Food (1), Candy (2), Cat Food (3): ").strip()
                if WhatFood == "1":
                    print("Oh no, your cat's sick with heart disease and died!")
                    sleep(5)
                    scene = "GAMEOVER"
                elif WhatFood == "2":
                    print("You've just poisoned your cat and they've died!")
                    sleep(5)
                    scene = "GAMEOVER"
                elif WhatFood == "3":
                    print("You've fed your cat some cat food and now hunger bar is full!")
                    print("Status: Joy level: ♡ ♡ ♡ ♡ ♡ ")
                    print("Hunger Level: 🍗🍗🍗🍗🍗")
                    sleep(4)
                    scene = "ENDINGDAY"
                else:
                    print("That wasn't a valid choice. Your cat waited too long and starved...")
                    sleep(5)
                    scene = "GAMEOVER"

            elif HungerChoice == "2":
                print("Oh no, your pet starved too long and has died!")
                sleep(5)
                scene = "GAMEOVER"
            else:
                print("Your cat looks confused... (invalid choice)")
                sleep(5)
                scene = "GAMEOVER"

        elif ChoiceCatOne == "2":
            print("You've taken your pet cat for a walk, joy level: ♡ ♡ ♡ ♡ ❤  Hunger level:🍗🍗🦴🦴🦴")
            sleep(2)
            HungerChoice = input(f"Oh no, {PetName} is hungry! Feed them (1) Ignore hunger (2): ").strip()

            if HungerChoice == "1":
                WhatFood = input("What will you give them? Dog Food (1), Candy (2), Cat Food (3): ").strip()
                if WhatFood == "1":
                    print("Oh no, your cat's sick with heart disease and died!")
                    sleep(5)
                    scene = "GAMEOVER"
                elif WhatFood == "2":
                    print("You've just poisoned your cat and they've died!")
                    sleep(5)
                    scene = "GAMEOVER"
                elif WhatFood == "3":
                    print("You've fed your cat some cat food and now hunger bar is full!")
                    print("Status: Joy level: ♡ ♡ ♡ ♡ ♡ ")
                    print("Hunger Level: 🍗🍗🍗🍗🍗")
                    sleep(4)
                    scene = "ENDINGDAY"
                else:
                    print("That wasn't a valid choice. Your cat waited too long and starved...")
                    sleep(5)
                    scene = "GAMEOVER"
            elif HungerChoice == "2":
                print("Oh no, your pet starved too long and has died!")
                sleep(5)
                scene = "GAMEOVER"
            else:
                print("Your cat looks confused... (invalid choice)")
                sleep(5)
                scene = "GAMEOVER"

        elif ChoiceCatOne == "3":
            print("You've fed your cat. Joy: ♡ ♡ ♡ ♡ ♡  | Hunger: 🍗🍗🍗🍗🍗 ")
            sleep(3)
            scene = "ENDINGDAY"
        elif ChoiceCatOne == "4":
            print("Your cat is overjoyed! Joy: ♡ ♡ ♡ ♡ ♡ ")
            sleep(3)
            scene = "SECRETENDINGCAT"
        else:
            print("That wasn't a valid action. Let's try again next time.")
            sleep(3)
            scene = "GAMEOVER"
        continue

    elif scene == "DOGCHOICE":
        clear()
        setTextColour(CYAN)
        print("You adopted a Dog!")
        PetNameDog = input("What would you like to name your dog? ").strip() or "Doggo"
        setTextColour(WHITE)
        print(f"\n{PetNameDog} barks happily. ")

        input("What do you want to do with your dog? <press enter to continue>  ")
        ChoiceDogOne = input("Play (1) Walk (2) Feed (3) Pat (4): ").strip()

        if ChoiceDogOne == "1":
            setTextColour(161, 201, 153)
            print("Your Dog is joyful right now. Joy is 5/5 now.")
            print(r'''
            ૮˶• ﻌ •˶ა
            ./づ~ 🦴''')
            sleep(2)
            setTextColour(WHITE)
            print("Joy level: ♡ ♡ ♡ ♡ ♡ ")
            print("Hunger Level:🍗🍗🍗🦴🦴")

            HungerChoice = input(f"Oh no, {PetNameDog} is hungry! Feed them (1) Ignore hunger (2): ").strip()

            if HungerChoice == "1":
                WhatFood = input("What will you give them? Cat Food (1), Chocolate (2), Dog Food (3): ").strip()
                if WhatFood == "1":
                    print("Oh no, your dog's sick and died!")
                    sleep(5)
                    scene = "GAMEOVER"
                elif WhatFood == "2":
                    print("You've just poisoned your dog and they've died!")
                    sleep(5)
                    scene = "GAMEOVER"
                elif WhatFood == "3":
                    print("You've fed your dog some dog food and now hunger bar is full!")
                    print("Status: Joy level: ♡ ♡ ♡ ♡ ♡ ")
                    print("Hunger Level: 🍗🍗🍗🍗🍗")
                    sleep(4)
                    scene = "ENDINGDAY"
                else:
                    print("That wasn't a valid choice. Your dog waited too long and starved...")
                    sleep(5)
                    scene = "GAMEOVER"

            elif HungerChoice == "2":
                print("Oh no, your pet starved too long and has died!")
                sleep(5)
                scene = "GAMEOVER"
            else:
                print("Your dog looks confused... (invalid choice)")
                sleep(5)
                scene = "GAMEOVER"

        elif ChoiceDogOne == "2":
            print("You've taken your dog for a walk. Joy: ♡ ♡ ♡ ♡ ♡  | Hunger: 🍗🍗🍗🍗🦴")
            sleep(2)
            HungerChoice = input(f"Oh no, {PetNameDog} is hungry! Feed them (1) Ignore hunger (2): ").strip()

            if HungerChoice == "1":
                WhatFood = input("What will you give them? Cat Food (1), Chocolate (2), Dog Food (3): ").strip()
                if WhatFood == "1":
                    print("Oh no, your dog's sick and died!")
                    sleep(5)
                    scene = "GAMEOVER"
                elif WhatFood == "2":
                    print("You've just poisoned your dog and they've died!")
                    sleep(5)
                    scene = "GAMEOVER"
                elif WhatFood == "3":
                    print("You've fed your dog some dog food and now hunger bar is full!")
                    print("Status: Joy level: ♡ ♡ ♡ ♡ ♡ ")
                    print("Hunger Level: 🍗🍗🍗🍗🍗")
                    sleep(4)
                    scene = "SECRETENDINGDOG"
                else:
                    print("That wasn't a valid choice. Your dog waited too long and starved...")
                    sleep(5)
                    scene = "GAMEOVER"
            elif HungerChoice == "2":
                print("Oh no, your pet starved too long and has died!")
                sleep(5)
                scene = "GAMEOVER"
            else:
                print("Your dog tilts its head in confusion... (invalid choice)")
                sleep(5)
                scene = "GAMEOVER"

        elif ChoiceDogOne == "3":
            print("You've fed your dog. Joy: ♡ ♡ ♡ ♡ ♡  | Hunger: 🍗🍗🍗🍗🍗 ")
            sleep(3)
            scene = "ENDINGDAY"
        elif ChoiceDogOne == "4":
            print("Your dog is happy! Joy: ♡ ♡ ♡ ♡ ♡ ")
            sleep(3)
            scene = "ENDINGDAY"
        else:
            print("That wasn't a valid action. Let's try again next time.")
            sleep(3)
            scene = "GAMEOVER"
        continue

    elif scene == "RABBITCHOICE":
        clear()
        setTextColour(CYAN)
        print("You adopted a Rabbit!")
        PetName = input("What will you name your Rabbit? ").strip() or "Bunny"
        setTextColour(WHITE)
        print(f"\n{PetName} hops happily.")
        input("What do you want to do with your rabbit? <press enter to continue>  ")
        ChoiceRABOne = input("Play (1) Pat (2) Feed (3) Cuddle (4): ").strip()

        if ChoiceRABOne == "1":
            print("Your Rabbit is joyful right now. Joy is 5/5 now.")
            print(r'''
   /)/)
  ( . .)
 c( づ♡
          ''')
            sleep(2)
            print("Joy level: ♡ ♡ ♡ ♡ ♡ ")
            print("Hunger Level:🍗🦴🦴")

            HungerChoice = input(f"Oh no, {PetName} is hungry! Feed them (1) Ignore hunger (2): ").strip()
            if HungerChoice == "1":
                WhatFood = input("What will you give them? Hay/Grass (1), Iceberg Lettuce (2), Rhubarb (3): ").strip()
                if WhatFood == "1":
                    print("You've fed your rabbit some hay/grass and now hunger bar is full!")
                    print("Status: Joy level: ♡ ♡ ♡ ♡ ♡ ")
                    print("Hunger Level: 🍗🍗🍗🍗🍗")
                    sleep(4)
                    scene = "ENDINGDAY"
                elif WhatFood == "2":
                    print("You've just upset your rabbit's tummy badly and they've died!")
                    sleep(5)
                    scene = "GAMEOVER"
                elif WhatFood == "3":
                    print("Rhubarb is toxic to rabbits. Your pet has died.")
                    sleep(5)
                    scene = "GAMEOVER"
                else:
                    print("That wasn't a valid choice. Your rabbit waited too long and starved...")
                    sleep(5)
                    scene = "GAMEOVER"
            elif HungerChoice == "2":
                print("Oh no, your pet starved too long and has died!")
                sleep(5)
                scene = "GAMEOVER"
            else:
                print("Your rabbit looks confused... (invalid choice)")
                sleep(5)
                scene = "GAMEOVER"

        elif ChoiceRABOne == "2":
            print("Your rabbit twitches its ears with joy! Joy: ♡ ♡ ♡ ♡ ♡ ")
            sleep(3)
            scene = "ENDINGDAY"

        elif ChoiceRABOne == "3":
            print("You've fed your rabbit. Joy: ♡ ♡ ♡ ♡ ♡  | Hunger: 🍗🍗🍗🍗🍗 ")
            sleep(3)
            scene = "ENDINGDAY"

        elif ChoiceRABOne == "4":
            print("Your rabbit hops into your arms happily! Joy: ♡ ♡ ♡ ♡ ♡ ")
            sleep(3)
            scene = "SECRETENDINGRAB"

        else:
            print("That wasn't a valid action. Let's try again next time.")
            sleep(3)
            scene = "GAMEOVER"
        continue

    elif scene == "OWLCHOICE":
        clear()
        setTextColour(CYAN)
        print("You adopted an Owl!")
        PetName = input("What will you name your Owl? ").strip() or "Birdy"
        setTextColour(WHITE)
        print(f"\n{PetName} hoots happily.")
        input("What do you want to do with your Owl? <press enter to continue>  ")
        ChoiceOwlOne = input("Play (1) Pat (2) Feed (3) Cuddle (4): ").strip()

        if ChoiceOwlOne == "1":
            print("Your Owl is joyfully flying right now. Joy is 5/5 now.")
            print(r'''
　　＜￣｀ヽ、　　 　 　       ／￣>
　   ゝ、　　 ＼　／ ⌒ ヽ  ノ  /
　　　  ゝ、　` ( ˶ • ▾ • ˶) ／
　　 　      >　 　 　  ,ノ
　　　　　     ∠_,,,/´”
''')
            sleep(2)
            print("Joy level: ♡ ♡ ♡ ♡ ♡ ")
            print("Hunger Level:🍗🍗🍗🦴")
            HungerChoice = input(f"Oh no, {PetName} is hungry! Feed them (1) Ignore hunger (2): ").strip()

            if HungerChoice == "1":
                WhatFood = input("What will you give them? Seeds (1), Candy (2), Dead Mouse (3): ").strip()
                if WhatFood == "1":
                    print("Owls are carnivores—seeds aren't suitable and your owl gets weak and dies.")
                    sleep(5)
                    scene = "GAMEOVER"
                elif WhatFood == "2":
                    print("Candy is toxic. Your owl has died.")
                    sleep(5)
                    scene = "GAMEOVER"
                elif WhatFood == "3":
                    print("You've fed your owl proper food and now hunger bar is full!")
                    print("Status: Joy level: ♡ ♡ ♡ ♡ ♡ ")
                    print("Hunger Level: 🍗🍗🍗🍗🍗")
                    sleep(4)
                    scene = "ENDINGDAY"
                else:
                    print("That wasn't a valid choice. Your owl waited too long and starved...")
                    sleep(5)
                    scene = "GAMEOVER"

            elif HungerChoice == "2":
                print("Oh no, your pet starved too long and has died!")
                sleep(5)
                scene = "GAMEOVER"
            else:
                print("Your owl looks confused... (invalid choice)")
                sleep(5)
                scene = "GAMEOVER"

        elif ChoiceOwlOne == "2":
            print("You gently pat the owl. Joy: ♡ ♡ ♡ ♡ ♡ ")
            sleep(3)
            scene = "ENDINGDAY"

        elif ChoiceOwlOne == "3":
            print("You fed your owl. Joy: ♡ ♡ ♡ ♡ ♡  | Hunger: 🍗🍗🍗🍗🍗 ")
            sleep(3)
            scene = "ENDINGDAY"

        elif ChoiceOwlOne == "4":
            print("Your owl snuggles into your cloak. Joy: ♡ ♡ ♡ ♡ ♡ ")
            sleep(3)
            scene = "ENDINGDAY"

        else:
            print("That wasn't a valid action. Let's try again next time.")
            sleep(3)
            scene = "GAMEOVER"
        continue

    elif scene == "GAMEOVER":
        music.stop()
        clear()
        setTextColour(RED)
        print("Reloading...")
        setTextColour(WHITE)
        ans = input("Start again? <Y> <N> ").strip().lower()
        if ans in ("y", "yes"):
            clear()
            scene = "BEGINNING"
            continue
        else:
            keepPlaying = False
            music.stop()
            continue

    elif scene == "ENDINGDAY":
        music.stop()
        clear()
        print(r'''
✩₊˚.⋆☾⋆⁺₊✧ GAME ENDED! ✩₊˚.⋆☾⋆⁺₊✧''')
        print("SONG:今はいいんだよfeat. 可不. ALL CREDITS GO TO MIMI SONG ISN'T")
        print(r'''
ヾ(＾ ∇ ＾) Bye~! Have a good day!''')
        again = input("Play again with a different lil buddy? <Y> <N> ").strip().lower()
        if again in ("y", "yes"):
            clear()
            scene = "BEGINNING"
            continue
        else:
            keepPlaying = False
            music.stop()
            continue

    elif scene == "SECRETENDINGCAT":
        clear()
        print(r'''
              ＿＿
　　　　　🌸＞　　 フ  
　　　　　| 　_　 _|       
　 　　　／` ミ_wノ
　　 　 /　　　 　|
　　　 /　 ヽ　　 ﾉ
　 　 │　　 |　|　|
　／￣|　　 |　|　|
　| (￣ヽ＿_ヽ_)__)
　＼二つ
　YOU GOT THE SECRET ENDING FOR YOUR KINDNESS OF
　PETTING THE CAT! <3''')
        keepPlaying = False
        music.stop()
        continue

    elif scene == "SECRETENDINGDOG":
        clear()
        print(r'''
♡   ႔ ႔     
   ᠸ^ ^ ⸝⸝      
     |、˜〵
     じしˍ,)⁐̤ᐷ
     YOU GOT THE SECRET ENDING FOR MAKING YOUR DOG HAPPY!! ''')
        keepPlaying = False
        music.stop()
        continue

    elif scene == "SECRETENDINGRAB":
        clear()
        print(r'''
　　  ／ |
　　 /　 ;　　
　。|　　:
　　|　　　'i,૮₍ ⸝ ⸝´˘`⸝ ⸝ ₎ა
☆　 'i　　　 ﾄ､_(  ヽ∩∩ ) ___ ,　　.
　.　　'i　　　　￣￣￣￣　　;'
　　　　丶,　　　　　　　,／　　。ﾟ　☆
　。ﾟ　　　　' ｰ- - - - '´´
　YOU'VE EARNED THE SECRET ENDING FOR YOUR RABBIT! YOUR RABBIT IS NOW FAST ASLEEP DREAMING! <3''')
        keepPlaying = False
        music.stop()
        continue
