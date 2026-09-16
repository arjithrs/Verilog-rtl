/*
 * Copyright (c) 2024 Your Name
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_um_full_adder (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path
    input  wire       ena,      // active high enable
    input  wire       clk,      // clock
    input  wire       rst_n     // active low reset
);

    wire a   = ui_in[0];
    wire b   = ui_in[1];
    wire cin = ui_in[2];

    wire sum  = a ^ b ^ cin;
    wire cout = (a & b) | (b & cin) | (a & cin);

    assign uo_out[0]   = sum;
    assign uo_out[1]   = cout;
    assign uo_out[7:2] = 6'b0;

    assign uio_out = 8'b0;
    assign uio_oe  = 8'b0;

    wire _unused = &{ena, clk, rst_n, ui_in[7:3], uio_in, 1'b0};

endmodule
