#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <math.h>

int main(void) {
  int *m = NULL;
  clock_t start,end;
  int mb_size = pow(2,20); // 1 megabit
  double time;
  int size;
for (int i = 0; i < 11; i++) {
  size = pow(2, i);
  start = clock();
  for (int j = 0; j < 100000; j++) {
    m = (int*)malloc(mb_size*size);
    free(m);
  }
  end = clock();
  time = (double)(end-start) / CLOCKS_PER_SEC;
  printf("%d Mb %.3fms\n", size, time*1000);
  m = NULL;
}
}
