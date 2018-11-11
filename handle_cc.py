import re
import sys

def mipmap(filename):
    with open(filename+".bak", "w") as targetf:
        lines = []
        with open(filename) as sourcef:
            for line in sourcef:
                line = line.strip()
                if not line:
                    continue
                if re.search(r"^\d+", line):
                    continue
                line, _ = re.subn(r"<.*?", " ", line)
                for item in line:
                    item.lower()
                lines.append(line)
            targetf.write("".join(lines))


mipmap("Jim_Acoasta_Trump.srt")
