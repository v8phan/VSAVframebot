# scrape frame data from site and add to Postgresql db
from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.orm import sessionmaker, declarative_base
import requests
from moveparser import moveparser, listoftuples
from sql_tables import Move, engine
from sqlalchemy.orm import Session
from sqlalchemy import create_engine

characterList = [
    ("Anakaris", "ana.png"),
    ("Aulbath", "aul.png"),
    ("Bishamon", "bis.png"),
    ("Bulleta", "bul.png"),
    ("Demitri", "dem.png"),
    ("Felicia", "fel.png"),
    ("Gallon", "gal.png"),
    ("Jedah", "jed.png"),
    ("Lei-Lei", "lei.png"),
    ("Lilith", "lil.png"),
    ("Morrigan", "mor.png"),
    ("Q-Bee", "bee.png"),
    ("Sasquatch", "sas.png"),
    ("Victor", "vic.png"),
    ("Zabel", "zab.png")
]

#change targeted character name here
request = requests.get(
         f"https://wiki.gbl.gg/index.php?title=Vampire_Savior/Zabel/Data&action=edit"
     )

moveChunks = request.text.split("FrameData-VSAV")

#for Anakaris
# with Session(engine) as session:
#     for chunk in moveChunks:
#         if 'moveId' in chunk:
#             # for x in listoftuples:
#                 print('THE STRING CHUNK HERE'+ chunk)
#                 newMove = Move(                     
#                     chara=moveparser(chunk, listoftuples[0][0], listoftuples[0][1]),
#                     moveId=moveparser(chunk, listoftuples[1][0], listoftuples[1][1]),
#                     input=moveparser(chunk, listoftuples[2][0], listoftuples[2][1]),
#                     images=moveparser(chunk, listoftuples[3][0], listoftuples[3][1]),
#                     hitboxes=moveparser(chunk, listoftuples[4][0], listoftuples[4][1]),
#                     reddmg=moveparser(chunk, listoftuples[5][0], listoftuples[5][1]),
#                     whitedmg=moveparser(chunk, listoftuples[6][0], listoftuples[6][1]),
#                     guard=moveparser(chunk, listoftuples[7][0], listoftuples[7][1]),
#                     startup=moveparser(chunk, listoftuples[8][0], listoftuples[8][1]),
#                     active=moveparser(chunk, listoftuples[9][0], listoftuples[9][1]),
#                     recovery=moveparser(chunk, listoftuples[10][0], listoftuples[10][1]),
#                     advHit=moveparser(chunk, listoftuples[11][0], listoftuples[11][1]),
#                     #
#                     advBlock=moveparser(chunk, listoftuples[19][0], listoftuples[19][1]),
#                     #
#                     invul=moveparser(chunk, listoftuples[14][0], listoftuples[14][1]),
#                     cancel=moveparser(chunk, listoftuples[15][0], listoftuples[15][1]),
#                     renda=moveparser(chunk, listoftuples[16][0], listoftuples[16][1]),
#                     meter=moveparser(chunk, listoftuples[17][0], listoftuples[17][1]),
#                     #
#                     advTech='',
#                     reaction=moveparser(chunk, listoftuples[20][0], listoftuples[20][1]),
#                     cursetime=moveparser(chunk, listoftuples[21][0], listoftuples[21][1])
#                     #
#                     )
#                 session.add(newMove)
#                 session.commit()
#     exit()

#for everyone else
with Session(engine) as session:
    for chunk in moveChunks:
        if ' = throw' in chunk:
            # print('THE STRING CHUNK HERE'+ chunk)
            newMove = Move(
                chara=moveparser(chunk, listoftuples[0][0], listoftuples[0][1]),
                moveId=moveparser(chunk, listoftuples[1][0], listoftuples[1][1]),
                input=moveparser(chunk, listoftuples[2][0], listoftuples[2][1]),
                images=moveparser(chunk, listoftuples[3][0], listoftuples[3][1]),
                hitboxes=moveparser(chunk, listoftuples[4][0], listoftuples[4][1]),
                reddmg=moveparser(chunk, listoftuples[5][0], listoftuples[5][1]),
                whitedmg=moveparser(chunk, listoftuples[6][0], listoftuples[6][1]),
                guard=moveparser(chunk, listoftuples[7][0], listoftuples[7][1]),
                startup=moveparser(chunk, listoftuples[8][0], listoftuples[8][1]),
                active=moveparser(chunk, listoftuples[9][0], listoftuples[9][1]),
                recovery=moveparser(chunk, listoftuples[10][0], listoftuples[10][1]),
                advHit=moveparser(chunk, listoftuples[11][0], listoftuples[11][1]),
                advBlock=moveparser(chunk, listoftuples[12][0], listoftuples[12][1]),
                advTech=moveparser(chunk, listoftuples[13][0], listoftuples[13][1]),
                invul=moveparser(chunk, listoftuples[14][0], listoftuples[14][1]),
                cancel=moveparser(chunk, listoftuples[15][0], listoftuples[15][1]),
                renda=moveparser(chunk, listoftuples[16][0], listoftuples[16][1]),
                meter=moveparser(chunk, listoftuples[17][0], listoftuples[17][1]),
                reaction=moveparser(chunk, listoftuples[18][0], listoftuples[18][1]),
                cursetime=''
            )
            #add logic to check if move already exists in db here
            if newMove.moveId not in ('LI_412[6]KK'):
                session.add(newMove)
                session.commit()
        elif 'moveId' in chunk:
            # print('THE STRING CHUNK HERE'+ chunk)
            newMove = Move(
                chara=moveparser(chunk, listoftuples[0][0], listoftuples[0][1]),
                moveId=moveparser(chunk, listoftuples[1][0], listoftuples[1][1]),
                input=moveparser(chunk, listoftuples[2][0], listoftuples[2][1]),
                images=moveparser(chunk, listoftuples[3][0], listoftuples[3][1]),
                hitboxes=moveparser(chunk, listoftuples[4][0], listoftuples[4][1]),
                reddmg=moveparser(chunk, listoftuples[5][0], listoftuples[5][1]),
                whitedmg=moveparser(chunk, listoftuples[6][0], listoftuples[6][1]),
                guard=moveparser(chunk, listoftuples[7][0], listoftuples[7][1]),
                startup=moveparser(chunk, listoftuples[8][0], listoftuples[8][1]),
                active=moveparser(chunk, listoftuples[9][0], listoftuples[9][1]),
                recovery=moveparser(chunk, listoftuples[10][0], listoftuples[10][1]),
                advHit=moveparser(chunk, listoftuples[11][0], listoftuples[11][1]),
                advBlock=moveparser(chunk, listoftuples[12][0], listoftuples[12][1]),
                advTech='',
                invul=moveparser(chunk, listoftuples[14][0], listoftuples[14][1]),
                cancel=moveparser(chunk, listoftuples[15][0], listoftuples[15][1]),
                renda=moveparser(chunk, listoftuples[16][0], listoftuples[16][1]),
                meter=moveparser(chunk, listoftuples[17][0], listoftuples[17][1]),
                reaction=moveparser(chunk, listoftuples[18][0], listoftuples[18][1]),
                cursetime=''
            )
            if newMove.moveId not in ('LI_412[6]KK'):
                session.add(newMove)
                session.commit()
    exit()
    
#                 # print('CHARA HERE IS '+ moveparser(chunk, listoftuples[0][0], listoftuples[0][1]))
#                 # print(newMove)
              

