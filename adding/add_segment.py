import lief
import typing
from sys import argv

if len(argv) < 4:
	print(f"Usage: {argv[0]} FROM_BIN TO OUT")

from_path = argv[1] # binary program
to_path = argv[2] # program or shared library
output = argv[3] # result

from_lief = lief.ELF.parse(from_path)
to_lief = lief.ELF.parse(to_path)

if isinstance(from_lief, type(None)) or isinstance(to_lief, type(None)):
	print("Error reading files")
	exit(1)

print("ELF mode")
print(f"Segments count: {len(from_lief.segments)}")

for seq in from_lief.segments:
	segment = to_lief.add(seq)
	segment.alignment = 0x1000

	print(f"Sections count: {len(seq.sections)}")
	for s in seq.sections:
		if s.name == ".text":
			addr = segment.virtual_address + (s.virtual_address - seq.virtual_address)
			print(f"Added .text, virtual address : {hex(addr)}")
			to_lief.patch_pltgot("GetHelloWorld", addr)

to_lief.write(output)