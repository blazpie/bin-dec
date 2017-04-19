import sys

while True:

    try:
        in_string = input("\nEnter a number and a numeral system base: ")
        if in_string.lower() == "exit":
            sys.exit("\nProgram shut down by user")
        in_string = in_string.split(' ') #spliting input to number and base
        in_number = in_string[0]
        in_base = int(in_string[1])
        out_number = None # creating output
        out_base = None

        if in_base == 2: #form binary to decimal
            out_number = 0
            for char , i in zip(list(reversed(in_number)) , range(len(in_number))):
                if int(char) in [0 , 1]: # to avoid non-binaries
                    out_number = out_number + int(char) * (in_base**i)
                    out_base = 10
                else:
                    print ("Invalid binary number!")
                    out_number = None
                    break

        elif in_base == 10: # form decimal to binary
            out_number = []
            out_base = 2
            in_number = int(in_number)
            while in_number > 0:
                digit = in_number % out_base
                out_number.append (str(int(digit)))
                in_number = (in_number - digit) / 2
            out_number = ''.join(list(reversed(out_number)))

        else: # when second part of input is neither 2 nor 10
            print ("Numeral system base should be 2 or 10!")

        if out_number != None and out_base != None: # printing result only when is correct
            out_number = str(out_number)
            out_base = str(out_base)
            print ("/-" + ("-" * len(out_number)) + "---" + ("-" * len(out_base)) + "-\ ")
            print ("| " + out_number + " | " + out_base + " |")
            print ("\-" + ("-" * len(out_number)) + "---" + ("-" * len(out_base)) + "-/ ")

    #error handling. Only KI and EOFE shut down program.
    except (ValueError, IndexError, NameError):
        print ("Invalid input!")
    except (OverflowError):
        print ("Number is too big")
    except (KeyboardInterrupt, EOFError):
        sys.exit("\nProgram shut down by user")
