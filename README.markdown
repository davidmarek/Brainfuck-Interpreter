Brainfuck
=========

Invocation
----------

To play with brainfuck start interpreter:

    python brainfuck/interpreter.py

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

