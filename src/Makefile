export LD_LIBRARY_PATH := $(HOME)/gcc-1/build/powerpc64le-unknown-linux-gnu/libgo/.libs/:$(HOME)/gcc-1/build/gcc/:/home/h4ck3rm1k3/install/libexec/gcc/powerpc64le-unknown-linux-gnu/5.0.0/
export PATH := $(HOME)/install/bin:$(PATH)
export GCCGO := gccgo --verbose -save-temps -O0 -L$(HOME)/gcc-1/build/powerpc64le-unknown-linux-gnu/libgo/
export GOTOOLDIR := $(HOME)/gcc-1/build/powerpc64le-unknown-linux-gnu
export GOBIN := $(HOME)/gcc-1/build/powerpc64le-unknown-linux-gnu
export GOPATH := $(HOME)/go/src
export GOROOT := $(HOME)/go
export WORK := /tmp/gccgo/work

tooldir:
	echo $(GOTOOLDIR)
	./gocc env GOTOOLDIR

internalobj:
	go build cmd/internal/obj

bootstrap1:
	/home/h4ck3rm1k3/go1.4/bin/go install -v bootstrap/...

rungo:
	/home/h4ck3rm1k3/go1.4/bin/go

bootstrap2:
	./dist.6 bootstrap -a -v=999

all:  dist.6

go/build.o: go/build/build.go go/build/doc.go go/build/read.go go/build/syslist.go
	$(GCCGO) -c -g -o go/build.o  $^


gocc :  cmd/go/main.go   cmd/go/generate.go		cmd/go/match_test.go	  cmd/go/test.go cmd/go/build.go      cmd/go/generate_test.go	cmd/go/pkg.go		  cmd/go/testgo.go cmd/go/clean.go      cmd/go/get.go		cmd/go/pkg_test.go	  cmd/go/tool.go cmd/go/context.go    cmd/go/go11.go		cmd/go/run.go		  cmd/go/vcs.go  cmd/go/discovery.go  cmd/go/go_windows_test.go	cmd/go/signal.go	  cmd/go/vcs_test.go  cmd/go/doc.go	     cmd/go/help.go	  cmd/go/version.go cmd/go/env.go	     cmd/go/http.go		cmd/go/signal_unix.go	  cmd/go/vet.go cmd/go/fix.go	     cmd/go/list.go		cmd/go/tag_test.go cmd/go/fmt.go	     cmd/go/main.go		cmd/go/testflag.go	cmd/go/generated.go
	$(GCCGO)  -g  -o gocc cmd/go/main.go   cmd/go/generate.go		cmd/go/match_test.go	  cmd/go/test.go cmd/go/build.go      cmd/go/generate_test.go	cmd/go/pkg.go		  cmd/go/testgo.go cmd/go/clean.go      cmd/go/get.go		cmd/go/pkg_test.go	  cmd/go/tool.go cmd/go/context.go    cmd/go/go11.go		cmd/go/run.go		  cmd/go/vcs.go  cmd/go/discovery.go  cmd/go/go_windows_test.go	cmd/go/signal.go	  cmd/go/vcs_test.go  cmd/go/doc.go	     cmd/go/help.go	  cmd/go/version.go cmd/go/env.go	     cmd/go/http.go		cmd/go/signal_unix.go	  cmd/go/vet.go cmd/go/fix.go	     cmd/go/list.go		cmd/go/tag_test.go cmd/go/fmt.go	     cmd/go/testflag.go		cmd/go/generated.go

trycgo: ./gocc
	./gocc build -v -x -compiler gccgo -work -n -a runtime/cgo

trycgo2: ./gocc
	strace -o strace.txt -f -s9999  ./gocc build -gccgoflags '-save-temps --verbose' -v -x -compiler gccgo -work -n -a runtime/cgo

trycmd: ./gocc
	./gocc build -v -x -compiler gccgo -work -n -a cmd/

tryfmt: ./gocc
	./gocc build -v -x -compiler gccgo -work -n -a fmt/

clean :
	find -name *.o -exec rm {} \;
	rm gocc

normal:
	bash ./all.bash


dist.6: cmd/dist/build.go cmd/dist/buildgo.go cmd/dist/buildruntime.go cmd/dist/buildtool.go cmd/dist/main.go cmd/dist/sys_default.go cmd/dist/util.go
	$(GCCGO) -g  -o dist.6 $^


cmd/internal/obj.o: cmd/internal/obj/ar.go cmd/internal/obj/data.go cmd/internal/obj/flag.go cmd/internal/obj/fmt.go cmd/internal/obj/funcdata.go cmd/internal/obj/go.go cmd/internal/obj/ld.go cmd/internal/obj/libc.go cmd/internal/obj/link.go cmd/internal/obj/mgc0.go cmd/internal/obj/obj.go cmd/internal/obj/objfile.go cmd/internal/obj/pass.go cmd/internal/obj/pcln.go cmd/internal/obj/stack.go cmd/internal/obj/sym.go cmd/internal/obj/textflag.go cmd/internal/obj/typekind.go cmd/internal/obj/util.go
	$(GCCGO) -c  -g -o $@ $^

DEPS = cmd/internal/obj/x86/6.out.go cmd/internal/obj/x86/anames6.go cmd/internal/obj/x86/asm6.go cmd/internal/obj/x86/list6.go cmd/internal/obj/x86/obj6.go cmd/internal/obj/x86/util.go

cmd/internal/obj/x86.o : cmd/internal/obj.o  $(DEPS)
	$(GCCGO) -L . -I . -c -g -o $@ $(DEPS)


galign6 : cmd/6g/galign.go
	$(GCCGO) -L . -I .  -g -o $@ $^ cmd/internal/obj.o

gg6:  cmd/6g/gg.go
	$(GCCGO) -L . -I .  -g -o $@ $^ cmd/internal/obj.o

ggen6:  cmd/6g/ggen.go
	$(GCCGO) -L . -I .  -g -o $@ $^ cmd/internal/obj.o

gsubr6: cmd/6g/gsubr.go
	$(GCCGO) -L . -I .  -g -o $@ $^ cmd/internal/obj.o

peep6: cmd/6g/peep.go
	$(GCCGO) -L . -I .  -g -o $@ $^ cmd/internal/obj.o

prog6: cmd/6g/prog.go
	$(GCCGO) -L . -I .  -g -o $@ $^ cmd/internal/obj.o

reg6: cmd/6g/reg.go
	$(GCCGO) -L . -I .  -g -o $@ $^ cmd/internal/obj.o

util6: cmd/6g/util.go
	$(GCCGO) -L . -I .  -g -o $@ $^ cmd/internal/obj.o

asm6 : ./cmd/asm/main.go cmd/internal/obj.o cmd/asm/internal/arch.o cmd/asm/internal/flags.o
	$(GCCGO) -I. -L. -g -o $@ $^

cmd/asm/internal/arch.o : ./cmd/asm/internal/arch/arch.go  cmd/internal/obj/x86.o
	$(GCCGO) -c -g -o $@ $^

cmd/asm/internal/flags.o: ./cmd/asm/internal/flags/flags.go
	$(GCCGO) -c -g -o $@ $^

lex6: cmd/6a/lex.go cmd/asm/internal/flags.o  \
	cmd/internal/obj.o      \
	text/scanner.o          \
	cmd/asm/internal/lex.o  \
	cmd/internal/obj/x86.o  \
	cmd/asm/internal/arch.o \
	cmd/internal/gc.o \
	cmd/internal/asm.o
	$(GCCGO) -L. -I. -g -o $@ $^

text/scanner.o : text/scanner/scanner.go
	$(GCCGO) -c -g -o $@ $^

cmd/asm/internal/lex.o: ./cmd/asm/internal/lex/input.go \
	 ./cmd/asm/internal/lex/lex.go \
	 ./cmd/asm/internal/lex/slice.go \
	 ./cmd/asm/internal/lex/stack.go \
	 ./cmd/asm/internal/lex/tokenizer.go \
	text/scanner.o
	$(GCCGO) -L. -I. -c -g -o $@ ./cmd/asm/internal/lex/input.go \
	 ./cmd/asm/internal/lex/lex.go \
	 ./cmd/asm/internal/lex/slice.go \
	 ./cmd/asm/internal/lex/stack.go \
	 ./cmd/asm/internal/lex/tokenizer.go



cmd/asm/internal/asm.o: cmd/asm/internal/lex.o cmd/asm/internal/flags.o cmd/asm/internal/asm/asm.go cmd/asm/internal/asm/parse.go cmd/asm/internal/lex.o cmd/asm/internal/arch.o
	$(GCCGO)  -g -c -o $@ cmd/asm/internal/asm/asm.go cmd/asm/internal/asm/parse.go

cmd/internal/asm.o: cmd/internal/obj.o cmd/internal/asm/asm2.go \
	cmd/internal/asm/asm.go  \
	cmd/internal/asm/lexbody.go \
	cmd/internal/asm/macbody.go
	$(GCCGO) -g -c -o $@ cmd/internal/asm/asm2.go \
	cmd/internal/asm/asm.go  \
	cmd/internal/asm/lexbody.go \
	cmd/internal/asm/macbody.go

cmd/internal/gc.o:  ./cmd/internal/gc/align.go \
	 ./cmd/internal/gc/array.go \
	 ./cmd/internal/gc/bits.go \
	 ./cmd/internal/gc/builtin.go \
	 ./cmd/internal/gc/builtins/runtime.go \
	 ./cmd/internal/gc/builtins/unsafe.go \
	 ./cmd/internal/gc/bv.go \
	 ./cmd/internal/gc/closure.go \
	 ./cmd/internal/gc/const.go \
	 ./cmd/internal/gc/cplx.go \
	 ./cmd/internal/gc/dcl.go \
	 ./cmd/internal/gc/esc.go \
	 ./cmd/internal/gc/export.go \
	 ./cmd/internal/gc/fmt.go \
	 ./cmd/internal/gc/gen.go \
	 ./cmd/internal/gc/go.go \
	 ./cmd/internal/gc/gsubr.go \
	 ./cmd/internal/gc/init.go \
	 ./cmd/internal/gc/inl.go \
	 ./cmd/internal/gc/lex.go \
	 ./cmd/internal/gc/md5.go \
	 ./cmd/internal/gc/mparith1.go \
	 ./cmd/internal/gc/mparith2.go \
	 ./cmd/internal/gc/mparith3.go \
	 ./cmd/internal/gc/obj.go \
	 ./cmd/internal/gc/opnames.go \
	 ./cmd/internal/gc/order.go \
	 ./cmd/internal/gc/pgen.go \
	 ./cmd/internal/gc/plive.go \
	 ./cmd/internal/gc/popt.go \
	 ./cmd/internal/gc/racewalk.go \
	 ./cmd/internal/gc/range.go \
	 ./cmd/internal/gc/reflect.go \
	 ./cmd/internal/gc/reg.go \
	 ./cmd/internal/gc/select.go \
	 ./cmd/internal/gc/sinit.go \
	 ./cmd/internal/gc/subr.go \
	 ./cmd/internal/gc/swt.go \
	 ./cmd/internal/gc/typecheck.go \
	 ./cmd/internal/gc/unsafe.go \
	 ./cmd/internal/gc/util.go \
	 ./cmd/internal/gc/walk.go \
	 ./cmd/internal/gc/y.go
	$(GCCGO) -c -g -o $@ $^


bootstrap: lex6 galign6 cgen6 galign6 gg6 ggen6 gsubr6 peep6 prog6 reg6 util6 asm6
