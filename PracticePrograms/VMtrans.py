
import sys

path = "/media/naylak15/New Volume1/University/Nand2Tetris/nand2tetris/projects/07/StackArithmetic/SimpleAdd/SimpleAdd.vm"
print("path:", path)

input = open(path, "r")
output = open(path.replace('.vm', '.asm'), "w")

def asm_push_constant(line, i):
    output.write("@" + line[14:])
    output.write("D=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")

def asm_push_local(line, i):
    output.write("@" + line[14:])
    output.write("D=A\n@LCL\nA=D+M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")

def asm_push_that(line, i):
    output.write("@" + line[10:])
    output.write("D=A\n@THAT\nA=D+M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")

def asm_push_argument(line, i):
    output.write[14:]
    output.write("D=A\n@ARG\nA=D+M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")

def asm_push_this(line, i):
    output.write("@" + line[10:])
    output.write("D=A\n@THIS\nA=D+M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")

def asm_push_temp(line, i):
    output.write("@" + line[10:])
    output.write("D=A\n@5\nA=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")

def asm_push_pointer_0(line, i):
    output.write("@" + line[10:])
    output.write("D=A\n@THIS\nA=D+M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")

def asm_push_pointer_1(line, i):
    output.write("@" + line[10:])
    output.write("D=A\n@THAT\nA=D+M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")

def asm_push_static(line, i):
    output.write("@Foo." + line[12:])
    output.write('D=M\n')
    output.write("@SP\nA=M\nM=D\n@SP\nM=M+1\n")

# Define Pop Commands as functions

def asm_pop_static(line, i):
    output.write("@SP\nM=M-1\nA=M\nD=M\n")
    output.write("@Foo." + line[11:])
    output.write('M=D\n')

def asm_pop_local(line, i):
    output.write('@' + line[10:])
    output.write("D=A\nLCL\nD=D+M\nSP\nA=M\nM=D\nA=A-1\nD=M\nA=A+1\nA=M\nM=D\n@SP\nM=M-1\n")

def asm_pop_argument(line, i):
    output.write('@' + line[13:])
    output.write("D=A\nARG\nD=D+M\nSP\nA=M\nM=D\nA=A-1\nD=M\nA=A+1\nA=M\nM=D\n@SP\nM=M-1\n")

def asm_pop_this(line, i):
    output.write('@' + line[9:])
    output.write("D=A\nTHIS\nD=D+M\nSP\nA=M\nM=D\nA=A-1\nD=M\nA=A+1\nA=M\nM=D\n@SP\nM=M-1\n")

def asm_pop_that(line, i):
    output.write('@' + line[10:])
    output.write("D=A\nTHAT\nD=D+M\nSP\nA=M\nM=D\nA=A-1\nD=M\nA=A+1\nA=M\nM=D\n@SP\nM=M-1\n")

def asm_pop_temp(line,i):
    output.write('@' + line[9:])
    output.write("D=A\n@5\nD=D+A\n@SP\nA=M\nM=D\nA=A-1\nD=M\nA=A+1\nA=M\nM=D\n@SP\nM=M-1\n")

def asm_pop_pointer_0(line, i):
    output.write("@SP\nM=M-1\n@3\nA=M\nM=D\n")

def asm_pop_pointer_1(line, i):
    output.write("@SP\nM=M-1\n@4\nA=M\nM=D\n")

# Defining Arithematic Commands

def add(line, i):
    output.write("@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=M+D\n@SP\nM=M+1\n")

def sub(line, i):
    output.write("@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=M-D\n@SP\nM=M+1\n")

def f_and(line, i):
    output.write("@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=D&M\n@SP\nM=M+1\n")

def f_or(line , i):
    output.write("@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=D|M\n@SP\nM=M+1\n")

def eq(line, i):
    output.write("@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nD=M-D\n@EQ" + str(i) + "\nD;JEQ\nD=0\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@EQ" + str(i) + "\n0;JMP\n(EQ" + str(i) + ")\nD=-1\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")

def lt(line, i):
    output.write("@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nD=M-D\n@LT" + str(i) + "\nD;JLT\nD=0\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@LT" + str(i) + "\n0;JMP\n(LT" + str(i) + ")\nD=-1\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")

def gt(line, i):
    output.write("@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nD=M-D\n@GT" + str(i) + "\nD;JGT\nD=0\n@SP\nA=M\nM=D\n@SP\nM=M+1\n@GT" + str(i) + "\n0;JMP\n(GT" + str(i) + ")\nD=-1\n@SP\nA=M\nM=D\n@SP\nM=M+1\n")

def neg(line, i):
    output.write("@SP\nM=M-1\nA=M\nD=!M\nM=D+1\n@SP\nM=M+1\n")

def f_not(line, i):
    output.write("@SP\nM=M-1\nA=M\nD=M\nD=!D\nM=D+1\n@SP\nM=M+1\n")

def other(line, i):
    pass

instructions = [
['add', '0', add] , 
['sub', '1', sub] , 
['neg', '2', neg] , 
['eq', '3', eq] , 
['gt', '4', gt] , 
['lt', '5', lt] , 
['and', '6', f_and] , 
['or', '7', f_or] , 
['not', '8', f_not],
['pop local', '9', asm_pop_local], 
['pop argument', '10', asm_pop_argument], 
['pop this', '11', asm_pop_this], 
['pop that', '12', asm_pop_that], 
['pop static', '13', asm_pop_static], 
['pop pointer 0', '14', asm_pop_pointer_0], 
['pop pointer 1', '15', asm_pop_pointer_1],
['pop temp', '16', asm_pop_temp], 
['push local', '17', asm_push_local], 
['push argument', '18', asm_push_argument], 
['push this', '19', asm_push_this], 
['push that', '20', asm_push_that], 
['push constant', '21', asm_push_constant], 
['push static', '22', asm_push_static],
['push pointer 0', '23', asm_push_pointer_0], 
['push pointer 1', '24', asm_push_pointer_1], 
['push temp', '25', asm_push_temp]
]

#function to find words in a string
def find_words(text, search):
    dText = text.split()
    dSearch = search.split()

    found_word = 0

    for text_word in dText:
        for search_word in dSearch:
            if text_word == search_word:
                found_word = 1
    
    if found_word == len(dSearch):
        return True
    else:
        return False


i = 0
lines = input.readlines()

for line in lines:
    if (line[0])  != '/':
        output.write("//INSTRUCTION: " + line)
        i = i + 1

        for instruction in instructions:
            if find_words(line, instruction[0]):
                instruction[2](line, i)

input.close
output.close
