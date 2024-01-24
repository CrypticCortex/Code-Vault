
import sys

#set the input and output paths to generate the .asm file inside of the directory

path = "/media/naylak15/New Volume1/University/Nand2Tetris/nand2tetris/projects/07/StackArithmetic/SimpleAdd/SimpleAdd.vm"
print("path:", path)

input = open(path,"r") 
output = open(path.replace('.vm','.asm'),"w") 
#ASM PUSH COMMANDS
def asm_push_constant(line, i):
    output.write('@'+line[14:])
    output.write('D=A\n@SP\nA=M\nM=D\n@SP\nM=M+1\n')

def asm_push_local(line, i):
    output.write('@'+line[11:])
    output.write('D=A\n@LCL\nA=D+M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n')

def asm_push_that(line, i):
    output.write('@'+line[10:])
    output.write('D=A\n@THAT\nA=D+M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n')

def asm_push_argument(line, i):
    output.write('@'+line[14:])
    output.write('D=A\n@ARG\nA=D+M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n')

def asm_push_this(line, i):
    output.write('@'+line[10:])
    output.write('D=A\n@THIS\nA=D+M\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n')

def asm_push_temp(line, i):
    output.write('@'+line[10:])
    output.write('D=A\n@5\nA=D+A\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n')

def asm_push_pointer_0(line, i):
    #output.write('@'+line[10:])
    output.write('@3\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n')

def asm_push_pointer_1(line, i):
    #output.write('@'+line[10:])
    output.write('@4\nD=M\n@SP\nA=M\nM=D\n@SP\nM=M+1\n')

def asm_push_static(line, i):
    output.write('@Foo.'+line[12:])
    output.write('D=M\n')
    output.write('@SP\nA=M\nM=D\n@SP\nM=M+1\n')

#ASM POP COMMANDS
def  asm_pop_static(line, i):
    output.write('@SP\nM=M-1\nA=M\nD=M\n')
    output.write('@Foo.'+line[11:])
    output.write('M=D\n')

def  asm_pop_local(line, i):
    output.write('@'+line[10:])
    output.write('D=A\n@LCL\nD=D+M\n@SP\nA=M\nM=D\nA=A-1\nD=M\nA=A+1\nA=M\nM=D\n@SP\nM=M-1\n')
    
def  asm_pop_argument(line, i):
    output.write('@'+line[13:])
    output.write('D=A\n@ARG\nD=D+M\n@SP\nA=M\nM=D\nA=A-1\nD=M\nA=A+1\nA=M\nM=D\n@SP\nM=M-1\n')

def  asm_pop_this(line, i):
    output.write('@'+line[9:])
    output.write('D=A\n@THIS\nD=D+M\n@SP\nA=M\nM=D\nA=A-1\nD=M\nA=A+1\nA=M\nM=D\n@SP\nM=M-1\n')
  
def  asm_pop_that(line, i):
    output.write('@'+line[9:])
    output.write('D=A\n@THAT\nD=D+M\n@SP\nA=M\nM=D\nA=A-1\nD=M\nA=A+1\nA=M\nM=D\n@SP\nM=M-1\n')

def  asm_pop_temp(line, i):
    output.write('@'+line[9:])
    output.write('D=A\n@5\nD=D+A\n@SP\nA=M\nM=D\nA=A-1\nD=M\nA=A+1\nA=M\nM=D\n@SP\nM=M-1\n')
  
def  asm_pop_pointer_0(line, i):
    output.write('@SP\nM=M-1\n@3\nM=A\nM=D\n')

def  asm_pop_pointer_1(line, i):
    output.write('@SP\nM=M-1\n@4\nM=A\nM=D\n')

#ASM ARITHMETICAL COMMANDS
def add(line, i):
    output.write('@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=D+M\n@SP\nM=M+1\n')

def sub(line, i):
    output.write('@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=M-D\n@SP\nM=M+1\n')

def f_and(line, i):
    output.write('@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=M&D\n@SP\nM=M+1\n')

def f_or(line, i):
    output.write('@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nM=M|D\n@SP\nM=M+1\n')

def eq(line, i):
    n=str(i)
    output.write('@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nD=D-M\n@JUMP'+n+'\nD,JEQ\nD=0\n@ENDING'+n+'\n0,JMP\n(JUMP'+n+')\nD=-1\n(ENDING'+n+')\n@SP\nA=M\nM=D\n@SP\nM=M+1\n')

def lt(line, i):
    n=str(i)
    output.write('@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nD=D-M\n@JUMP'+n+'\nD,JGT\nD=0\n@ENDING'+n+'\n0,JMP\n(JUMP'+n+')\nD=-1\n(ENDING'+n+')\n@SP\nA=M\nM=D\n@SP\nM=M+1\n')

def gt(line, i):
    n=str(i)
    output.write('@SP\nM=M-1\nA=M\nD=M\n@SP\nM=M-1\nA=M\nD=D-M\n@JUMP'+n+'\nD,JLT\nD=0\n@ENDING'+n+'\n0,JMP\n(JUMP'+n+')\nD=-1\n(ENDING'+n+')\n@SP\nA=M\nM=D\n@SP\nM=M+1\n')

def neg(line, i):
    n=str(i)
    output.write('@SP\nM=M-1\nA=M\nD=!M\nM=D+1\n@SP\nM=M+1\n')

def f_not(line, i):
    n=str(i)
    output.write('@SP\nM=M-1\nA=M\nD=!M\nM=D\n@SP\nM=M+1\n')

def other(line,i):
    pass

instructions = [['add', '0', add],
                ['sub', '1', sub],
                ['neg', '2', neg],
                ['eq', '3', eq],
                ['gt', '4', gt],
                ['lt','5', lt],
                ['and','6', f_and],
                ['or','7', f_or],
                ['not','8', f_not],
                ['pop local','9', asm_pop_local],
                ['pop argument','10', asm_pop_argument],
                ['pop this','11', asm_pop_this],
                ['pop that','12', asm_pop_that],
                ['pop static','13', asm_pop_static],
                ['pop pointer 0','14', asm_pop_pointer_0],
                ['pop pointer 1','15', asm_pop_pointer_1],
                ['pop temp','16', asm_pop_temp],
                ['push local','17', asm_push_local],
                ['push argument','18', asm_push_argument],
                ['push this','19', asm_push_this],
                ['push that','20', asm_push_that],
                ['push constant','21',asm_push_constant],
                ['push static','22', asm_push_static],
                ['push pointer 0','23', asm_push_pointer_0],
                ['push pointer 1','24', asm_push_pointer_1],
                ['push temp','25', asm_push_temp]]

#function to find words in a string
def find_words(text, search):
    """Find exact words"""
    dText   = text.split()  
    dSearch = search.split()

    found_word = 0

    for text_word in dText:
        for search_word in dSearch:
            if search_word == text_word:
                found_word += 1

    if found_word == len(dSearch):
        return True
    else:
        return False

i=0
lines = input.readlines()
for line in lines:
    if (line[0]) != '/':
        #print(line)
        #it creates a command in the .asm file
        output.write("//INSTRUCTION: "+line)
        i=i+1
        #it classifies the asm intruction
        for instruction in instructions:
            if find_words(line,instruction[0]):
                print('INSTRUCTION', instruction[0],'to >>> ASM:', line[:-1], 'OK')
                instruction[2](line,i)
        #for char in line:
            #print(char)
#add (END)\n @END\n 0;JMP\n to the .asm file
output.write('(END)\n')
output.write('@END\n')
output.write('0;JMP\n')



input.close
output.close
