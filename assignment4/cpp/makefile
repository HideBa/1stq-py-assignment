
.PHONY gendebug
gendebug:
	clang++ -g -O0 -o debug_exe triangulate.cpp


.PHONY genrelease
genrelease:
	clang++ -O3 -o release_exe triangulate.cpp

.PHONY run-d
run-d:
	./debug_exe

.PHONY run-r
run-r:
	./release_exe