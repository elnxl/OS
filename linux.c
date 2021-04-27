#include "string.h"
#include "stdio.h"
#include "sys/mman.h"
#include <unistd.h>

int main()
{
    int pagesize = sysconf(_SC_PAGE_SIZE);
    for (int i = 0; i < 10000000; i++)
    {
        char *ptr = (char *)mmap(NULL, pagesize * sizeof(char), PROT_READ | PROT_WRITE, MAP_PRIVATE | MAP_ANONYMOUS, 0, 0);
        if (ptr)
        {
            for (int i = 0; i < pagesize; i++)
            {
                ptr[i] = 0;
            }
        }
    }
    return 0;
}