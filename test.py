'''
-		Operands	Count = 59	System.Collections.Generic.List<string>
		[0]	"def"	string
		[1]	"compute_hcf"	string
		[2]	"("	string
		[3]	"x"	string
		[4]	","	string
		[5]	"y"	string
		[6]	")"	string
		[7]	":"	string
		[8]	"x"	string
		[9]	"y"	string
		[10]	":"	string
		[11]	"smaller"	string
		[12]	"y"	string
		[13]	"else"	string
		[14]	":"	string
		[15]	"smaller"	string
		[16]	"x"	string
		[17]	"i"	string
		[18]	"in"	string
		[19]	"range"	string
		[20]	"("	string
		[21]	"1"	string
		[22]	","	string
		[23]	"smaller"	string
		[24]	"1"	string

-		Operators	Count = 15	System.Collections.Generic.List<string>
		[0]	"if"	string
		[1]	">"	string
		[2]	"="	string
		[3]	"="	string
		[4]	"for"	string
		[5]	"+"	string
		[6]	"if"	string
		[7]	"%"	string
		[8]	"=="	string
		[9]	"and"	string
		[10]	"%"	string
		[11]	"=="	string
		[12]	"="	string
		[13]	"="	string
		[14]	"="	string
'''
# Python program to find H.C.F of two numbers

# define a function
def compute_hcf(x, y):

# choose the smaller number
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller+1):
        if((x % i == 0) and (y % i == 0)):
            hcf = i
            try:
                print(x)
                for i2 in range(1, smaller+1):
                    print("Something went wrong"+i2)
            except:
                print("Something went wrong")
            finally:
                print("The 'try except' is finished")
    return hcf

num1 = 54 
num2 = 24

print("The H.C.F. is", compute_hcf(num1, num2))