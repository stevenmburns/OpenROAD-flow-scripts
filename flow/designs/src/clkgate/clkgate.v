
module clkgate(clk, en, inp, out);
   input clk;

   input en;

   input [7:0] inp;

   output [7:0] out;

   reg [7:0]    state;

   wire         en_clk;

   assign out = state;
   OPENROAD_CLKGATE CG0 (.CK(clk), .E(en), .GCK(en_clk));

   always @(posedge en_clk) begin
      state  <= inp;
   end

endmodule   
