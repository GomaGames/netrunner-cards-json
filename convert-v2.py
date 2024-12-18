'''
Reads a v1 pack.json and expands it to individual v2 json cards.

Usage:

    python convert-v2.py pack/{set-name}.json

'''
import csv
import json
import os
import sys

if len(sys.argv) < 2:
    os.sys.stderr.write("Missing arguments.\nUsage: python convert-v2.py pack/{set-name}.json\n")
    os.sys.exit(1)

json_path = sys.argv[1]
printings = []
count = 0

if os.path.isfile(json_path):
    with open(json_path, "r") as file:
        pack_json = json.load(file)
        for row in pack_json:
            card_json_path = "./v2/cards/%s.json" % row['id']
            if 'subtypes' in row:
                try:
                    row['subtypes'] = json.loads(row['subtypes'])
                except:
                    pass
            if 'advancement_requirement' in row:
                row['advancement_requirement'] = int(row['advancement_requirement'])
            if 'agenda_points' in row:
                row['agenda_points'] = int(row['agenda_points'])
            if 'deck_limit' in row:
                row['deck_limit'] = int(row['deck_limit'])
            if 'is_unique' in row:
                row['is_unique'] = bool(row['is_unique'])
            elif 'uniqueness' in row:
                row['is_unique'] = bool(row['uniqueness'])
            if 'cost' in row:
                row['cost'] = int(row['cost'])
            if 'deck_limit' in row:
                row['deck_limit'] = int(row['deck_limit'])
            if 'influence_limit' in row:
                row['influence_limit'] = int(row['influence_limit'])
            if 'minimum_deck_size' in row:
                row['minimum_deck_size'] = int(row['minimum_deck_size'])
            if 'trash_cost' in row:
                row['trash_cost'] = int(row['trash_cost'])
            if 'strength' in row:
                row['strength'] = int(row['strength'])
            if 'memory_cost' in row:
                row['memory_cost'] = int(row['memory_cost'])
            if 'quantity' in row:
                row['quantity'] = int(row['quantity'])
            if 'type_code' in row:
                row['card_type_id'] = row['type_code']
            if 'side_code' in row:
                row['side_id'] = row['side_code']
            if 'faction_code' in row:
                row['faction_id'] = row['faction_code'].replace('-','_')
            if 'base_link' in row:
                row['base_link'] = int(row['base_link'])
            if 'faction_cost' in row:
                row['influence_cost'] = int(row['faction_cost'])

            with open(card_json_path, "w") as file:
                file.write(json.dumps(row, indent=2))
                count+=1
                print("Wrote card json to %s" % card_json_path)

            printing = {
                "card_id": row['id'],
                "card_set_id": 'fire_and_fealty',
                "id": row['code'],
                "illustrator": "",
                "position": int(row['position']),
                "quantity": int(row['quantity']),
                "released_by": "santa"
            }

            if 'flavor' in row:
                printing["flavor"] = row['flavor']

            printings.append(printing)

print("Done writing %d files." % count)

with open("./v2/printings/fire_and_fealty.json", "w") as file:
    file.write(json.dumps(printings, indent=2))
    print("Wrote printings json to ./v2/printings/fire_and_fealty.json")

