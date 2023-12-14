init python:
    # lists of all options to choose from
    faces = ["smile", "shocked", "sad", "smirk", "angry"]
    hair_colours = ["blue", "pink", "purple"]
    outfits = ["1", "2", "3", "4", "5", "6"]

    # what is currently being displayed
    face = faces[0]
    hair_colour = hair_colours[0]
    outfit = outfits[0]
    # where character's name is saved
    character_name = ""
    main_character = Character(name = "character_name", dynamic = True)

    def customize_character(part, direction):
        """
        gives arrows functionality to parse through the options for face, hair colour, and outfit

        Args:
            part (str): face, hair_colour, or outfit, depends on which arrow is being pressed
            direction (str): left or right, depends on which arrow is being pressed
        """
        global face
        global hair_colour
        global outfit

        if direction == "right":
            if part == "face":
                if faces.index(face) < len(faces) - 1:
                    face = faces[faces.index(face) + 1]
                else:
                    face = faces[0]
            if part == "hair_colour":
                if hair_colours.index(hair_colour) < len(hair_colours) - 1:
                    hair_colour = hair_colours[hair_colours.index(hair_colour) + 1]
                else:
                    hair_colour = hair_colours[0]
            if part == "outfit":
                if outfits.index(outfit) < len(outfits) - 1:
                    outfit = outfits[outfits.index(outfit) + 1]
                else:
                    outfit = outfits[0]

        elif direction == "left":
            if part == "face":
                if faces.index(face) > 0:
                    face = faces[faces.index(face) - 1]
                else:
                    face = faces[-1]
            if part == "hair_colour":
                if hair_colours.index(hair_colour) > 0:
                    hair_colour = hair_colours[hair_colours.index(hair_colour) - 1]
                else:
                    hair_colour = hair_colours[-1]
            if part == "outfit":
                if outfits.index(outfit) > 0:
                    outfit = outfits[outfits.index(outfit) - 1]
                else:
                    outfit = outfits[-1]

        # saves character changes
        renpy.retain_after_load()





# where the main character image is saved
image character = Composite(
    (505, 1200),
    (0, 0), "character_customizer/body.png",
    (0, 0), "character_customizer/face-[face].png",
    (0, 0), "character_customizer/outfit-[outfit].png",
    (0, 0), "character_customizer/hair-[hair_colour].png"
)

# TRANSFORMS
transform smaller:
    """
    makes image slightly smaller
    """
    zoom 0.7

transform face_zoom:
    """
    not currently used in script and needs to be reworked
    puts character zoomed in for editing face
    """
    zoom 2
    yalign(-0.1)

transform character_transform:
    """
    puts character in center of screen, slightly smaller than file size
    """
    zoom 0.8
    align(0.0, 0.5)

transform arrows:
    """
    makes buttons get bigger when hovered over
    """
    zoom 0.5
    anchor(0.5, 0.5)
    on hover:
        zoom 0.55
    on idle:
        zoom 0.5

# SCREENS AND LABELS
screen character_customization:
    """
    this displays the character customizer and arrows that take user input
    """
    add "character" at smaller align(0.5, 0.5)
    # Face
    imagebutton idle "character_customizer/arrow-right.png" align(0.7, 0.3) action Function(customize_character, part = "face", direction = "right") at arrows
    imagebutton idle "character_customizer/arrow-left.png" align(0.3, 0.3) action Function(customize_character, part = "face", direction = "left") at arrows
    # Hair
    imagebutton idle "character_customizer/arrow-right.png" align(0.7, 0.5) action Function(customize_character, part = "hair_colour", direction = "right") at arrows
    imagebutton idle "character_customizer/arrow-left.png" align(0.3, 0.5) action Function(customize_character, part = "hair_colour", direction = "left") at arrows
    # Outfit
    imagebutton idle "character_customizer/arrow-right.png" align(0.7, 0.7) action Function(customize_character, part = "outfit", direction = "right") at arrows
    imagebutton idle "character_customizer/arrow-left.png" align(0.3, 0.7) action Function(customize_character, part = "outfit", direction = "left") at arrows


label scene_01:
    """
    the first scene that is called after character is saved
    """
    scene bg_pool
    show character at character_transform

    main_character "This is a custom character"

screen start_screen:
    """
    displays background, name input bar, and start button
    """
    image "bg_pool.png"
    # start button
    imagebutton idle "character_customizer/start_button.png" align(0.5, 0.9) action Jump("scene_01") at arrows
    # this makes it so the items are aligned with eachother on the x axis
    hbox:
        align(0.5, 0.1)
        text "Your name:" size 18 color "#000000" yalign 0.5 outlines[(absolute(2), "#ffffff", 0, 0)]
        # character name input textbox
        frame:
            background "#ffffff"
            yalign 0.5
            input value VariableInputValue("character_name") minwidth 150 length 10

    # this calls other screen to act as an overlay
    use character_customization