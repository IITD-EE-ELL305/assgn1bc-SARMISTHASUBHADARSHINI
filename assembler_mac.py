#add,sun,mul,div implemented
def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

opcodes = {"add": "00000",
           "sub": "00001",
           "mul": "00010",
           "div": "00011",
           "mov": "01001"}
reg = ["r1","r2","r3","r4","r5","r6","r7","r8","r9","r10","r11","r12","r13","r14","r15","r16"]
inp = str(input())
x = inp.replace(",", " ")
p = x.split(" ")
res = ""

I = "0"
if check_int(p[-1]):
    I = "1"
operand = p[0]
res = res+opcodes[operand]+" "+I
bin18_i = lambda x : ''.join(reversed( [str((x >> i) & 1) for i in range(18)] ) )
bin18_r = lambda x : ''.join( [str((x >> i) & 1) for i in range(18)] ) 
if operand != "mov":
    rd = p[1]
    rdbin = str(bin18_r(int(rd[1:])))
    rs1 = p[2]
    rs1bin = str(bin18_r(int(rs1[1:])))
    rs2 = p[3]
    if I == "1":
        imm = str(bin18_i(int(rs2)))
    else:
        imm = str(bin18_r(int(rs2[1:])))
    res = res +" "+ rdbin + " "+ rs1bin+ " "+ imm

print(res)





