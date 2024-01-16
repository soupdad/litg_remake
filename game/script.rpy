init python:
    # USER DEFINED FUNCTIONS
    def reset_season_1():
        amount_npcs_like_mc = {"allegra":15, "cherry":15, "erikah":15, "jake":15, "jasper":15, "jen":15, "levi":15, "lucy":15, "mason":15, "miles":15, "reese":15, "rohan":15, "sammi":15, "talia":15, "tim":15}
        s01_mc_name = "You"
        s01_mc_job = ""


    def check_if_like_outfit(liked_outfits:list):
        if s01_mc_outfit in liked_outfits:
            return True
        else:
            return False

    


# TRANSFORMS
transform little_hop:
    yalign 1.0
    easein_bounce 0.05 yalign 0.9
    easeout_bounce 0.05 yalign 1.0

transform double_zoom:
    zoom 2.2

transform half_size:
    zoom 0.5

transform map_icon:
    zoom 0.3
    anchor(0.5, 0.5)
    on hover:
        zoom 0.35
    on idle:
        zoom 0.3

transform select_episode_button:
    zoom 1
    anchor(0.5, 0.5)
    on hover:
        zoom 1.04
    on idle:
        zoom 1

# ON SCREEN POSITIONS
transform mc_spot:
    easein 0.2 xalign 0.05
    

transform beside_mc:
    easein 0.2 xalign 0.25

transform npc_1:
    xalign 1.5 yalign 1.0
    easein 0.2 xalign 0.55

transform npc_2:
    xalign 1.5 yalign 1.0
    easein 0.2 xalign 0.75

transform npc_3:
    xalign 1.5 yalign 1.0
    easein 0.2 xalign 0.95

transform npc_exit:
    easeout 0.2 xalign 1.5


label start:
    menu:
        "Test":
            jump testing
        "Season 1":
            # jump season_01
            jump s1e1p2
        "Season 2":
            "Coming soon! Pick a Different Season"
            jump start
        "Season 2: Wedding":
            call screen s2w_select_episode
        "Season 3":
            jump s3e1p1
    return
# uncomment once done season 1, and actually making menu
""" label season_01:
    menu:
        "Episode 1":
            jump episode_01
        "Episode 2":
            "Coming soon! Pick a Different Episode"
            jump season_01
        "Episode 3":
            "Coming soon! Pick a Different Episode"
            jump season_01

label episode_01:
    menu:
        "Part 1":
            jump s1e1p1_01
        "Part 2":
            "Coming soon! Pick a Different Part"
            jump episode_01
        "Part 3":
            "Coming soon! Pick a Different Part"
            jump episode_01 """

label episode_unavailable:
    call screen episode_unavailable

    call screen s2w_select_episode





    # return
