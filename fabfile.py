from fabric.api import *
import re

def status(server=None):
    if server is not None:
        rough_status = local("vagrant status %s" % server, capture=True)
    else:
        rough_status = local("vagrant status", capture=True)

    lines = []
    for line in rough_status.split("\n"):
        print line
        if re.match("^core-[0-9]{1,2}\\s+", line):
            chunks = re.split("\\s+", line)
            lines.append(
            #lines.append(re.split("\\s+", line))
    print "\n".join([str(line) for line in lines])


