import json

def convert() :
 f = open("log_events.log", "r")
 content = f.read()
 splitcontent = content.splitlines()

 for line in splitcontent :
    pipesplit = line.split(' | ')
    print(pipesplit)
    with open("json_log.json", 'a') as fout:
        json.dump(pipesplit, fout, indent=4)