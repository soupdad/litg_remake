# MC
define s01_mc = Character("[s01_mc_name]")
$ s01_mc_job = ""
# $ s01_mc_outfit = "blue_bathing_suit"

init python:
    s01_mc_outfit = "orange_bathing_suit"
    amount_npcs_like_mc = {"allegra":15, "cherry":15, "erikah":15, "jake":15, "jasper":15, "jen":15, "levi":15, "lucy":15, "mason":15, "miles":15, "reese":15, "rohan":15, "sammi":15, "talia":15, "tim":15}


    def check_if_like_outfit(liked_outfits:list):
        if s01_mc_outfit in liked_outfits:
            return True
        else:
            return False

# scale of 0-30? interactions then make it go lower or higher
# $ amount_npcs_like_mc = {"allegra":15, "cherry":15, "erikah":15, "jake":15, "jasper":15, "jen":15, "levi":15, "lucy":15, "mason":15, "miles":15, "reese":15, "rohan":15, "sammi":15, "talia":15, "tim":15}


# Allegra
define allegra = Character("Allegra")
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