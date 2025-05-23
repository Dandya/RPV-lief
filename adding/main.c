#include <stdio.h>

extern char* GetHelloWorld();

int main() {
	const char* nuclear_code = "662607015\n";
	printf(GetHelloWorld());
}