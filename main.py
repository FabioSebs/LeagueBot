import random
import cassiopeia as cass
from dotenv import load_dotenv
import os

#Env Files
load_dotenv()
RIOT = os.getenv("riot")


cass.set_riot_api_key(RIOT)

def getBestChamps(tag):
    summoner = cass.Summoner(name=tag, region="NA")
    good_with = summoner.champion_masteries.filter(lambda cm: cm.level >= 6)
    return [cm.champion.name for cm in good_with]