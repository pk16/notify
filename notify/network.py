# system
import tweepy
import string
import requests
import json
from bs4 import BeautifulSoup
import re

# package
import output as op
from system import exitApp
import app

requests.packages.urllib3.disable_warnings()

auth = tweepy.OAuthHandler('bPlXGjOCAm3TRys6kE88DRZ7T', 'tamznLbRd2c87KAqxEa4wJpPbWVLb3yTWMrzRy5qOY5UqymIQ8')
auth.set_access_token('1408428276-T1vRMv4kHxkJ6tQtorVHvEOYI2hTnYAqPog9RSL', 'Z96Xm7vjlKWDS6OfN9G9nsAF0jOJM2F7hxlbkQwFK5VaU')
api = tweepy.API(auth)

def getTweet(hashtag):
    try:
        tweet = api.search(hashtag)[0]
        userData = "@" + tweet.user.screen_name
        tweetData = tweet.text
    except IndexError:
        userData = ""
        tweetData = "Not Found"
    tweetData = (filter(lambda x: x in string.printable, tweetData))
    return ("{}\n\n{}".format(userData,tweetData))

def getTrending(woeid):
    lis = []
    try:
        data = api.trends_place(woeid)
    except Exception as e:
        op.popUp("Error","Can not get the trend. Network Error",0)
        app.main()
    data = data[0]
    trendsData = data["trends"]
    for elem in trendsData:
        lis.append(elem["name"])
    return lis

def getHackerEvents():
    url = "https://www.hackerearth.com/api/events/upcoming/?format=json"
    jsonData = requests.get(url).json()
    lis = []
    for elem in jsonData["response"]:
        lis.append({"Title":elem["title"] , "Start":elem["start_timestamp"] , "End":elem["end_timestamp"] })
    return lis

def getOtherEvents(site):
    url = "https://www.hackerrank.com/calendar/feed.rss"
    data = requests.get(url)
    soup = BeautifulSoup(data.text)
    xml = soup.find_all("item")
    lis = []
    for elem in reversed(xml):
        if site.lower() in elem.url.text:
            title = re.sub(r'\s+'," ",re.sub('[-]+','', re.sub(site,'',elem.title.text))).lstrip(' ')
            lis.append({"Title":title , "Start":elem.starttime.text , "End":elem.endtime.text})
    return lis

def getLiveMatches(url="http://static.cricinfo.com/rss/livescores.xml"):
    data = requests.get(url)
    soup = BeautifulSoup(data.text)
    xml = soup.find_all("item")
    matches = map( lambda item : re.sub(r'\s+'," ",re.sub('[^A-Za-z ]+', '', item.title.text)), xml)
    matchId = map( lambda item : re.search(r'\d+',item.guid.text).group(), xml)
    return (matchId, matches)

def getPlayingTeamNames(jsonurl):
    #Get the playing team names and store it in teamId:teamName dict format
    data = requests.get(jsonurl)
    jsonData = data.json()
    playingTeams={ team.get("team_id"):team.get("team_name") for team in jsonData.get("team") }
    return playingTeams

def getLatestScore(jsonurl,playingTeams):
    data = requests.get(jsonurl)
    jsonData = data.json()
    matchStatus = jsonData.get("live").get("status")
    title = matchStatus
    score = ""

    if(not jsonData.get("live").get("innings")):
        return (title,score)

    if("won by" in matchStatus):
        return (title,score)

    innings = jsonData.get("live").get("innings")
    batting_team_id=innings.get("batting_team_id")
    battingTeamName = playingTeams[batting_team_id]
    bowling_team_id=innings.get("bowling_team_id")
    bowlingTeamName = playingTeams.get(bowling_team_id)

    overs = innings.get("overs")

    runs=innings.get("runs")

    wickets = innings.get("wickets")

    try:
        requiredRuns = jsonData.get("comms")[1].get("required_string")
    except IndexError:
        requiredRuns = ""

    title = battingTeamName + " vs " + bowlingTeamName
    score = "score: " + runs + "/" + wickets + "\n" + "overs: " + overs + "\n" + requiredRuns

    return (title,score)