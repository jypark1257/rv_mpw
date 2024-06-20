#define BUF_OFFSET 0x20000000

int main(){
	// dmem pointer and "int *" to apply integer format for dmem_offset values
    int *pim_buf = (int *)(BUF_OFFSET);

    // store PIM Weight
    for(int i = 0; i < 256; i++) {
        pim_buf[i] = i;
    }

    int i;
        // store PIM Weight
    for(i = 0; i < 256; i++) {
        int data = pim_buf[i];
        pim_buf[i] = pim_buf[i] + 1;
    }
}
