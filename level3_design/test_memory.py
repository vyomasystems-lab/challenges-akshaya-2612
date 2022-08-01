# See LICENSE.vyoma for details

import os
import random
from pathlib import Path

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import RisingEdge, FallingEdge, Timer

@cocotb.test()
async def test_memory(dut):
    """Test for memory"""

    cocotb.log.info('#### CTB: Develop your test here! ######')

    clock = Clock(dut.clk, 50, units="ns")  # Create a 50ns period clock on port clk
    cocotb.start_soon(clock.start())        # Start the clock
    
    # reset
    dut.reset.value=1
    await FallingEdge(dut.clk)
    dut.reset.value=0
    await FallingEdge(dut.clk)
    '''
    dut.reset.value=1
    await Timer(50,'ns')
    dut.reset.value=0
    await Timer(50,'ns')
    '''
    # address and data 
    writeEn=1
    dut.write_enable.value=writeEn
    await Timer(25,'ns')
    addr=120
    dut.address.value = addr
    inp=32
    dut.data_input.value = inp
    await Timer(25,'ns')
    writeEn=0
    dut.write_enable.value=writeEn
    addr=120
    dut.address.value=addr
    await Timer(1,'ns')

    assert int(dut.data_output.value)==32, f"Result is Incorrect : {dut.data_output.value}!=32"
