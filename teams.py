import statsapi


def get_LeagueData(League, Division="All"):
    
    return statsapi.standings_data(leagueId=League,division=Division)
# def get_ALCentral():
# def get_ALWest():
# def get_NLEast():
# def get_NLCentral():
# def get_NLWest():
