
#define DMA_CTRL (*((volatile unsigned int*)0x10000000) & 0x01)

int main() {

    int source;
    int size;
    size = 256;
    source = 0x00001000;


    while(DMA_CTRL) ;
    asm volatile ( 
        "pim_write %[a], 1(%[b])\n\t"
        :
        : [a] "r" (source), [b] "r" (size)
    );
    
    for (int i = 0; i < 256*2; ++i) {
        asm volatile ("nop");
    }
}