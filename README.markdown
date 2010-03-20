Brainfuck
=========

Invocation
----------

Start playing with brainfuck immediately:

    python brainfuck/interpreter.py -i

You can also specify input file:

    python brainfuck/interpreter.py -f myProgram.bf
    
Examples
--------

First 8 bytes of memory are registers. Users should use them only as specified
in the documentation of the function. If you are writing your own function, 
then please set all used register to 0.

    +++>                            M0 = 3
    ++<                             M1 = 2

Sum M0 and M1 | Result in M2

    ADD M0 M1 M2
    [->>+>+<<<]>>>[-<<<+>>>]<<      Copy M0 to M2 | temp M3 | pc in M1
    [->+>+<<]>>[-<<+>>]             Copy M1 to M2 | temp M3 | pc in M3
    ++++++[<++++++++>-]<            Add "0" to M2 | temp M3 | pc in M2
    .                               Print sum | pc in M2
    [-]<<                           Clear M2 | pc in M0

Subtract M1 from M0 | Result in M2

    SUB M0 M1 M2
    [->>+>+<<<]>>>[-<<<+>>>]<<     Copy M0 to M2 | temp M3 | pc in M1
    [->->+<<]>>[-<<+>>]            Subtract M1 from M2 | temp M3 | pc in M3
    ++++++[<++++++++>-]<           Add "0" to M2 | temp M3 | pc in M2
    .                              Print sub | pc in M2
    [-]<<                          Clear M2 | pc in M0

Multiply M0 and M1 | result in M2

    MUL M0 M1 M2
    [->>>+>+<<<<]>>>>[-<<<<+>>>>]<     Copy M0 to M3 | temp M3 M4 | pc in M3
    [-<<[->+>>+<<<]>>>[-<<<+>>>]<]     Copy M3 x M1 to M2 | temp M3 M4 | pc in M3
    ++++++[-<++++++++>]<               Add "0" to M2 | temp M3 | pc in M2
    .                                  Print mul | pc in M2
    [-]<<                              Clear M2 | pc in M0


TODO:
=====

Instruction Set
---------------

    mov     Addr    Val     # Memory[Addr] = Val
    while   Addr            # while(Memory[Addr] != 0) {
    end     Addr            # } 
    inc     Addr            # Memory[Addr]++
    dec     Addr            # Memory[Addr]--
    put     Addr            # print Memory[Addr]
    get     Addr            # input Memory[Addr]

