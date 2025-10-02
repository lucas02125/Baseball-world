import statsapi

print(statsapi.standings(leagueId="103,104", division="all", 
include_wildcard=True, season=1969, standingsTypes=None, date=None))