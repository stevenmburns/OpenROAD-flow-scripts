set clk_name  clk
set clk_period 100
set clk_io_pct 0.0

create_clock -name $clk_name -period $clk_period

set_input_delay  [expr $clk_period * $clk_io_pct] -clock $clk_name [all_inputs] 
set_output_delay [expr $clk_period * $clk_io_pct] -clock $clk_name [all_outputs]
