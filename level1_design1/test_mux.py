# See LICENSE.vyoma for details

import cocotb
from cocotb.triggers import Timer
#test file
@cocotb.test()
async def test_mux(dut):
    """Test for mux2"""
    cocotb.log.info('##### CTB: Develop your test here ########')
    
    dut.inp0.value =1
    dut.sel.value = 0
    await Timer(1,'ns')
    assert dut.out.value==1 , f"Result is Incorrect : {dut.out.value}!= 1"

    dut.inp1.value =1
    dut.sel.value = 1
    await Timer(1,'ns')
    assert dut.out.value==1 , f"Result is Incorrect : {dut.out.value}!= 1"

    dut.inp3.value =1
    dut.sel.value = 3
    await Timer(1,'ns')
    assert dut.out.value==1 , f"Result is Incorrect : {dut.out.value}!= 1"
    
    dut.inp4.value =1
    dut.sel.value = 4
    await Timer(1,'ns')
    assert dut.out.value==1 , f"Result is Incorrect : {dut.out.value}!= 1"

    dut.inp5.value =1
    dut.sel.value = 5
    await Timer(1,'ns')
    assert dut.out.value==1 , f"Result is Incorrect : {dut.out.value}!= 1"

    dut.inp6.value =1
    dut.sel.value = 6
    await Timer(1,'ns')
    assert dut.out.value==1 , f"Result is Incorrect : {dut.out.value}!= 1"

    dut.inp7.value =1
    dut.sel.value = 7
    await Timer(1,'ns')
    assert dut.out.value==1 , f"Result is Incorrect : {dut.out.value}!= 1"
    dut.inp8.value =1
    dut.sel.value = 8
    await Timer(1,'ns')
    assert dut.out.value==1 , f"Result is Incorrect : {dut.out.value}!= 1"

    dut.inp9.value =1
    dut.sel.value = 9
    await Timer(1,'ns')
    assert dut.out.value==1 , f"Result is Incorrect : {dut.out.value}!= 1"

    dut.inp10.value =1
    dut.sel.value = 10
    await Timer(1,'ns')
    assert dut.out.value==1 , f"Result is Incorrect : {dut.out.value}!= 1"

    dut.inp11.value =1
    dut.sel.value = 11
    await Timer(1,'ns')
    assert dut.out.value==1 , f"Result is Incorrect : {dut.out.value}!= 1"
    
    dut.inp12.value =1
    dut.sel.value = 12
    await Timer(1,'ns')
    assert dut.out.value==1 , f"Result is Incorrect : {dut.out.value}!= 1"
    
    dut.inp13.value =1
    dut.sel.value = 13
    await Timer(1,'ns')
    assert dut.out.value==1 , f"Result is Incorrect : {dut.out.value}!= 1"

    dut.inp14.value =1
    dut.sel.value = 14
    await Timer(1,'ns')
    assert dut.out.value==1 , f"Result is Incorrect : {dut.out.value}!= 1"

    dut.inp15.value =1
    dut.sel.value = 15
    await Timer(1,'ns')
    assert dut.out.value==1 , f"Result is Incorrect : {dut.out.value}!= 1"

    dut.inp16.value =1
    dut.sel.value = 16
    await Timer(1,'ns')
    assert dut.out.value==1 , f"Result is Incorrect : {dut.out.value}!= 1"

    dut.inp17.value =1
    dut.sel.value = 17
    await Timer(1,'ns')
    assert dut.out.value==1 , f"Result is Incorrect : {dut.out.value}!= 1"

    dut.inp18.value =1
    dut.sel.value = 18
    await Timer(1,'ns')
    assert dut.out.value==1 , f"Result is Incorrect : {dut.out.value}!= 1"

    dut.inp19.value =1
    dut.sel.value = 19
    await Timer(1,'ns')
    assert dut.out.value==1 , f"Result is Incorrect : {dut.out.value}!= 1"

    dut.inp20.value =1
    dut.sel.value = 20
    await Timer(1,'ns')
    assert dut.out.value==1 , f"Result is Incorrect : {dut.out.value}!= 1"

    dut.inp21.value =1
    dut.sel.value = 21
    await Timer(1,'ns')
    assert dut.out.value==1 , f"Result is Incorrect : {dut.out.value}!= 1"

    dut.inp22.value =1
    dut.sel.value = 22
    await Timer(1,'ns')
    assert dut.out.value==1 , f"Result is Incorrect : {dut.out.value}!= 1"

    dut.inp23.value =1
    dut.sel.value = 23
    await Timer(1,'ns')
    assert dut.out.value==1 , f"Result is Incorrect : {dut.out.value}!= 1"

    dut.inp24.value =1
    dut.sel.value = 24
    await Timer(1,'ns')
    assert dut.out.value==1 , f"Result is Incorrect : {dut.out.value}!= 1"

    dut.inp25.value =1
    dut.sel.value = 25
    await Timer(1,'ns')
    assert dut.out.value==1 , f"Result is Incorrect : {dut.out.value}!= 1"

    dut.inp26.value =1
    dut.sel.value = 26
    await Timer(1,'ns')
    assert dut.out.value==1 , f"Result is Incorrect : {dut.out.value}!= 1"

    dut.inp27.value =1
    dut.sel.value = 27
    await Timer(1,'ns')
    assert dut.out.value==1 , f"Result is Incorrect : {dut.out.value}!= 1"

    dut.inp28.value =1
    dut.sel.value = 28
    await Timer(1,'ns')
    assert dut.out.value==1 , f"Result is Incorrect : {dut.out.value}!= 1"

    dut.inp29.value =1
    dut.sel.value = 29
    await Timer(1,'ns')
    assert dut.out.value==1 , f"Result is Incorrect : {dut.out.value}!= 1"
    
    dut.inp30.value =1
    dut.sel.value = 30
    await Timer(1,'ns')
    assert dut.out.value==1 , f"Result is Incorrect : {dut.out.value}!= 1"

    
