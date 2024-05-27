
#define DMA_CTRL (*((volatile unsigned int*)0x10000000) & 0x01)

int main() {

    int source;
    int size;
    size = 256;
    source = 0x20000000;

    asm volatile ( 
        "pim_write %[a], 1(%[b])\n\t"
        :
        : [a] "r" (source), [b] "r" (size)
    );
    asm volatile ( 
        "pim_compute %[a], 1(%[b])\n\t"
        :
        : [a] "r" (source), [b] "r" (size)
    );
    asm volatile ( 
        "pim_load %[a], 1(%[b])\n\t"
        :
        : [a] "r" (source), [b] "r" (size)
    );

}