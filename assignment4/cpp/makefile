.PHONY: build-d build-r run-d run-r

build-d:
	clang++ -std=c++11 -g -O0 -o debug.exe triangulate.cpp

build-r:
	clang++ -std=c++11 -O3 -o release.exe triangulate.cpp

run-d:
	./debug_exe

run-r:
	./release_exe