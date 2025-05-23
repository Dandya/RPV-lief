#include <stdio.h>

[[gnu::constructor]] void init() {
  printf("I'm hacker!\n");
}