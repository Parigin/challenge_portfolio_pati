from pages.base_page import BasePage


class Dashboard(BasePage):
    button_xpath = "//*[@id='login']"
    player_count_xpath = "//*[@id=\"__next\"]/div[1]/main/div[2]/div[1]/div"
    matches_count_xpath = "//*[@id=\"__next\"]/div[1]/main/div[2]/div[2]/div"
    reports_count_xpath = "//*[@id=\"__next\"]/div[1]/main/div[2]/div[3]/div"
    events_count_xpath = "//*[@id=\"__next\"]/div[1]/main/div[2]/div[4]/div"
    add_player_xpath = "//*/a/button/span[1]"
    main_page_xpath = "//*[@id=\"__next\"]/div[1]/div/div/div/ul[1]/div[1]/div[2]/span"
    players_xpath = "//*[@id=\"__next\"]/div[1]/div/div/div/ul[1]/div[2]/div[2]/span"
    languages_xpath = "//*[@id=\"__next\"]/div[1]/div/div/div/ul[2]/div[1]"
    sign_out_xpath = "//*[@id=\"__next\"]/div[1]/div/div/div/ul[2]/div[2]/div[2]/span"
    dev_team_contact_xpath = "//*[@id=\"__next\"]/div[1]/main/div[3]/div[1]/div/div[3]/a/span[1]"
