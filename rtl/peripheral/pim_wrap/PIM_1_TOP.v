module PIM_TOP (
	input CLK, 
	input RSTN,

	//BUS interface
	input [31:0] i_address,
	input [31:0] i_data,
	output [31:0] o_data
);

	wire [7:0] counter;

	//BL driver
	wire weight_buffer_in_en, weight_buffer_out_en;
	wire [15:0] cam_weight_in_data, mac_weight_in_data;
	wire cam_bl_out_en, mac_bl_out_en;

	//WL driver
	wire [8:0] WL_address;

	//activation
	wire activation_buffer_in_en, activation_buffer_out_en;
	wire [31:0] activation_in_data;

	//result
	wire result_buffer_out_en;
	wire [31:0] result_buffer_out;

	//connected to CAM
	wire [255:0] CAM_BL;
	wire [287:0] CAM_WL;
	wire [287:0] CAM_activation_data;
	wire CAM_activation_in_en;
//
	wire CAM_result_out_en;
	wire [31:0] CAM_result0;
	wire [31:0] CAM_result1;
	wire [31:0] CAM_result2;
	wire [31:0] CAM_result3;
	wire [31:0] CAM_result4;
	wire [31:0] CAM_result5;
	wire [31:0] CAM_result6;
	wire [31:0] CAM_result7;
	wire [31:0] CAM_result8;
	wire [31:0] CAM_result9;
	wire [31:0] CAM_result10;
	wire [31:0] CAM_result11;
	wire [31:0] CAM_result12;
	wire [31:0] CAM_result13;
	wire [31:0] CAM_result14;
	wire [31:0] CAM_result15;
	wire [31:0] CAM_result16;
	wire [31:0] CAM_result17;
	wire [31:0] CAM_result18;
	wire [31:0] CAM_result19;
	wire [31:0] CAM_result20;
	wire [31:0] CAM_result21;
	wire [31:0] CAM_result22;
	wire [31:0] CAM_result23;
	wire [31:0] CAM_result24;
	wire [31:0] CAM_result25;
	wire [31:0] CAM_result26;
	wire [31:0] CAM_result27;
	wire [31:0] CAM_result28;
	wire [31:0] CAM_result29;
	wire [31:0] CAM_result30;
	wire [31:0] CAM_result31;
	wire [31:0] CAM_result32;
	wire [31:0] CAM_result33;
	wire [31:0] CAM_result34;
	wire [31:0] CAM_result35;
	wire [31:0] CAM_result36;
	wire [31:0] CAM_result37;
	wire [31:0] CAM_result38;
	wire [31:0] CAM_result39;
	wire [31:0] CAM_result40;
	wire [31:0] CAM_result41;
	wire [31:0] CAM_result42;
	wire [31:0] CAM_result43;
	wire [31:0] CAM_result44;
	wire [31:0] CAM_result45;
	wire [31:0] CAM_result46;
	wire [31:0] CAM_result47;
	wire [31:0] CAM_result48;
	wire [31:0] CAM_result49;
	wire [31:0] CAM_result50;
	wire [31:0] CAM_result51;
	wire [31:0] CAM_result52;
	wire [31:0] CAM_result53;
	wire [31:0] CAM_result54;
	wire [31:0] CAM_result55;
	wire [31:0] CAM_result56;
	wire [31:0] CAM_result57;
	wire [31:0] CAM_result58;
	wire [31:0] CAM_result59;
	wire [31:0] CAM_result60;
	wire [31:0] CAM_result61;
	wire [31:0] CAM_result62;
	wire [31:0] CAM_result63;
	wire [31:0] CAM_result64;
	wire [31:0] CAM_result65;
	wire [31:0] CAM_result66;
	wire [31:0] CAM_result67;
	wire [31:0] CAM_result68;
	wire [31:0] CAM_result69;
	wire [31:0] CAM_result70;
	wire [31:0] CAM_result71;
	wire [31:0] CAM_result72;
	wire [31:0] CAM_result73;
	wire [31:0] CAM_result74;
	wire [31:0] CAM_result75;
	wire [31:0] CAM_result76;
	wire [31:0] CAM_result77;
	wire [31:0] CAM_result78;
	wire [31:0] CAM_result79;
	wire [31:0] CAM_result80;
	wire [31:0] CAM_result81;
	wire [31:0] CAM_result82;
	wire [31:0] CAM_result83;
	wire [31:0] CAM_result84;
	wire [31:0] CAM_result85;
	wire [31:0] CAM_result86;
	wire [31:0] CAM_result87;
	wire [31:0] CAM_result88;
	wire [31:0] CAM_result89;
	wire [31:0] CAM_result90;
	wire [31:0] CAM_result91;
	wire [31:0] CAM_result92;
	wire [31:0] CAM_result93;
	wire [31:0] CAM_result94;
	wire [31:0] CAM_result95;
	wire [31:0] CAM_result96;
	wire [31:0] CAM_result97;
	wire [31:0] CAM_result98;
	wire [31:0] CAM_result99;
	wire [31:0] CAM_result100;
	wire [31:0] CAM_result101;
	wire [31:0] CAM_result102;
	wire [31:0] CAM_result103;
	wire [31:0] CAM_result104;
	wire [31:0] CAM_result105;
	wire [31:0] CAM_result106;
	wire [31:0] CAM_result107;
	wire [31:0] CAM_result108;
	wire [31:0] CAM_result109;
	wire [31:0] CAM_result110;
	wire [31:0] CAM_result111;
	wire [31:0] CAM_result112;
	wire [31:0] CAM_result113;
	wire [31:0] CAM_result114;
	wire [31:0] CAM_result115;
	wire [31:0] CAM_result116;
	wire [31:0] CAM_result117;
	wire [31:0] CAM_result118;
	wire [31:0] CAM_result119;
	wire [31:0] CAM_result120;
	wire [31:0] CAM_result121;
	wire [31:0] CAM_result122;
	wire [31:0] CAM_result123;
	wire [31:0] CAM_result124;
	wire [31:0] CAM_result125;
	wire [31:0] CAM_result126;
	wire [31:0] CAM_result127;
	wire [31:0] CAM_result128;
	wire [31:0] CAM_result129;
	wire [31:0] CAM_result130;
	wire [31:0] CAM_result131;
	wire [31:0] CAM_result132;
	wire [31:0] CAM_result133;
	wire [31:0] CAM_result134;
	wire [31:0] CAM_result135;
	wire [31:0] CAM_result136;
	wire [31:0] CAM_result137;
	wire [31:0] CAM_result138;
	wire [31:0] CAM_result139;
	wire [31:0] CAM_result140;
	wire [31:0] CAM_result141;
	wire [31:0] CAM_result142;
	wire [31:0] CAM_result143;
	wire [31:0] CAM_result144;
	wire [31:0] CAM_result145;
	wire [31:0] CAM_result146;
	wire [31:0] CAM_result147;
	wire [31:0] CAM_result148;
	wire [31:0] CAM_result149;
	wire [31:0] CAM_result150;
	wire [31:0] CAM_result151;
	wire [31:0] CAM_result152;
	wire [31:0] CAM_result153;
	wire [31:0] CAM_result154;
	wire [31:0] CAM_result155;
	wire [31:0] CAM_result156;
	wire [31:0] CAM_result157;
	wire [31:0] CAM_result158;
	wire [31:0] CAM_result159;
	wire [31:0] CAM_result160;
	wire [31:0] CAM_result161;
	wire [31:0] CAM_result162;
	wire [31:0] CAM_result163;
	wire [31:0] CAM_result164;
	wire [31:0] CAM_result165;
	wire [31:0] CAM_result166;
	wire [31:0] CAM_result167;
	wire [31:0] CAM_result168;
	wire [31:0] CAM_result169;
	wire [31:0] CAM_result170;
	wire [31:0] CAM_result171;
	wire [31:0] CAM_result172;
	wire [31:0] CAM_result173;
	wire [31:0] CAM_result174;
	wire [31:0] CAM_result175;
	wire [31:0] CAM_result176;
	wire [31:0] CAM_result177;
	wire [31:0] CAM_result178;
	wire [31:0] CAM_result179;
	wire [31:0] CAM_result180;
	wire [31:0] CAM_result181;
	wire [31:0] CAM_result182;
	wire [31:0] CAM_result183;
	wire [31:0] CAM_result184;
	wire [31:0] CAM_result185;
	wire [31:0] CAM_result186;
	wire [31:0] CAM_result187;
	wire [31:0] CAM_result188;
	wire [31:0] CAM_result189;
	wire [31:0] CAM_result190;
	wire [31:0] CAM_result191;
	wire [31:0] CAM_result192;
	wire [31:0] CAM_result193;
	wire [31:0] CAM_result194;
	wire [31:0] CAM_result195;
	wire [31:0] CAM_result196;
	wire [31:0] CAM_result197;
	wire [31:0] CAM_result198;
	wire [31:0] CAM_result199;
	wire [31:0] CAM_result200;
	wire [31:0] CAM_result201;
	wire [31:0] CAM_result202;
	wire [31:0] CAM_result203;
	wire [31:0] CAM_result204;
	wire [31:0] CAM_result205;
	wire [31:0] CAM_result206;
	wire [31:0] CAM_result207;
	wire [31:0] CAM_result208;
	wire [31:0] CAM_result209;
	wire [31:0] CAM_result210;
	wire [31:0] CAM_result211;
	wire [31:0] CAM_result212;
	wire [31:0] CAM_result213;
	wire [31:0] CAM_result214;
	wire [31:0] CAM_result215;
	wire [31:0] CAM_result216;
	wire [31:0] CAM_result217;
	wire [31:0] CAM_result218;
	wire [31:0] CAM_result219;
	wire [31:0] CAM_result220;
	wire [31:0] CAM_result221;
	wire [31:0] CAM_result222;
	wire [31:0] CAM_result223;
	wire [31:0] CAM_result224;
	wire [31:0] CAM_result225;
	wire [31:0] CAM_result226;
	wire [31:0] CAM_result227;
	wire [31:0] CAM_result228;
	wire [31:0] CAM_result229;
	wire [31:0] CAM_result230;
	wire [31:0] CAM_result231;
	wire [31:0] CAM_result232;
	wire [31:0] CAM_result233;
	wire [31:0] CAM_result234;
	wire [31:0] CAM_result235;
	wire [31:0] CAM_result236;
	wire [31:0] CAM_result237;
	wire [31:0] CAM_result238;
	wire [31:0] CAM_result239;
	wire [31:0] CAM_result240;
	wire [31:0] CAM_result241;
	wire [31:0] CAM_result242;
	wire [31:0] CAM_result243;
	wire [31:0] CAM_result244;
	wire [31:0] CAM_result245;
	wire [31:0] CAM_result246;
	wire [31:0] CAM_result247;
	wire [31:0] CAM_result248;
	wire [31:0] CAM_result249;
	wire [31:0] CAM_result250;
	wire [31:0] CAM_result251;
	wire [31:0] CAM_result252;
	wire [31:0] CAM_result253;
	wire [31:0] CAM_result254;
	wire [31:0] CAM_result255;
//

	//connected to MAC
	wire [255:0] MAC_BL;
	wire [287:0] MAC_WL;
	wire [287:0] MAC_activation_data;
	wire MAC_activation_in_en;
//
	wire MAC_result_out_en;
	wire [31:0] MAC_result0;
	wire [31:0] MAC_result1;
	wire [31:0] MAC_result2;
	wire [31:0] MAC_result3;
	wire [31:0] MAC_result4;
	wire [31:0] MAC_result5;
	wire [31:0] MAC_result6;
	wire [31:0] MAC_result7;
	wire [31:0] MAC_result8;
	wire [31:0] MAC_result9;
	wire [31:0] MAC_result10;
	wire [31:0] MAC_result11;
	wire [31:0] MAC_result12;
	wire [31:0] MAC_result13;
	wire [31:0] MAC_result14;
	wire [31:0] MAC_result15;
	wire [31:0] MAC_result16;
	wire [31:0] MAC_result17;
	wire [31:0] MAC_result18;
	wire [31:0] MAC_result19;
	wire [31:0] MAC_result20;
	wire [31:0] MAC_result21;
	wire [31:0] MAC_result22;
	wire [31:0] MAC_result23;
	wire [31:0] MAC_result24;
	wire [31:0] MAC_result25;
	wire [31:0] MAC_result26;
	wire [31:0] MAC_result27;
	wire [31:0] MAC_result28;
	wire [31:0] MAC_result29;
	wire [31:0] MAC_result30;
	wire [31:0] MAC_result31;
	wire [31:0] MAC_result32;
	wire [31:0] MAC_result33;
	wire [31:0] MAC_result34;
	wire [31:0] MAC_result35;
	wire [31:0] MAC_result36;
	wire [31:0] MAC_result37;
	wire [31:0] MAC_result38;
	wire [31:0] MAC_result39;
	wire [31:0] MAC_result40;
	wire [31:0] MAC_result41;
	wire [31:0] MAC_result42;
	wire [31:0] MAC_result43;
	wire [31:0] MAC_result44;
	wire [31:0] MAC_result45;
	wire [31:0] MAC_result46;
	wire [31:0] MAC_result47;
	wire [31:0] MAC_result48;
	wire [31:0] MAC_result49;
	wire [31:0] MAC_result50;
	wire [31:0] MAC_result51;
	wire [31:0] MAC_result52;
	wire [31:0] MAC_result53;
	wire [31:0] MAC_result54;
	wire [31:0] MAC_result55;
	wire [31:0] MAC_result56;
	wire [31:0] MAC_result57;
	wire [31:0] MAC_result58;
	wire [31:0] MAC_result59;
	wire [31:0] MAC_result60;
	wire [31:0] MAC_result61;
	wire [31:0] MAC_result62;
	wire [31:0] MAC_result63;
	wire [31:0] MAC_result64;
	wire [31:0] MAC_result65;
	wire [31:0] MAC_result66;
	wire [31:0] MAC_result67;
	wire [31:0] MAC_result68;
	wire [31:0] MAC_result69;
	wire [31:0] MAC_result70;
	wire [31:0] MAC_result71;
	wire [31:0] MAC_result72;
	wire [31:0] MAC_result73;
	wire [31:0] MAC_result74;
	wire [31:0] MAC_result75;
	wire [31:0] MAC_result76;
	wire [31:0] MAC_result77;
	wire [31:0] MAC_result78;
	wire [31:0] MAC_result79;
	wire [31:0] MAC_result80;
	wire [31:0] MAC_result81;
	wire [31:0] MAC_result82;
	wire [31:0] MAC_result83;
	wire [31:0] MAC_result84;
	wire [31:0] MAC_result85;
	wire [31:0] MAC_result86;
	wire [31:0] MAC_result87;
	wire [31:0] MAC_result88;
	wire [31:0] MAC_result89;
	wire [31:0] MAC_result90;
	wire [31:0] MAC_result91;
	wire [31:0] MAC_result92;
	wire [31:0] MAC_result93;
	wire [31:0] MAC_result94;
	wire [31:0] MAC_result95;
	wire [31:0] MAC_result96;
	wire [31:0] MAC_result97;
	wire [31:0] MAC_result98;
	wire [31:0] MAC_result99;
	wire [31:0] MAC_result100;
	wire [31:0] MAC_result101;
	wire [31:0] MAC_result102;
	wire [31:0] MAC_result103;
	wire [31:0] MAC_result104;
	wire [31:0] MAC_result105;
	wire [31:0] MAC_result106;
	wire [31:0] MAC_result107;
	wire [31:0] MAC_result108;
	wire [31:0] MAC_result109;
	wire [31:0] MAC_result110;
	wire [31:0] MAC_result111;
	wire [31:0] MAC_result112;
	wire [31:0] MAC_result113;
	wire [31:0] MAC_result114;
	wire [31:0] MAC_result115;
	wire [31:0] MAC_result116;
	wire [31:0] MAC_result117;
	wire [31:0] MAC_result118;
	wire [31:0] MAC_result119;
	wire [31:0] MAC_result120;
	wire [31:0] MAC_result121;
	wire [31:0] MAC_result122;
	wire [31:0] MAC_result123;
	wire [31:0] MAC_result124;
	wire [31:0] MAC_result125;
	wire [31:0] MAC_result126;
	wire [31:0] MAC_result127;
	wire [31:0] MAC_result128;
	wire [31:0] MAC_result129;
	wire [31:0] MAC_result130;
	wire [31:0] MAC_result131;
	wire [31:0] MAC_result132;
	wire [31:0] MAC_result133;
	wire [31:0] MAC_result134;
	wire [31:0] MAC_result135;
	wire [31:0] MAC_result136;
	wire [31:0] MAC_result137;
	wire [31:0] MAC_result138;
	wire [31:0] MAC_result139;
	wire [31:0] MAC_result140;
	wire [31:0] MAC_result141;
	wire [31:0] MAC_result142;
	wire [31:0] MAC_result143;
	wire [31:0] MAC_result144;
	wire [31:0] MAC_result145;
	wire [31:0] MAC_result146;
	wire [31:0] MAC_result147;
	wire [31:0] MAC_result148;
	wire [31:0] MAC_result149;
	wire [31:0] MAC_result150;
	wire [31:0] MAC_result151;
	wire [31:0] MAC_result152;
	wire [31:0] MAC_result153;
	wire [31:0] MAC_result154;
	wire [31:0] MAC_result155;
	wire [31:0] MAC_result156;
	wire [31:0] MAC_result157;
	wire [31:0] MAC_result158;
	wire [31:0] MAC_result159;
	wire [31:0] MAC_result160;
	wire [31:0] MAC_result161;
	wire [31:0] MAC_result162;
	wire [31:0] MAC_result163;
	wire [31:0] MAC_result164;
	wire [31:0] MAC_result165;
	wire [31:0] MAC_result166;
	wire [31:0] MAC_result167;
	wire [31:0] MAC_result168;
	wire [31:0] MAC_result169;
	wire [31:0] MAC_result170;
	wire [31:0] MAC_result171;
	wire [31:0] MAC_result172;
	wire [31:0] MAC_result173;
	wire [31:0] MAC_result174;
	wire [31:0] MAC_result175;
	wire [31:0] MAC_result176;
	wire [31:0] MAC_result177;
	wire [31:0] MAC_result178;
	wire [31:0] MAC_result179;
	wire [31:0] MAC_result180;
	wire [31:0] MAC_result181;
	wire [31:0] MAC_result182;
	wire [31:0] MAC_result183;
	wire [31:0] MAC_result184;
	wire [31:0] MAC_result185;
	wire [31:0] MAC_result186;
	wire [31:0] MAC_result187;
	wire [31:0] MAC_result188;
	wire [31:0] MAC_result189;
	wire [31:0] MAC_result190;
	wire [31:0] MAC_result191;
	wire [31:0] MAC_result192;
	wire [31:0] MAC_result193;
	wire [31:0] MAC_result194;
	wire [31:0] MAC_result195;
	wire [31:0] MAC_result196;
	wire [31:0] MAC_result197;
	wire [31:0] MAC_result198;
	wire [31:0] MAC_result199;
	wire [31:0] MAC_result200;
	wire [31:0] MAC_result201;
	wire [31:0] MAC_result202;
	wire [31:0] MAC_result203;
	wire [31:0] MAC_result204;
	wire [31:0] MAC_result205;
	wire [31:0] MAC_result206;
	wire [31:0] MAC_result207;
	wire [31:0] MAC_result208;
	wire [31:0] MAC_result209;
	wire [31:0] MAC_result210;
	wire [31:0] MAC_result211;
	wire [31:0] MAC_result212;
	wire [31:0] MAC_result213;
	wire [31:0] MAC_result214;
	wire [31:0] MAC_result215;
	wire [31:0] MAC_result216;
	wire [31:0] MAC_result217;
	wire [31:0] MAC_result218;
	wire [31:0] MAC_result219;
	wire [31:0] MAC_result220;
	wire [31:0] MAC_result221;
	wire [31:0] MAC_result222;
	wire [31:0] MAC_result223;
	wire [31:0] MAC_result224;
	wire [31:0] MAC_result225;
	wire [31:0] MAC_result226;
	wire [31:0] MAC_result227;
	wire [31:0] MAC_result228;
	wire [31:0] MAC_result229;
	wire [31:0] MAC_result230;
	wire [31:0] MAC_result231;
	wire [31:0] MAC_result232;
	wire [31:0] MAC_result233;
	wire [31:0] MAC_result234;
	wire [31:0] MAC_result235;
	wire [31:0] MAC_result236;
	wire [31:0] MAC_result237;
	wire [31:0] MAC_result238;
	wire [31:0] MAC_result239;
	wire [31:0] MAC_result240;
	wire [31:0] MAC_result241;
	wire [31:0] MAC_result242;
	wire [31:0] MAC_result243;
	wire [31:0] MAC_result244;
	wire [31:0] MAC_result245;
	wire [31:0] MAC_result246;
	wire [31:0] MAC_result247;
	wire [31:0] MAC_result248;
	wire [31:0] MAC_result249;
	wire [31:0] MAC_result250;
	wire [31:0] MAC_result251;
	wire [31:0] MAC_result252;
	wire [31:0] MAC_result253;
	wire [31:0] MAC_result254;
	wire [31:0] MAC_result255;
//

	
	pim_controller controller(
		.CLK						(CLK), 
		.RSTN						(RSTN),

		.i_address_bus				(i_address),
		.i_data_bus					(i_data),

		.i_pim_result_out_en		(CAM_result_out_en),

		.i_result_buffer_out		(result_buffer_out),

		.o_weight_in_en				(weight_buffer_in_en),	
		.o_weight_out_en			(weight_buffer_out_en),
		.o_cam_weight_in_data		(cam_weight_in_data),
		.o_mac_weight_in_data		(mac_weight_in_data),

		.o_WL_address				(WL_address),

		.o_activation_in_en			(activation_buffer_in_en),
		.o_activation_out_en		(activation_buffer_out_en),
		.o_activation_in_data		(activation_in_data),

		.o_result_out_en			(result_buffer_out_en),

		.o_data_bus					(o_data),

		.o_counter					(counter)
	);

	//weight 
	BL_driver BLD_CAM (
		.CLK						(CLK),
		.RSTN						(RSTN),
		.i_weight_in_en				(weight_buffer_in_en),			
		.i_weight_out_en			(weight_buffer_out_en),
		.i_counter					(counter[3:0]),
		.i_data						(cam_weight_in_data),
		.o_weight_out_en			(cam_bl_out_en),
		.o_data						(CAM_BL)
	);

	BL_driver BLD_MAC (
		.CLK						(CLK),
		.RSTN						(RSTN),
		.i_weight_in_en				(weight_buffer_in_en),			
		.i_weight_out_en			(weight_buffer_out_en),
		.i_counter					(counter[3:0]),
		.i_data						(mac_weight_in_data),
		.o_weight_out_en			(mac_bl_out_en),
		.o_data						(MAC_BL)
	);

	
	WL_driver WLD_CAM (
		.i_pim_weight_in_en			(cam_bl_out_en),
		.i_WL_address				(WL_address),
		.o_WL						(CAM_WL)
	);

	WL_driver WLD_MAC (
		.i_pim_weight_in_en			(mac_bl_out_en),
		.i_WL_address				(WL_address),
		.o_WL						(MAC_WL)
	);

	//activation	
	activation_buffer AB_CAM (
		.CLK						(CLK),
		.RSTN						(RSTN),
		.i_activation_in_en			(activation_buffer_in_en),		
		.i_activation_out_en		(activation_buffer_out_en),
		.i_counter					(counter),
		.i_data						(activation_in_data),
		.o_activation_out_en		(CAM_activation_in_en),
		.o_data						(CAM_activation_data)
	);

	//activation	
	activation_buffer AB_MAC (
		.CLK						(CLK),
		.RSTN						(RSTN),
		.i_activation_in_en			(activation_buffer_in_en),		
		.i_activation_out_en		(activation_buffer_out_en),
		.i_counter					(counter),
		.i_data						(activation_in_data),
		.o_activation_out_en		(MAC_activation_in_en),
		.o_data						(MAC_activation_data)
	);
	
	//pim
	pim CAM (
		.CLK						(CLK),
		.RSTN						(RSTN),
		.i_BL						(CAM_BL),
		.i_WL						(CAM_WL),
		.i_activation_data			(CAM_activation_data),
		.i_activation_in_en			(CAM_activation_in_en),
		.o_result_out_en			(CAM_result_out_en),
		.o_result0					(CAM_result0),
		.o_result1					(CAM_result1),
		.o_result2					(CAM_result2),
		.o_result3					(CAM_result3),
		.o_result4					(CAM_result4),
		.o_result5					(CAM_result5),
		.o_result6					(CAM_result6),
		.o_result7					(CAM_result7),
		.o_result8					(CAM_result8),
		.o_result9					(CAM_result9),
		.o_result10					(CAM_result10),
		.o_result11					(CAM_result11),
		.o_result12					(CAM_result12),
		.o_result13					(CAM_result13),
		.o_result14					(CAM_result14),
		.o_result15					(CAM_result15),
		.o_result16					(CAM_result16),
		.o_result17					(CAM_result17),
		.o_result18					(CAM_result18),
		.o_result19					(CAM_result19),
		.o_result20					(CAM_result20),
		.o_result21					(CAM_result21),
		.o_result22					(CAM_result22),
		.o_result23					(CAM_result23),
		.o_result24					(CAM_result24),
		.o_result25					(CAM_result25),
		.o_result26					(CAM_result26),
		.o_result27					(CAM_result27),
		.o_result28					(CAM_result28),
		.o_result29					(CAM_result29),
		.o_result30					(CAM_result30),
		.o_result31					(CAM_result31),
		.o_result32					(CAM_result32),
		.o_result33					(CAM_result33),
		.o_result34					(CAM_result34),
		.o_result35					(CAM_result35),
		.o_result36					(CAM_result36),
		.o_result37					(CAM_result37),
		.o_result38					(CAM_result38),
		.o_result39					(CAM_result39),
		.o_result40					(CAM_result40),
		.o_result41					(CAM_result41),
		.o_result42					(CAM_result42),
		.o_result43					(CAM_result43),
		.o_result44					(CAM_result44),
		.o_result45					(CAM_result45),
		.o_result46					(CAM_result46),
		.o_result47					(CAM_result47),
		.o_result48					(CAM_result48),
		.o_result49					(CAM_result49),
		.o_result50					(CAM_result50),
		.o_result51					(CAM_result51),
		.o_result52					(CAM_result52),
		.o_result53					(CAM_result53),
		.o_result54					(CAM_result54),
		.o_result55					(CAM_result55),
		.o_result56					(CAM_result56),
		.o_result57					(CAM_result57),
		.o_result58					(CAM_result58),
		.o_result59					(CAM_result59),
		.o_result60					(CAM_result60),
		.o_result61					(CAM_result61),
		.o_result62					(CAM_result62),
		.o_result63					(CAM_result63),
		.o_result64					(CAM_result64),
		.o_result65					(CAM_result65),
		.o_result66					(CAM_result66),
		.o_result67					(CAM_result67),
		.o_result68					(CAM_result68),
		.o_result69					(CAM_result69),
		.o_result70					(CAM_result70),
		.o_result71					(CAM_result71),
		.o_result72					(CAM_result72),
		.o_result73					(CAM_result73),
		.o_result74					(CAM_result74),
		.o_result75					(CAM_result75),
		.o_result76					(CAM_result76),
		.o_result77					(CAM_result77),
		.o_result78					(CAM_result78),
		.o_result79					(CAM_result79),
		.o_result80					(CAM_result80),
		.o_result81					(CAM_result81),
		.o_result82					(CAM_result82),
		.o_result83					(CAM_result83),
		.o_result84					(CAM_result84),
		.o_result85					(CAM_result85),
		.o_result86					(CAM_result86),
		.o_result87					(CAM_result87),
		.o_result88					(CAM_result88),
		.o_result89					(CAM_result89),
		.o_result90					(CAM_result90),
		.o_result91					(CAM_result91),
		.o_result92					(CAM_result92),
		.o_result93					(CAM_result93),
		.o_result94					(CAM_result94),
		.o_result95					(CAM_result95),
		.o_result96					(CAM_result96),
		.o_result97					(CAM_result97),
		.o_result98					(CAM_result98),
		.o_result99					(CAM_result99),
		.o_result100				(CAM_result100),
		.o_result101				(CAM_result101),
		.o_result102				(CAM_result102),
		.o_result103				(CAM_result103),
		.o_result104				(CAM_result104),
		.o_result105				(CAM_result105),
		.o_result106				(CAM_result106),
		.o_result107				(CAM_result107),
		.o_result108				(CAM_result108),
		.o_result109				(CAM_result109),
		.o_result110				(CAM_result110),
		.o_result111				(CAM_result111),
		.o_result112				(CAM_result112),
		.o_result113				(CAM_result113),
		.o_result114				(CAM_result114),
		.o_result115				(CAM_result115),
		.o_result116				(CAM_result116),
		.o_result117				(CAM_result117),
		.o_result118				(CAM_result118),
		.o_result119				(CAM_result119),
		.o_result120				(CAM_result120),
		.o_result121				(CAM_result121),
		.o_result122				(CAM_result122),
		.o_result123				(CAM_result123),
		.o_result124				(CAM_result124),
		.o_result125				(CAM_result125),
		.o_result126				(CAM_result126),
		.o_result127				(CAM_result127),
		.o_result128				(CAM_result128),
		.o_result129				(CAM_result129),
		.o_result130				(CAM_result130),
		.o_result131				(CAM_result131),
		.o_result132				(CAM_result132),
		.o_result133				(CAM_result133),
		.o_result134				(CAM_result134),
		.o_result135				(CAM_result135),
		.o_result136				(CAM_result136),
		.o_result137				(CAM_result137),
		.o_result138				(CAM_result138),
		.o_result139				(CAM_result139),
		.o_result140				(CAM_result140),
		.o_result141				(CAM_result141),
		.o_result142				(CAM_result142),
		.o_result143				(CAM_result143),
		.o_result144				(CAM_result144),
		.o_result145				(CAM_result145),
		.o_result146				(CAM_result146),
		.o_result147				(CAM_result147),
		.o_result148				(CAM_result148),
		.o_result149				(CAM_result149),
		.o_result150				(CAM_result150),
		.o_result151				(CAM_result151),
		.o_result152				(CAM_result152),
		.o_result153				(CAM_result153),
		.o_result154				(CAM_result154),
		.o_result155				(CAM_result155),
		.o_result156				(CAM_result156),
		.o_result157				(CAM_result157),
		.o_result158				(CAM_result158),
		.o_result159				(CAM_result159),
		.o_result160				(CAM_result160),
		.o_result161				(CAM_result161),
		.o_result162				(CAM_result162),
		.o_result163				(CAM_result163),
		.o_result164				(CAM_result164),
		.o_result165				(CAM_result165),
		.o_result166				(CAM_result166),
		.o_result167				(CAM_result167),
		.o_result168				(CAM_result168),
		.o_result169				(CAM_result169),
		.o_result170				(CAM_result170),
		.o_result171				(CAM_result171),
		.o_result172				(CAM_result172),
		.o_result173				(CAM_result173),
		.o_result174				(CAM_result174),
		.o_result175				(CAM_result175),
		.o_result176				(CAM_result176),
		.o_result177				(CAM_result177),
		.o_result178				(CAM_result178),
		.o_result179				(CAM_result179),
		.o_result180				(CAM_result180),
		.o_result181				(CAM_result181),
		.o_result182				(CAM_result182),
		.o_result183				(CAM_result183),
		.o_result184				(CAM_result184),
		.o_result185				(CAM_result185),
		.o_result186				(CAM_result186),
		.o_result187				(CAM_result187),
		.o_result188				(CAM_result188),
		.o_result189				(CAM_result189),
		.o_result190				(CAM_result190),
		.o_result191				(CAM_result191),
		.o_result192				(CAM_result192),
		.o_result193				(CAM_result193),
		.o_result194				(CAM_result194),
		.o_result195				(CAM_result195),
		.o_result196				(CAM_result196),
		.o_result197				(CAM_result197),
		.o_result198				(CAM_result198),
		.o_result199				(CAM_result199),
		.o_result200				(CAM_result200),
		.o_result201				(CAM_result201),
		.o_result202				(CAM_result202),
		.o_result203				(CAM_result203),
		.o_result204				(CAM_result204),
		.o_result205				(CAM_result205),
		.o_result206				(CAM_result206),
		.o_result207				(CAM_result207),
		.o_result208				(CAM_result208),
		.o_result209				(CAM_result209),
		.o_result210				(CAM_result210),
		.o_result211				(CAM_result211),
		.o_result212				(CAM_result212),
		.o_result213				(CAM_result213),
		.o_result214				(CAM_result214),
		.o_result215				(CAM_result215),
		.o_result216				(CAM_result216),
		.o_result217				(CAM_result217),
		.o_result218				(CAM_result218),
		.o_result219				(CAM_result219),
		.o_result220				(CAM_result220),
		.o_result221				(CAM_result221),
		.o_result222				(CAM_result222),
		.o_result223				(CAM_result223),
		.o_result224				(CAM_result224),
		.o_result225				(CAM_result225),
		.o_result226				(CAM_result226),
		.o_result227				(CAM_result227),
		.o_result228				(CAM_result228),
		.o_result229				(CAM_result229),
		.o_result230				(CAM_result230),
		.o_result231				(CAM_result231),
		.o_result232				(CAM_result232),
		.o_result233				(CAM_result233),
		.o_result234				(CAM_result234),
		.o_result235				(CAM_result235),
		.o_result236				(CAM_result236),
		.o_result237				(CAM_result237),
		.o_result238				(CAM_result238),
		.o_result239				(CAM_result239),
		.o_result240				(CAM_result240),
		.o_result241				(CAM_result241),
		.o_result242				(CAM_result242),
		.o_result243				(CAM_result243),
		.o_result244				(CAM_result244),
		.o_result245				(CAM_result245),
		.o_result246				(CAM_result246),
		.o_result247				(CAM_result247),
		.o_result248				(CAM_result248),
		.o_result249				(CAM_result249),
		.o_result250				(CAM_result250),
		.o_result251				(CAM_result251),
		.o_result252				(CAM_result252),
		.o_result253				(CAM_result253),
		.o_result254				(CAM_result254),
		.o_result255				(CAM_result255)
	);

	pim MAC (
		.CLK						(CLK),
		.RSTN						(RSTN),
		.i_BL						(MAC_BL),
		.i_WL						(MAC_WL),
		.i_activation_data			(MAC_activation_data),
		.i_activation_in_en			(MAC_activation_in_en),
		.o_result_out_en			(MAC_result_out_en),
		.o_result0					(MAC_result0),
		.o_result1					(MAC_result1),
		.o_result2					(MAC_result2),
		.o_result3					(MAC_result3),
		.o_result4					(MAC_result4),
		.o_result5					(MAC_result5),
		.o_result6					(MAC_result6),
		.o_result7					(MAC_result7),
		.o_result8					(MAC_result8),
		.o_result9					(MAC_result9),
		.o_result10					(MAC_result10),
		.o_result11					(MAC_result11),
		.o_result12					(MAC_result12),
		.o_result13					(MAC_result13),
		.o_result14					(MAC_result14),
		.o_result15					(MAC_result15),
		.o_result16					(MAC_result16),
		.o_result17					(MAC_result17),
		.o_result18					(MAC_result18),
		.o_result19					(MAC_result19),
		.o_result20					(MAC_result20),
		.o_result21					(MAC_result21),
		.o_result22					(MAC_result22),
		.o_result23					(MAC_result23),
		.o_result24					(MAC_result24),
		.o_result25					(MAC_result25),
		.o_result26					(MAC_result26),
		.o_result27					(MAC_result27),
		.o_result28					(MAC_result28),
		.o_result29					(MAC_result29),
		.o_result30					(MAC_result30),
		.o_result31					(MAC_result31),
		.o_result32					(MAC_result32),
		.o_result33					(MAC_result33),
		.o_result34					(MAC_result34),
		.o_result35					(MAC_result35),
		.o_result36					(MAC_result36),
		.o_result37					(MAC_result37),
		.o_result38					(MAC_result38),
		.o_result39					(MAC_result39),
		.o_result40					(MAC_result40),
		.o_result41					(MAC_result41),
		.o_result42					(MAC_result42),
		.o_result43					(MAC_result43),
		.o_result44					(MAC_result44),
		.o_result45					(MAC_result45),
		.o_result46					(MAC_result46),
		.o_result47					(MAC_result47),
		.o_result48					(MAC_result48),
		.o_result49					(MAC_result49),
		.o_result50					(MAC_result50),
		.o_result51					(MAC_result51),
		.o_result52					(MAC_result52),
		.o_result53					(MAC_result53),
		.o_result54					(MAC_result54),
		.o_result55					(MAC_result55),
		.o_result56					(MAC_result56),
		.o_result57					(MAC_result57),
		.o_result58					(MAC_result58),
		.o_result59					(MAC_result59),
		.o_result60					(MAC_result60),
		.o_result61					(MAC_result61),
		.o_result62					(MAC_result62),
		.o_result63					(MAC_result63),
		.o_result64					(MAC_result64),
		.o_result65					(MAC_result65),
		.o_result66					(MAC_result66),
		.o_result67					(MAC_result67),
		.o_result68					(MAC_result68),
		.o_result69					(MAC_result69),
		.o_result70					(MAC_result70),
		.o_result71					(MAC_result71),
		.o_result72					(MAC_result72),
		.o_result73					(MAC_result73),
		.o_result74					(MAC_result74),
		.o_result75					(MAC_result75),
		.o_result76					(MAC_result76),
		.o_result77					(MAC_result77),
		.o_result78					(MAC_result78),
		.o_result79					(MAC_result79),
		.o_result80					(MAC_result80),
		.o_result81					(MAC_result81),
		.o_result82					(MAC_result82),
		.o_result83					(MAC_result83),
		.o_result84					(MAC_result84),
		.o_result85					(MAC_result85),
		.o_result86					(MAC_result86),
		.o_result87					(MAC_result87),
		.o_result88					(MAC_result88),
		.o_result89					(MAC_result89),
		.o_result90					(MAC_result90),
		.o_result91					(MAC_result91),
		.o_result92					(MAC_result92),
		.o_result93					(MAC_result93),
		.o_result94					(MAC_result94),
		.o_result95					(MAC_result95),
		.o_result96					(MAC_result96),
		.o_result97					(MAC_result97),
		.o_result98					(MAC_result98),
		.o_result99					(MAC_result99),
		.o_result100				(MAC_result100),
		.o_result101				(MAC_result101),
		.o_result102				(MAC_result102),
		.o_result103				(MAC_result103),
		.o_result104				(MAC_result104),
		.o_result105				(MAC_result105),
		.o_result106				(MAC_result106),
		.o_result107				(MAC_result107),
		.o_result108				(MAC_result108),
		.o_result109				(MAC_result109),
		.o_result110				(MAC_result110),
		.o_result111				(MAC_result111),
		.o_result112				(MAC_result112),
		.o_result113				(MAC_result113),
		.o_result114				(MAC_result114),
		.o_result115				(MAC_result115),
		.o_result116				(MAC_result116),
		.o_result117				(MAC_result117),
		.o_result118				(MAC_result118),
		.o_result119				(MAC_result119),
		.o_result120				(MAC_result120),
		.o_result121				(MAC_result121),
		.o_result122				(MAC_result122),
		.o_result123				(MAC_result123),
		.o_result124				(MAC_result124),
		.o_result125				(MAC_result125),
		.o_result126				(MAC_result126),
		.o_result127				(MAC_result127),
		.o_result128				(MAC_result128),
		.o_result129				(MAC_result129),
		.o_result130				(MAC_result130),
		.o_result131				(MAC_result131),
		.o_result132				(MAC_result132),
		.o_result133				(MAC_result133),
		.o_result134				(MAC_result134),
		.o_result135				(MAC_result135),
		.o_result136				(MAC_result136),
		.o_result137				(MAC_result137),
		.o_result138				(MAC_result138),
		.o_result139				(MAC_result139),
		.o_result140				(MAC_result140),
		.o_result141				(MAC_result141),
		.o_result142				(MAC_result142),
		.o_result143				(MAC_result143),
		.o_result144				(MAC_result144),
		.o_result145				(MAC_result145),
		.o_result146				(MAC_result146),
		.o_result147				(MAC_result147),
		.o_result148				(MAC_result148),
		.o_result149				(MAC_result149),
		.o_result150				(MAC_result150),
		.o_result151				(MAC_result151),
		.o_result152				(MAC_result152),
		.o_result153				(MAC_result153),
		.o_result154				(MAC_result154),
		.o_result155				(MAC_result155),
		.o_result156				(MAC_result156),
		.o_result157				(MAC_result157),
		.o_result158				(MAC_result158),
		.o_result159				(MAC_result159),
		.o_result160				(MAC_result160),
		.o_result161				(MAC_result161),
		.o_result162				(MAC_result162),
		.o_result163				(MAC_result163),
		.o_result164				(MAC_result164),
		.o_result165				(MAC_result165),
		.o_result166				(MAC_result166),
		.o_result167				(MAC_result167),
		.o_result168				(MAC_result168),
		.o_result169				(MAC_result169),
		.o_result170				(MAC_result170),
		.o_result171				(MAC_result171),
		.o_result172				(MAC_result172),
		.o_result173				(MAC_result173),
		.o_result174				(MAC_result174),
		.o_result175				(MAC_result175),
		.o_result176				(MAC_result176),
		.o_result177				(MAC_result177),
		.o_result178				(MAC_result178),
		.o_result179				(MAC_result179),
		.o_result180				(MAC_result180),
		.o_result181				(MAC_result181),
		.o_result182				(MAC_result182),
		.o_result183				(MAC_result183),
		.o_result184				(MAC_result184),
		.o_result185				(MAC_result185),
		.o_result186				(MAC_result186),
		.o_result187				(MAC_result187),
		.o_result188				(MAC_result188),
		.o_result189				(MAC_result189),
		.o_result190				(MAC_result190),
		.o_result191				(MAC_result191),
		.o_result192				(MAC_result192),
		.o_result193				(MAC_result193),
		.o_result194				(MAC_result194),
		.o_result195				(MAC_result195),
		.o_result196				(MAC_result196),
		.o_result197				(MAC_result197),
		.o_result198				(MAC_result198),
		.o_result199				(MAC_result199),
		.o_result200				(MAC_result200),
		.o_result201				(MAC_result201),
		.o_result202				(MAC_result202),
		.o_result203				(MAC_result203),
		.o_result204				(MAC_result204),
		.o_result205				(MAC_result205),
		.o_result206				(MAC_result206),
		.o_result207				(MAC_result207),
		.o_result208				(MAC_result208),
		.o_result209				(MAC_result209),
		.o_result210				(MAC_result210),
		.o_result211				(MAC_result211),
		.o_result212				(MAC_result212),
		.o_result213				(MAC_result213),
		.o_result214				(MAC_result214),
		.o_result215				(MAC_result215),
		.o_result216				(MAC_result216),
		.o_result217				(MAC_result217),
		.o_result218				(MAC_result218),
		.o_result219				(MAC_result219),
		.o_result220				(MAC_result220),
		.o_result221				(MAC_result221),
		.o_result222				(MAC_result222),
		.o_result223				(MAC_result223),
		.o_result224				(MAC_result224),
		.o_result225				(MAC_result225),
		.o_result226				(MAC_result226),
		.o_result227				(MAC_result227),
		.o_result228				(MAC_result228),
		.o_result229				(MAC_result229),
		.o_result230				(MAC_result230),
		.o_result231				(MAC_result231),
		.o_result232				(MAC_result232),
		.o_result233				(MAC_result233),
		.o_result234				(MAC_result234),
		.o_result235				(MAC_result235),
		.o_result236				(MAC_result236),
		.o_result237				(MAC_result237),
		.o_result238				(MAC_result238),
		.o_result239				(MAC_result239),
		.o_result240				(MAC_result240),
		.o_result241				(MAC_result241),
		.o_result242				(MAC_result242),
		.o_result243				(MAC_result243),
		.o_result244				(MAC_result244),
		.o_result245				(MAC_result245),
		.o_result246				(MAC_result246),
		.o_result247				(MAC_result247),
		.o_result248				(MAC_result248),
		.o_result249				(MAC_result249),
		.o_result250				(MAC_result250),
		.o_result251				(MAC_result251),
		.o_result252				(MAC_result252),
		.o_result253				(MAC_result253),
		.o_result254				(MAC_result254),
		.o_result255				(MAC_result255)
	);

	//result
	result_buffer RB(
		.CLK						(CLK),
		.RSTN						(RSTN),
		.i_result_in_en				(CAM_result_out_en),
		.i_result_out_en			(result_buffer_out_en),
		.i_counter					(counter),
		.i_data0					(CAM_result0),
		.i_data1					(CAM_result1),
		.i_data2					(CAM_result2),
		.i_data3					(CAM_result3),
		.i_data4					(CAM_result4),
		.i_data5					(CAM_result5),
		.i_data6					(CAM_result6),
		.i_data7					(CAM_result7),
		.i_data8					(CAM_result8),
		.i_data9					(CAM_result9),
		.i_data10					(CAM_result10),
		.i_data11					(CAM_result11),
		.i_data12					(CAM_result12),
		.i_data13					(CAM_result13),
		.i_data14					(CAM_result14),
		.i_data15					(CAM_result15),
		.i_data16					(CAM_result16),
		.i_data17					(CAM_result17),
		.i_data18					(CAM_result18),
		.i_data19					(CAM_result19),
		.i_data20					(CAM_result20),
		.i_data21					(CAM_result21),
		.i_data22					(CAM_result22),
		.i_data23					(CAM_result23),
		.i_data24					(CAM_result24),
		.i_data25					(CAM_result25),
		.i_data26					(CAM_result26),
		.i_data27					(CAM_result27),
		.i_data28					(CAM_result28),
		.i_data29					(CAM_result29),
		.i_data30					(CAM_result30),
		.i_data31					(CAM_result31),
		.i_data32					(CAM_result32),
		.i_data33					(CAM_result33),
		.i_data34					(CAM_result34),
		.i_data35					(CAM_result35),
		.i_data36					(CAM_result36),
		.i_data37					(CAM_result37),
		.i_data38					(CAM_result38),
		.i_data39					(CAM_result39),
		.i_data40					(CAM_result40),
		.i_data41					(CAM_result41),
		.i_data42					(CAM_result42),
		.i_data43					(CAM_result43),
		.i_data44					(CAM_result44),
		.i_data45					(CAM_result45),
		.i_data46					(CAM_result46),
		.i_data47					(CAM_result47),
		.i_data48					(CAM_result48),
		.i_data49					(CAM_result49),
		.i_data50					(CAM_result50),
		.i_data51					(CAM_result51),
		.i_data52					(CAM_result52),
		.i_data53					(CAM_result53),
		.i_data54					(CAM_result54),
		.i_data55					(CAM_result55),
		.i_data56					(CAM_result56),
		.i_data57					(CAM_result57),
		.i_data58					(CAM_result58),
		.i_data59					(CAM_result59),
		.i_data60					(CAM_result60),
		.i_data61					(CAM_result61),
		.i_data62					(CAM_result62),
		.i_data63					(CAM_result63),
		.i_data64					(CAM_result64),
		.i_data65					(CAM_result65),
		.i_data66					(CAM_result66),
		.i_data67					(CAM_result67),
		.i_data68					(CAM_result68),
		.i_data69					(CAM_result69),
		.i_data70					(CAM_result70),
		.i_data71					(CAM_result71),
		.i_data72					(CAM_result72),
		.i_data73					(CAM_result73),
		.i_data74					(CAM_result74),
		.i_data75					(CAM_result75),
		.i_data76					(CAM_result76),
		.i_data77					(CAM_result77),
		.i_data78					(CAM_result78),
		.i_data79					(CAM_result79),
		.i_data80					(CAM_result80),
		.i_data81					(CAM_result81),
		.i_data82					(CAM_result82),
		.i_data83					(CAM_result83),
		.i_data84					(CAM_result84),
		.i_data85					(CAM_result85),
		.i_data86					(CAM_result86),
		.i_data87					(CAM_result87),
		.i_data88					(CAM_result88),
		.i_data89					(CAM_result89),
		.i_data90					(CAM_result90),
		.i_data91					(CAM_result91),
		.i_data92					(CAM_result92),
		.i_data93					(CAM_result93),
		.i_data94					(CAM_result94),
		.i_data95					(CAM_result95),
		.i_data96					(CAM_result96),
		.i_data97					(CAM_result97),
		.i_data98					(CAM_result98),
		.i_data99					(CAM_result99),
		.i_data100					(CAM_result100),		
		.i_data101					(CAM_result101),
		.i_data102					(CAM_result102),
		.i_data103					(CAM_result103),
		.i_data104					(CAM_result104),
		.i_data105					(CAM_result105),
		.i_data106					(CAM_result106),
		.i_data107					(CAM_result107),
		.i_data108					(CAM_result108),
		.i_data109					(CAM_result109),
		.i_data110					(CAM_result110),
		.i_data111					(CAM_result111),
		.i_data112					(CAM_result112),
		.i_data113					(CAM_result113),
		.i_data114					(CAM_result114),
		.i_data115					(CAM_result115),
		.i_data116					(CAM_result116),
		.i_data117					(CAM_result117),
		.i_data118					(CAM_result118),
		.i_data119					(CAM_result119),
		.i_data120					(CAM_result120),
		.i_data121					(CAM_result121),
		.i_data122					(CAM_result122),
		.i_data123					(CAM_result123),
		.i_data124					(CAM_result124),
		.i_data125					(CAM_result125),
		.i_data126					(CAM_result126),
		.i_data127					(CAM_result127),
		.i_data128					(CAM_result128),
		.i_data129					(CAM_result129),
		.i_data130					(CAM_result130),
		.i_data131					(CAM_result131),
		.i_data132					(CAM_result132),
		.i_data133					(CAM_result133),
		.i_data134					(CAM_result134),
		.i_data135					(CAM_result135),
		.i_data136					(CAM_result136),
		.i_data137					(CAM_result137),
		.i_data138					(CAM_result138),
		.i_data139					(CAM_result139),
		.i_data140					(CAM_result140),
		.i_data141					(CAM_result141),
		.i_data142					(CAM_result142),
		.i_data143					(CAM_result143),
		.i_data144					(CAM_result144),
		.i_data145					(CAM_result145),
		.i_data146					(CAM_result146),
		.i_data147					(CAM_result147),
		.i_data148					(CAM_result148),
		.i_data149					(CAM_result149),
		.i_data150					(CAM_result150),
		.i_data151					(CAM_result151),
		.i_data152					(CAM_result152),
		.i_data153					(CAM_result153),
		.i_data154					(CAM_result154),
		.i_data155					(CAM_result155),
		.i_data156					(CAM_result156),
		.i_data157					(CAM_result157),
		.i_data158					(CAM_result158),
		.i_data159					(CAM_result159),
		.i_data160					(CAM_result160),
		.i_data161					(CAM_result161),
		.i_data162					(CAM_result162),
		.i_data163					(CAM_result163),
		.i_data164					(CAM_result164),
		.i_data165					(CAM_result165),
		.i_data166					(CAM_result166),
		.i_data167					(CAM_result167),
		.i_data168					(CAM_result168),
		.i_data169					(CAM_result169),
		.i_data170					(CAM_result170),
		.i_data171					(CAM_result171),
		.i_data172					(CAM_result172),
		.i_data173					(CAM_result173),
		.i_data174					(CAM_result174),
		.i_data175					(CAM_result175),
		.i_data176					(CAM_result176),
		.i_data177					(CAM_result177),
		.i_data178					(CAM_result178),
		.i_data179					(CAM_result179),
		.i_data180					(CAM_result180),
		.i_data181					(CAM_result181),
		.i_data182					(CAM_result182),
		.i_data183					(CAM_result183),
		.i_data184					(CAM_result184),
		.i_data185					(CAM_result185),
		.i_data186					(CAM_result186),
		.i_data187					(CAM_result187),
		.i_data188					(CAM_result188),
		.i_data189					(CAM_result189),
		.i_data190					(CAM_result190),
		.i_data191					(CAM_result191),
		.i_data192					(CAM_result192),
		.i_data193					(CAM_result193),
		.i_data194					(CAM_result194),
		.i_data195					(CAM_result195),
		.i_data196					(CAM_result196),
		.i_data197					(CAM_result197),
		.i_data198					(CAM_result198),
		.i_data199					(CAM_result199),
		.i_data200					(CAM_result200),
		.i_data201					(CAM_result201),
		.i_data202					(CAM_result202),
		.i_data203					(CAM_result203),
		.i_data204					(CAM_result204),
		.i_data205					(CAM_result205),
		.i_data206					(CAM_result206),
		.i_data207					(CAM_result207),
		.i_data208					(CAM_result208),
		.i_data209					(CAM_result209),
		.i_data210					(CAM_result210),
		.i_data211					(CAM_result211),
		.i_data212					(CAM_result212),
		.i_data213					(CAM_result213),
		.i_data214					(CAM_result214),
		.i_data215					(CAM_result215),
		.i_data216					(CAM_result216),
		.i_data217					(CAM_result217),
		.i_data218					(CAM_result218),
		.i_data219					(CAM_result219),
		.i_data220					(CAM_result220),
		.i_data221					(CAM_result221),
		.i_data222					(CAM_result222),
		.i_data223					(CAM_result223),
		.i_data224					(CAM_result224),
		.i_data225					(CAM_result225),
		.i_data226					(CAM_result226),
		.i_data227					(CAM_result227),
		.i_data228					(CAM_result228),
		.i_data229					(CAM_result229),
		.i_data230					(CAM_result230),
		.i_data231					(CAM_result231),
		.i_data232					(CAM_result232),
		.i_data233					(CAM_result233),
		.i_data234					(CAM_result234),
		.i_data235					(CAM_result235),
		.i_data236					(CAM_result236),
		.i_data237					(CAM_result237),
		.i_data238					(CAM_result238),
		.i_data239					(CAM_result239),
		.i_data240					(CAM_result240),
		.i_data241					(CAM_result241),
		.i_data242					(CAM_result242),
		.i_data243					(CAM_result243),
		.i_data244					(CAM_result244),
		.i_data245					(CAM_result245),
		.i_data246					(CAM_result246),
		.i_data247					(CAM_result247),
		.i_data248					(CAM_result248),
		.i_data249					(CAM_result249),
		.i_data250					(CAM_result250),
		.i_data251					(CAM_result251),
		.i_data252					(CAM_result252),
		.i_data253					(CAM_result253),
		.i_data254					(CAM_result254),
		.i_data255					(CAM_result255),
		.o_data						(result_buffer_out)
	);

	
endmodule


