all: m_2.elf good1.bin good2.bin

%.o: %.nasm
	nasm -f elf64 $< -o $@

%.bin: %.o
	ld -m elf_x86_64 $< -o $@

libdata.so:
	gcc data.c -shared -o libdata.so

m_2.elf: libdata.so
	gcc main.c -L$(realpath .) -ldata -o m_2.elf

clean:
	rm *.bin *.o *.elf *.so || true