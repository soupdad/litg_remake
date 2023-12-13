label start:
    jump scene_01

    """ menu:
        "Season 1":
            # jump season_01
            jump s1e1p1_01
        "Season 2":
            "Coming soon! Pick a Different Season"
            jump start
        "Season 3":
            "Coming soon! Pick a Different Season"
            jump start
    return """
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






    # return
