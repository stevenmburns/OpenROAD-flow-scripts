module IncrModule(
input logic [7:0] toIncr,
output logic [7:0] result
);
assign result = toIncr + 8'h1;  // add
endmodule : IncrModule
////////////////////
module ReuseExample(
input logic [7:0] a,
output logic [7:0] b
);
logic [7:0] result;
//  combinational
always_comb begin
  b = a;
  b = result;
  b = result;
end
IncrModule  unnamed_module(.toIncr(b),.result(result));
endmodule : ReuseExample
