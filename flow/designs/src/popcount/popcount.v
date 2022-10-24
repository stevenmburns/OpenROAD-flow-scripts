module popcount(input [1023:0] i, output [10:0] o);
   bsg_popcount #(.width_p(1024)) u (.i(i), .o(o));
endmodule		 
