import game
import player
import standings
import scoreboard
from random import randint

team_commands = {"score" : game.getGameScore,
                "nextgame" : game.getNextGame,
                "last5" : game.getLast5,
                "record": standings.teamRecord,
                "teamstats" : game.getTeamStats
}

standings_commands = {"standings" : standings.getStandings}

scoreboard_commands = {"scoreboard" : scoreboard.getScoreboard}

player_commands = {"recent" : player.getPlayerLast3,
                   "stats" : player.getPlayerStats,
                   "livestats" : player.getPlayerLiveStats,
                   "profile" : player.getProfile
}

conf_aliases = {
    "west" : "west",
    "western" : "west",
    "w" : "west",
    "western conference" : "west",
    "east" : "east",
    "eastern" : "east",
    "e" : "east",
    "pacific" : "pacific",
    "northwest": "northwest",
    "southwest": "southwest",
    "atlantic" : "atlantic",
    "central": "central",
    "southeast": "southeast",
    "tank" : "tank",
    "tankathon" : "tank"
}


teams_aliases = { 
    'hawks': '1610612737',
    'atlanta': '1610612737',
    'atl': '1610612737',
    'atlanta hawks': '1610612737',
    'celtics': '1610612738',
    'boston': '1610612738',
    'bos': '1610612738',
    'boston celtics': '1610612738',
    'nets': '1610612751',
    'brooklyn': '1610612751',
    'brk': '1610612751',
    'brooklyn nets': '1610612751',
    'hornets': '1610612766',
    'charlotte': '1610612766',
    'cha': '1610612766',
    'charlotte hornets': '1610612766',
    'bulls': '1610612741',
    'chicago': '1610612741',
    'chi': '1610612741',
    'chicago bulls': '1610612741',
    'cavaliers': '1610612739',
    'cleveland': '1610612739',
    'cle': '1610612739',
    'cleveland cavaliers': '1610612739',
    'cavs': '1610612739',
    'mavericks': '1610612742',
    'dallas': '1610612742',
    'dal': '1610612742',
    'dallas mavericks': '1610612742',
    'mavs': '1610612742',
    'nuggets': '1610612743',
    'denver': '1610612743',
    'den': '1610612743',
    'denver nuggets': '1610612743',
    'pistons': '1610612765',
    'detroit': '1610612765',
    'det': '1610612765',
    'detroit pistons': '1610612765',
    'warriors': '1610612744',
    'golden state': '1610612744',
    'gsw': '1610612744',
    'golden state warriors': '1610612744',
    'rockets': '1610612745',
    'houston': '1610612745',
    'hou': '1610612745',
    'houston rockets': '1610612745',
    'pacers': '1610612754',
    'indiana': '1610612754',
    'ind': '1610612754',
    'indiana pacers': '1610612754',
    'clippers': '1610612746',
    'la clippers': '1610612746',
    'lac': '1610612746',
    'los angeles clippers': '1610612746',
    'lakers': '1610612747',
    'la lakers': '1610612747',
    'lal': '1610612747',
    'los angeles lakers': '1610612747',
    'grizzlies': '1610612763',
    'memphis': '1610612763',
    'mem': '1610612763',
    'memphis grizzlies': '1610612763',
    'heat': '1610612748',
    'miami': '1610612748',
    'mia': '1610612748',
    'miami heat': '1610612748',
    'bucks': '1610612749',
    'milwaukee': '1610612749',
    'mil': '1610612749',
    'bucks': '1610612749',
    'timberwolves': '1610612750',
    'minnesota': '1610612750',
    'min': '1610612750',
    'wolves': '1610612750',
    'minnesota timberwolves': '1610612750',
    'pelicans': '1610612740',
    'new orleans': '1610612740',
    'nop': '1610612740',
    'pels': '1610612740',
    'new orleans pelicans': '1610612740',
    'knicks': '1610612752',
    'new york': '1610612752',
    'nyk': '1610612752',
    'new york knicks': '1610612752',
    'thunder': '1610612760',
    'oklahoma city': '1610612760',
    'okc': '1610612760',
    'oklahoma city thunder': '1610612760',
    'magic': '1610612753',
    'orlando': '1610612753',
    'orl': '1610612753',
    'orlando magic': '1610612753',
    'sixers': '1610612755',
    'philadelphia': '1610612755',
    '76ers': '1610612755',
    '6ers': '1610612755',
    'phi': '1610612755',
    'philadelphia 76ers': '1610612755',
    'suns': '1610612756',
    'phoenix': '1610612756',
    'phx': '1610612756',
    'hawks': '1610612756',
    'blazers': '1610612757',
    'portland': '1610612757',
    'por': '1610612757',
    'trail blazers': '1610612757',
    'portland trail blazers': '1610612757',
    'kings': '1610612758',
    'sacramento': '1610612758',
    'sac': '1610612758',
    'sacramento kings': '1610612758',
    'spurs': '1610612759',
    'san antonio': '1610612759',
    'sas': '1610612759',
    'san antonio spurs': '1610612759',
    'raps': '1610612761',
    'raptors': '1610612761',
    'toronto': '1610612761',
    'craps': '1610612761',
    'tor': '1610612761',
    'toronto raptors': '1610612761',
    'jazz': '1610612762',
    'utah': '1610612762',
    'uta': '1610612762',
    'utah jazz': '1610612762',
    'wizards': '1610612764',
    'washington': '1610612764',
    'wsh': '1610612764',
    'washington wizards': '1610612764'
}


hinkie_quotes = ["The goal is simple: A larger quiver. This quiver will give us more options immediately and more options over time.",
                 "Why do we watch basketball games front to back? Why not watch games back to front, or out of order?",
                 "This approach, like many that create value, isn't popular, particularly locally.",
                 "It's about the willingness to say three simple words : I don't know.",
                 "You have to be non-consensus and right.",
                 "Fear has been the dominant motivator of the actions of too many for too long.",
                 "Maintain the longest view in the room.",
                 "Progress isn't linear.",
                 "We talk a lot about the process, not the outcome.",
                 "A new scientific truth does not triumph by convincing its opponents and making them see the light, but rather because its opponents eventually die.",
                 "Violence at the rim.",
                 "Grit matters.",
                 "In this league, the long view picks at the lock of mediocrity.",
                 "Team building is about one thing - the players.",
                 "Value optionality",
                 "You don't get to the moon by climbing a tree.",
                 "A competitive league like the NBA necessitates a zig while our competitors comfortably zag.",
                 "Sometimes the optimal place for your light is hiding directly under a bushel.",
                 "It is critical to be cycle aware in a talent-driven league."]

def getHinkieQuote():
    return hinkie_quotes[randint(0,len(hinkie_quotes)-1)]


def runCommand(command,args):
        if(args == None):
            if(command in scoreboard_commands):
                return scoreboard_commands[command]()
            elif(command == "quote"):
                return getHinkieQuote()
        else:
            args = args.lower()
            if(command in team_commands):
                return team_commands[command](int(teams_aliases[args]))
            elif(command in standings_commands):
                return standings_commands[command](conf_aliases[args])
            elif(command in scoreboard_commands):
                return scoreboard_commads[command]()
            elif(command in player_commands):
                try:
                    firstName,lastName = args.split(" ",1)
                    return player_commands[command](firstName,lastName)
                except:
                    return "Need player first and last name"
            else:
                return None
