#cd /home/h4ck3rm1k3/go/src/cmd/dist
WORK=.

gccgo -I $WORK -c -g -fgo-relative-import-path=cmd/dist -o cmd/dist.o ./cmd/dist/build.go ./cmd/dist/buildgo.go ./cmd/dist/buildruntime.go ./cmd/dist/buildtool.go ./cmd/dist/main.go ./cmd/dist/sys_default.go ./cmd/dist/test.go ./cmd/dist/util.go ./cmd/dist/util_gccgo.go
ar cru cmd/libdist.a cmd/dist.o
gccgo -o cmd/dist/dist cmd/dist.o 
./cmd/dist/dist env -p
