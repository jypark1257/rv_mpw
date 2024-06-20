#include "ascii.h"
#include "uart.h"
#include "string.h"

int8_t* read_token(int8_t* b, uint32_t n, int8_t* ds)
{
    for (uint32_t i = 0; i < n; i++) {
        int8_t ch = uread_int8();
        for (uint32_t j = 0; ds[j] != '\0'; j++) {
            if (ch == ds[j]) {
                b[i] = '\0';
                return b;
            }
        }
        b[i] = ch;
    }
    b[n - 1] = '\0';
    return b;
}



#define BUFFER_LEN 128

int main() {

    uwrite_int8s("\r\n");

    for ( ; ; ) {
        uwrite_int8s("IDS> ");

        int8_t buffer[BUFFER_LEN];
        int8_t* input = read_token(buffer, BUFFER_LEN, " \x0d");

        if (strcmp(input, "echo") == 0) {
            int8_t* input_echo = read_token(buffer, BUFFER_LEN, " \x0d");
            uwrite_int8s(input_echo);
            uwrite_int8s("\n\r");
        } else if (strcmp(input, "dump") == 0) {
        
        } else {
            uwrite_int8s("Unrecognized token: ");
            uwrite_int8s(input);
            uwrite_int8s("\n\r");
        }
    }

    //int source;
    //int weight_size;
    //int act_size;
    //int result_size;
    //weight_size = 4068;
    //act_size = 72;
    //result_size = 256;
    //source = 0x20000000;

    //asm volatile ( 
    //    "pim_write %[a], 1(%[b])\n\t"
    //    :
    //    : [a] "r" (source), [b] "r" (weight_size)
    //);
    //asm volatile ( 
    //    "pim_compute %[a], 1(%[b])\n\t"
    //    :
    //    : [a] "r" (source), [b] "r" (act_size)
    //);
    //asm volatile ( 
    //    "pim_load %[a], 1(%[b])\n\t"
    //    :
    //    : [a] "r" (source), [b] "r" (result_size)
    //);

}