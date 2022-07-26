# LEVEL 1 - DESIGN 1 : MULTIPLEXER
<img width="960" alt="image" src="https://user-images.githubusercontent.com/102654877/180646242-a161d318-0ed7-4524-aee4-ff08ec4035f9.png">
## Verification Environment
The test bench drives inputs to the Design under test ,i.e. mux module, which takes 31 2-bit inputs and one 5-bit select input and gives one 2-bit output.
The input is selected one by one from 0 to 30, and select signal is driven accordingly. 
### Bug 1:
For example, following test is made for testing input 12:

```
dut.inp12.value =1
    dut.sel.value = 12
    await Timer(1,'ns')
    assert dut.out.value==1 , f"Result is Incorrect : {dut.out.value}!= 1" 

```
Following error is obtained:
assert dut.out.value==1 , f"Result is Incorrect : {dut.out.value}!= 1"
                     AssertionError: Result is Incorrect : 00!= 1
### Bug 2:

### Bug 3:

## Test Scenario 
### Bug 1:
- Test inputs: inp12=1, sel=12 
- Expected Output: out= 01
- Observed Output in the DUT dut.out= 00
Output mismatches for the above inputs proving that there is a design bug.

### Bug 2:
### Bug 3:

## Design Fix
Updating the design and re- running the test makes the test pass.
### Bug 1:

### Bug 2:
### Bug 3:
The updated design is checked in as mux_fix.v
## Design Bug
Based on the above test input and analysing the design, we see the following
### Bug 1: 
<img width="241" alt="image" src="https://user-images.githubusercontent.com/102654877/181082559-b3fe63c7-3c1e-4763-839c-4ea13be7c1c8.png">
For the inp12, sel signal should be equal to 5'b01100 instead of 5'b01101 as in design code.

### Bug 2:
### Bug 3:
