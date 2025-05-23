#include <stdio.h>

extern char* GetHelloWorld();

int main() {
	printf(GetHelloWorld());
}