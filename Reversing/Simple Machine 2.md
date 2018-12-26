> A SIMPLE MACHINE  
WHAT IS THIS?  
You stand before assembly code for a custom Virtual Machine.<br><br>
You will find the flag once you understand the code.<br><br>
Everything you need to know is described below. Don’t forget to check ou the example code!<br><br>
Get the machine code Here<br><br>
TOP LEVEL DESCRIPTION<br>
The machine is stack based, which means most operations pop data off the top of the stack and push the result. for further<br> reference, https://en.wikipedia.org/wiki/Stack_machine#Advantages_of_stack_machine_instruction_sets<br><br>
The machine state is defined by an Instruction Pointer, and a Stack data structure.<br><br>
The next instruction to be executed is pointed to by IP, and it generally reads/write values from/to the top of the stack.<br><br>
[... TOO LONG...]  

The size of the file is 102 bytes. Not too long, especially when the size of instructions is 1 byte (102 instructions in total).<br><br>

The first 38 instructions are pushes. It seems obvious that those 38 pushes are the flag or will be used to do operations on the flag. But first thing, we should split the code into functions.<br><br>

After the 38 first pushes, the following instructions appear (I added the labels):
>loop:  
&nbsp;&nbsp;&nbsp;&nbsp;PUSH 11  
&nbsp;&nbsp;&nbsp;&nbsp;JSE&nbsp;&nbsp;&nbsp;&nbsp;; exit<br>  	
&nbsp;&nbsp;&nbsp;&nbsp;READ  
&nbsp;&nbsp;&nbsp;&nbsp;PUSH 12  
&nbsp;&nbsp;&nbsp;&nbsp;CALL&nbsp;&nbsp;&nbsp;&nbsp;; func1  
&nbsp;&nbsp;&nbsp;&nbsp;LOAD 1  
&nbsp;&nbsp;&nbsp;&nbsp;PUSH 10  
&nbsp;&nbsp;&nbsp;&nbsp;PUSH 0  
&nbsp;&nbsp;&nbsp;&nbsp;SUB  
&nbsp;&nbsp;&nbsp;&nbsp;CJE&nbsp;&nbsp;&nbsp;&nbsp;; loop  
&nbsp;&nbsp;&nbsp;&nbsp;PUSH 48  
&nbsp;&nbsp;&nbsp;&nbsp;PUSH 1  
&nbsp;&nbsp;&nbsp;&nbsp;JUMP  
exit:  
&nbsp;&nbsp;&nbsp;&nbsp;PUSH 49  
&nbsp;&nbsp;&nbsp;&nbsp;WRITE  
&nbsp;&nbsp;&nbsp;&nbsp;PUSH 47  
&nbsp;&nbsp;&nbsp;&nbsp;JUMP&nbsp;&nbsp;&nbsp;&nbsp;; exitting the machine

At first glance it's pretty intimidating. But it's actually like the following python code:
> flag = ''  
s = stack() # with all the pushes  
while not s.empty():  
&nbsp;&nbsp;&nbsp;&nbsp;user_input = int(input(''))  
&nbsp;&nbsp;&nbsp;&nbsp;flag += func1(s.pop(), user_input)  
print('1')

Nice! Not so scary now. Now we need to figure out what is the func1 does.  
The call instruction, jumps to 12 instructions ahead (because there is a PUSH 12 before it). So, the func1 instructions are:
> func1:  
&nbsp;&nbsp;&nbsp;&nbsp;LOAD 2  
&nbsp;&nbsp;&nbsp;&nbsp;LOAD 2  
&nbsp;&nbsp;&nbsp;&nbsp;PUSH 0  
&nbsp;&nbsp;&nbsp;&nbsp;PUSH 37  
&nbsp;&nbsp;&nbsp;&nbsp;CJE&nbsp;&nbsp;&nbsp;&nbsp;;exit_func1  
&nbsp;&nbsp;&nbsp;&nbsp;LOAD 2  
&nbsp;&nbsp;&nbsp;&nbsp;SWAP 1  
&nbsp;&nbsp;&nbsp;&nbsp;PUSH 0  
&nbsp;&nbsp;&nbsp;&nbsp;PUSH 32  
&nbsp;&nbsp;&nbsp;&nbsp;CJE&nbsp;&nbsp;&nbsp;&nbsp;;exit_func1  
&nbsp;&nbsp;&nbsp;&nbsp;PUSH 0  
&nbsp;&nbsp;&nbsp;&nbsp;SWAP 1  
&nbsp;&nbsp;&nbsp;&nbsp;LOAD 4  
&nbsp;&nbsp;&nbsp;&nbsp;PUSH 27  
&nbsp;&nbsp;&nbsp;&nbsp;CJE&nbsp;&nbsp;&nbsp;&nbsp;;exit_func1  
&nbsp;&nbsp;&nbsp;&nbsp;POP  
&nbsp;&nbsp;&nbsp;&nbsp;PUSH 2  
&nbsp;&nbsp;&nbsp;&nbsp;LOAD 2  
&nbsp;&nbsp;&nbsp;&nbsp;DIV  
&nbsp;&nbsp;&nbsp;&nbsp;PUSH 2  
&nbsp;&nbsp;&nbsp;&nbsp;LOAD 5  
&nbsp;&nbsp;&nbsp;&nbsp;DIV  
&nbsp;&nbsp;&nbsp;&nbsp;SWAP 1  
&nbsp;&nbsp;&nbsp;&nbsp;SWAP 2  
&nbsp;&nbsp;&nbsp;&nbsp;ADD  
&nbsp;&nbsp;&nbsp;&nbsp;PUSH 2  
&nbsp;&nbsp;&nbsp;&nbsp;SWAP 1  
&nbsp;&nbsp;&nbsp;&nbsp;DIV  
&nbsp;&nbsp;&nbsp;&nbsp;SWAP 1  
&nbsp;&nbsp;&nbsp;&nbsp;POP  
&nbsp;&nbsp;&nbsp;&nbsp;LOAD 2  
&nbsp;&nbsp;&nbsp;&nbsp;LOAD 2  
&nbsp;&nbsp;&nbsp;&nbsp;PUSH 36  
&nbsp;&nbsp;&nbsp;&nbsp;PUSH 0  
&nbsp;&nbsp;&nbsp;&nbsp;SUB  
&nbsp;&nbsp;&nbsp;&nbsp;CALL&nbsp;&nbsp;&nbsp;&nbsp;;func1  
&nbsp;&nbsp;&nbsp;&nbsp;PUSH 2  
&nbsp;&nbsp;&nbsp;&nbsp;MUL  
&nbsp;&nbsp;&nbsp;&nbsp;ADD  
&nbsp;&nbsp;&nbsp;&nbsp;SWAP 2  
&nbsp;&nbsp;&nbsp;&nbsp;POP  
&nbsp;&nbsp;&nbsp;&nbsp;POP  
exit_func:  
&nbsp;&nbsp;&nbsp;&nbsp;SWAP 3  
&nbsp;&nbsp;&nbsp;&nbsp;POP  
&nbsp;&nbsp;&nbsp;&nbsp;SWAP 1  
&nbsp;&nbsp;&nbsp;&nbsp;POP  
&nbsp;&nbsp;&nbsp;&nbsp;RET  

Yep. Much longer and there is a recursive call. Not so fun. So let's break it to pieces.  
In the beginning, there is a clear pattern - check the stack 2 times, push 0 and the offset to the exit of the function, and checking if a variable is equal to 0.  

>&nbsp;&nbsp;&nbsp;&nbsp;LOAD 2  
&nbsp;&nbsp;&nbsp;&nbsp;LOAD 2  
&nbsp;&nbsp;&nbsp;&nbsp;PUSH 0  
&nbsp;&nbsp;&nbsp;&nbsp;PUSH 37  
&nbsp;&nbsp;&nbsp;&nbsp;CJE&nbsp;&nbsp;&nbsp;&nbsp;;exit_func1
&nbsp;&nbsp;&nbsp;&nbsp;LOAD 2  
&nbsp;&nbsp;&nbsp;&nbsp;SWAP 1  
&nbsp;&nbsp;&nbsp;&nbsp;PUSH 0  
&nbsp;&nbsp;&nbsp;&nbsp;PUSH 32  
&nbsp;&nbsp;&nbsp;&nbsp;CJE&nbsp;&nbsp;&nbsp;&nbsp;;exit_func1  
&nbsp;&nbsp;&nbsp;&nbsp;PUSH 0  
&nbsp;&nbsp;&nbsp;&nbsp;SWAP 1  
&nbsp;&nbsp;&nbsp;&nbsp;LOAD 4  
&nbsp;&nbsp;&nbsp;&nbsp;PUSH 27  
&nbsp;&nbsp;&nbsp;&nbsp;CJE&nbsp;&nbsp;&nbsp;&nbsp;;exit_func1


Those first 2 patterns, are the 2 next ifs:
> if a == 0:  
> &nbsp;&nbsp;&nbsp;&nbsp;return   
> if b == 0:  
> &nbsp;&nbsp;&nbsp;&nbsp;return  

The third pattern is seems more complicated but it actually not. It actually checks if the 2 function inputs are equal (you can try and follow the instructions yourself).  
So the third if is:
> if a == b:  
> &nbsp;&nbsp;&nbsp;&nbsp;return  

Sweet :sunglasses: We covered about third of the function (if you are familiar with CTFs you can guess that the function is XOR).
Let's continue to this block of instructions (between the 2 POPs):
> &nbsp;&nbsp;&nbsp;&nbsp;PUSH 2  
&nbsp;&nbsp;&nbsp;&nbsp;LOAD 2  
&nbsp;&nbsp;&nbsp;&nbsp;DIV  
&nbsp;&nbsp;&nbsp;&nbsp;PUSH 2  
&nbsp;&nbsp;&nbsp;&nbsp;LOAD 5  
&nbsp;&nbsp;&nbsp;&nbsp;DIV  
&nbsp;&nbsp;&nbsp;&nbsp;SWAP 1  
&nbsp;&nbsp;&nbsp;&nbsp;SWAP 2  
&nbsp;&nbsp;&nbsp;&nbsp;ADD  
&nbsp;&nbsp;&nbsp;&nbsp;PUSH 2  
&nbsp;&nbsp;&nbsp;&nbsp;SWAP 1  
&nbsp;&nbsp;&nbsp;&nbsp;DIV  
&nbsp;&nbsp;&nbsp;&nbsp;SWAP 1  

This block is equal to the following python code:
> a_div, a_mod = a/2, a%2  
> b_div, b_mod = b/2, a%2  
> c = (a_mod + b_mod) % 2  

Now it's really clear that this function XORs the 2 given variables. Ok but what is getting XORED?
So, we know that the flag starts with "flag{" and ends with "}".  
If you'll got back to the pushes, you can assemble the list [0, 125, 26, 116, 29, 113, 29, 114, 32, 71, 41, 64, 44, 64, 47, 125, 26, 116, 29, 113, 29, 45, 127, 24, 118, 63, 115, 63, 112, 34, 112, 31, 71, 60, 91, 58, 86, 48].  
125 = "}". So this is the back of the flag. Let go to the start.  

48 != "f". So let's calculate the results of 48 xor "f". 0x30^0x66=0x56 (=86). Wait!!!! 
86 is the next variable. Let's check the next character. 0x56^0x6c=0x3a (=58). Ok I see a pattern.
So if you'll try to xor any value with the next value (from the end to the start of the list) you should get the flag.
It's possible to do it by hand but it's too long. So a simple python script can do it for you and give you the flag **flag{XoRROLLIngR0llingRollingRolling}**.<br><br>

The was an awesome challenge (not too difficult but the idea of using a stack based "machine is pretty sweet in my opinion). 85 points.



