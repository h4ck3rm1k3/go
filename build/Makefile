export LD_LIBRARY_PATH := $(HOME)/gcc-1/build/powerpc64le-unknown-linux-gnu/libgo/.libs/:$(HOME)/gcc-1/build/gcc/:/home/h4ck3rm1k3/install/libexec/gcc/powerpc64le-unknown-linux-gnu/5.0.0/
export PATH := $(HOME)/install/bin:$(PATH)
export GCCGO := $(HOME)/gcc-1/build/gcc/gccgo
export GOTOOLDIR := $(HOME)/gcc-1/build/powerpc64le-unknown-linux-gnu
export GOBIN := $(HOME)/gcc-1/build/powerpc64le-unknown-linux-gnu
export GOPATH := $(HOME)/go/build/
export GOROOT := $(HOME)/go
export WORK := /tmp/gccgo/work

compile:
	#strace -f -s 99 -o strace.txt
	~/go/src/gocc build -v -x -compiler gccgo -work  -a github.com/h4ck3rm1k3/gocore/...

setup:
	rm -rf /home/h4ck3rm1k3/testgo/src/github.com/h4ck3rm1k3/gocore/*
	mkdir -p $(GOPATH)/src/github.com/h4ck3rm1k3/gocore/
	cp -r ~/go/src/* $(GOPATH)/src/github.com/h4ck3rm1k3/gocore/
