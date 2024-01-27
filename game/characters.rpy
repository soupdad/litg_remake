####################################################################
## General
####################################################################
define thought = Character(window_background = Image("bg_thought.png", xalign=0.5, yalign=1.0))
define text = Character(window_background = Image("bg_text_message.png", xalign=0.5, yalign=1.0), color = "#ffffff")

# init python:
#     def little_jump(event, interact=True, **kwargs):
#         if not interact:
#             return
        
#         yalign 1.0
#         easein_bounce 0.05 yalign 0.9
#         easeout_bounce 0.05 yalign 1.0

# transform little_hop:
#     yalign 1.0
#     easein_bounce 0.05 yalign 0.9
#     easeout_bounce 0.05 yalign 1.0

####################################################################
## Season 1
####################################################################

## MC
define s01_mc = Character("s01_mc_name", dynamic = True, window_background = Image("bg_dialog.png", xalign=0.5, yalign=1.0))

# probably going to change this later
# define thought = Character("Thought")

# UNCOMMENT AND/OR DELETE WHEN DEPLOYING CODE
# define persistent.s01_mc_job = ""
default s01_mc_name = "Filler Name"
define s01_mc_job = "Trainee Heart Surgeon"
define s01_mc_outfit = "orange_bathing_suit"

### NPCS
## Allegra
define allegra = Character("Allegra")
    #placeholders to be changed with actual outfits later
define allegra_liked_outfits = ["blue_bathing_suit", "red_dress"]

## Cherry
define cherry = Character("Cherry")

## Erikah
define erikah = Character("Erikah")

## Jake
define jake = Character("Jake")

## Jasper
define jasper = Character("Jasper")

## Jen
define jen = Character("Jen")

## Levi
define levi = Character("Levi")

## Lucy
define lucy = Character("Lucy")

## Mason
define mason = Character("Mason")

## Miles
define miles = Character("Miles")

## Reese
define reese = Character("Reese")

## Rohan
define rohan = Character("Rohan")

## Sammi
define sammi = Character("Sammi")

## Talia
define talia = Character("Talia")

## Tim
define tim = Character("Tim")

####################################################################
## Season 2
####################################################################

define s2_mc = Character("s2_mc_name", dynamic = True, window_background = Image("bg_dialog.png", xalign=0.5, yalign=1.0))

### NPCs
## Arjun
image arjun = "season_02/npcs/arjun.png"
define arjun = Character("Arjun", image = "arjun", window_background = Image("bg_dialog.png", xalign=0.5, yalign=1.0))

## Blake
image blake = "season_02/npcs/blake.png"
define blake = Character("Blake", image = "blake", window_background = Image("bg_dialog.png", xalign=0.5, yalign=1.0))

## Bobby
image bobby = "season_02/npcs/bobby.png"
define bobby = Character("Bobby", image = "bobby", window_background = Image("bg_dialog.png", xalign=0.5, yalign=1.0))

## Carl
image carl = "season_02/npcs/carl.png"
define carl = Character("Carl", image = "carl", window_background = Image("bg_dialog.png", xalign=0.5, yalign=1.0))

## Chelsea
image chelsea = "season_02/npcs/chelsea.png"
define chelsea = Character("Chelsea", image = "chelsea", window_background = Image("bg_dialog.png", xalign=0.5, yalign=1.0))

## Elijah
image elijah = "season_02/npcs/elijah.png"
define elijah = Character("Elijah", image = "elijah", window_background = Image("bg_dialog.png", xalign=0.5, yalign=1.0))

## Elisa
image elisa = "season_02/npcs/elisa.png"
define elisa = Character("Elisa", image = "elisa", window_background = Image("bg_dialog.png", xalign=0.5, yalign=1.0))

## Felix
image felix = "season_02/npcs/felix.png"
define felix = Character("Felix", image = "felix", window_background = Image("bg_dialog.png", xalign=0.5, yalign=1.0))

## Gary
image gary = "season_02/npcs/gary.png"
define gary = Character("Gary", image = "gary", window_background = Image("bg_dialog.png", xalign=0.5, yalign=1.0))

## Graham
image graham = "season_02/npcs/graham.png"
define graham = Character("Graham", image = "graham", window_background = Image("bg_dialog.png", xalign=0.5, yalign=1.0))

## Hannah
image hannah = "season_02/npcs/hannah.png"
define hannah = Character("Hannah", image = "hannah", window_background = Image("bg_dialog.png", xalign=0.5, yalign=1.0))

## Henrik
image henrik = "season_02/npcs/henrik.png"
define henrik = Character("Henrik", image = "henrik", window_background = Image("bg_dialog.png", xalign=0.5, yalign=1.0))

## Hope
image hope = "season_02/npcs/hope.png"
define hope = Character("Hope", image = "hope", window_background = Image("bg_dialog.png", xalign=0.5, yalign=1.0))

## Jakub
image jakub = "season_02/npcs/jakub.png"
define jakub = Character("Jakub", image = "jakub", window_background = Image("bg_dialog.png", xalign=0.5, yalign=1.0))

## Jo
image jo = "season_02/npcs/jo.png"
define jo = Character("Jo", image = "jo", window_background = Image("bg_dialog.png", xalign=0.5, yalign=1.0))

## Kassam
image kassam = "season_02/npcs/kassam.png"
define kassam = Character("Kassam", image = "kassam", window_background = Image("bg_dialog.png", xalign=0.5, yalign=1.0))

## Lottie
image lottie = "season_02/npcs/lottie.png"
define lottie = Character("Lottie", image = "lottie", window_background = Image("bg_dialog.png", xalign=0.5, yalign=1.0))

## Lucas
image lucas = "season_02/npcs/lucas.png"
define lucas = Character("Lucas", image = "lucas", window_background = Image("bg_dialog.png", xalign=0.5, yalign=1.0))

## Marisol
image marisol = "season_02/npcs/marisol.png"
define marisol = Character("Marisol", image = "marisol", window_background = Image("bg_dialog.png", xalign=0.5, yalign=1.0))

## Noah
image noah = "season_02/npcs/noah.png"
define noah = Character("Noah", image = "noah", window_background = Image("bg_dialog.png", xalign=0.5, yalign=1.0))

## Priya
image priya = "season_02/npcs/priya.png"
define priya = Character("Priya", image = "priya", window_background = Image("bg_dialog.png", xalign=0.5, yalign=1.0))

## Rahim
image rahim = "season_02/npcs/ibrahim.png"
define rahim = Character("Ibrahim", image = "rahim", window_background = Image("bg_dialog.png", xalign=0.5, yalign=1.0))

## Rocco
image rocco = "season_02/npcs/rocco.png"
define rocco = Character("Rocco", image = "rocco", window_background = Image("bg_dialog.png", xalign=0.5, yalign=1.0))

## Shannon
image shannon = "season_02/npcs/shannon.png"
define shannon = Character("Shannon", image = "shannon", window_background = Image("bg_dialog.png", xalign=0.5, yalign=1.0))


## Wedding
image s2w_mc = "season_02/npcs/mc.png"
image s2w_mc happy = "season_02/npcs/mc-happy.png"

define s2w_mc = Character("s2w_mc_name", dynamic = True, image = "s2w_mc", window_background = Image("bg_dialog.png", xalign=0.5, yalign=1.0))



####################################################################
## Season 3
####################################################################
### MC
default s3_mc_name = "Larissa"
define s3_mc = Character("s3_mc_name", dynamic = True, window_background = Image("bg_dialog.png", xalign=0.5, yalign=1.0))
define s3_mc_attr = {'Outfit':'orange_bathing_suit', 'Job':'Scientist', 'Bisexual':False, 
                    'Sweet':0, 'Bold':0, 'Funny':0}

# UNCOMMENT AND/OR DELETE WHEN DEPLOYING CODE
# define persistent.s03_mc_job = ""
# define persistent.s03_mc_name = ""


### NPCs
## AJ
define aj = Character("AJ", window_background = Image("bg_dialog.png", xalign=0.5, yalign=1.0))
image aj = "season_03/npcs/aj.png"

## Bill
define bill = Character("Bill", window_background = Image("bg_dialog.png", xalign=0.5, yalign=1.0))
image bill = "season_03/npcs/bill.png"

## Camilo
define camilo = Character("Camilo", window_background = Image("bg_dialog.png", xalign=0.5, yalign=1.0))
image camilo = "season_03/npcs/camilo.png"

## Ciaran
define ciaran = Character("Ciaran", window_background = Image("bg_dialog.png", xalign=0.5, yalign=1.0))

## Elladine
define elladine = Character("Elladine", window_background = Image("bg_dialog.png", xalign=0.5, yalign=1.0))
image elladine = "season_03/npcs/elladine.png"

## Genevieve
define genevieve = Character("Genevieve", window_background = Image("bg_dialog.png", xalign=0.5, yalign=1.0))
image genevieve = "season_03/npcs/genevieve.png"

## Harry
define harry = Character("Harry", window_background = Image("bg_dialog.png", xalign=0.5, yalign=1.0))
image harry = "season_03/npcs/harry.png"

## Iona
define iona = Character("Iona", window_background = Image("bg_dialog.png", xalign=0.5, yalign=1.0))
image iona = "season_03/npcs/iona.png"

## Lily
define lily = Character("Lily", window_background = Image("bg_dialog.png", xalign=0.5, yalign=1.0))

## Miki
define miki = Character("Miki", window_background = Image("bg_dialog.png", xalign=0.5, yalign=1.0))
image miki = "season_03/npcs/miki.png"

## Nicky
define nicky = Character("Nicky", window_background = Image("bg_dialog.png", xalign=0.5, yalign=1.0))
image nicky = "season_03/npcs/nicky.png"

## Rafi
define rafi = Character("Rafi", window_background = Image("bg_dialog.png", xalign=0.5, yalign=1.0))

## Seb
define seb = Character("Seb", window_background = Image("bg_dialog.png", xalign=0.5, yalign=1.0))
image seb = "season_03/npcs/seb.png"

## Tai
define tai = Character("Tai", window_background = Image("bg_dialog.png", xalign=0.5, yalign=1.0))

## Yasmin
define yasmin = Character("Yasmin", window_background = Image("bg_dialog.png", xalign=0.5, yalign=1.0))