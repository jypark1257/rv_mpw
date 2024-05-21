OUTPUT_ARCH( "riscv" )

MEMORY {
    imem  (rwx): ORIGIN = 0x40000000, LENGTH = 0x00001000
    dmem  (rwx): ORIGIN = 0x40001000, LENGTH = 0x00001000
}

ENTRY(_start)
SECTIONS
{
    . = 0x40000000;
    /* gp is set to start of memory for gp relative addressing of static vars*/
    /* gp start is ram origin + 0x800 --- because offset for load/store is 12b */
    /* 12b signed = -2048 to +2047 */
    .text.init : 
    { 
        *(.init)
    } > imem
    . = 0x40001000;
    .data :
    {
        PROVIDE(_global_pointer = . + 0x800);
        PROVIDE(_sdata = .);
        *(.result)
        *(.data)
        PROVIDE(_edata = .);
    } > dmem
    .bss :
    {
        *(.bss)
    } > dmem
    /* Stack Pointer - End of Memory */
    PROVIDE(_stack_pointer = ORIGIN(dmem) + LENGTH(dmem));
}