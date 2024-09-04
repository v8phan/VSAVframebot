# from sql_tables import Move
import requests


listoftuples = [
    ("chara = ", "| moveId"),
    ("moveId = ", "| input"),
    ("input = ", "| images"),
    ("images = ", "| hitboxes"),
    ("hitboxes = ", "| reddmg"),
    ("reddmg = ", "| whitedmg"),
    ("whitedmg = ", "| guard"),
    ("guard = ", "| startup"),
    ("startup = ", "| active"),
    ("active = ", "| recovery"),
    ("recovery = ", "| advHit"),
    ("advHit = ", "| advBlock"),
    ("advBlock = ", "| advTech"),
    ("advTech = ", "| invul"),
    ("invul = ", "| cancel"),
    ("cancel = ", "| renda"),
    ("renda = ", "| meter"),
    ("meter = ", "| reaction"),
    ("reaction = ", "} "),
    # for anakaris
    ("advBlock = ", "| invul"),
    ("reaction = ", "| cursetime"),
    ("cursetime = ", "} "),
]


# parses through text element fstring


# split text into separate lines, check if field exists in chunk first
def moveparser(text, sub1, sub2):

    idx1 = text.find(sub1)
    idx2 = text.find(sub2)
    if (
        #"Aulbath | "
        #"Anakaris | "
        #"Bishamon | "
        #"Bulleta | "
        #"Demitri | "
        #"Felicia | "
        #"Gallon | "
        #"Jedah | "
        #"Lei-Lei | "
        #"Lilith | "
        #"Q-Bee | "
        #"Sasquatch | "
        #"Victor | "
        "Zabel | " 
        in text[idx1 + len(sub1) : idx2]
    ):
        return ""
    else:
        return text[idx1 + len(sub1) : idx2].rstrip()


# request = requests.get(
#          f"https://wiki.gbl.gg/index.php?title=Vampire_Savior/Anakaris/Data&action=edit"
#      )

# moveChunks = request.text.split("FrameData-VSAV")

# fchunk in moveChunks:
#     if "moveId" in chunk:
#         print(chunk)
#         print('\n==========BREAK===============\n')

# if 'moveId' in moveChunks:
#     fx in moveChunks
#     print('CHARA IS ' + moveparser(moveChunks, listoftuples[0][0], listoftuples[0][1]))
#     print('MOVEID IS ' + moveparser(moveChunks, listoftuples[1][0], listoftuples[1][1]))

# test
text = """| chara = Anakaris | moveId = AN_5LP
| input = 5LP
| images = vsav-AN-5-lp.png
| hitboxes = vsav-AN-5-lp-hitbox.png
| reddmg = 9
| whitedmg = 5
| guard = mid
| startup = 5
| active = 3
| recovery = 8
| advHit = 8
| advBlock = 7
| invul =
| cancel = yes
| renda = N/A
| meter = H: 6 G: 3 W: 0
| reaction = knockback
| cursetime =
}}

=====&lt;font style="visibility:hidden; float:right">5MP&lt;/font>=====
{{
"""
# print('moveid is ' + moveparser(text, listoftuples[1][0], listoftuples[1][1]))
