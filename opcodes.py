# test line

class ADDWF:
    # Add WREG and f
    # operands: f, d, a
    # cycles: 1
    # affected status bits: C, DC, Z, OV, N

    cycles = 1

    def __init__(self):
        pass

class ADDWFC:
    # Add WREG and Carry bit to f
    # operands: f, d, a
    # cycles: 1
    # affected status bits: C, DC, Z, OV, N

    cycles = 1

    def __init__(self):
        pass

class ANDWF:
    # AND WREG with f
    # operands: f, d, a
    # cycles: 1
    # affected status bits: Z, N

    cycles = 1

    def __init__(self):
        pass

class CLRF:
    # Clear f
    # operands: f, a
    # cycles: 1
    # affected status bits: Z

    cycles = 1

    def __init__(self):
        pass

class COMF:
    # Complement f
    # operands: f, d, a
    # cycles: 1
    # affected status bits: Z, N

    cycles = 1

    def __init__(self):
        pass

class DECF:
    # Decrement f
    # operands: f, d, a
    # cycles: 1
    # affected status bits: C, DC, Z, OV, N

    cycles = 1

    def __init__(self):
        pass

class INCF:
    # Increment f
    # operands: f, d, a
    # cycles: 1
    # affected status bits: C, DC, Z, OV, N

    cycles = 1

    def __init__(self):
        pass

class IORWF:
    # Inclusive OR WREG with f
    # operands: f, d, a
    # cycles: 1
    # affected status bits: Z, N

    cycles = 1

    def __init__(self):
        pass

class MOVF:
    # Move f to WREG or f
    # operands: f, d, a
    # cycles: 1
    # affected status bits: Z, N

    cycles = 1

    def __init__(self):
        pass

class MOVFF:
    # Move fs (12-bit source)
to fd (12-bit destination)
    # operands: fs, fd
    # cycles: 2
    # affected status bits: None

    cycles = 2

    def __init__(self):
        pass

class MOVFFL:
    # Move fs (14-bit source)
to fd (14-bit destination)
    # operands: fs, fd
    # cycles: 3
    # affected status bits: None

    cycles = 3

    def __init__(self):
        pass

class MOVWF:
    # Move WREG to f
    # operands: f, a
    # cycles: 1
    # affected status bits: None

    cycles = 1

    def __init__(self):
        pass

class MULWF:
    # Multiply WREG with f
    # operands: f, a
    # cycles: 1
    # affected status bits: None

    cycles = 1

    def __init__(self):
        pass

class NEGF:
    # Negate f
    # operands: f, a
    # cycles: 1
    # affected status bits: C, DC, Z, OV, N

    cycles = 1

    def __init__(self):
        pass

class RLCF:
    # Rotate Left f through Carry
    # operands: f, d, a
    # cycles: 1
    # affected status bits: C, Z, N

    cycles = 1

    def __init__(self):
        pass

class RLNCF:
    # Rotate Left f (No Carry)
    # operands: f, d, a
    # cycles: 1
    # affected status bits: Z, N

    cycles = 1

    def __init__(self):
        pass

class RRCF:
    # Rotate Right f through Carry
    # operands: f, d, a
    # cycles: 1
    # affected status bits: C, Z, N

    cycles = 1

    def __init__(self):
        pass

class RRNCF:
    # Rotate Right f (No Carry)
    # operands: f, d, a
    # cycles: 1
    # affected status bits: Z, N

    cycles = 1

    def __init__(self):
        pass

class SETF:
    # Set f
    # operands: f, a
    # cycles: 1
    # affected status bits: None

    cycles = 1

    def __init__(self):
        pass

class SUBFWB:
    # Subtract f from WREG with
Borrow
    # operands: f, d, a
    # cycles: 1
    # affected status bits: C, DC, Z, OV, N

    cycles = 1

    def __init__(self):
        pass

class SUBWF:
    # Subtract WREG from f
    # operands: f, d, a
    # cycles: 1
    # affected status bits: C, DC, Z, OV, N

    cycles = 1

    def __init__(self):
        pass

class SUBWFB:
    # Subtract WREG from f with
Borrow
    # operands: f, d, a
    # cycles: 1
    # affected status bits: C, DC, Z, OV, N

    cycles = 1

    def __init__(self):
        pass

class SWAPF:
    # Swap nibbles in f
    # operands: f, d, a
    # cycles: 1
    # affected status bits: None

    cycles = 1

    def __init__(self):
        pass

class XORWF:
    # Exclusive OR WREG with f
    # operands: f, d, a
    # cycles: 1
    # affected status bits: Z, N

    cycles = 1

    def __init__(self):
        pass

class CPFSEQ:
    # Compare f with WREG, skip
if =
    # operands: f, a
    # cycles: 1 – 4
    # affected status bits: None

    cycles = 1 – 4

    def __init__(self):
        pass

class CPFSGT:
    # Compare f with WREG, skip
if >
    # operands: f, a
    # cycles: 1 – 4
    # affected status bits: None

    cycles = 1 – 4

    def __init__(self):
        pass

class CPFSLT:
    # Compare f with WREG, skip
if <
    # operands: f, a
    # cycles: 1 – 4
    # affected status bits: None

    cycles = 1 – 4

    def __init__(self):
        pass

class DECFSZ:
    # Decrement f, Skip if 0
    # operands: f, d, a
    # cycles: 1 – 4
    # affected status bits: None

    cycles = 1 – 4

    def __init__(self):
        pass

class DCFSNZ:
    # Decrement f, Skip if Not 0
    # operands: f, d, a
    # cycles: 1 – 4
    # affected status bits: None

    cycles = 1 – 4

    def __init__(self):
        pass

class INCFSZ:
    # Increment f, Skip if 0
    # operands: f, d, a
    # cycles: 1 – 4
    # affected status bits: None

    cycles = 1 – 4

    def __init__(self):
        pass

class INFSNZ:
    # Increment f, Skip if Not 0
    # operands: f, d, a
    # cycles: 1 – 4
    # affected status bits: None

    cycles = 1 – 4

    def __init__(self):
        pass

class TSTFSZ:
    # Test f, skip if 0
    # operands: f, a
    # cycles: 1 – 4
    # affected status bits: None

    cycles = 1 – 4

    def __init__(self):
        pass

class BCF:
    # Bit Clear f
    # operands: f, b, a
    # cycles: 1
    # affected status bits: None

    cycles = 1

    def __init__(self):
        pass

class BSF:
    # Bit Set f
    # operands: f, b, a
    # cycles: 1
    # affected status bits: None

    cycles = 1

    def __init__(self):
        pass

class BTG:
    # Bit Toggle f
    # operands: f, b, a
    # cycles: 1
    # affected status bits: None

    cycles = 1

    def __init__(self):
        pass

class BC:
    # Branch if Carry
    # operands: n
    # cycles: 1 – 2
    # affected status bits: None

    cycles = 1 – 2

    def __init__(self):
        pass

class BN:
    # Branch if Negative
    # operands: n
    # cycles: 1 – 2
    # affected status bits: None

    cycles = 1 – 2

    def __init__(self):
        pass

class BNC:
    # Branch if Not Carry
    # operands: n
    # cycles: 1 – 2
    # affected status bits: None

    cycles = 1 – 2

    def __init__(self):
        pass

class BNN:
    # Branch if Not Negative
    # operands: n
    # cycles: 1 – 2
    # affected status bits: None

    cycles = 1 – 2

    def __init__(self):
        pass

class BNOV:
    # Branch if Not Overflow
    # operands: n
    # cycles: 1 – 2
    # affected status bits: None

    cycles = 1 – 2

    def __init__(self):
        pass

class BNZ:
    # Branch if Not Zero
    # operands: n
    # cycles: 1 – 2
    # affected status bits: None

    cycles = 1 – 2

    def __init__(self):
        pass

class BOV:
    # Branch if Overflow
    # operands: n
    # cycles: 1 – 2
    # affected status bits: None

    cycles = 1 – 2

    def __init__(self):
        pass

class BRA:
    # Branch Unconditionally
    # operands: n
    # cycles: 2
    # affected status bits: None

    cycles = 2

    def __init__(self):
        pass

class BZ:
    # Branch if Zero
    # operands: n
    # cycles: 1 – 2
    # affected status bits: None

    cycles = 1 – 2

    def __init__(self):
        pass

class CALL:
    # Call subroutine
    # operands: k, s
    # cycles: 2
    # affected status bits: None

    cycles = 2

    def __init__(self):
        pass

class CALLW:
    # Call subroutine using WREG
    # operands: —
    # cycles: 2
    # affected status bits: None

    cycles = 2

    def __init__(self):
        pass

class GOTO:
    # Go to address
    # operands: k
    # cycles: 2
    # affected status bits: None

    cycles = 2

    def __init__(self):
        pass

class RCALL:
    # Relative Call
    # operands: n
    # cycles: 2
    # affected status bits: None

    cycles = 2

    def __init__(self):
        pass

class RETFIE:
    # Return from interrupt enable
    # operands: s
    # cycles: 2
    # affected status bits: INTCONx STAT bits

    cycles = 2

    def __init__(self):
        pass

class RETLW:
    # Return with literal in WREG
    # operands: k
    # cycles: 2
    # affected status bits: None

    cycles = 2

    def __init__(self):
        pass

class RETURN:
    # Return from Subroutine
    # operands: s
    # cycles: 2
    # affected status bits: None

    cycles = 2

    def __init__(self):
        pass

class DAW:
    # Decimal Adjust WREG
    # operands: —
    # cycles: 1
    # affected status bits: C

    cycles = 1

    def __init__(self):
        pass

class NOP:
    # No Operation
    # operands: —
    # cycles: 1
    # affected status bits: None

    cycles = 1

    def __init__(self):
        pass

class NOP:
    # No Operation
    # operands: —
    # cycles: 1
    # affected status bits: None

    cycles = 1

    def __init__(self):
        pass

class POP:
    # Pop top of return stack
(TOS)
    # operands: —
    # cycles: 1
    # affected status bits: None

    cycles = 1

    def __init__(self):
        pass

class PUSH:
    # Push top of return stack
(TOS)
    # operands: —
    # cycles: 1
    # affected status bits: None

    cycles = 1

    def __init__(self):
        pass

class RESET:
    # Software device Reset
    # operands: —
    # cycles: 1
    # affected status bits: All

    cycles = 1

    def __init__(self):
        pass

class SLEEP:
    # Go into Standby mode
    # operands: —
    # cycles: 1
    # affected status bits: TO, PD

    cycles = 1

    def __init__(self):
        pass

class ADDFSR:
    # Add FSR (fn) with literal (k)
    # operands: fn, k
    # cycles: 1
    # affected status bits: None

    cycles = 1

    def __init__(self):
        pass

class ADDLW:
    # Add literal and WREG
    # operands: k
    # cycles: 1
    # affected status bits: C, DC, Z, OV, N

    cycles = 1

    def __init__(self):
        pass

class ANDLW:
    # AND literal with WREG
    # operands: k
    # cycles: 1
    # affected status bits: Z, N

    cycles = 1

    def __init__(self):
        pass

class IORLW:
    # Inclusive OR literal with
WREG
    # operands: k
    # cycles: 1
    # affected status bits: Z, N

    cycles = 1

    def __init__(self):
        pass

class LFSR:
    # Load FSR(fn) with a 14-bit
literal (k)
    # operands: fn, k
    # cycles: 2
    # affected status bits: None

    cycles = 2

    def __init__(self):
        pass

class MOVLB:
    # Move literal to BSR<5:0>
    # operands: k
    # cycles: 1
    # affected status bits: None

    cycles = 1

    def __init__(self):
        pass

class MOVLW:
    # Move literal to WREG
    # operands: k
    # cycles: 1
    # affected status bits: None

    cycles = 1

    def __init__(self):
        pass

class MULLW:
    # Multiply literal with WREG
    # operands: k
    # cycles: 1
    # affected status bits: None

    cycles = 1

    def __init__(self):
        pass

class RETLW:
    # Return with literal in WREG
    # operands: k
    # cycles: 2
    # affected status bits: None

    cycles = 2

    def __init__(self):
        pass

class SUBFSR:
    # Subtract literal (k) from FSR
(fn)
    # operands: fn, k
    # cycles: 1
    # affected status bits: None

    cycles = 1

    def __init__(self):
        pass

class SUBLW:
    # Subtract WREG from literal
    # operands: k
    # cycles: 1
    # affected status bits: C, DC, Z, OV, N

    cycles = 1

    def __init__(self):
        pass

class TBLRD*:
    # Table Read
    # operands: —
    # cycles: 2
    # affected status bits: None

    cycles = 2

    def __init__(self):
        pass

class TBLRD*+:
    # Table Read with post-
increment
    # operands: —
    # cycles: 2
    # affected status bits: None

    cycles = 2

    def __init__(self):
        pass

class TBLRD*-:
    # Table Read with post-
decrement
    # operands: —
    # cycles: 2
    # affected status bits: None

    cycles = 2

    def __init__(self):
        pass

class TBLRD+*:
    # Table Read with pre-
increment
    # operands: —
    # cycles: 2
    # affected status bits: None

    cycles = 2

    def __init__(self):
        pass

class TBLWT*:
    # Table Write
    # operands: —
    # cycles: 2
    # affected status bits: None

    cycles = 2

    def __init__(self):
        pass

class TBLWT*+:
    # Table Write with post-
increment
    # operands: —
    # cycles: 2
    # affected status bits: None

    cycles = 2

    def __init__(self):
        pass

class TBLWT*-:
    # Table Write with post-
decrement
    # operands: —
    # cycles: 2
    # affected status bits: None

    cycles = 2

    def __init__(self):
        pass

class TBLWT+*:
    # Table Write with pre-
increment
    # operands: —
    # cycles: 2
    # affected status bits: None

    cycles = 2

    def __init__(self):
        pass
