module pim (
	input			CLK,
	input  			RSTN,
	input [255:0]   i_BL,
	input [287:0]	i_WL,
	input [287:0]   i_activation_data,
	input 			i_activation_in_en,
	output 			o_result_out_en,
	output reg [31:0] o_result0,
	output reg [31:0] o_result1,
	output reg [31:0] o_result2,
	output reg [31:0] o_result3,
	output reg [31:0] o_result4,
	output reg [31:0] o_result5,
	output reg [31:0] o_result6,
	output reg [31:0] o_result7,
	output reg [31:0] o_result8,
	output reg [31:0] o_result9,
	output reg [31:0] o_result10,
	output reg [31:0] o_result11,
	output reg [31:0] o_result12,
	output reg [31:0] o_result13,
	output reg [31:0] o_result14,
	output reg [31:0] o_result15,
	output reg [31:0] o_result16,
	output reg [31:0] o_result17,
	output reg [31:0] o_result18,
	output reg [31:0] o_result19,
	output reg [31:0] o_result20,
	output reg [31:0] o_result21,
	output reg [31:0] o_result22,
	output reg [31:0] o_result23,
	output reg [31:0] o_result24,
	output reg [31:0] o_result25,
	output reg [31:0] o_result26,
	output reg [31:0] o_result27,
	output reg [31:0] o_result28,
	output reg [31:0] o_result29,
	output reg [31:0] o_result30,
	output reg [31:0] o_result31,
	output reg [31:0] o_result32,
	output reg [31:0] o_result33,
	output reg [31:0] o_result34,
	output reg [31:0] o_result35,
	output reg [31:0] o_result36,
	output reg [31:0] o_result37,
	output reg [31:0] o_result38,
	output reg [31:0] o_result39,
	output reg [31:0] o_result40,
	output reg [31:0] o_result41,
	output reg [31:0] o_result42,
	output reg [31:0] o_result43,
	output reg [31:0] o_result44,
	output reg [31:0] o_result45,
	output reg [31:0] o_result46,
	output reg [31:0] o_result47,
	output reg [31:0] o_result48,
	output reg [31:0] o_result49,
	output reg [31:0] o_result50,
	output reg [31:0] o_result51,
	output reg [31:0] o_result52,
	output reg [31:0] o_result53,
	output reg [31:0] o_result54,
	output reg [31:0] o_result55,
	output reg [31:0] o_result56,
	output reg [31:0] o_result57,
	output reg [31:0] o_result58,
	output reg [31:0] o_result59,
	output reg [31:0] o_result60,
	output reg [31:0] o_result61,
	output reg [31:0] o_result62,
	output reg [31:0] o_result63,
	output reg [31:0] o_result64,
	output reg [31:0] o_result65,
	output reg [31:0] o_result66,
	output reg [31:0] o_result67,
	output reg [31:0] o_result68,
	output reg [31:0] o_result69,
	output reg [31:0] o_result70,
	output reg [31:0] o_result71,
	output reg [31:0] o_result72,
	output reg [31:0] o_result73,
	output reg [31:0] o_result74,
	output reg [31:0] o_result75,
	output reg [31:0] o_result76,
	output reg [31:0] o_result77,
	output reg [31:0] o_result78,
	output reg [31:0] o_result79,
	output reg [31:0] o_result80,
	output reg [31:0] o_result81,
	output reg [31:0] o_result82,
	output reg [31:0] o_result83,
	output reg [31:0] o_result84,
	output reg [31:0] o_result85,
	output reg [31:0] o_result86,
	output reg [31:0] o_result87,
	output reg [31:0] o_result88,
	output reg [31:0] o_result89,
	output reg [31:0] o_result90,
	output reg [31:0] o_result91,
	output reg [31:0] o_result92,
	output reg [31:0] o_result93,
	output reg [31:0] o_result94,
	output reg [31:0] o_result95,
	output reg [31:0] o_result96,
	output reg [31:0] o_result97,
	output reg [31:0] o_result98,
	output reg [31:0] o_result99,
	output reg [31:0] o_result100,
	output reg [31:0] o_result101,
	output reg [31:0] o_result102,
	output reg [31:0] o_result103,
	output reg [31:0] o_result104,
	output reg [31:0] o_result105,
	output reg [31:0] o_result106,
	output reg [31:0] o_result107,
	output reg [31:0] o_result108,
	output reg [31:0] o_result109,
	output reg [31:0] o_result110,
	output reg [31:0] o_result111,
	output reg [31:0] o_result112,
	output reg [31:0] o_result113,
	output reg [31:0] o_result114,
	output reg [31:0] o_result115,
	output reg [31:0] o_result116,
	output reg [31:0] o_result117,
	output reg [31:0] o_result118,
	output reg [31:0] o_result119,
	output reg [31:0] o_result120,
	output reg [31:0] o_result121,
	output reg [31:0] o_result122,
	output reg [31:0] o_result123,
	output reg [31:0] o_result124,
	output reg [31:0] o_result125,
	output reg [31:0] o_result126,
	output reg [31:0] o_result127,
	output reg [31:0] o_result128,
	output reg [31:0] o_result129,
	output reg [31:0] o_result130,
	output reg [31:0] o_result131,
	output reg [31:0] o_result132,
	output reg [31:0] o_result133,
	output reg [31:0] o_result134,
	output reg [31:0] o_result135,
	output reg [31:0] o_result136,
	output reg [31:0] o_result137,
	output reg [31:0] o_result138,
	output reg [31:0] o_result139,
	output reg [31:0] o_result140,
	output reg [31:0] o_result141,
	output reg [31:0] o_result142,
	output reg [31:0] o_result143,
	output reg [31:0] o_result144,
	output reg [31:0] o_result145,
	output reg [31:0] o_result146,
	output reg [31:0] o_result147,
	output reg [31:0] o_result148,
	output reg [31:0] o_result149,
	output reg [31:0] o_result150,
	output reg [31:0] o_result151,
	output reg [31:0] o_result152,
	output reg [31:0] o_result153,
	output reg [31:0] o_result154,
	output reg [31:0] o_result155,
	output reg [31:0] o_result156,
	output reg [31:0] o_result157,
	output reg [31:0] o_result158,
	output reg [31:0] o_result159,
	output reg [31:0] o_result160,
	output reg [31:0] o_result161,
	output reg [31:0] o_result162,
	output reg [31:0] o_result163,
	output reg [31:0] o_result164,
	output reg [31:0] o_result165,
	output reg [31:0] o_result166,
	output reg [31:0] o_result167,
	output reg [31:0] o_result168,
	output reg [31:0] o_result169,
	output reg [31:0] o_result170,
	output reg [31:0] o_result171,
	output reg [31:0] o_result172,
	output reg [31:0] o_result173,
	output reg [31:0] o_result174,
	output reg [31:0] o_result175,
	output reg [31:0] o_result176,
	output reg [31:0] o_result177,
	output reg [31:0] o_result178,
	output reg [31:0] o_result179,
	output reg [31:0] o_result180,
	output reg [31:0] o_result181,
	output reg [31:0] o_result182,
	output reg [31:0] o_result183,
	output reg [31:0] o_result184,
	output reg [31:0] o_result185,
	output reg [31:0] o_result186,
	output reg [31:0] o_result187,
	output reg [31:0] o_result188,
	output reg [31:0] o_result189,
	output reg [31:0] o_result190,
	output reg [31:0] o_result191,
	output reg [31:0] o_result192,
	output reg [31:0] o_result193,
	output reg [31:0] o_result194,
	output reg [31:0] o_result195,
	output reg [31:0] o_result196,
	output reg [31:0] o_result197,
	output reg [31:0] o_result198,
	output reg [31:0] o_result199,
	output reg [31:0] o_result200,
	output reg [31:0] o_result201,
	output reg [31:0] o_result202,
	output reg [31:0] o_result203,
	output reg [31:0] o_result204,
	output reg [31:0] o_result205,
	output reg [31:0] o_result206,
	output reg [31:0] o_result207,
	output reg [31:0] o_result208,
	output reg [31:0] o_result209,
	output reg [31:0] o_result210,
	output reg [31:0] o_result211,
	output reg [31:0] o_result212,
	output reg [31:0] o_result213,
	output reg [31:0] o_result214,
	output reg [31:0] o_result215,
	output reg [31:0] o_result216,
	output reg [31:0] o_result217,
	output reg [31:0] o_result218,
	output reg [31:0] o_result219,
	output reg [31:0] o_result220,
	output reg [31:0] o_result221,
	output reg [31:0] o_result222,
	output reg [31:0] o_result223,
	output reg [31:0] o_result224,
	output reg [31:0] o_result225,
	output reg [31:0] o_result226,
	output reg [31:0] o_result227,
	output reg [31:0] o_result228,
	output reg [31:0] o_result229,
	output reg [31:0] o_result230,
	output reg [31:0] o_result231,
	output reg [31:0] o_result232,
	output reg [31:0] o_result233,
	output reg [31:0] o_result234,
	output reg [31:0] o_result235,
	output reg [31:0] o_result236,
	output reg [31:0] o_result237,
	output reg [31:0] o_result238,
	output reg [31:0] o_result239,
	output reg [31:0] o_result240,
	output reg [31:0] o_result241,
	output reg [31:0] o_result242,
	output reg [31:0] o_result243,
	output reg [31:0] o_result244,
	output reg [31:0] o_result245,
	output reg [31:0] o_result246,
	output reg [31:0] o_result247,
	output reg [31:0] o_result248,
	output reg [31:0] o_result249,
	output reg [31:0] o_result250,
	output reg [31:0] o_result251,
	output reg [31:0] o_result252,
	output reg [31:0] o_result253,
	output reg [31:0] o_result254,
	output reg [31:0] o_result255
);

	reg [255:0] weight [0:287];
	reg [287:0] activation [0:7];
	reg [2:0] counter, counter2;
	reg cal;

	always @(posedge CLK) begin
		if (!RSTN) begin
			weight[0] <= 0;
			weight[1] <= 0;
			weight[2] <= 0;
			weight[3] <= 0;
			weight[4] <= 0;
			weight[5] <= 0;
			weight[6] <= 0;
			weight[7] <= 0;
			weight[8] <= 0;
			weight[9] <= 0;
			weight[10] <= 0;
			weight[11] <= 0;
			weight[12] <= 0;
			weight[13] <= 0;
			weight[14] <= 0;
			weight[15] <= 0;
			weight[16] <= 0;
			weight[17] <= 0;
			weight[18] <= 0;
			weight[19] <= 0;
			weight[20] <= 0;
			weight[21] <= 0;
			weight[22] <= 0;
			weight[23] <= 0;
			weight[24] <= 0;
			weight[25] <= 0;
			weight[26] <= 0;
			weight[27] <= 0;
			weight[28] <= 0;
			weight[29] <= 0;
			weight[30] <= 0;
			weight[31] <= 0;
			weight[32] <= 0;
			weight[33] <= 0;
			weight[34] <= 0;
			weight[35] <= 0;
			weight[36] <= 0;
			weight[37] <= 0;
			weight[38] <= 0;
			weight[39] <= 0;
			weight[40] <= 0;
			weight[41] <= 0;
			weight[42] <= 0;
			weight[43] <= 0;
			weight[44] <= 0;
			weight[45] <= 0;
			weight[46] <= 0;
			weight[47] <= 0;
			weight[48] <= 0;
			weight[49] <= 0;
			weight[50] <= 0;
			weight[51] <= 0;
			weight[52] <= 0;
			weight[53] <= 0;
			weight[54] <= 0;
			weight[55] <= 0;
			weight[56] <= 0;
			weight[57] <= 0;
			weight[58] <= 0;
			weight[59] <= 0;
			weight[60] <= 0;
			weight[61] <= 0;
			weight[62] <= 0;
			weight[63] <= 0;
			weight[64] <= 0;
			weight[65] <= 0;
			weight[66] <= 0;
			weight[67] <= 0;
			weight[68] <= 0;
			weight[69] <= 0;
			weight[70] <= 0;
			weight[71] <= 0;
			weight[72] <= 0;
			weight[73] <= 0;
			weight[74] <= 0;
			weight[75] <= 0;
			weight[76] <= 0;
			weight[77] <= 0;
			weight[78] <= 0;
			weight[79] <= 0;
			weight[80] <= 0;
			weight[81] <= 0;
			weight[82] <= 0;
			weight[83] <= 0;
			weight[84] <= 0;
			weight[85] <= 0;
			weight[86] <= 0;
			weight[87] <= 0;
			weight[88] <= 0;
			weight[89] <= 0;
			weight[90] <= 0;
			weight[91] <= 0;
			weight[92] <= 0;
			weight[93] <= 0;
			weight[94] <= 0;
			weight[95] <= 0;
			weight[96] <= 0;
			weight[97] <= 0;
			weight[98] <= 0;
			weight[99] <= 0;
			weight[100] <= 0;
			weight[101] <= 0;
			weight[102] <= 0;
			weight[103] <= 0;
			weight[104] <= 0;
			weight[105] <= 0;
			weight[106] <= 0;
			weight[107] <= 0;
			weight[108] <= 0;
			weight[109] <= 0;
			weight[110] <= 0;
			weight[111] <= 0;
			weight[112] <= 0;
			weight[113] <= 0;
			weight[114] <= 0;
			weight[115] <= 0;
			weight[116] <= 0;
			weight[117] <= 0;
			weight[118] <= 0;
			weight[119] <= 0;
			weight[120] <= 0;
			weight[121] <= 0;
			weight[122] <= 0;
			weight[123] <= 0;
			weight[124] <= 0;
			weight[125] <= 0;
			weight[126] <= 0;
			weight[127] <= 0;
			weight[128] <= 0;
			weight[129] <= 0;
			weight[130] <= 0;
			weight[131] <= 0;
			weight[132] <= 0;
			weight[133] <= 0;
			weight[134] <= 0;
			weight[135] <= 0;
			weight[136] <= 0;
			weight[137] <= 0;
			weight[138] <= 0;
			weight[139] <= 0;
			weight[140] <= 0;
			weight[141] <= 0;
			weight[142] <= 0;
			weight[143] <= 0;
			weight[144] <= 0;
			weight[145] <= 0;
			weight[146] <= 0;
			weight[147] <= 0;
			weight[148] <= 0;
			weight[149] <= 0;
			weight[150] <= 0;
			weight[151] <= 0;
			weight[152] <= 0;
			weight[153] <= 0;
			weight[154] <= 0;
			weight[155] <= 0;
			weight[156] <= 0;
			weight[157] <= 0;
			weight[158] <= 0;
			weight[159] <= 0;
			weight[160] <= 0;
			weight[161] <= 0;
			weight[162] <= 0;
			weight[163] <= 0;
			weight[164] <= 0;
			weight[165] <= 0;
			weight[166] <= 0;
			weight[167] <= 0;
			weight[168] <= 0;
			weight[169] <= 0;
			weight[170] <= 0;
			weight[171] <= 0;
			weight[172] <= 0;
			weight[173] <= 0;
			weight[174] <= 0;
			weight[175] <= 0;
			weight[176] <= 0;
			weight[177] <= 0;
			weight[178] <= 0;
			weight[179] <= 0;
			weight[180] <= 0;
			weight[181] <= 0;
			weight[182] <= 0;
			weight[183] <= 0;
			weight[184] <= 0;
			weight[185] <= 0;
			weight[186] <= 0;
			weight[187] <= 0;
			weight[188] <= 0;
			weight[189] <= 0;
			weight[190] <= 0;
			weight[191] <= 0;
			weight[192] <= 0;
			weight[193] <= 0;
			weight[194] <= 0;
			weight[195] <= 0;
			weight[196] <= 0;
			weight[197] <= 0;
			weight[198] <= 0;
			weight[199] <= 0;
			weight[200] <= 0;
			weight[201] <= 0;
			weight[202] <= 0;
			weight[203] <= 0;
			weight[204] <= 0;
			weight[205] <= 0;
			weight[206] <= 0;
			weight[207] <= 0;
			weight[208] <= 0;
			weight[209] <= 0;
			weight[210] <= 0;
			weight[211] <= 0;
			weight[212] <= 0;
			weight[213] <= 0;
			weight[214] <= 0;
			weight[215] <= 0;
			weight[216] <= 0;
			weight[217] <= 0;
			weight[218] <= 0;
			weight[219] <= 0;
			weight[220] <= 0;
			weight[221] <= 0;
			weight[222] <= 0;
			weight[223] <= 0;
			weight[224] <= 0;
			weight[225] <= 0;
			weight[226] <= 0;
			weight[227] <= 0;
			weight[228] <= 0;
			weight[229] <= 0;
			weight[230] <= 0;
			weight[231] <= 0;
			weight[232] <= 0;
			weight[233] <= 0;
			weight[234] <= 0;
			weight[235] <= 0;
			weight[236] <= 0;
			weight[237] <= 0;
			weight[238] <= 0;
			weight[239] <= 0;
			weight[240] <= 0;
			weight[241] <= 0;
			weight[242] <= 0;
			weight[243] <= 0;
			weight[244] <= 0;
			weight[245] <= 0;
			weight[246] <= 0;
			weight[247] <= 0;
			weight[248] <= 0;
			weight[249] <= 0;
			weight[250] <= 0;
			weight[251] <= 0;
			weight[252] <= 0;
			weight[253] <= 0;
			weight[254] <= 0;
			weight[255] <= 0;
			weight[256] <= 0;
			weight[257] <= 0;
			weight[258] <= 0;
			weight[259] <= 0;
			weight[260] <= 0;
			weight[261] <= 0;
			weight[262] <= 0;
			weight[263] <= 0;
			weight[264] <= 0;
			weight[265] <= 0;
			weight[266] <= 0;
			weight[267] <= 0;
			weight[268] <= 0;
			weight[269] <= 0;
			weight[270] <= 0;
			weight[271] <= 0;
			weight[272] <= 0;
			weight[273] <= 0;
			weight[274] <= 0;
			weight[275] <= 0;
			weight[276] <= 0;
			weight[277] <= 0;
			weight[278] <= 0;
			weight[279] <= 0;
			weight[280] <= 0;
			weight[281] <= 0;
			weight[282] <= 0;
			weight[283] <= 0;
			weight[284] <= 0;
			weight[285] <= 0;
			weight[286] <= 0;
			weight[287] <= 0;
		end else begin
			if (i_WL[  0]) begin 
				weight[  0] <= i_BL; 
			end else if (i_WL[  1]) begin 
				weight[  1] <= i_BL; 
			end else if (i_WL[  2]) begin 
				weight[  2] <= i_BL; 
			end else if (i_WL[  3]) begin 
				weight[  3] <= i_BL; 
			end else if (i_WL[  4]) begin 
				weight[  4] <= i_BL; 
			end else if (i_WL[  5]) begin 
				weight[  5] <= i_BL; 
			end else if (i_WL[  6]) begin 
				weight[  6] <= i_BL; 
			end else if (i_WL[  7]) begin 
				weight[  7] <= i_BL; 
			end else if (i_WL[  8]) begin 
				weight[  8] <= i_BL; 
			end else if (i_WL[  9]) begin 
				weight[  9] <= i_BL; 
			end else if (i_WL[ 10]) begin 
				weight[ 10] <= i_BL; 
			end else if (i_WL[ 11]) begin 
				weight[ 11] <= i_BL; 
			end else if (i_WL[ 12]) begin 
				weight[ 12] <= i_BL; 
			end else if (i_WL[ 13]) begin 
				weight[ 13] <= i_BL; 
			end else if (i_WL[ 14]) begin 
				weight[ 14] <= i_BL; 
			end else if (i_WL[ 15]) begin 
				weight[ 15] <= i_BL; 
			end else if (i_WL[ 16]) begin 
				weight[ 16] <= i_BL; 
			end else if (i_WL[ 17]) begin 
				weight[ 17] <= i_BL; 
			end else if (i_WL[ 18]) begin 
				weight[ 18] <= i_BL; 
			end else if (i_WL[ 19]) begin 
				weight[ 19] <= i_BL; 
			end else if (i_WL[ 20]) begin 
				weight[ 20] <= i_BL; 
			end else if (i_WL[ 21]) begin 
				weight[ 21] <= i_BL; 
			end else if (i_WL[ 22]) begin 
				weight[ 22] <= i_BL; 
			end else if (i_WL[ 23]) begin 
				weight[ 23] <= i_BL; 
			end else if (i_WL[ 24]) begin 
				weight[ 24] <= i_BL; 
			end else if (i_WL[ 25]) begin 
				weight[ 25] <= i_BL; 
			end else if (i_WL[ 26]) begin 
				weight[ 26] <= i_BL; 
			end else if (i_WL[ 27]) begin 
				weight[ 27] <= i_BL; 
			end else if (i_WL[ 28]) begin 
				weight[ 28] <= i_BL; 
			end else if (i_WL[ 29]) begin 
				weight[ 29] <= i_BL; 
			end else if (i_WL[ 30]) begin 
				weight[ 30] <= i_BL; 
			end else if (i_WL[ 31]) begin 
				weight[ 31] <= i_BL; 
			end else if (i_WL[ 32]) begin 
				weight[ 32] <= i_BL; 
			end else if (i_WL[ 33]) begin 
				weight[ 33] <= i_BL; 
			end else if (i_WL[ 34]) begin 
				weight[ 34] <= i_BL; 
			end else if (i_WL[ 35]) begin 
				weight[ 35] <= i_BL; 
			end else if (i_WL[ 36]) begin 
				weight[ 36] <= i_BL; 
			end else if (i_WL[ 37]) begin 
				weight[ 37] <= i_BL; 
			end else if (i_WL[ 38]) begin 
				weight[ 38] <= i_BL; 
			end else if (i_WL[ 39]) begin 
				weight[ 39] <= i_BL; 
			end else if (i_WL[ 40]) begin 
				weight[ 40] <= i_BL; 
			end else if (i_WL[ 41]) begin 
				weight[ 41] <= i_BL; 
			end else if (i_WL[ 42]) begin 
				weight[ 42] <= i_BL; 
			end else if (i_WL[ 43]) begin 
				weight[ 43] <= i_BL; 
			end else if (i_WL[ 44]) begin 
				weight[ 44] <= i_BL; 
			end else if (i_WL[ 45]) begin 
				weight[ 45] <= i_BL; 
			end else if (i_WL[ 46]) begin 
				weight[ 46] <= i_BL; 
			end else if (i_WL[ 47]) begin 
				weight[ 47] <= i_BL; 
			end else if (i_WL[ 48]) begin 
				weight[ 48] <= i_BL; 
			end else if (i_WL[ 49]) begin 
				weight[ 49] <= i_BL; 
			end else if (i_WL[ 50]) begin 
				weight[ 50] <= i_BL; 
			end else if (i_WL[ 51]) begin 
				weight[ 51] <= i_BL; 
			end else if (i_WL[ 52]) begin 
				weight[ 52] <= i_BL; 
			end else if (i_WL[ 53]) begin 
				weight[ 53] <= i_BL; 
			end else if (i_WL[ 54]) begin 
				weight[ 54] <= i_BL; 
			end else if (i_WL[ 55]) begin 
				weight[ 55] <= i_BL; 
			end else if (i_WL[ 56]) begin 
				weight[ 56] <= i_BL; 
			end else if (i_WL[ 57]) begin 
				weight[ 57] <= i_BL; 
			end else if (i_WL[ 58]) begin 
				weight[ 58] <= i_BL; 
			end else if (i_WL[ 59]) begin 
				weight[ 59] <= i_BL; 
			end else if (i_WL[ 60]) begin 
				weight[ 60] <= i_BL; 
			end else if (i_WL[ 61]) begin 
				weight[ 61] <= i_BL; 
			end else if (i_WL[ 62]) begin 
				weight[ 62] <= i_BL; 
			end else if (i_WL[ 63]) begin 
				weight[ 63] <= i_BL; 
			end else if (i_WL[ 64]) begin 
				weight[ 64] <= i_BL; 
			end else if (i_WL[ 65]) begin 
				weight[ 65] <= i_BL; 
			end else if (i_WL[ 66]) begin 
				weight[ 66] <= i_BL; 
			end else if (i_WL[ 67]) begin 
				weight[ 67] <= i_BL; 
			end else if (i_WL[ 68]) begin 
				weight[ 68] <= i_BL; 
			end else if (i_WL[ 69]) begin 
				weight[ 69] <= i_BL; 
			end else if (i_WL[ 70]) begin 
				weight[ 70] <= i_BL; 
			end else if (i_WL[ 71]) begin 
				weight[ 71] <= i_BL; 
			end else if (i_WL[ 72]) begin 
				weight[ 72] <= i_BL; 
			end else if (i_WL[ 73]) begin 
				weight[ 73] <= i_BL; 
			end else if (i_WL[ 74]) begin 
				weight[ 74] <= i_BL; 
			end else if (i_WL[ 75]) begin 
				weight[ 75] <= i_BL; 
			end else if (i_WL[ 76]) begin 
				weight[ 76] <= i_BL; 
			end else if (i_WL[ 77]) begin 
				weight[ 77] <= i_BL; 
			end else if (i_WL[ 78]) begin 
				weight[ 78] <= i_BL; 
			end else if (i_WL[ 79]) begin 
				weight[ 79] <= i_BL; 
			end else if (i_WL[ 80]) begin 
				weight[ 80] <= i_BL; 
			end else if (i_WL[ 81]) begin 
				weight[ 81] <= i_BL; 
			end else if (i_WL[ 82]) begin 
				weight[ 82] <= i_BL; 
			end else if (i_WL[ 83]) begin 
				weight[ 83] <= i_BL; 
			end else if (i_WL[ 84]) begin 
				weight[ 84] <= i_BL; 
			end else if (i_WL[ 85]) begin 
				weight[ 85] <= i_BL; 
			end else if (i_WL[ 86]) begin 
				weight[ 86] <= i_BL; 
			end else if (i_WL[ 87]) begin 
				weight[ 87] <= i_BL; 
			end else if (i_WL[ 88]) begin 
				weight[ 88] <= i_BL; 
			end else if (i_WL[ 89]) begin 
				weight[ 89] <= i_BL; 
			end else if (i_WL[ 90]) begin 
				weight[ 90] <= i_BL; 
			end else if (i_WL[ 91]) begin 
				weight[ 91] <= i_BL; 
			end else if (i_WL[ 92]) begin 
				weight[ 92] <= i_BL; 
			end else if (i_WL[ 93]) begin 
				weight[ 93] <= i_BL; 
			end else if (i_WL[ 94]) begin 
				weight[ 94] <= i_BL; 
			end else if (i_WL[ 95]) begin 
				weight[ 95] <= i_BL; 
			end else if (i_WL[ 96]) begin 
				weight[ 96] <= i_BL; 
			end else if (i_WL[ 97]) begin 
				weight[ 97] <= i_BL; 
			end else if (i_WL[ 98]) begin 
				weight[ 98] <= i_BL; 
			end else if (i_WL[ 99]) begin 
				weight[ 99] <= i_BL; 
			end else if (i_WL[100]) begin 
				weight[100] <= i_BL; 
			end else if (i_WL[101]) begin 
				weight[101] <= i_BL; 
			end else if (i_WL[102]) begin 
				weight[102] <= i_BL; 
			end else if (i_WL[103]) begin 
				weight[103] <= i_BL; 
			end else if (i_WL[104]) begin 
				weight[104] <= i_BL; 
			end else if (i_WL[105]) begin 
				weight[105] <= i_BL; 
			end else if (i_WL[106]) begin 
				weight[106] <= i_BL; 
			end else if (i_WL[107]) begin 
				weight[107] <= i_BL; 
			end else if (i_WL[108]) begin 
				weight[108] <= i_BL; 
			end else if (i_WL[109]) begin 
				weight[109] <= i_BL; 
			end else if (i_WL[110]) begin 
				weight[110] <= i_BL; 
			end else if (i_WL[111]) begin 
				weight[111] <= i_BL; 
			end else if (i_WL[112]) begin 
				weight[112] <= i_BL; 
			end else if (i_WL[113]) begin 
				weight[113] <= i_BL; 
			end else if (i_WL[114]) begin 
				weight[114] <= i_BL; 
			end else if (i_WL[115]) begin 
				weight[115] <= i_BL; 
			end else if (i_WL[116]) begin 
				weight[116] <= i_BL; 
			end else if (i_WL[117]) begin 
				weight[117] <= i_BL; 
			end else if (i_WL[118]) begin 
				weight[118] <= i_BL; 
			end else if (i_WL[119]) begin 
				weight[119] <= i_BL; 
			end else if (i_WL[120]) begin 
				weight[120] <= i_BL; 
			end else if (i_WL[121]) begin 
				weight[121] <= i_BL; 
			end else if (i_WL[122]) begin 
				weight[122] <= i_BL; 
			end else if (i_WL[123]) begin 
				weight[123] <= i_BL; 
			end else if (i_WL[124]) begin 
				weight[124] <= i_BL; 
			end else if (i_WL[125]) begin 
				weight[125] <= i_BL; 
			end else if (i_WL[126]) begin 
				weight[126] <= i_BL; 
			end else if (i_WL[127]) begin 
				weight[127] <= i_BL; 
			end else if (i_WL[128]) begin 
				weight[128] <= i_BL; 
			end else if (i_WL[129]) begin 
				weight[129] <= i_BL; 
			end else if (i_WL[130]) begin 
				weight[130] <= i_BL; 
			end else if (i_WL[131]) begin 
				weight[131] <= i_BL; 
			end else if (i_WL[132]) begin 
				weight[132] <= i_BL; 
			end else if (i_WL[133]) begin 
				weight[133] <= i_BL; 
			end else if (i_WL[134]) begin 
				weight[134] <= i_BL; 
			end else if (i_WL[135]) begin 
				weight[135] <= i_BL; 
			end else if (i_WL[136]) begin 
				weight[136] <= i_BL; 
			end else if (i_WL[137]) begin 
				weight[137] <= i_BL; 
			end else if (i_WL[138]) begin 
				weight[138] <= i_BL; 
			end else if (i_WL[139]) begin 
				weight[139] <= i_BL; 
			end else if (i_WL[140]) begin 
				weight[140] <= i_BL; 
			end else if (i_WL[141]) begin 
				weight[141] <= i_BL; 
			end else if (i_WL[142]) begin 
				weight[142] <= i_BL; 
			end else if (i_WL[143]) begin 
				weight[143] <= i_BL; 
			end else if (i_WL[144]) begin 
				weight[144] <= i_BL; 
			end else if (i_WL[145]) begin 
				weight[145] <= i_BL; 
			end else if (i_WL[146]) begin 
				weight[146] <= i_BL; 
			end else if (i_WL[147]) begin 
				weight[147] <= i_BL; 
			end else if (i_WL[148]) begin 
				weight[148] <= i_BL; 
			end else if (i_WL[149]) begin 
				weight[149] <= i_BL; 
			end else if (i_WL[150]) begin 
				weight[150] <= i_BL; 
			end else if (i_WL[151]) begin 
				weight[151] <= i_BL; 
			end else if (i_WL[152]) begin 
				weight[152] <= i_BL; 
			end else if (i_WL[153]) begin 
				weight[153] <= i_BL; 
			end else if (i_WL[154]) begin 
				weight[154] <= i_BL; 
			end else if (i_WL[155]) begin 
				weight[155] <= i_BL; 
			end else if (i_WL[156]) begin 
				weight[156] <= i_BL; 
			end else if (i_WL[157]) begin 
				weight[157] <= i_BL; 
			end else if (i_WL[158]) begin 
				weight[158] <= i_BL; 
			end else if (i_WL[159]) begin 
				weight[159] <= i_BL; 
			end else if (i_WL[160]) begin 
				weight[160] <= i_BL; 
			end else if (i_WL[161]) begin 
				weight[161] <= i_BL; 
			end else if (i_WL[162]) begin 
				weight[162] <= i_BL; 
			end else if (i_WL[163]) begin 
				weight[163] <= i_BL; 
			end else if (i_WL[164]) begin 
				weight[164] <= i_BL; 
			end else if (i_WL[165]) begin 
				weight[165] <= i_BL; 
			end else if (i_WL[166]) begin 
				weight[166] <= i_BL; 
			end else if (i_WL[167]) begin 
				weight[167] <= i_BL; 
			end else if (i_WL[168]) begin 
				weight[168] <= i_BL; 
			end else if (i_WL[169]) begin 
				weight[169] <= i_BL; 
			end else if (i_WL[170]) begin 
				weight[170] <= i_BL; 
			end else if (i_WL[171]) begin 
				weight[171] <= i_BL; 
			end else if (i_WL[172]) begin 
				weight[172] <= i_BL; 
			end else if (i_WL[173]) begin 
				weight[173] <= i_BL; 
			end else if (i_WL[174]) begin 
				weight[174] <= i_BL; 
			end else if (i_WL[175]) begin 
				weight[175] <= i_BL; 
			end else if (i_WL[176]) begin 
				weight[176] <= i_BL; 
			end else if (i_WL[177]) begin 
				weight[177] <= i_BL; 
			end else if (i_WL[178]) begin 
				weight[178] <= i_BL; 
			end else if (i_WL[179]) begin 
				weight[179] <= i_BL; 
			end else if (i_WL[180]) begin 
				weight[180] <= i_BL; 
			end else if (i_WL[181]) begin 
				weight[181] <= i_BL; 
			end else if (i_WL[182]) begin 
				weight[182] <= i_BL; 
			end else if (i_WL[183]) begin 
				weight[183] <= i_BL; 
			end else if (i_WL[184]) begin 
				weight[184] <= i_BL; 
			end else if (i_WL[185]) begin 
				weight[185] <= i_BL; 
			end else if (i_WL[186]) begin 
				weight[186] <= i_BL; 
			end else if (i_WL[187]) begin 
				weight[187] <= i_BL; 
			end else if (i_WL[188]) begin 
				weight[188] <= i_BL; 
			end else if (i_WL[189]) begin 
				weight[189] <= i_BL; 
			end else if (i_WL[190]) begin 
				weight[190] <= i_BL; 
			end else if (i_WL[191]) begin 
				weight[191] <= i_BL; 
			end else if (i_WL[192]) begin 
				weight[192] <= i_BL; 
			end else if (i_WL[193]) begin 
				weight[193] <= i_BL; 
			end else if (i_WL[194]) begin 
				weight[194] <= i_BL; 
			end else if (i_WL[195]) begin 
				weight[195] <= i_BL; 
			end else if (i_WL[196]) begin 
				weight[196] <= i_BL; 
			end else if (i_WL[197]) begin 
				weight[197] <= i_BL; 
			end else if (i_WL[198]) begin 
				weight[198] <= i_BL; 
			end else if (i_WL[199]) begin 
				weight[199] <= i_BL; 
			end else if (i_WL[200]) begin 
				weight[200] <= i_BL; 
			end else if (i_WL[201]) begin 
				weight[201] <= i_BL; 
			end else if (i_WL[202]) begin 
				weight[202] <= i_BL; 
			end else if (i_WL[203]) begin 
				weight[203] <= i_BL; 
			end else if (i_WL[204]) begin 
				weight[204] <= i_BL; 
			end else if (i_WL[205]) begin 
				weight[205] <= i_BL; 
			end else if (i_WL[206]) begin 
				weight[206] <= i_BL; 
			end else if (i_WL[207]) begin 
				weight[207] <= i_BL; 
			end else if (i_WL[208]) begin 
				weight[208] <= i_BL; 
			end else if (i_WL[209]) begin 
				weight[209] <= i_BL; 
			end else if (i_WL[210]) begin 
				weight[210] <= i_BL; 
			end else if (i_WL[211]) begin 
				weight[211] <= i_BL; 
			end else if (i_WL[212]) begin 
				weight[212] <= i_BL; 
			end else if (i_WL[213]) begin 
				weight[213] <= i_BL; 
			end else if (i_WL[214]) begin 
				weight[214] <= i_BL; 
			end else if (i_WL[215]) begin 
				weight[215] <= i_BL; 
			end else if (i_WL[216]) begin 
				weight[216] <= i_BL; 
			end else if (i_WL[217]) begin 
				weight[217] <= i_BL; 
			end else if (i_WL[218]) begin 
				weight[218] <= i_BL; 
			end else if (i_WL[219]) begin 
				weight[219] <= i_BL; 
			end else if (i_WL[220]) begin 
				weight[220] <= i_BL; 
			end else if (i_WL[221]) begin 
				weight[221] <= i_BL; 
			end else if (i_WL[222]) begin 
				weight[222] <= i_BL; 
			end else if (i_WL[223]) begin 
				weight[223] <= i_BL; 
			end else if (i_WL[224]) begin 
				weight[224] <= i_BL; 
			end else if (i_WL[225]) begin 
				weight[225] <= i_BL; 
			end else if (i_WL[226]) begin 
				weight[226] <= i_BL; 
			end else if (i_WL[227]) begin 
				weight[227] <= i_BL; 
			end else if (i_WL[228]) begin 
				weight[228] <= i_BL; 
			end else if (i_WL[229]) begin 
				weight[229] <= i_BL; 
			end else if (i_WL[230]) begin 
				weight[230] <= i_BL; 
			end else if (i_WL[231]) begin 
				weight[231] <= i_BL; 
			end else if (i_WL[232]) begin 
				weight[232] <= i_BL; 
			end else if (i_WL[233]) begin 
				weight[233] <= i_BL; 
			end else if (i_WL[234]) begin 
				weight[234] <= i_BL; 
			end else if (i_WL[235]) begin 
				weight[235] <= i_BL; 
			end else if (i_WL[236]) begin 
				weight[236] <= i_BL; 
			end else if (i_WL[237]) begin 
				weight[237] <= i_BL; 
			end else if (i_WL[238]) begin 
				weight[238] <= i_BL; 
			end else if (i_WL[239]) begin 
				weight[239] <= i_BL; 
			end else if (i_WL[240]) begin 
				weight[240] <= i_BL; 
			end else if (i_WL[241]) begin 
				weight[241] <= i_BL; 
			end else if (i_WL[242]) begin 
				weight[242] <= i_BL; 
			end else if (i_WL[243]) begin 
				weight[243] <= i_BL; 
			end else if (i_WL[244]) begin 
				weight[244] <= i_BL; 
			end else if (i_WL[245]) begin 
				weight[245] <= i_BL; 
			end else if (i_WL[246]) begin 
				weight[246] <= i_BL; 
			end else if (i_WL[247]) begin 
				weight[247] <= i_BL; 
			end else if (i_WL[248]) begin 
				weight[248] <= i_BL; 
			end else if (i_WL[249]) begin 
				weight[249] <= i_BL; 
			end else if (i_WL[250]) begin 
				weight[250] <= i_BL; 
			end else if (i_WL[251]) begin 
				weight[251] <= i_BL; 
			end else if (i_WL[252]) begin 
				weight[252] <= i_BL; 
			end else if (i_WL[253]) begin 
				weight[253] <= i_BL; 
			end else if (i_WL[254]) begin 
				weight[254] <= i_BL; 
			end else if (i_WL[255]) begin 
				weight[255] <= i_BL; 
			end else if (i_WL[256]) begin 
				weight[256] <= i_BL; 
			end else if (i_WL[257]) begin 
				weight[257] <= i_BL; 
			end else if (i_WL[258]) begin 
				weight[258] <= i_BL; 
			end else if (i_WL[259]) begin 
				weight[259] <= i_BL; 
			end else if (i_WL[260]) begin 
				weight[260] <= i_BL; 
			end else if (i_WL[261]) begin 
				weight[261] <= i_BL; 
			end else if (i_WL[262]) begin 
				weight[262] <= i_BL; 
			end else if (i_WL[263]) begin 
				weight[263] <= i_BL; 
			end else if (i_WL[264]) begin 
				weight[264] <= i_BL; 
			end else if (i_WL[265]) begin 
				weight[265] <= i_BL; 
			end else if (i_WL[266]) begin 
				weight[266] <= i_BL; 
			end else if (i_WL[267]) begin 
				weight[267] <= i_BL; 
			end else if (i_WL[268]) begin 
				weight[268] <= i_BL; 
			end else if (i_WL[269]) begin 
				weight[269] <= i_BL; 
			end else if (i_WL[270]) begin 
				weight[270] <= i_BL; 
			end else if (i_WL[271]) begin 
				weight[271] <= i_BL; 
			end else if (i_WL[272]) begin 
				weight[272] <= i_BL; 
			end else if (i_WL[273]) begin 
				weight[273] <= i_BL; 
			end else if (i_WL[274]) begin 
				weight[274] <= i_BL; 
			end else if (i_WL[275]) begin 
				weight[275] <= i_BL; 
			end else if (i_WL[276]) begin 
				weight[276] <= i_BL; 
			end else if (i_WL[277]) begin 
				weight[277] <= i_BL; 
			end else if (i_WL[278]) begin 
				weight[278] <= i_BL; 
			end else if (i_WL[279]) begin 
				weight[279] <= i_BL; 
			end else if (i_WL[280]) begin 
				weight[280] <= i_BL; 
			end else if (i_WL[281]) begin 
				weight[281] <= i_BL; 
			end else if (i_WL[282]) begin 
				weight[282] <= i_BL; 
			end else if (i_WL[283]) begin 
				weight[283] <= i_BL; 
			end else if (i_WL[284]) begin 
				weight[284] <= i_BL; 
			end else if (i_WL[285]) begin 
				weight[285] <= i_BL; 
			end else if (i_WL[286]) begin 
				weight[286] <= i_BL; 
			end else if (i_WL[287]) begin 
				weight[287] <= i_BL; 
			end
		end
	end

	always @(posedge CLK) begin
		if (!RSTN) begin
			activation[0] <= 0;
			activation[1] <= 0;
			activation[2] <= 0;
			activation[3] <= 0;
			activation[4] <= 0;
			activation[5] <= 0;
			activation[6] <= 0;
			activation[7] <= 0;
		end else begin
			if (i_activation_in_en) begin
				activation[counter] <= i_activation_data;
			end
		end
	end

	always @(*) begin
		if (counter2 == 3'd7) begin
			o_result0 =   weight[0][31:0];
			o_result1 =   weight[1][31:0];
			o_result2 =   weight[2][31:0];
			o_result3 =   weight[3][31:0];
			o_result4 =   weight[4][31:0];
			o_result5 =   weight[5][31:0];
			o_result6 =   weight[6][31:0];
			o_result7 =   weight[7][31:0];
			o_result8 =   weight[8][31:0];
			o_result9 =   weight[9][31:0];
			o_result10 =  weight[10][31:0];
			o_result11 =  weight[11][31:0];
			o_result12 =  weight[12][31:0];
			o_result13 =  weight[13][31:0];
			o_result14 =  weight[14][31:0];
			o_result15 =  weight[15][31:0];
			o_result16 =  weight[16][31:0];
			o_result17 =  weight[17][31:0];
			o_result18 =  weight[18][31:0];
			o_result19 =  weight[19][31:0];
			o_result20 =  weight[20][31:0];
			o_result21 =  weight[21][31:0];
			o_result22 =  weight[22][31:0];
			o_result23 =  weight[23][31:0];
			o_result24 =  weight[24][31:0];
			o_result25 =  weight[25][31:0];
			o_result26 =  weight[26][31:0];
			o_result27 =  weight[27][31:0];
			o_result28 =  weight[28][31:0];
			o_result29 =  weight[29][31:0];
			o_result30 =  weight[30][31:0];
			o_result31 =  weight[31][31:0];
			o_result32 =  weight[32][31:0];
			o_result33 =  weight[33][31:0];
			o_result34 =  weight[34][31:0];
			o_result35 =  weight[35][31:0];
			o_result36 =  weight[36][31:0];
			o_result37 =  weight[37][31:0];
			o_result38 =  weight[38][31:0];
			o_result39 =  weight[39][31:0];
			o_result40 =  weight[40][31:0];
			o_result41 =  weight[41][31:0];
			o_result42 =  weight[42][31:0];
			o_result43 =  weight[43][31:0];
			o_result44 =  weight[44][31:0];
			o_result45 =  weight[45][31:0];
			o_result46 =  weight[46][31:0];
			o_result47 =  weight[47][31:0];
			o_result48 =  weight[48][31:0];
			o_result49 =  weight[49][31:0];
			o_result50 =  weight[50][31:0];
			o_result51 =  weight[51][31:0];
			o_result52 =  weight[52][31:0];
			o_result53 =  weight[53][31:0];
			o_result54 =  weight[54][31:0];
			o_result55 =  weight[55][31:0];
			o_result56 =  weight[56][31:0];
			o_result57 =  weight[57][31:0];
			o_result58 =  weight[58][31:0];
			o_result59 =  weight[59][31:0];
			o_result60 =  weight[60][31:0];
			o_result61 =  weight[61][31:0];
			o_result62 =  weight[62][31:0];
			o_result63 =  weight[63][31:0];
			o_result64 =  weight[64][31:0];
			o_result65 =  weight[65][31:0];
			o_result66 =  weight[66][31:0];
			o_result67 =  weight[67][31:0];
			o_result68 =  weight[68][31:0];
			o_result69 =  weight[69][31:0];
			o_result70 =  weight[70][31:0];
			o_result71 =  weight[71][31:0];
			o_result72 =  weight[72][31:0];
			o_result73 =  weight[73][31:0];
			o_result74 =  weight[74][31:0];
			o_result75 =  weight[75][31:0];
			o_result76 =  weight[76][31:0];
			o_result77 =  weight[77][31:0];
			o_result78 =  weight[78][31:0];
			o_result79 =  weight[79][31:0];
			o_result80 =  weight[80][31:0];
			o_result81 =  weight[81][31:0];
			o_result82 =  weight[82][31:0];
			o_result83 =  weight[83][31:0];
			o_result84 =  weight[84][31:0];
			o_result85 =  weight[85][31:0];
			o_result86 =  weight[86][31:0];
			o_result87 =  weight[87][31:0];
			o_result88 =  weight[88][31:0];
			o_result89 =  weight[89][31:0];
			o_result90 =  weight[90][31:0];
			o_result91 =  weight[91][31:0];
			o_result92 =  weight[92][31:0];
			o_result93 =  weight[93][31:0];
			o_result94 =  weight[94][31:0];
			o_result95 =  weight[95][31:0];
			o_result96 =  weight[96][31:0];
			o_result97 =  weight[97][31:0];
			o_result98 =  weight[98][31:0];
			o_result99 =  weight[99][31:0];
			o_result100 = weight[100][31:0];
			o_result101 = weight[101][31:0];
			o_result102 = weight[102][31:0];
			o_result103 = weight[103][31:0];
			o_result104 = weight[104][31:0];
			o_result105 = weight[105][31:0];
			o_result106 = weight[106][31:0];
			o_result107 = weight[107][31:0];
			o_result108 = weight[108][31:0];
			o_result109 = weight[109][31:0];
			o_result110 = weight[110][31:0];
			o_result111 = weight[111][31:0];
			o_result112 = weight[112][31:0];
			o_result113 = weight[113][31:0];
			o_result114 = weight[114][31:0];
			o_result115 = weight[115][31:0];
			o_result116 = weight[116][31:0];
			o_result117 = weight[117][31:0];
			o_result118 = weight[118][31:0];
			o_result119 = weight[119][31:0];
			o_result120 = weight[120][31:0];
			o_result121 = weight[121][31:0];
			o_result122 = weight[122][31:0];
			o_result123 = weight[123][31:0];
			o_result124 = weight[124][31:0];
			o_result125 = weight[125][31:0];
			o_result126 = weight[126][31:0];
			o_result127 = weight[127][31:0];
			o_result128 = weight[128][31:0];
			o_result129 = weight[129][31:0];
			o_result130 = weight[130][31:0];
			o_result131 = weight[131][31:0];
			o_result132 = weight[132][31:0];
			o_result133 = weight[133][31:0];
			o_result134 = weight[134][31:0];
			o_result135 = weight[135][31:0];
			o_result136 = weight[136][31:0];
			o_result137 = weight[137][31:0];
			o_result138 = weight[138][31:0];
			o_result139 = weight[139][31:0];
			o_result140 = weight[140][31:0];
			o_result141 = weight[141][31:0];
			o_result142 = weight[142][31:0];
			o_result143 = weight[143][31:0];
			o_result144 = weight[144][31:0];
			o_result145 = weight[145][31:0];
			o_result146 = weight[146][31:0];
			o_result147 = weight[147][31:0];
			o_result148 = weight[148][31:0];
			o_result149 = weight[149][31:0];
			o_result150 = weight[150][31:0];
			o_result151 = weight[151][31:0];
			o_result152 = weight[152][31:0];
			o_result153 = weight[153][31:0];
			o_result154 = weight[154][31:0];
			o_result155 = weight[155][31:0];
			o_result156 = weight[156][31:0];
			o_result157 = weight[157][31:0];
			o_result158 = weight[158][31:0];
			o_result159 = weight[159][31:0];
			o_result160 = weight[160][31:0];
			o_result161 = weight[161][31:0];
			o_result162 = weight[162][31:0];
			o_result163 = weight[163][31:0];
			o_result164 = weight[164][31:0];
			o_result165 = weight[165][31:0];
			o_result166 = weight[166][31:0];
			o_result167 = weight[167][31:0];
			o_result168 = weight[168][31:0];
			o_result169 = weight[169][31:0];
			o_result170 = weight[170][31:0];
			o_result171 = weight[171][31:0];
			o_result172 = weight[172][31:0];
			o_result173 = weight[173][31:0];
			o_result174 = weight[174][31:0];
			o_result175 = weight[175][31:0];
			o_result176 = weight[176][31:0];
			o_result177 = weight[177][31:0];
			o_result178 = weight[178][31:0];
			o_result179 = weight[179][31:0];
			o_result180 = weight[180][31:0];
			o_result181 = weight[181][31:0];
			o_result182 = weight[182][31:0];
			o_result183 = weight[183][31:0];
			o_result184 = weight[184][31:0];
			o_result185 = weight[185][31:0];
			o_result186 = weight[186][31:0];
			o_result187 = weight[187][31:0];
			o_result188 = weight[188][31:0];
			o_result189 = weight[189][31:0];
			o_result190 = weight[190][31:0];
			o_result191 = weight[191][31:0];
			o_result192 = weight[192][31:0];
			o_result193 = weight[193][31:0];
			o_result194 = weight[194][31:0];
			o_result195 = weight[195][31:0];
			o_result196 = weight[196][31:0];
			o_result197 = weight[197][31:0];
			o_result198 = weight[198][31:0];
			o_result199 = weight[199][31:0];
			o_result200 = weight[200][31:0];
			o_result201 = weight[201][31:0];
			o_result202 = weight[202][31:0];
			o_result203 = weight[203][31:0];
			o_result204 = weight[204][31:0];
			o_result205 = weight[205][31:0];
			o_result206 = weight[206][31:0];
			o_result207 = weight[207][31:0];
			o_result208 = weight[208][31:0];
			o_result209 = weight[209][31:0];
			o_result210 = weight[210][31:0];
			o_result211 = weight[211][31:0];
			o_result212 = weight[212][31:0];
			o_result213 = weight[213][31:0];
			o_result214 = weight[214][31:0];
			o_result215 = weight[215][31:0];
			o_result216 = weight[216][31:0];
			o_result217 = weight[217][31:0];
			o_result218 = weight[218][31:0];
			o_result219 = weight[219][31:0];
			o_result220 = weight[220][31:0];
			o_result221 = weight[221][31:0];
			o_result222 = weight[222][31:0];
			o_result223 = weight[223][31:0];
			o_result224 = weight[224][31:0];
			o_result225 = weight[225][31:0];
			o_result226 = weight[226][31:0];
			o_result227 = weight[227][31:0];
			o_result228 = weight[228][31:0];
			o_result229 = weight[229][31:0];
			o_result230 = weight[230][31:0];
			o_result231 = weight[231][31:0];
			o_result232 = weight[232][31:0];
			o_result233 = weight[233][31:0];
			o_result234 = weight[234][31:0];
			o_result235 = weight[235][31:0];
			o_result236 = weight[236][31:0];
			o_result237 = weight[237][31:0];
			o_result238 = weight[238][31:0];
			o_result239 = weight[239][31:0];
			o_result240 = weight[240][31:0];
			o_result241 = weight[241][31:0];
			o_result242 = weight[242][31:0];
			o_result243 = weight[243][31:0];
			o_result244 = weight[244][31:0];
			o_result245 = weight[245][31:0];
			o_result246 = weight[246][31:0];
			o_result247 = weight[247][31:0];
			o_result248 = weight[248][31:0];
			o_result249 = weight[249][31:0];
			o_result250 = weight[250][31:0];
			o_result251 = weight[251][31:0];
			o_result252 = weight[252][31:0];
			o_result253 = weight[253][31:0];
			o_result254 = weight[254][31:0];
			o_result255 = weight[255][31:0];
		end
	end

	assign o_result_out_en = (counter2 == 3'd7) ? 1 : 0;

	always @(posedge CLK) begin
		if (!RSTN) begin
			counter <= 0;
			counter2 <= 0;
		end else begin
			if (i_activation_in_en) begin
				counter <= counter + 1;
			end
			if (cal) begin
				counter2 <= counter2 + 1;
			end else begin
				counter2 <= 0;
			end
		end
	end

	
	always @(posedge CLK) begin
		if (!RSTN) begin
			cal <= 0;
		end else begin
			if (i_activation_in_en) begin
				if (counter == 3'd7) begin
					cal <= 1;
				end
			end
			if (counter2 == 3'd7) begin
				cal <= 0;
			end
		end
	end









endmodule