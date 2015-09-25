#include <stdio.h>

int main(){
  int i = 0,x;
  i = 1;
  for(x=0; x < 32; x++) {
    printf("%d\n",i);
    i = i << 1;
  }
  return 0;
}
