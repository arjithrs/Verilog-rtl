`timescale 1ns / 1ps

module tb_tt_fulladder;

    // Inputs to DUT (reg)
    reg  [7:0] ui_in;
    reg  [7:0] uio_in;
    reg        ena;
    reg        clk;
    reg        rst_n;

    // Outputs from DUT (wire)
    wire [7:0] uo_out;
    wire [7:0] uio_out;
    wire [7:0] uio_oe;

    // Instantiate Design Under Test (DUT)
    tt_fulladder dut (
        .ui_in  (ui_in),
        .uo_out (uo_out),
        .uio_in (uio_in),
        .uio_out(uio_out),
        .uio_oe (uio_oe),
        .ena    (ena),
        .clk    (clk),
        .rst_n  (rst_n)
    );

    // 100 kHz Clock Generation (10 us period)
    always #5000 clk = ~clk;

    // Test stimulus variables
    integer i;
    reg a, b, cin;
    reg expected_sum, expected_cout;

    initial begin
        // Waveform dump for GTKWave / EDA Playground
        $dumpfile("tb.vcd");
        $dumpvars(0, tb_tt_fulladder);

        // Initialize signals
        clk   = 0;
        rst_n = 0;
        ena   = 1;
        ui_in = 0;
        uio_in = 0;

        // Apply reset sequence
        #20000;
        rst_n = 1;
        #10000;

        $display("----------------------------------------------");
        $display("    FULL ADDER VERILOG TESTBENCH SIMULATION   ");
        $display("----------------------------------------------");

        // Iterate through all 8 truth table combinations
        for (i = 0; i < 8; i = i + 1) begin
            a   = i[0];
            b   = i[1];
            cin = i[2];

            // Drive inputs to ui_in[0]=A, ui_in[1]=B, ui_in[2]=Cin
            ui_in = {5'b00000, cin, b, a};

            #10000; // Wait 1 clock cycle

            // Calculate golden model outputs
            expected_sum  = a ^ b ^ cin;
            expected_cout = (a & b) | (b & cin) | (a & cin);

            // Self-checking assertion
            if ((uo_out[0] === expected_sum) && (uo_out[1] === expected_cout)) begin
                $display("[PASS] A=%b B=%b Cin=%b | Sum=%b Cout=%b (uo_out=%b)", 
                         a, b, cin, uo_out[0], uo_out[1], uo_out[1:0]);
            end else begin
                $display("[FAIL] A=%b B=%b Cin=%b | Expected: Sum=%b Cout=%b | Got: Sum=%b Cout=%b", 
                         a, b, cin, expected_sum, expected_cout, uo_out[0], uo_out[1]);
            end
        end

        $display("----------------------------------------------");
        $display("              SIMULATION COMPLETE             ");
        $display("----------------------------------------------");
        $finish;
    end

endmodule
