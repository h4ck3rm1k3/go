export LD_LIBRARY_PATH := $(HOME)/install/lib64/
export GOROOT_BOOTSTRAP:= $(HOME)/install
#export GOROOT := /home/h4ck3rm1k3/go
#export GOPATH := /home/h4ck3rm1k3/go/src
#export GOROOT_BOOTSTRAP=~/gccgo_for_bootstrap

bootstrap2 :
	/home/h4ck3rm1k3/go/bin/go install -v bootstrap/...

bootstrap :
	bash -x ./make.bash

test1:
	/home/h4ck3rm1k3/gcc-1/build/gcc/go1 -dumpbase sometest.go  -g -version  -I /home/h4ck3rm1k3/testgo2/src -L/home/h4ck3rm1k3/install/lib/gcc/powerpc64le-unknown-linux-gnu/5.0.0 -L/home/h4ck3rm1k3/install/lib/gcc/powerpc64le-unknown-linux-gnu/5.0.0/../../../../lib64 -L/lib/../lib64 -L/usr/lib/../lib64 -L/home/h4ck3rm1k3/install/lib/gcc/powerpc64le-unknown-linux-gnu/5.0.0/../../.. -fgo-dump-ast total.go
	cat total.go.dump.ast


cgox : $(HOME)/go/src/cmd/cgo/ast.go $(HOME)/go/src/cmd/cgo/doc.go $(HOME)/go/src/cmd/cgo/gcc.go \
	$(HOME)/go/src/cmd/cgo/godefs.go $(HOME)/go/src/cmd/cgo/main.go $(HOME)/go/src/cmd/cgo/out.go $(HOME)/go/src/cmd/cgo/util.go \
	$(HOME)/go/src/cmd/cgo/gen.go 
	/home/h4ck3rm1k3/install/bin/gccgo -I $(WORK) --verbose -fgo-dump-ast -g -fgo-relative-import-path=$(HOME)/go/src/cmd/cgo -o cgox \
	$(HOME)/go/src/cmd/cgo/ast.go \
	$(HOME)/go/src/cmd/cgo/doc.go \
	$(HOME)/go/src/cmd/cgo/gcc.go \
	$(HOME)/go/src/cmd/cgo/godefs.go \
	$(HOME)/go/src/cmd/cgo/main.go \
	$(HOME)/go/src/cmd/cgo/out.go \
	$(HOME)/go/src/cmd/cgo/util.go \
	$(HOME)/go/src/cmd/cgo/gen.go \

test : cgox
	LD_LIBRARY_PATH=/home/h4ck3rm1k3/install/lib64/ ./cgox -gccgo=true -debug-gcc=true -debug-define=true  test123.go
