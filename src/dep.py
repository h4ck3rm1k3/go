import re
import sys

f = open(sys.argv[1])
for l in f.readlines():
    l = l.rstrip()
    m =re.match("\#DEP\((.+)\,(.+)\)",l)
    if m:
        g= m.groups()
        remove = "github.com/h4ck3rm1k3/gocore/"
        a =g[0].replace(remove,'')
        b =g[1].replace(remove,'')
        
        prefix = '$(GOPATH)/src/github.com/h4ck3rm1k3/gocore/'
        print prefix + a + ".o :" + prefix + b+ ".o"
f.close()
