all: libdata.so libwho.so libprint.so

libdata.so:
	gcc data.c -shared -o libdata.so

libwho.so:
	gcc who.c -shared -o libwho.so

libprint.so:
	gcc print.c -shared -o libprint.so

clean:
	rm *.bin *.o *.elf *.so || true