# LEVEL 1 - DESIGN 2 : Sequence Detector - 1011
<img width="960" alt="image" src="https://user-images.githubusercontent.com/102654877/180646242-a161d318-0ed7-4524-aee4-ff08ec4035f9.png">
## Verification Environment
The test bench drives inputs to the Design under test ,i.e. seq_detect module, which takes inputs of 1-bit clock,reset and input bit and give one 1-bit output named as seq_seen, which is high when sequence 1011 is detected.

### Bug 1:
For example, following test is made for testing input 01011:

```
    dut.inp_bit.value=0
    dut.inp_bit.value=1
    dut.inp_bit.value=0
    dut.inp_bit.value=1
    dut.inp_bit.value=1
    
    print ("sequence detector test case")

    assert dut.seq_seen.value == 1, f"Adder result is incorrect: {dut.seq_seen.value}!=1"

```
Following error is obtained:
assert dut.seq_seen.value == 1, f"Adder result is incorrect: {dut.seq_seen.value}!=1"
                     AssertionError: Adder result is incorrect: 0!=1

## Test Scenario 
### Bug 1:
- Test inputs: inp_bit=0,inp_bit=1,inp_bit=0,inp_bit=1,inp_bit=1 
- Expected Output: seq_seen=1
- Observed Output in the DUT dut.seq_seen= 0
Output mismatches for the above inputs proving that there is a design bug.

