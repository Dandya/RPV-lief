#include <stdlib.h>

[[gnu::constructor]] void init() {
  system("/usr/bin/whoami");
}