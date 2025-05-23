all: m_3.elf libs

m_3.elf: libs
	gcc main.c -L$(realpath ./libgood) -ldata -o m_3.elf

libs:
	make -C libgood
	make -C libbad

clean:
	rm *.bin *.o *.elf *.so || true
	make -C libgood clean || true
	make -C libbad clean || true