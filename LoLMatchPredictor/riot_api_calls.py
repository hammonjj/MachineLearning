# Riot API Calls
RiotApiKey = "RGAPI-3ce19b6e-3650-45b9-9eaf-1e8736fd4ccc"

# Regions: na1, euw1, kr


def get_summoner_info(summoner, region):
    return f"https://{region}.api.riotgames.com/lol/summoner/v4/summoners/by-name/{summoner}?api_key={RiotApiKey}"


def get_match_info(match_id, region):
    return f"https://{region}.api.riotgames.com/lol/match/v4/matches/{match_id}?api_key={RiotApiKey}"
