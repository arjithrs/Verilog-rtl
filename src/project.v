/*
 * Copyright (c) 2024 Your Name
 * SPDX-License-Identifier: Apache-2.0
 */

`default_nettype none

module tt_fulladder (
    input  wire [7:0] ui_in,    // Dedicated inputs
    output wire [7:0] uo_out,   // Dedicated outputs
    input  wire [7:0] uio_in,   // IOs: Input path
    output wire [7:0] uio_out,  // IOs: Output path
    output wire [7:0] uio_oe,   // IOs: Enable path (active high: 0=input, 1=output)
    input  wire       ena,      // always 1 when design is powered
    input  wire       clk,      // clock
    input  wire       rst_n     // reset_n - low to reset
);

    // Input pin assignments
    wire a   = ui_in[0];
    wire b   = ui_in[1];
    wire cin = ui_in[2];

    // Full Adder Boolean Logic
    wire sum  = a ^ b ^ cin;
    wire cout = (a & b) | (b & cin) | (a & cin);

    // Output pin assignments
    assign uo_out[0]   = sum;
    assign uo_out[1]   = cout;
    assign uo_out[7:2] = 6'b0; // Set unused output pins to zero

    // Bidirectional IOs disabled
    assign uio_out = 8'b0;
    assign uio_oe  = 8'b0;

    // Suppress warnings for unused inputs
    wire _unused = &{ena, clk, rst_n, ui_in[7:3], uio_in, 1'b0};

endmodule
