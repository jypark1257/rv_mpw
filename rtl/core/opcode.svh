// OPCODES 
parameter OPCODE_R = 7'b01_100_11;
parameter OPCODE_I = 7'b00_100_11;
parameter OPCODE_BRANCH = 7'b11_000_11;
parameter OPCODE_STORE = 7'b01_000_11;
parameter OPCODE_LOAD = 7'b00_000_11;
parameter OPCODE_JALR = 7'b11_001_11;
parameter OPCODE_JAL = 7'b11_01111;
parameter OPCODE_AUIPC = 7'b00_101_11;
parameter OPCODE_LUI = 7'b01_101_11;
parameter OPCODE_SYSTEM = 7'b11_100_11;    // CSRXX, ECALL (NOT IMPLEMENTED), EBREAK (NOT IMPLEMENTED)
parameter OPCODE_CUSTOM_0 = 7'b00_010_11;
parameter OPCODE_CUSTON_1 = 7'b01_010_11;
parameter OPCODE_CUSTON_2 = 7'b10_110_11;  // custom / rv128
parameter OPCODE_CUSTON_3 = 7'b11_110_11;  // custom / rv128

// FUNCT3 (ALU)
parameter FUNCT3_ADD_SUB = 3'b000;
parameter FUNCT3_SLL = 3'b001;
parameter FUNCT3_SLT = 3'b010;
parameter FUNCT3_SLTU = 3'b011;
parameter FUNCT3_XOR = 3'b100;
parameter FUNCT3_SRL_SRA = 3'b101;
parameter FUNCT3_OR = 3'b110;
parameter FUNCT3_AND = 3'b111;

// FUNCT3 (BRANCH)
parameter BRANCH_BEQ = 3'b000;
parameter BRANCH_BNE = 3'b001;
parameter BRANCH_BLT = 3'b100;
parameter BRANCH_BGE = 3'b101;
parameter BRANCH_BLTU = 3'b110;
parameter BRANCH_BGEU = 3'b111;

// SIGNED LOAD, STORE
parameter FUNCT3_BYTE = 3'b000;
parameter FUNCT3_HALF = 3'b001;
parameter FUNCT3_WORD = 3'b010;

// UNSIGNED LOAD FUNCT3
parameter FUNCT3_BYTE_U = 3'b100;
parameter FUNCT3_HALF_U = 3'b101;

// ARITHMETIC and MULTIPLIER related FUNCT7
parameter FUNCT7_MUL = 7'h01;


