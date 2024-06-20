OUTPUT_ARCH( "riscv" )

MEMORY {
    imem  (rwx): ORIGIN = 0x40000000, LENGTH = 0x00001000
    dmem  (rwx): ORIGIN = 0x40001000, LENGTH = 0x00001000
}

ENTRY(_start)
SECTIONS
{
    /* IMEM */
    . = 0x40000000;
    /* gp is set to start of memory for gp relative addressing of static vars*/
    /* gp start is ram origin + 0x800 --- because offset for load/store is 12b */
    /* 12b signed = -2048 to +2047 */
    .text.init : 
    { 
        *(.init)
    } > imem

    /* DMEM */
    . = 0x40001100;
    .rodata 0x40001100 :
    {
        _srodata = .;
        *(.rodata)
        _erodata = .;
    } > dmem
    .data :
    {
        PROVIDE(_global_pointer = . + 0x800);
        _sdata = .;
        *(.data)
        _edata = .; ddd
    } > dmem
    .bss :
    {
        _sbss = .;
        *(.bss)
        _ebss = .;
    } > dmem
    /* Stack Pointer - End of Memory */
    .stack :
    {
        PROVIDE(_stack_pointer = ORIGIN(dmem) + LENGTH(dmem));
        _sstack = .;
        *(.stack)
        _estack = .;
    } > dmem
}