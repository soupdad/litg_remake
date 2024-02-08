init python:
    ######################################################################
    ### Season 1
    ######################################################################
    ## General
    
    # scale of 0-30? interactions then make it go lower or higher
    # add and remove keys and values when islanders are added or voted off
    # s1_amount_npcs_like_mc = {"allegra":15, "cherry":15, "erikah":15, "jake":15, "jasper":15, "jen":15, "levi":15, "lucy":15, "mason":15, "miles":15, "reese":15, "rohan":15, "sammi":15, "talia":15, "tim":15}
    s1_amount_npcs_like_mc = {"Allegra":15, "Erikah":15, "Jake":15, "Jasper":15, 
                            "Jen":15, "Levi":15, "Mason":15, "Miles":15, 
                            "Talia":15, "Tim":15}
    
    ## s1e1p1
    s1e1p1_boy_spoke_to = ""
    s1e1p1_cracking_onto_boys = 0
    s1e1p1_initial_meeting_likes = []

    ## s1e1p2
    s1e1p2_who_have_i_talked_to = []

    ######################################################################
    ### Season 2
    ######################################################################
    ## General
    s2_coupled_up_with = []
    s2_current_partner = ""
    s2_plan_to_move_in = False
    s2_secret_moment = "No one"
    s2_travel_plans = "No one"
    s2_win = True
    s2_spent_prize_on = "Random"

    ## Wedding
    s2w_partner = ''
    s2w_partner_pronouns = ["he", "him", "his"]
    s2w_living_together = False
    s2w_secret_moment = "No one"
    s2w_travel_plans = "No one"
    s2w_win = True
    s2w_spent_prize_on = "Random"
    s2w_mc_bp = ''
    s2w_partner_bp = ''
    s2w_officiant = ''


    s2wp1_talked_to = []

    ######################################################################
    ### Season 3
    ######################################################################
    ## General
    def he_she():
        if s3_current_partner in ["AJ", "Yasmin", "Elladine", "Genevieve", "Iona", "Miki", "Lily"]:
            return "she"
        else:
            return "he"
    def him_her():
        if s3_current_partner in ["AJ", "Yasmin", "Elladine", "Genevieve", "Iona", "Miki", "Lily"]:
            return "her"
        else:
            return "him"
    def his_her():
        if s3_current_partner in ["AJ", "Yasmin", "Elladine", "Genevieve", "Iona", "Miki", "Lily"]:
            return "her"
        else:
            return "his"
    s3_coupled_up_with = []
    s3_current_partner = ""
    s3_current_outfit = ""
    # Pronouns
    s3_partner_he_she = ""
    s3_partner_him_her = ""
    s3_partner_his_hers = ""
    
    s3_bff_he_she = ""
    s3_bff_him_her = ""
    s3_bff_his_her = ""

    # add and remove keys and values when islanders are added or voted off
    s3_amount_npcs_like_mc = {"AJ":15, "Elladine":15, "Iona":15, "Genevieve":15, "Miki":15,"Nicky":15, "Seb":15}
    s3_li_like_mc = {"Bill":15, "Camilo":15, "Harry":15, }
    s3_3rd_girl_options = {"Bill":"Miki", "Camilo":"Iona", "Harry":"Genevieve"}
    s3_3rd_girl = ""
    s3_npc_preferred_outfits = {"":""}
    s3_best_friend = ""
    s3_character_profile = ""
                        
    ## Episode 1, Part 1