
# LEVEL 2 - DESIGN : Bitmanipulation Coprocessor
<img width="960" alt="image" src="https://user-images.githubusercontent.com/102654877/180646242-a161d318-0ed7-4524-aee4-ff08ec4035f9.png">
## Verification Environment
The test bench drives inputs to the Design under test ,i.e. mkbitmanip module, which takes four 32-bit inputs and give 33-bit output as putvalue.

### Bug 1:
For example, following test is made for testing input:

```
 # input transaction
    mav_putvalue_src1 = 0x5
    mav_putvalue_src2 = 0x2
    mav_putvalue_src3 = 0x4
    mav_putvalue_instr = 0x101010B3

    # expected output from the model
    expected_mav_putvalue = bitmanip(mav_putvalue_instr, mav_putvalue_src1, mav_putvalue_src2, mav_putvalue_src3)

    # driving the input transaction
    dut.mav_putvalue_src1.value = mav_putvalue_src1
    dut.mav_putvalue_src2.value = mav_putvalue_src2
    dut.mav_putvalue_src3.value = mav_putvalue_src3
    dut.EN_mav_putvalue.value = 1
    dut.mav_putvalue_instr.value = mav_putvalue_instr
  
    yield Timer(1) 

    # obtaining the output
    dut_output = dut.mav_putvalue.value

    cocotb.log.info(f'DUT OUTPUT={hex(dut_output)}')
    cocotb.log.info(f'EXPECTED OUTPUT={hex(expected_mav_putvalue)}')
    
    # comparison
    error_message = f'Value mismatch DUT = {hex(dut_output)} does not match MODEL = {hex(expected_mav_putvalue)}'
    assert dut_output == expected_mav_putvalue, error_message

```
Following error is obtained:
assert dut_output == expected_mav_putvalue, error_message
                     AssertionError: Value mismatch DUT = 0xa does not match MODEL = 0x0

## Test Scenario 
### Bug 1:
- Test inputs: mav_putvalue_src1 = 0x5, mav_putvalue_src2 = 0x2, mav_putvalue_src3 = 0x4, mav_putvalue_instr = 0x101010B3
- Expected Output: out= 0x0
- Observed Output in the DUT dut.out= 0xa

Output mismatches for the above inputs proving that there is a design bug.
