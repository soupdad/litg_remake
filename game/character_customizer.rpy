image character = Composite(
    (505, 1200),
    (0, 0), "character_customizer/body.png",
    (0, 0), "character_customizer/face-[face].png",
    (0, 0), "character_customizer/outfit-[outfit].png",
    (0, 0), "character_customizer/hair-[hair_colour].png"
)

transform smaller:
    zoom 0.8

transform character_transform:
    zoom 0.8
    align(0.0, 0.5)

transform arrows:
    zoom 0.5
    anchor(0.5, 0.5)
    on hover:
        zoom 0.55
    on idle:
        zoom 0.5

screen character_customization:
    add "character" at smaller align(0.5, 0.5)
    # Face
    imagebutton idle "character_customizer/arrow-right.png" align(0.7, 0.3) action Function(customize_character, type = "face", direction = "right") at arrows
    imagebutton idle "character_customizer/arrow-left.png" align(0.3, 0.3) action Function(customize_character, type = "face", direction = "left") at arrows
    # Hair
    imagebutton idle "character_customizer/arrow-right.png" align(0.7, 0.3) action Function(customize_character, type = "hair", direction = "right") at arrows
    imagebutton idle "character_customizer/arrow-left.png" align(0.3, 0.3) action Function(customize_character, type = "hair", direction = "left") at arrows
    # Outfit
    imagebutton idle "character_customizer/arrow-right.png" align(0.7, 0.3) action Function(customize_character, type = "outfit", direction = "right") at arrows
    imagebutton idle "character_customizer/arrow-left.png" align(0.3, 0.3) action Function(customize_character, type = "outfit", direction = "left") at arrows


label scene_01:
    scene bg_pool
    show character at character_transform

    "This is a custom character"

label character_customizer:
    init python:
        body = "body"
        faces = ["smile", "shocked", "sad", "smirk", "angry"]
        hair_colours = ["blue", "pink", "purple"]
        outfits = ["1", "2", "3", "4", "5", "6"]

        face = faces[0]
        hair_colour = hair_colours[0]
        outfit = outfits[0]
    # $ body = "body"
    # $ faces = ["sad", "shocked", "smile", "smirk", "angry"]
    # $ hair_colours = ["blue", "pink", "purple"]
    # $ outfits = ["1", "2", "3", "4", "5", "6"]

    # $ face = faces[0]
    # $ hair_colour = hair_colours[0]
    # $ outfit = outfits[0]

    return