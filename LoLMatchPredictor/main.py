import riot_api_calls as rac

if __name__ == "__main__":
    print("Main Running")
    print(rac.get_summoner_info("shadogi", "na1"))

    # Sequence
    # - Start with my user and pull match history
    # - Get stats from match (validate against duplicates) and then choose another summoner to get matches from
    #   - Each match gets its own thread
    # - Commit match stats to MongoDB for later processing
