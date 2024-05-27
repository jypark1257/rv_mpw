module result_buffer (
	input i_clk,
	input i_rst,
	input i_result_in_en,
	input i_result_out_en,
	input [7:0] i_counter,
	input [8191:0] i_data,
	output reg [31:0] o_data
);

	reg [31:0] buffer [0:256];

	always @(posedge i_clk) begin
		if (i_rst) begin
			buffer[  0] <= 0;
			buffer[  1] <= 0;
			buffer[  2] <= 0;
			buffer[  3] <= 0;
			buffer[  4] <= 0;
			buffer[  5] <= 0;
			buffer[  6] <= 0;
			buffer[  7] <= 0;
			buffer[  8] <= 0;
			buffer[  9] <= 0;
			buffer[ 10] <= 0;
			buffer[ 11] <= 0;
			buffer[ 12] <= 0;
			buffer[ 13] <= 0;
			buffer[ 14] <= 0;
			buffer[ 15] <= 0;
			buffer[ 16] <= 0;
			buffer[ 17] <= 0;
			buffer[ 18] <= 0;
			buffer[ 19] <= 0;
			buffer[ 20] <= 0;
			buffer[ 21] <= 0;
			buffer[ 22] <= 0;
			buffer[ 23] <= 0;
			buffer[ 24] <= 0;
			buffer[ 25] <= 0;
			buffer[ 26] <= 0;
			buffer[ 27] <= 0;
			buffer[ 28] <= 0;
			buffer[ 29] <= 0;
			buffer[ 30] <= 0;
			buffer[ 31] <= 0;
			buffer[ 32] <= 0;
			buffer[ 33] <= 0;
			buffer[ 34] <= 0;
			buffer[ 35] <= 0;
			buffer[ 36] <= 0;
			buffer[ 37] <= 0;
			buffer[ 38] <= 0;
			buffer[ 39] <= 0;
			buffer[ 40] <= 0;
			buffer[ 41] <= 0;
			buffer[ 42] <= 0;
			buffer[ 43] <= 0;
			buffer[ 44] <= 0;
			buffer[ 45] <= 0;
			buffer[ 46] <= 0;
			buffer[ 47] <= 0;
			buffer[ 48] <= 0;
			buffer[ 49] <= 0;
			buffer[ 50] <= 0;
			buffer[ 51] <= 0;
			buffer[ 52] <= 0;
			buffer[ 53] <= 0;
			buffer[ 54] <= 0;
			buffer[ 55] <= 0;
			buffer[ 56] <= 0;
			buffer[ 57] <= 0;
			buffer[ 58] <= 0;
			buffer[ 59] <= 0;
			buffer[ 60] <= 0;
			buffer[ 61] <= 0;
			buffer[ 62] <= 0;
			buffer[ 63] <= 0;
			buffer[ 64] <= 0;
			buffer[ 65] <= 0;
			buffer[ 66] <= 0;
			buffer[ 67] <= 0;
			buffer[ 68] <= 0;
			buffer[ 69] <= 0;
			buffer[ 70] <= 0;
			buffer[ 71] <= 0;
			buffer[ 72] <= 0;
			buffer[ 73] <= 0;
			buffer[ 74] <= 0;
			buffer[ 75] <= 0;
			buffer[ 76] <= 0;
			buffer[ 77] <= 0;
			buffer[ 78] <= 0;
			buffer[ 79] <= 0;
			buffer[ 80] <= 0;
			buffer[ 81] <= 0;
			buffer[ 82] <= 0;
			buffer[ 83] <= 0;
			buffer[ 84] <= 0;
			buffer[ 85] <= 0;
			buffer[ 86] <= 0;
			buffer[ 87] <= 0;
			buffer[ 88] <= 0;
			buffer[ 89] <= 0;
			buffer[ 90] <= 0;
			buffer[ 91] <= 0;
			buffer[ 92] <= 0;
			buffer[ 93] <= 0;
			buffer[ 94] <= 0;
			buffer[ 95] <= 0;
			buffer[ 96] <= 0;
			buffer[ 97] <= 0;
			buffer[ 98] <= 0;
			buffer[ 99] <= 0;
			buffer[100] <= 0;
			buffer[101] <= 0;
			buffer[102] <= 0;
			buffer[103] <= 0;
			buffer[104] <= 0;
			buffer[105] <= 0;
			buffer[106] <= 0;
			buffer[107] <= 0;
			buffer[108] <= 0;
			buffer[109] <= 0;
			buffer[110] <= 0;
			buffer[111] <= 0;
			buffer[112] <= 0;
			buffer[113] <= 0;
			buffer[114] <= 0;
			buffer[115] <= 0;
			buffer[116] <= 0;
			buffer[117] <= 0;
			buffer[118] <= 0;
			buffer[119] <= 0;
			buffer[120] <= 0;
			buffer[121] <= 0;
			buffer[122] <= 0;
			buffer[123] <= 0;
			buffer[124] <= 0;
			buffer[125] <= 0;
			buffer[126] <= 0;
			buffer[127] <= 0;
			buffer[128] <= 0;
			buffer[129] <= 0;
			buffer[130] <= 0;
			buffer[131] <= 0;
			buffer[132] <= 0;
			buffer[133] <= 0;
			buffer[134] <= 0;
			buffer[135] <= 0;
			buffer[136] <= 0;
			buffer[137] <= 0;
			buffer[138] <= 0;
			buffer[139] <= 0;
			buffer[140] <= 0;
			buffer[141] <= 0;
			buffer[142] <= 0;
			buffer[143] <= 0;
			buffer[144] <= 0;
			buffer[145] <= 0;
			buffer[146] <= 0;
			buffer[147] <= 0;
			buffer[148] <= 0;
			buffer[149] <= 0;
			buffer[150] <= 0;
			buffer[151] <= 0;
			buffer[152] <= 0;
			buffer[153] <= 0;
			buffer[154] <= 0;
			buffer[155] <= 0;
			buffer[156] <= 0;
			buffer[157] <= 0;
			buffer[158] <= 0;
			buffer[159] <= 0;
			buffer[160] <= 0;
			buffer[161] <= 0;
			buffer[162] <= 0;
			buffer[163] <= 0;
			buffer[164] <= 0;
			buffer[165] <= 0;
			buffer[166] <= 0;
			buffer[167] <= 0;
			buffer[168] <= 0;
			buffer[169] <= 0;
			buffer[170] <= 0;
			buffer[171] <= 0;
			buffer[172] <= 0;
			buffer[173] <= 0;
			buffer[174] <= 0;
			buffer[175] <= 0;
			buffer[176] <= 0;
			buffer[177] <= 0;
			buffer[178] <= 0;
			buffer[179] <= 0;
			buffer[180] <= 0;
			buffer[181] <= 0;
			buffer[182] <= 0;
			buffer[183] <= 0;
			buffer[184] <= 0;
			buffer[185] <= 0;
			buffer[186] <= 0;
			buffer[187] <= 0;
			buffer[188] <= 0;
			buffer[189] <= 0;
			buffer[190] <= 0;
			buffer[191] <= 0;
			buffer[192] <= 0;
			buffer[193] <= 0;
			buffer[194] <= 0;
			buffer[195] <= 0;
			buffer[196] <= 0;
			buffer[197] <= 0;
			buffer[198] <= 0;
			buffer[199] <= 0;
			buffer[200] <= 0;
			buffer[201] <= 0;
			buffer[202] <= 0;
			buffer[203] <= 0;
			buffer[204] <= 0;
			buffer[205] <= 0;
			buffer[206] <= 0;
			buffer[207] <= 0;
			buffer[208] <= 0;
			buffer[209] <= 0;
			buffer[210] <= 0;
			buffer[211] <= 0;
			buffer[212] <= 0;
			buffer[213] <= 0;
			buffer[214] <= 0;
			buffer[215] <= 0;
			buffer[216] <= 0;
			buffer[217] <= 0;
			buffer[218] <= 0;
			buffer[219] <= 0;
			buffer[220] <= 0;
			buffer[221] <= 0;
			buffer[222] <= 0;
			buffer[223] <= 0;
			buffer[224] <= 0;
			buffer[225] <= 0;
			buffer[226] <= 0;
			buffer[227] <= 0;
			buffer[228] <= 0;
			buffer[229] <= 0;
			buffer[230] <= 0;
			buffer[231] <= 0;
			buffer[232] <= 0;
			buffer[233] <= 0;
			buffer[234] <= 0;
			buffer[235] <= 0;
			buffer[236] <= 0;
			buffer[237] <= 0;
			buffer[238] <= 0;
			buffer[239] <= 0;
			buffer[240] <= 0;
			buffer[241] <= 0;
			buffer[242] <= 0;
			buffer[243] <= 0;
			buffer[244] <= 0;
			buffer[245] <= 0;
			buffer[246] <= 0;
			buffer[247] <= 0;
			buffer[248] <= 0;
			buffer[249] <= 0;
			buffer[250] <= 0;
			buffer[251] <= 0;
			buffer[252] <= 0;
			buffer[253] <= 0;
			buffer[254] <= 0;
			buffer[255] <= 0;
		end else begin
			if (i_result_in_en) begin
				buffer[  0] <= i_data[8191:8160];
				buffer[  1] <= i_data[8159:8128];
				buffer[  2] <= i_data[8127:8096];
				buffer[  3] <= i_data[8095:8064];
				buffer[  4] <= i_data[8063:8032];
				buffer[  5] <= i_data[8031:8000];
				buffer[  6] <= i_data[7999:7968];
				buffer[  7] <= i_data[7967:7936];
				buffer[  8] <= i_data[7935:7904];
				buffer[  9] <= i_data[7903:7872];
				buffer[ 10] <= i_data[7871:7840];
				buffer[ 11] <= i_data[7839:7808];
				buffer[ 12] <= i_data[7807:7776];
				buffer[ 13] <= i_data[7775:7744];
				buffer[ 14] <= i_data[7743:7712];
				buffer[ 15] <= i_data[7711:7680];
				buffer[ 16] <= i_data[7679:7648];
				buffer[ 17] <= i_data[7647:7616];
				buffer[ 18] <= i_data[7615:7584];
				buffer[ 19] <= i_data[7583:7552];
				buffer[ 20] <= i_data[7551:7520];
				buffer[ 21] <= i_data[7519:7488];
				buffer[ 22] <= i_data[7487:7456];
				buffer[ 23] <= i_data[7455:7424];
				buffer[ 24] <= i_data[7423:7392];
				buffer[ 25] <= i_data[7391:7360];
				buffer[ 26] <= i_data[7359:7328];
				buffer[ 27] <= i_data[7327:7296];
				buffer[ 28] <= i_data[7295:7264];
				buffer[ 29] <= i_data[7263:7232];
				buffer[ 30] <= i_data[7231:7200];
				buffer[ 31] <= i_data[7199:7168];
				buffer[ 32] <= i_data[7167:7136];
				buffer[ 33] <= i_data[7135:7104];
				buffer[ 34] <= i_data[7103:7072];
				buffer[ 35] <= i_data[7071:7040];
				buffer[ 36] <= i_data[7039:7008];
				buffer[ 37] <= i_data[7007:6976];
				buffer[ 38] <= i_data[6975:6944];
				buffer[ 39] <= i_data[6943:6912];
				buffer[ 40] <= i_data[6911:6880];
				buffer[ 41] <= i_data[6879:6848];
				buffer[ 42] <= i_data[6847:6816];
				buffer[ 43] <= i_data[6815:6784];
				buffer[ 44] <= i_data[6783:6752];
				buffer[ 45] <= i_data[6751:6720];
				buffer[ 46] <= i_data[6719:6688];
				buffer[ 47] <= i_data[6687:6656];
				buffer[ 48] <= i_data[6655:6624];
				buffer[ 49] <= i_data[6623:6592];
				buffer[ 50] <= i_data[6591:6560];
				buffer[ 51] <= i_data[6559:6528];
				buffer[ 52] <= i_data[6527:6496];
				buffer[ 53] <= i_data[6495:6464];
				buffer[ 54] <= i_data[6463:6432];
				buffer[ 55] <= i_data[6431:6400];
				buffer[ 56] <= i_data[6399:6368];
				buffer[ 57] <= i_data[6367:6336];
				buffer[ 58] <= i_data[6335:6304];
				buffer[ 59] <= i_data[6303:6272];
				buffer[ 60] <= i_data[6271:6240];
				buffer[ 61] <= i_data[6239:6208];
				buffer[ 62] <= i_data[6207:6176];
				buffer[ 63] <= i_data[6175:6144];
				buffer[ 64] <= i_data[6143:6112];
				buffer[ 65] <= i_data[6111:6080];
				buffer[ 66] <= i_data[6079:6048];
				buffer[ 67] <= i_data[6047:6016];
				buffer[ 68] <= i_data[6015:5984];
				buffer[ 69] <= i_data[5983:5952];
				buffer[ 70] <= i_data[5951:5920];
				buffer[ 71] <= i_data[5919:5888];
				buffer[ 72] <= i_data[5887:5856];
				buffer[ 73] <= i_data[5855:5824];
				buffer[ 74] <= i_data[5823:5792];
				buffer[ 75] <= i_data[5791:5760];
				buffer[ 76] <= i_data[5759:5728];
				buffer[ 77] <= i_data[5727:5696];
				buffer[ 78] <= i_data[5695:5664];
				buffer[ 79] <= i_data[5663:5632];
				buffer[ 80] <= i_data[5631:5600];
				buffer[ 81] <= i_data[5599:5568];
				buffer[ 82] <= i_data[5567:5536];
				buffer[ 83] <= i_data[5535:5504];
				buffer[ 84] <= i_data[5503:5472];
				buffer[ 85] <= i_data[5471:5440];
				buffer[ 86] <= i_data[5439:5408];
				buffer[ 87] <= i_data[5407:5376];
				buffer[ 88] <= i_data[5375:5344];
				buffer[ 89] <= i_data[5343:5312];
				buffer[ 90] <= i_data[5311:5280];
				buffer[ 91] <= i_data[5279:5248];
				buffer[ 92] <= i_data[5247:5216];
				buffer[ 93] <= i_data[5215:5184];
				buffer[ 94] <= i_data[5183:5152];
				buffer[ 95] <= i_data[5151:5120];
				buffer[ 96] <= i_data[5119:5088];
				buffer[ 97] <= i_data[5087:5056];
				buffer[ 98] <= i_data[5055:5024];
				buffer[ 99] <= i_data[5023:4992];
				buffer[100] <= i_data[4991:4960];
				buffer[101] <= i_data[4959:4928];
				buffer[102] <= i_data[4927:4896];
				buffer[103] <= i_data[4895:4864];
				buffer[104] <= i_data[4863:4832];
				buffer[105] <= i_data[4831:4800];
				buffer[106] <= i_data[4799:4768];
				buffer[107] <= i_data[4767:4736];
				buffer[108] <= i_data[4735:4704];
				buffer[109] <= i_data[4703:4672];
				buffer[110] <= i_data[4671:4640];
				buffer[111] <= i_data[4639:4608];
				buffer[112] <= i_data[4607:4576];
				buffer[113] <= i_data[4575:4544];
				buffer[114] <= i_data[4543:4512];
				buffer[115] <= i_data[4511:4480];
				buffer[116] <= i_data[4479:4448];
				buffer[117] <= i_data[4447:4416];
				buffer[118] <= i_data[4415:4384];
				buffer[119] <= i_data[4383:4352];
				buffer[120] <= i_data[4351:4320];
				buffer[121] <= i_data[4319:4288];
				buffer[122] <= i_data[4287:4256];
				buffer[123] <= i_data[4255:4224];
				buffer[124] <= i_data[4223:4192];
				buffer[125] <= i_data[4191:4160];
				buffer[126] <= i_data[4159:4128];
				buffer[127] <= i_data[4127:4096];
				buffer[128] <= i_data[4095:4064];
				buffer[129] <= i_data[4063:4032];
				buffer[130] <= i_data[4031:4000];
				buffer[131] <= i_data[3999:3968];
				buffer[132] <= i_data[3967:3936];
				buffer[133] <= i_data[3935:3904];
				buffer[134] <= i_data[3903:3872];
				buffer[135] <= i_data[3871:3840];
				buffer[136] <= i_data[3839:3808];
				buffer[137] <= i_data[3807:3776];
				buffer[138] <= i_data[3775:3744];
				buffer[139] <= i_data[3743:3712];
				buffer[140] <= i_data[3711:3680];
				buffer[141] <= i_data[3679:3648];
				buffer[142] <= i_data[3647:3616];
				buffer[143] <= i_data[3615:3584];
				buffer[144] <= i_data[3583:3552];
				buffer[145] <= i_data[3551:3520];
				buffer[146] <= i_data[3519:3488];
				buffer[147] <= i_data[3487:3456];
				buffer[148] <= i_data[3455:3424];
				buffer[149] <= i_data[3423:3392];
				buffer[150] <= i_data[3391:3360];
				buffer[151] <= i_data[3359:3328];
				buffer[152] <= i_data[3327:3296];
				buffer[153] <= i_data[3295:3264];
				buffer[154] <= i_data[3263:3232];
				buffer[155] <= i_data[3231:3200];
				buffer[156] <= i_data[3199:3168];
				buffer[157] <= i_data[3167:3136];
				buffer[158] <= i_data[3135:3104];
				buffer[159] <= i_data[3103:3072];
				buffer[160] <= i_data[3071:3040];
				buffer[161] <= i_data[3039:3008];
				buffer[162] <= i_data[3007:2976];
				buffer[163] <= i_data[2975:2944];
				buffer[164] <= i_data[2943:2912];
				buffer[165] <= i_data[2911:2880];
				buffer[166] <= i_data[2879:2848];
				buffer[167] <= i_data[2847:2816];
				buffer[168] <= i_data[2815:2784];
				buffer[169] <= i_data[2783:2752];
				buffer[170] <= i_data[2751:2720];
				buffer[171] <= i_data[2719:2688];
				buffer[172] <= i_data[2687:2656];
				buffer[173] <= i_data[2655:2624];
				buffer[174] <= i_data[2623:2592];
				buffer[175] <= i_data[2591:2560];
				buffer[176] <= i_data[2559:2528];
				buffer[177] <= i_data[2527:2496];
				buffer[178] <= i_data[2495:2464];
				buffer[179] <= i_data[2463:2432];
				buffer[180] <= i_data[2431:2400];
				buffer[181] <= i_data[2399:2368];
				buffer[182] <= i_data[2367:2336];
				buffer[183] <= i_data[2335:2304];
				buffer[184] <= i_data[2303:2272];
				buffer[185] <= i_data[2271:2240];
				buffer[186] <= i_data[2239:2208];
				buffer[187] <= i_data[2207:2176];
				buffer[188] <= i_data[2175:2144];
				buffer[189] <= i_data[2143:2112];
				buffer[190] <= i_data[2111:2080];
				buffer[191] <= i_data[2079:2048];
				buffer[192] <= i_data[2047:2016];
				buffer[193] <= i_data[2015:1984];
				buffer[194] <= i_data[1983:1952];
				buffer[195] <= i_data[1951:1920];
				buffer[196] <= i_data[1919:1888];
				buffer[197] <= i_data[1887:1856];
				buffer[198] <= i_data[1855:1824];
				buffer[199] <= i_data[1823:1792];
				buffer[200] <= i_data[1791:1760];
				buffer[201] <= i_data[1759:1728];
				buffer[202] <= i_data[1727:1696];
				buffer[203] <= i_data[1695:1664];
				buffer[204] <= i_data[1663:1632];
				buffer[205] <= i_data[1631:1600];
				buffer[206] <= i_data[1599:1568];
				buffer[207] <= i_data[1567:1536];
				buffer[208] <= i_data[1535:1504];
				buffer[209] <= i_data[1503:1472];
				buffer[210] <= i_data[1471:1440];
				buffer[211] <= i_data[1439:1408];
				buffer[212] <= i_data[1407:1376];
				buffer[213] <= i_data[1375:1344];
				buffer[214] <= i_data[1343:1312];
				buffer[215] <= i_data[1311:1280];
				buffer[216] <= i_data[1279:1248];
				buffer[217] <= i_data[1247:1216];
				buffer[218] <= i_data[1215:1184];
				buffer[219] <= i_data[1183:1152];
				buffer[220] <= i_data[1151:1120];
				buffer[221] <= i_data[1119:1088];
				buffer[222] <= i_data[1087:1056];
				buffer[223] <= i_data[1055:1024];
				buffer[224] <= i_data[1023:992];
				buffer[225] <= i_data[991:960];
				buffer[226] <= i_data[959:928];
				buffer[227] <= i_data[927:896];
				buffer[228] <= i_data[895:864];
				buffer[229] <= i_data[863:832];
				buffer[230] <= i_data[831:800];
				buffer[231] <= i_data[799:768];
				buffer[232] <= i_data[767:736];
				buffer[233] <= i_data[735:704];
				buffer[234] <= i_data[703:672];
				buffer[235] <= i_data[671:640];
				buffer[236] <= i_data[639:608];
				buffer[237] <= i_data[607:576];
				buffer[238] <= i_data[575:544];
				buffer[239] <= i_data[543:512];
				buffer[240] <= i_data[511:480];
				buffer[241] <= i_data[479:448];
				buffer[242] <= i_data[447:416];
				buffer[243] <= i_data[415:384];
				buffer[244] <= i_data[383:352];
				buffer[245] <= i_data[351:320];
				buffer[246] <= i_data[319:288];
				buffer[247] <= i_data[287:256];
				buffer[248] <= i_data[255:224];
				buffer[249] <= i_data[223:192];
				buffer[250] <= i_data[191:160];
				buffer[251] <= i_data[159:128];
				buffer[252] <= i_data[127:96];
				buffer[253] <= i_data[95:64];
				buffer[254] <= i_data[63:32];
				buffer[255] <= i_data[31:0];
			end
		end
	end

	always @(*) begin
		if (i_rst) begin
			o_data <= 0;
		end else begin
			if (i_result_out_en) begin
				o_data <= buffer[i_counter];
			end else begin
				o_data <= 0;
			end
		end
	end

endmodule