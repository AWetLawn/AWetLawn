# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define me = Character("me", what_italic=True, color="#ff0000")
define har = Character("Harsh")
define ani = Character("Anirudh")
define kara = Character("Symphonie de l'Amour")
define ski = Character("Skittles9823", color="#0B0513")
define del = Character("Deletescape", color="#f06292")
define dul = Character("DulceTiSeduce", color="#7C4DFF")
define shu = Character("Shubby", color="#4169E1")


# The game starts here.

label start:

    scene bg lawn

    show anirudh

    ani "Hello everyo-"

    hide anirudh
    show anirudh at left
    show harsh at right

    menu:

        "/ban":
            jump ban

        "/gban":
            jump gban

label ban:

    ani "NOOOOOOOO"
    har "/ban"

    hide anirudh
    hide harsh
    show harsh at right
    show kara at left

    kara "Banned!"

    hide kara
    hide harsh

    jump cont

label gban:

    ani "SPARE ME PLOX!"
    har "/gban"

    hide anirudh
    hide harsh
    show harsh at right
    show kara at left

    kara "gban complete!"

    hide kara
    hide harsh

    jump cont


label cont:

    show skittles9823 happy

    ski "Oh, welcome to my Lawn"

    ski "Such a beautiful day to sit on my Lawnchair!"

    hide skittles9823
    show skittles9823 happy at left
    show deletescape at right

    del "wtf bitch, this is my lawn"

    hide deletescape
    show deletescape at center

    del "And I made that Lawnchair myself"

    ski "ofuk"

    "who the fuck you gunna support now?"

    menu:

        "I support Skittles9823":
            jump skittles

        "I support deletescape":
            jump deletescape

label skittles:

    hide deletescape
    hide skittles9823
    show skittles9823 turnt
    ski "K, fuck delete-chan, I will show him who truly rules these groups!"
    ski "how could I revenge on him?"

menu:

    "Pee on the chair and make it wet":
        jump ski_pee_on_chair

    "Pee on the Lawn and make it wet":
        jump ski_pee_on_lawn

    "Pee on everything":
        jump ski_pee_on_everything

label ski_pee_on_chair:

    ski "Oh boy, I love to do this!"
    scene bg chair peed

label ski_pee_on_lawn:

    ski "Lmao fuck that Pixel 1 Lawn!"
    scene bg lawn peed

label ski_pee_on_everything:

    ski "Fuck all this shit!"
    scene bg everything peed

jump end

label deletescape:

    hide skittles9823
    hide deletescape
    show deletescape
    ""

label end:
    me "How the fuck does one end a visual novel wtf"
    me "This is the end, for now, the story will probably completely change in future versions because it sucks (like dulce)"

return
