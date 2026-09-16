`import cocotb
from cocotb.clock import Clock
from cocotb.triggers import ClockCycles


@cocotb.test()
async def test_project(dut):
    clock = Clock(dut.clk, 10, unit="us")
    cocotb.start_soon(clock.start())

    dut.ena.value = 1
    dut.ui_in.value = 0
    dut.uio_in.value = 0
    dut.rst_n.value = 0
    await ClockCycles(dut.clk, 10)
    dut.rst_n.value = 1

    for a in range(2):
        for b in range(2):
            for cin in range(2):
                dut.ui_in.value = (cin << 2) | (b << 1) | a
                await ClockCycles(dut.clk, 1)

                expected_sum = a ^ b ^ cin
                expected_cout = (a & b) | (b & cin) | (a & cin)
                expected_uo = (expected_cout << 1) | expected_sum

                assert dut.uo_out.value == expected_uo
