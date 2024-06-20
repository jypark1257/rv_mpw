#include "ascii.h"
#include "uart.h"
#include "string.h"
#include "pim.h"

#define BUFFER_LEN 128

typedef void (*entry_t)(void);

int main(void)
{
    uwrite_int8s("\n\r");

    for ( ; ; ) {
        uwrite_int8s("RV_PJY> ");

        int8_t buffer[BUFFER_LEN];
        int8_t sel_pim[BUFFER_LEN];
        int8_t size[BUFFER_LEN];
        int8_t *input = read_token(buffer, BUFFER_LEN, " \x0d");

        if (strcmp(input, "echo") == 0) {
            int8_t *input_echo = read_token(buffer, BUFFER_LEN, " \x0d");
            uwrite_int8s(input_echo);
            uwrite_int8s("\n\r");
        } 
        //else if (strcmp(input, "dump") == 0) {
        //    /* Instruction parsing */
        //    int8_t *str_source_addr = read_token(buffer, BUFFER_LEN, " \x0d");
        //    int8_t *str_size = read_token(size, BUFFER_LEN, " \x0d");
        //    uint32_t *source_addr = (uint32_t *)ascii_dec_to_uint32(str_source_addr);
        //    uint32_t size = ascii_dec_to_uint32(str_size);
//
        //    dump_buffer(source_addr, size);
        //} else if (strcmp(input, "pim_write") == 0) {
        //    /* Instruction parsing */
        //    int8_t *str_source_addr = read_token(buffer, BUFFER_LEN, " \x0d");
        //    int8_t *str_sel_pim = read_token(sel_pim, BUFFER_LEN, " \x0d");
        //    int8_t *str_size = read_token(size, BUFFER_LEN, " \x0d");
        //    uint32_t source_addr = ascii_dec_to_uint32(str_source_addr);
        //    uint8_t sel_pim = ascii_dec_to_uint8(str_sel_pim);
        //    uint32_t size = ascii_dec_to_uint32(str_size);
        //    //pim_write(source_addr, sel_pim, size);
//
        //    /* print parameter */
        //    uwrite_int8s("pim_write "); uwrite_int8s(uint32_to_ascii_hex(source_addr, str_source_addr, BUFFER_LEN)); 
        //    uwrite_int8s(", "); uwrite_int8s(uint8_to_ascii_hex(sel_pim, str_sel_pim, BUFFER_LEN)); 
        //    uwrite_int8s("("); uwrite_int8s(uint32_to_ascii_hex(size, str_size, BUFFER_LEN)); uwrite_int8s(")");
        //    uwrite_int8s("\n\r");
        //} 
        else {
            uwrite_int8s("Unrecognized token: ");
            uwrite_int8s(input);
            uwrite_int8s("\n\r");
        }
    }

    while (1);

    return 0;
}
