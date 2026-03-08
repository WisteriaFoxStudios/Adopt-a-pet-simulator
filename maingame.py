import streamlit as st

st.set_page_config(page_title="Ivy Pets", page_icon="🐾")

# ---------- state ----------
if "scene" not in st.session_state:
    st.session_state.scene = "BEGINNING"
if "pet_name" not in st.session_state:
    st.session_state.pet_name = ""
if "pet_type" not in st.session_state:
    st.session_state.pet_type = ""
if "gameover_message" not in st.session_state:
    st.session_state.gameover_message = "Game over."
if "ending_message" not in st.session_state:
    st.session_state.ending_message = "✩₊˚.⋆☾⋆⁺₊✧ GAME ENDED! ✩₊˚.⋆☾⋆⁺₊✧"


# ---------- helpers ----------
def restart():
    st.session_state.scene = "BEGINNING"
    st.session_state.pet_name = ""
    st.session_state.pet_type = ""
    st.session_state.gameover_message = "Game over."
    st.session_state.ending_message = "✩₊˚.⋆☾⋆⁺₊✧ GAME ENDED! ✩₊˚.⋆☾⋆⁺₊✧"


def go_to(scene_name):
    st.session_state.scene = scene_name


def set_gameover(message):
    st.session_state.gameover_message = message
    go_to("GAMEOVER")


def set_ending(message):
    st.session_state.ending_message = message
    go_to("ENDINGDAY")


def joy_bar(level):
    return " ".join(["♡"] * level)


def hunger_bar(level):
    return " ".join(["🍗"] * level + ["🦴"] * (5 - level))


# ---------- music ----------
st.title("🐾 Ivy Pets")

try:
    with open("Fallen down cover piano.mp3", "rb") as f:
        st.audio(f.read(), format="audio/mp3")
except FileNotFoundError:
    st.warning("Music file not found. Make sure it is in the same folder as app.py.")

scene = st.session_state.scene

# ---------- scenes ----------
if scene == "BEGINNING":
    st.code(
        r"""
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
""",
        language="text",
    )

    st.write("Welcome to Ivy's Pets")
    st.write("Here, you can adopt a variety of pets,")
    st.write("all in need of finding love and care in a new home!")

    if st.button("Press Enter Key to enter shop!"):
        go_to("INSIDESHOP")
        st.rerun()

elif scene == "INSIDESHOP":
    st.subheader("You enter the shop to see the following pets:")

    st.write("Option 1:")
    st.code(
        r"""     ╱|、
    (˚ˎ 。7  
    |、˜〵          
    じしˍ,)ノ 
    CAT""",
        language="text",
    )

    st.write("Option 2:")
    st.code(
        r"""
     ︵ 
  ૮(`ᴥ ⁻ 𑁬
   |    ⸝ 〵
   じしˍ,  )୭
    DOG""",
        language="text",
    )

    st.write("Option 3:")
    st.code(
        r""".         ⊹ ₊
    __  ♡
⊂⊂  • )  
/     | 
⊂_﹏u
RABBIT""",
        language="text",
    )

    st.write("Option 4:")
    st.code(
        r"""<￣｀ヽ　　              ／￣＞ 
　ゝ、　＼　 ／<>ヽ,ノ　 /´ 
    ゝ、　`꒰˶• ▾ •˶꒱ ／   
　　　　  　>　　 ノ  
          --''--''--
OWL""",
        language="text",
    )

    pet = st.radio("Which option will you go with?", ["Cat", "Dog", "Rabbit", "Owl"])

    if st.button("Adopt this pet"):
        st.session_state.pet_type = pet
        st.session_state.pet_name = ""
        if pet == "Cat":
            go_to("CATCHOICE")
        elif pet == "Dog":
            go_to("DOGCHOICE")
        elif pet == "Rabbit":
            go_to("RABBITCHOICE")
        else:
            go_to("OWLCHOICE")
        st.rerun()

elif scene == "CATCHOICE":
    st.subheader("You've adopted your Cat 🐱")
    name = st.text_input("What will you name your cat?", value=st.session_state.pet_name or "Kitty")

    if st.button("Confirm cat name"):
        st.session_state.pet_name = name or "Kitty"
        st.rerun()

    if st.session_state.pet_name:
        st.write(f"{st.session_state.pet_name} purrs happily. 🐱")
        action = st.radio("What do you want to do with your cat?", ["Play", "Walk", "Feed", "Pat"])

        if st.button("Continue cat action"):
            if action == "Play":
                go_to("CATPLAY")
            elif action == "Walk":
                go_to("CATWALK")
            elif action == "Feed":
                set_ending("You've fed your cat. Joy: ♡ ♡ ♡ ♡ ♡ | Hunger: 🍗🍗🍗🍗🍗")
            elif action == "Pat":
                go_to("SECRETENDINGCAT")
            else:
                set_gameover("That wasn't a valid action. Let's try again next time.")
            st.rerun()

elif scene == "CATPLAY":
    pet_name = st.session_state.pet_name
    st.write("Your Cat is joyful right now. Joy is 5/5 now.")
    st.code(
        r"""
          へ  ♡       
         ૮  >  <) 
         /  ⁻  ៸|                                                                                      
      乀(ˍ, ل ل""",
        language="text",
    )
    st.write(f"Joy level: {joy_bar(5)}")
    st.write(f"Hunger Level: {hunger_bar(3)}")

    hunger_choice = st.radio(f"Oh no, {pet_name} is hungry! Feed them?", ["Feed them", "Ignore hunger"])

    if st.button("Continue after cat play"):
        if hunger_choice == "Feed them":
            go_to("CATFEED")
        else:
            set_gameover("Oh no, your pet starved too long and has died!")
        st.rerun()

elif scene == "CATWALK":
    pet_name = st.session_state.pet_name
    st.write("You've taken your pet cat for a walk, joy level: ♡ ♡ ♡ ♡ ❤")
    st.write(f"Hunger level: {hunger_bar(2)}")

    hunger_choice = st.radio(f"Oh no, {pet_name} is hungry! Feed them?", ["Feed them", "Ignore hunger"])

    if st.button("Continue after cat walk"):
        if hunger_choice == "Feed them":
            go_to("CATFEED")
        else:
            set_gameover("Oh no, your pet starved too long and has died!")
        st.rerun()

elif scene == "CATFEED":
    food = st.radio("What will you give them?", ["Dog Food", "Candy", "Cat Food"])

    if st.button("Feed cat"):
        if food == "Dog Food":
            set_gameover("Oh no, your cat's sick with heart disease and died!")
        elif food == "Candy":
            set_gameover("You've just poisoned your cat and they've died!")
        elif food == "Cat Food":
            set_ending("You've fed your cat some cat food and now hunger bar is full!\nStatus: Joy level: ♡ ♡ ♡ ♡ ♡\nHunger Level: 🍗🍗🍗🍗🍗")
        else:
            set_gameover("That wasn't a valid choice. Your cat waited too long and starved...")
        st.rerun()

elif scene == "DOGCHOICE":
    st.subheader("You adopted a Dog 🐶")
    name = st.text_input("What would you like to name your dog?", value=st.session_state.pet_name or "Doggo")

    if st.button("Confirm dog name"):
        st.session_state.pet_name = name or "Doggo"
        st.rerun()

    if st.session_state.pet_name:
        st.write(f"{st.session_state.pet_name} barks happily.")
        action = st.radio("What do you want to do with your dog?", ["Play", "Walk", "Feed", "Pat"])

        if st.button("Continue dog action"):
            if action == "Play":
                go_to("DOGPLAY")
            elif action == "Walk":
                go_to("DOGWALK")
            elif action == "Feed":
                set_ending("You've fed your dog. Joy: ♡ ♡ ♡ ♡ ♡ | Hunger: 🍗🍗🍗🍗🍗")
            elif action == "Pat":
                set_ending("Your dog is happy! Joy: ♡ ♡ ♡ ♡ ♡")
            else:
                set_gameover("That wasn't a valid action. Let's try again next time.")
            st.rerun()

elif scene == "DOGPLAY":
    pet_name = st.session_state.pet_name
    st.write("Your Dog is joyful right now. Joy is 5/5 now.")
    st.code(
        r"""
            ૮˶• ﻌ •˶ა
            ./づ~ 🦴""",
        language="text",
    )
    st.write(f"Joy level: {joy_bar(5)}")
    st.write(f"Hunger Level: {hunger_bar(3)}")

    hunger_choice = st.radio(f"Oh no, {pet_name} is hungry! Feed them?", ["Feed them", "Ignore hunger"])

    if st.button("Continue after dog play"):
        if hunger_choice == "Feed them":
            go_to("DOGFEEDNORMAL")
        else:
            set_gameover("Oh no, your pet starved too long and has died!")
        st.rerun()

elif scene == "DOGWALK":
    pet_name = st.session_state.pet_name
    st.write("You've taken your dog for a walk. Joy: ♡ ♡ ♡ ♡ ♡")
    st.write(f"Hunger level: {hunger_bar(4)}")

    hunger_choice = st.radio(f"Oh no, {pet_name} is hungry! Feed them?", ["Feed them", "Ignore hunger"])

    if st.button("Continue after dog walk"):
        if hunger_choice == "Feed them":
            go_to("DOGFEEDSECRET")
        else:
            set_gameover("Oh no, your pet starved too long and has died!")
        st.rerun()

elif scene == "DOGFEEDNORMAL":
    food = st.radio("What will you give them?", ["Cat Food", "Chocolate", "Dog Food"])

    if st.button("Feed dog"):
        if food == "Cat Food":
            set_gameover("Oh no, your dog's sick and died!")
        elif food == "Chocolate":
            set_gameover("You've just poisoned your dog and they've died!")
        elif food == "Dog Food":
            set_ending("You've fed your dog some dog food and now hunger bar is full!\nStatus: Joy level: ♡ ♡ ♡ ♡ ♡\nHunger Level: 🍗🍗🍗🍗🍗")
        else:
            set_gameover("That wasn't a valid choice. Your dog waited too long and starved...")
        st.rerun()

elif scene == "DOGFEEDSECRET":
    food = st.radio("What will you give them?", ["Cat Food", "Chocolate", "Dog Food"])

    if st.button("Feed dog for secret ending"):
        if food == "Cat Food":
            set_gameover("Oh no, your dog's sick and died!")
        elif food == "Chocolate":
            set_gameover("You've just poisoned your dog and they've died!")
        elif food == "Dog Food":
            go_to("SECRETENDINGDOG")
        else:
            set_gameover("That wasn't a valid choice. Your dog waited too long and starved...")
        st.rerun()

elif scene == "RABBITCHOICE":
    st.subheader("You adopted a Rabbit 🐰")
    name = st.text_input("What will you name your rabbit?", value=st.session_state.pet_name or "Bunny")

    if st.button("Confirm rabbit name"):
        st.session_state.pet_name = name or "Bunny"
        st.rerun()

    if st.session_state.pet_name:
        st.write(f"{st.session_state.pet_name} hops happily.")
        action = st.radio("What do you want to do with your rabbit?", ["Play", "Pat", "Feed", "Cuddle"])

        if st.button("Continue rabbit action"):
            if action == "Play":
                go_to("RABBITPLAY")
            elif action == "Pat":
                set_ending("Your rabbit twitches its ears with joy! Joy: ♡ ♡ ♡ ♡ ♡")
            elif action == "Feed":
                set_ending("You've fed your rabbit. Joy: ♡ ♡ ♡ ♡ ♡ | Hunger: 🍗🍗🍗🍗🍗")
            elif action == "Cuddle":
                go_to("SECRETENDINGRAB")
            else:
                set_gameover("That wasn't a valid action. Let's try again next time.")
            st.rerun()

elif scene == "RABBITPLAY":
    pet_name = st.session_state.pet_name
    st.write("Your Rabbit is joyful right now. Joy is 5/5 now.")
    st.code(
        r"""
   /)/)
  ( . .)
 c( づ♡""",
        language="text",
    )
    st.write(f"Joy level: {joy_bar(5)}")
    st.write("Hunger Level: 🍗🦴🦴")

    hunger_choice = st.radio(f"Oh no, {pet_name} is hungry! Feed them?", ["Feed them", "Ignore hunger"])

    if st.button("Continue after rabbit play"):
        if hunger_choice == "Feed them":
            go_to("RABBITFEED")
        else:
            set_gameover("Oh no, your pet starved too long and has died!")
        st.rerun()

elif scene == "RABBITFEED":
    food = st.radio("What will you give them?", ["Hay/Grass", "Iceberg Lettuce", "Rhubarb"])

    if st.button("Feed rabbit"):
        if food == "Hay/Grass":
            set_ending("You've fed your rabbit some hay/grass and now hunger bar is full!\nStatus: Joy level: ♡ ♡ ♡ ♡ ♡\nHunger Level: 🍗🍗🍗🍗🍗")
        elif food == "Iceberg Lettuce":
            set_gameover("You've just upset your rabbit's tummy badly and they've died!")
        elif food == "Rhubarb":
            set_gameover("Rhubarb is toxic to rabbits. Your pet has died.")
        else:
            set_gameover("That wasn't a valid choice. Your rabbit waited too long and starved...")
        st.rerun()

elif scene == "OWLCHOICE":
    st.subheader("You adopted an Owl 🦉")
    name = st.text_input("What will you name your owl?", value=st.session_state.pet_name or "Birdy")

    if st.button("Confirm owl name"):
        st.session_state.pet_name = name or "Birdy"
        st.rerun()

    if st.session_state.pet_name:
        st.write(f"{st.session_state.pet_name} hoots happily.")
        action = st.radio("What do you want to do with your owl?", ["Play", "Pat", "Feed", "Cuddle"])

        if st.button("Continue owl action"):
            if action == "Play":
                go_to("OWLPLAY")
            elif action == "Pat":
                set_ending("You gently pat the owl. Joy: ♡ ♡ ♡ ♡ ♡")
            elif action == "Feed":
                set_ending("You fed your owl. Joy: ♡ ♡ ♡ ♡ ♡ | Hunger: 🍗🍗🍗🍗🍗")
            elif action == "Cuddle":
                set_ending("Your owl snuggles into your cloak. Joy: ♡ ♡ ♡ ♡ ♡")
            else:
                set_gameover("That wasn't a valid action. Let's try again next time.")
            st.rerun()

elif scene == "OWLPLAY":
    pet_name = st.session_state.pet_name
    st.write("Your Owl is joyfully flying right now. Joy is 5/5 now.")
    st.code(
        r"""
　　＜￣｀ヽ、　　 　 　       ／￣>
　   ゝ、　　 ＼　／ ⌒ ヽ  ノ  /
　　　  ゝ、　` ( ˶ • ▾ • ˶) ／
　　 　      >　 　 　  ,ノ
　　　　　     ∠_,,,/´”""",
        language="text",
    )
    st.write(f"Joy level: {joy_bar(5)}")
    st.write(f"Hunger Level: {hunger_bar(3)}")

    hunger_choice = st.radio(f"Oh no, {pet_name} is hungry! Feed them?", ["Feed them", "Ignore hunger"])

    if st.button("Continue after owl play"):
        if hunger_choice == "Feed them":
            go_to("OWLFEED")
        else:
            set_gameover("Oh no, your pet starved too long and has died!")
        st.rerun()

elif scene == "OWLFEED":
    food = st.radio("What will you give them?", ["Seeds", "Candy", "Dead Mouse"])

    if st.button("Feed owl"):
        if food == "Seeds":
            set_gameover("Owls are carnivores—seeds aren't suitable and your owl gets weak and dies.")
        elif food == "Candy":
            set_gameover("Candy is toxic. Your owl has died.")
        elif food == "Dead Mouse":
            set_ending("You've fed your owl proper food and now hunger bar is full!\nStatus: Joy level: ♡ ♡ ♡ ♡ ♡\nHunger Level: 🍗🍗🍗🍗🍗")
        else:
            set_gameover("That wasn't a valid choice. Your owl waited too long and starved...")
        st.rerun()

elif scene == "GAMEOVER":
    st.error(st.session_state.gameover_message)
    col1, col2 = st.columns(2)

    with col1:
        if st.button("Start again"):
            restart()
            st.rerun()

    with col2:
        if st.button("Go back to shop"):
            restart()
            go_to("INSIDESHOP")
            st.rerun()

elif scene == "ENDINGDAY":
    st.success("✩₊˚.⋆☾⋆⁺₊✧ GAME ENDED! ✩₊˚.⋆☾⋆⁺₊✧")
    st.write(st.session_state.ending_message)
    st.write("SONG: 今はいいんだよ feat. 可不. ALL CREDITS GO TO MIMI.")
    st.write("ヾ(＾ ∇ ＾) Bye~! Have a good day!")

    if st.button("Play again with a different buddy"):
        restart()
        st.rerun()

elif scene == "SECRETENDINGCAT":
    st.success("YOU GOT THE SECRET ENDING FOR YOUR KINDNESS OF PETTING THE CAT! <3")
    st.code(
        r"""
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
　PETTING THE CAT! <3""",
        language="text",
    )

    if st.button("Play again"):
        restart()
        st.rerun()

elif scene == "SECRETENDINGDOG":
    st.success("YOU GOT THE SECRET ENDING FOR MAKING YOUR DOG HAPPY!!")
    st.code(
        r"""
♡   ႔ ႔     
   ᠸ^ ^ ⸝⸝      
     |、˜〵
     じしˍ,)⁐̤ᐷ
     YOU GOT THE SECRET ENDING FOR MAKING YOUR DOG HAPPY!!""",
        language="text",
    )

    if st.button("Play again"):
        restart()
        st.rerun()

elif scene == "SECRETENDINGRAB":
    st.success("YOU'VE EARNED THE SECRET ENDING FOR YOUR RABBIT! YOUR RABBIT IS NOW FAST ASLEEP DREAMING! <3")
    st.code(
        r"""
　　  ／ |
　　 /　 ;　　
　。|　　:
　　|　　　'i,૮₍ ⸝ ⸝´˘`⸝ ⸝ ₎ა
☆　 'i　　　 ﾄ､_(  ヽ∩∩ ) ___ ,　　.
　.　　'i　　　　￣￣￣￣　　;'
　　　　丶,　　　　　　　,／　　。ﾟ　☆
　。ﾟ　　　　' ｰ- - - - '´´
　YOU'VE EARNED THE SECRET ENDING FOR YOUR RABBIT! YOUR RABBIT IS NOW FAST ASLEEP DREAMING! <3""",
        language="text",
    )

    if st.button("Play again"):
        restart()
        st.rerun()
