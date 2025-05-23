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

section = lief.ELF.Section(f".test.good", lief.ELF.Section.TYPE.PROGBITS)
section.type = lief.ELF.Section.TYPE.PROGBITS
section += lief.ELF.Section.FLAGS.EXECINSTR
section += lief.ELF.Section.FLAGS.ALLOC
section += lief.ELF.Section.FLAGS.WRITE
section.content  = from_lief.get_section(".text").content
section.alignment = 0x1000
section = to_lief.add(section, loaded=True)

print(f"Virtual address: {hex(section.virtual_address)}")

if to_lief.has(lief.ELF.DynamicEntry.TAG.INIT_ARRAY):
	init_array = to_lief.get(lief.ELF.DynamicEntry.TAG.INIT_ARRAY)
	assert isinstance(init_array, lief.ELF.DynamicEntryArray)
	callbacks = init_array.array
	callbacks[0] = section.virtual_address
	init_array.array = callbacks

if to_lief.has(lief.ELF.DynamicEntry.TAG.INIT):
	init = to_lief.get(lief.ELF.DynamicEntry.TAG.INIT)
	init.value = section.virtual_address

to_lief.write(output)