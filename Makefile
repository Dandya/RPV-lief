all: build

build:
	make -C replacing
	make -C adding
	make -C linking

clean:
	make -C replacing clean || true
	make -C adding clean || true
	make -C linking clean || true