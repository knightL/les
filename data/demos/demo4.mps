NAME          DEMO3
ROWS
 N  OBJECTIVE
 L  C1
 L  C2
 L  C3
COLUMNS
    X1      OBJECTIVE          1
    X2      OBJECTIVE          1
    X3      OBJECTIVE          1
    X4      OBJECTIVE          1
    X1      C1                 1
    X2      C1                 1   C2                 1
    X3      C2                 1   C3                 1
    X4      C3                 1
RHS
    RHS1    C1                 1   C2                 1
    RHS1    C3                 1 
BOUNDS
 UP BND1    X1                 1
 LO BND1    X1                 0
 UP BND1    X2                 1
 LO BND1    X2                 0
 UP BND1    X3                 1
 LO BND1    X3                 0
 UP BND1    X4                 1
 LO BND1    X4                 0
ENDATA
