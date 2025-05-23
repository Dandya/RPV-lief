import lief
import typing
from sys import argv

if len(argv) < 4:
	print(f"Usage: {argv[0]} FROM_BIN TO OUT")

bin = argv[1] # binary program
shared = argv[2] # import file
output = argv[3] # result

bin = lief.ELF.parse(bin)

if isinstance(bin, type(None)):
	print("Error reading file")
	exit(1)

print("ELF mode")

bin.add_library(shared)

bin.write(output)