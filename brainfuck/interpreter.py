#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import with_statement

import os
import sys


class Memory(object):
    """Memory of brainfuck interpreter."""

    def __init__(self):
        """Initialize memory."""

        self.mem = {}

    def __getitem__(self, address):
        """Get number on given address."""

        if not self.mem.has_key(address):
            self.mem[address] = 0
        return self.mem[address]

    def __setitem__(self, address, value):
        """Set number on given address."""

        self.mem[address] = value

    def clean(self):
        self.mem = {}


class InterpreterError(Exception):
    """Exception in interpreter invocation."""

    pass


class Interpreter(object):
    """Brainfuck interpreter."""

    def __init__(self):
        """Initialize brainfuck interpreter and environment."""

        self.memory = Memory()
        self._init_environment()

    def _init_environment(self):
        """Clean memory and set pointers to 0."""

        self.pc = 0
        self.mc = 0
        self.stack = []
        self.source = ""
        self.memory.clean()


    def load_file(self, filename):
        """Load brainfuck source code from file."""

        # First clean previous environment.
        self._init_environment()

        # Open the source file and load it.
        with open(filename, 'r') as source:
            this.source = self._clean_source_code(''.join(source.readlines()))
            return

        # If something went wrong raise an exception.
        raise InterpreterError("Cannot open source file.")

    def load_string(self, code):
        """Load brainfuck source code from string."""

        self.pc = 0
        self.stack = []
        self.source = self._clean_source_code(code)

    def _clean_source_code(self, code):
        """Remove all comments from source code."""

        return filter(lambda x: x in "<>+-,.[]", code)


    def eval_code(self):
        """Evaluate the loaded code."""

        while 0 <= self.pc < len(self.source):
            self.step()

    def step(self):
        """Evaluate next instruction."""

        if self.source[self.pc] == '>':
            self.mc += 1
        elif self.source[self.pc] == '<':
            self.mc -= 1
        elif self.source[self.pc] == '+':
            self.memory[self.mc] += 1
        elif self.source[self.pc] == '-':
            self.memory[self.mc] -= 1
        elif self.source[self.pc] == '.':
            sys.stdout.write("%c" % self.memory[self.mc])
            sys.stdout.flush()
        elif self.source[self.pc] == ',':
            user_input = raw_input()
            self.memory[self.mc] = ord(user_input[:1]) if user_input else ord("\n")
        elif self.source[self.pc] == '[':
            if self.memory[self.mc] != 0:
                self.stack.append(self.pc)
            else:
                bc = 1
                while (bc != 0) and (self.pc < len(self.source)-1):
                    self.pc += 1
                    if self.source[self.pc] == '[':
                        bc += 1
                    elif self.source[self.pc] == ']':
                        bc -= 1
        elif self.source[self.pc] == ']':
            if self.memory[self.mc] != 0:
                self.pc = self.stack.pop() - 1

        self.pc += 1


if __name__ == '__main__':
    import readline

    interpreter = Interpreter()
    try:
        while True:
            try:
                line = raw_input("brainfuck> ")
                interpreter.load_string(line)
                interpreter.eval_code()
            except KeyboardInterrupt:
                print ""
    except EOFError:
        sys.exit(0)

