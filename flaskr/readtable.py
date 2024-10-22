# functions to populate the embed

from sqlalchemy import select
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sql_tables import Move
import imageparser

# user = "postgres"
# password = "Pviet95."
# host = "localhost"
# port = "5432"
# database = "VSAV"

user = "postgres.zuidpuiggoibnnvrtbfn"
password = "xDohks76sW%Y"
host = "aws-0-us-east-1.pooler.supabase.com"
port = "6543"
database = "postgres"

# for creating connection string
connection_str = f"postgresql://{user}:{password}@{host}:{port}/{database}"
engine = create_engine(connection_str, echo=True)


# def lookupMove(character, request):
#     stmt = select(
#         Move.reddmg,
#         Move.whitedmg,
#         Move.guard,
#         Move.startup,
#         Move.active,
#         Move.recovery,
#         Move.advHit,
#         Move.advBlock,
#         Move.advTech,
#         Move.invul,
#         Move.cancel,
#         Move.renda,
#         Move.meter,
#         Move.reaction,
#     ).where(Move.chara == character, Move.input == request)
#     with Session(engine) as session:
#         for x in session.execute(stmt):
#             return (
#                 "reddmg: "
#                 + x[0]
#                 + "\nwhitedmg: "
#                 + x[1]
#                 + "\nguard: "
#                 + x[2]
#                 + "\nstartup: "
#                 + x[3]
#                 + "\nactive: "
#                 + x[4]
#                 + "\nrecovery: "
#                 + x[5]
#                 + "\nadvHit: "
#                 + x[6]
#                 + "\nadvBlock: "
#                 + x[7]
#                 + "\nadvTech: "
#                 + x[8]
#                 + "\ninvul: "
#                 + x[9]
#                 + "\ncancel: "
#                 + x[10]
#                 + "\nrenda: "
#                 + x[11]
#                 + "\nmeter: "
#                 + x[12]
#                 + "\nreaction: "
#                 + x[13]
#             )

def formatMove(dic):
    print(dic)
    formattedString = ""
    for item in dic:
        formattedString += item + ': ' + str(dic[item]) + '\n'
    return formattedString

def lookupMove(character, request):
    stmt = select(
        Move.reddmg,
        Move.whitedmg,
        Move.guard,
        Move.startup,
        Move.active,
        Move.recovery,
        Move.advHit,
        Move.advBlock,
        Move.advTech,
        Move.invul,
        Move.cancel,
        Move.renda,
        Move.meter,
        Move.reaction,
    ).where(Move.chara == character, Move.input == request)
    # movepropdict = {'reddmg': x[0], 'whitedmg': x[1], 'guard': x[2], 'startup': x[3], 'active': x[4]}
    movepropdict = {
        "reddmg": "",
        "whitedmg": "",
        "guard": "",
        "startup": "",
        "active": "",
        "recovery": "",
        "advHit": "",
        "advBlock": "",
        "advTech": "",
        "invul": "",
        "cancel": "",
        "renda": "",
        "meter": "",
        "reaction": "",
    }
    res = {}
    with Session(engine) as session:
        for x in session.execute(stmt):
            movepropdict["reddmg"] = x[0]
            movepropdict["whitedmg"] = x[1]
            movepropdict["guard"] = x[2]
            movepropdict["startup"] = x[3]
            movepropdict["active"] = x[4]
            movepropdict["recovery"] = x[5]
            movepropdict["advHit"] = x[6]
            movepropdict["advBlock"] = x[7]
            movepropdict["advTech"] = x[8]
            movepropdict["invul"] = x[9]
            movepropdict["cancel"] = x[10]
            movepropdict["renda"] = x[11]
            movepropdict["meter"] = x[12]
            movepropdict["reaction"] = x[13]
            #res = {}
            for key, value in movepropdict.items():
                if value is not None:
                    res[key] = value
            return formatMove(res)

# lookupMove('Victor', '5LP')




def getCharByAlias(dictionary, alias):
    try:
        for n, alist in dictionary.items():
            for x in alist:
                if alias == x:
                    return(alist[0])
        # print(type(alias))
    except:
        print('not found')



def lookupMoveList(character):
    stmt = select(Move.input).where(Move.chara == character)
    with Session(engine) as session:
        return list(session.execute(stmt))


def findHitbox(character, request):
    stmt = select(Move.hitboxes).where(Move.chara == character, Move.input == request)
    with Session(engine) as session:
        image_url_list = []
        for x in session.execute(stmt):
            parsedfilesuffixes = imageparser.imageparser(x)
            for j in parsedfilesuffixes:
                image_url_list.append(f"https://wiki.gbl.gg{j}")

            return image_url_list


# pulls from wiki for character image
def findCharPic(character):
    if character == "Anakaris":
        return "https://wiki.gbl.gg/images/thumb/3/3b/Vsav-nav-portrait-anakaris.gif/70px-Vsav-nav-portrait-anakaris.gif"
    elif character == "Aulbath":
        return "https://wiki.gbl.gg/images/thumb/6/6f/Vsav-nav-portrait-aulbath.gif/70px-Vsav-nav-portrait-aulbath.gif"
    elif character == "Bishamon":
        return "https://wiki.gbl.gg/images/thumb/0/04/Vsav-nav-portrait-bishamon.gif/70px-Vsav-nav-portrait-bishamon.gif"
    elif character == "Bulleta":
        return "https://wiki.gbl.gg/images/thumb/a/a4/Vsav-nav-portrait-bulleta.gif/70px-Vsav-nav-portrait-bulleta.gif"
    elif character == "Demitri":
        return "https://wiki.gbl.gg/images/thumb/d/d7/Vsav-nav-portrait-demitri.gif/70px-Vsav-nav-portrait-demitri.gif"
    elif character == "Felicia":
        return "https://wiki.gbl.gg/images/thumb/b/ba/Vsav-nav-portrait-felicia.gif/70px-Vsav-nav-portrait-felicia.gif"
    elif character == "Gallon":
        return "https://wiki.gbl.gg/images/thumb/8/88/Vsav-nav-portrait-gallon.gif/70px-Vsav-nav-portrait-gallon.gif"
    elif character == "Jedah":
        return "https://wiki.gbl.gg/images/thumb/4/4a/Vsav-nav-portrait-jedah.gif/70px-Vsav-nav-portrait-jedah.gif"
    elif character == "Lei-Lei":
        return "https://wiki.gbl.gg/images/thumb/2/26/Vsav-nav-portrait-lei-lei.gif/70px-Vsav-nav-portrait-lei-lei.gif"
    elif character == "Lilith":
        return "https://wiki.gbl.gg/images/thumb/3/3b/Vsav-nav-portrait-lilith.gif/70px-Vsav-nav-portrait-lilith.gif"
    elif character == "Morrigan":
        return "https://wiki.gbl.gg/images/thumb/7/7f/Vsav-nav-portrait-morrigan.gif/70px-Vsav-nav-portrait-morrigan.gif"
    elif character == "Q-Bee":
        return "https://wiki.gbl.gg/images/thumb/b/b5/Vsav-nav-portrait-q-bee.gif/70px-Vsav-nav-portrait-q-bee.gif"
    elif character == "Sasquatch":
        return "https://wiki.gbl.gg/images/thumb/2/24/Vsav-nav-portrait-sasquatch.gif/70px-Vsav-nav-portrait-sasquatch.gif"
    elif character == "Victor":
        return "https://wiki.gbl.gg/images/thumb/1/18/Vsav-nav-portrait-victor.gif/70px-Vsav-nav-portrait-victor.gif"
    elif character == "Zabel":
        return "https://wiki.gbl.gg/images/thumb/5/5a/Vsav-nav-portrait-zabel.gif/70px-Vsav-nav-portrait-zabel.gif"
