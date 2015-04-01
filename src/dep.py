import re
import sys

all = {}
deps = []

f = open(sys.argv[1])
print "export GOPATH := ~/testgo2/"
for l in f.readlines():
    print l
    l = l.rstrip()
    m =re.match("\#DEP\((.+)\,(.+)\)",l)
    if m:
        g= m.groups()
        remove = "github.com/h4ck3rm1k3/gocore/"
        a =g[0].replace(remove,'')
        b =g[1].replace(remove,'')
        
        prefix = '$(GOPATH)/src/github.com/h4ck3rm1k3/gocore/'

        target= prefix + a + ".o"
        deps.append( target + ":" + prefix + b+ ".o")
        all[target]=1

print "\n".join(deps)
print "all:" + " ".join(all)

f.close()
