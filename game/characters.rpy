## MC
# define s01_mc_image = "s01_mc_placeholder"
# DELETE WHEN DEPLOYING CODE
# image s01_mc_img = "images/season_01/character_placeholders/s01_mc.png"
default s01_mc_name = "Filler Name"
define s01_mc = Character("[s01_mc_name]", image = "s01_mc")

# UNCOMMENT AND DELETE WHEN DEPLOYING CODE
# define persistent.s01_mc_job = ""
define s01_mc_job = "Trainee Heart Surgeon"
default amount_npcs_like_mc = {"allegra":15, "cherry":15, "erikah":15, "jake":15, "jasper":15, "jen":15, "levi":15, "lucy":15, "mason":15, "miles":15, "reese":15, "rohan":15, "sammi":15, "talia":15, "tim":15}

init python:
    # UNCOMMENT AND DELETE WHEN DEPLOYING CODE
    s01_mc_outfit = ""
    s01_mc_outfit = "orange_bathing_suit"

    # scale of 0-30? interactions then make it go lower or higher
    # amount_npcs_like_mc = {"allegra":15, "cherry":15, "erikah":15, "jake":15, "jasper":15, "jen":15, "levi":15, "lucy":15, "mason":15, "miles":15, "reese":15, "rohan":15, "sammi":15, "talia":15, "tim":15}


# Allegra
define allegra = Character("Allegra", image = "allegra")
    #placeholders to be changed with actual outfits later
define allegra_liked_outfits = ["blue_bathing_suit", "red_dress"]










# Cherry
define cherry = Character("Cherry")

# Erikah
define erikah = Character("Erikah")

# Jake
define jake = Character("Jake")

# Jasper
define jasper = Character("Jasper")

# Jen
define jen = Character("Jen")

# Levi
define levi = Character("Levi")

# Lucy
define lucy = Character("Lucy")

# Mason
define mason = Character("Mason")

# Miles
define miles = Character("Miles")

# Reese
define reese = Character("Reese")

# Rohan
define rohan = Character("Rohan")

# Sammi
define sammi = Character("Sammi")

#Talia
define talia = Character("Talia")

# Tim
define tim = Character("Tim")