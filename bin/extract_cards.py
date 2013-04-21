import sqlite3
import json
import sys



db = sqlite3.connect(sys.argv[1])
db.row_factory = sqlite3.Row

for card in db.execute(
            "select * from cards"):
  c = dict()
  c['id'] = card['id']
  c['reviews'] = list()

  for r in db.execute("select * from revlog where cid = ? order by id asc", (card['id'], )):
    correct = False

    c['reviews'].append({
        'datetime' : r['id'],
        'correct' : r['ease'] > 1,
        'ease' : r['ease']
      })

  print json.dumps(c)
