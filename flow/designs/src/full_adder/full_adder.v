module and2(
    a,
    b,
    z
);
    input a;
    input b;
    output z;
    wire _0;
    wire _1;
    wire _2;
    assign _0 = a;
    assign _1 = b;
    assign _2 = _0 & _1;
    assign z = _2;
endmodule

module xor2(
    a,
    b,
    z
);
    input a;
    input b;
    output z;
    wire _0;
    wire _1;
    wire _2;
    wire _3;
    wire _4;
    wire _5;
    wire _6;
    assign _0 = a;
    assign _1 = b;
    assign _2 = !_1;
    assign _3 = _0 & _2;
    assign _4 = !_0;
    assign _5 = _4 & _1;
    assign _6 = _3 | _5;
    assign z = _6;
endmodule

module or2(
    a,
    b,
    z
);
    input a;
    input b;
    output z;
    wire _0;
    wire _1;
    wire _2;
    assign _0 = a;
    assign _1 = b;
    assign _2 = _0 | _1;
    assign z = _2;
endmodule

module half_adder(
    a,
    b,
    s,
    co
);
    input a;
    input b;
    output s;
    output co;
    wire _0;
    wire _1;
    wire _5;
    wire _9;
    assign _0 = a;
    assign _1 = b;
    assign s = _5;
    assign co = _9;
    xor2 u0 (
        .a(_0),
        .b(_1),
        .z(_5)
    );
    and2 u1 (
        .a(_0),
        .b(_1),
        .z(_9)
    );
endmodule

module full_adder(
    a,
    b,
    c,
    s,
    co
);
    input a;
    input b;
    input c;
    output s;
    output co;
    wire _0;
    wire _1;
    wire _2;
    wire _6;
    wire _7;
    wire _11;
    wire _12;
    wire _16;
    assign _0 = a;
    assign _1 = b;
    assign _2 = c;
    assign s = _11;
    assign co = _16;
    half_adder ha0 (
        .a(_0),
        .b(_1),
        .s(_6),
        .co(_7)
    );
    half_adder ha1 (
        .a(_6),
        .b(_2),
        .s(_11),
        .co(_12)
    );
    or2 o (
        .a(_7),
        .b(_12),
        .z(_16)
    );
endmodule

