from mpyq import MPQArchive
import pprint
import re
import sys

def get_commands(filename):
    archive = MPQArchive(filename, listfile=False)
    script = archive.read_file('war3map.j')
    if not script:
        script = archive.read_file(r'Scripts\war3map.j')
    script = script.decode('utf-8', errors='replace')

    re_str = r'call TriggerRegisterPlayerChatEvent\([^,]*,([^,]*),[ ]*"([^"]*)"[ ]*,[^,]*\)'

    cmds =  dict()
    for player, cmd in re.findall(re_str, script):
        if cmd not in cmds:
            cmds[cmd] = []
        cmds[cmd].append(player.strip())

    return cmds

if __name__ == '__main__':
    filename = sys.argv[1]
    pprint.pprint(get_commands(filename))
