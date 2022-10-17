module active_lo_latch(clk, d, q);
   input clk;
   input d;
   output q;
   reg    q;
   always @(clk or d)
      if (!clk)
        q <= d;
endmodule      

module active_hi_latch(clk, d, q);
   input clk;
   input d;
   output q;
   reg    q;
   always @(clk or d)
      if (clk)
        q <= d;
endmodule      


module latch_based_reg_file(clk, wdata, we, waddr, raddr, rdata);
   input clk;
   input       we;

   input [2:0] wdata;
   input [0:0] waddr;
   input [0:0] raddr;
   output [2:0] rdata;
   reg [2:0] rdata;
   wire   [2:0] latched_wdata;
   
   wire raw_en_clk_0;
   wire raw_en_clk_1;

   wire en_clk_0;
   wire en_clk_1;
  
   wire [2:0]   state_0;
   wire [2:0]   state_1;


   assign raw_en_clk_0 = we & (waddr == 1'b0);
   assign raw_en_clk_1 = we & (waddr == 1'b1);

   active_lo_latch L_0 (.clk(clk), .d(wdata[0]), .q(latched_wdata[0]));
   active_lo_latch L_1 (.clk(clk), .d(wdata[1]), .q(latched_wdata[1]));
   active_lo_latch L_2 (.clk(clk), .d(wdata[2]), .q(latched_wdata[2]));

   OPENROAD_CLKGATE CG_0 (.CK(clk), .E(raw_en_clk_0), .GCK(en_clk_0));
   OPENROAD_CLKGATE CG_1 (.CK(clk), .E(raw_en_clk_1), .GCK(en_clk_1));

   active_hi_latch D_0_0 (.clk(en_clk_0), .d(latched_wdata[0]), .q(state_0[0]));
   active_hi_latch D_0_1 (.clk(en_clk_0), .d(latched_wdata[1]), .q(state_0[1]));
   active_hi_latch D_0_2 (.clk(en_clk_0), .d(latched_wdata[2]), .q(state_0[2]));

   active_hi_latch D_1_0 (.clk(en_clk_1), .d(latched_wdata[0]), .q(state_1[0]));
   active_hi_latch D_1_1 (.clk(en_clk_1), .d(latched_wdata[1]), .q(state_1[1]));
   active_hi_latch D_1_2 (.clk(en_clk_1), .d(latched_wdata[2]), .q(state_1[2]));

   always_comb begin
      rdata = 3'bx;
      if (raddr == 1'b0) begin
         rdata = state_0;
      end else if (raddr == 1'b1) begin
         rdata = state_1;
      end
   end

endmodule
