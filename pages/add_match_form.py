from pages.base_page import BasePage


class Dashboard(BasePage):
    my_team_xpath = "//*[@id=\"__next\"]/div[1]/main/div[2]/form/div[2]/div/div[1]/div/div"
    enemy_team_xpath = "//*[@id=\"__next\"]/div[1]/main/div[2]/form/div[2]/div/div[2]/div"
    my_team_score_xpath = "//*[@id=\"__next\"]/div[1]/main/div[2]/form/div[2]/div/div[3]/div/div"
    enemy_team_score_xpath = "//*[@id=\"__next\"]/div[1]/main/div[2]/form/div[2]/div/div[4]/div"
    date_xpath = "//*[@id=\"__next\"]/div[1]/main/div[2]/form/div[2]/div/div[5]/div"
    t_shirt_color_xpath = "//*[@id=\"__next\"]/div[1]/main/div[2]/form/div[2]/div/div[7]/div/div"
    league_xpath = "//*[@id=\"__next\"]/div[1]/main/div[2]/form/div[2]/div/div[8]/div/div"
    time_played_xpath = "//*[@id=\"__next\"]/div[1]/main/div[2]/form/div[2]/div/div[9]/div/div/input"
    number_xpath = "//*[@id=\"__next\"]/div[1]/main/div[2]/form/div[2]/div/div[10]/div"
    web_match_xpath = "//*[@id=\"__next\"]/div[1]/main/div[2]/form/div[2]/div/div[11]"
    general_xpath = "//*[@id=\"__next\"]/div[1]/main/div[2]/form/div[2]/div/div[12]/div"
    rating_xpath = "//*[@id=\"__next\"]/div[1]/main/div[2]/form/div[2]/div/div[13]"
