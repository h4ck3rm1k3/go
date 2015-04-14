#mkdir -p ~/gccgo_for_bootstrap/bin;
#ln -s /usr/bin/go-5 ~/gccgo_for_bootstrap/bin/go;
export GOROOT_BOOTSTRAP=~/install
#export GOROOT_BOOTSTRAP=~/gccgo_for_bootstrap
./make.bash
