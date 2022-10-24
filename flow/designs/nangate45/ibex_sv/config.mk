export DESIGN_NICKNAME = ibex_sv
export DESIGN_NAME = ibex_core
export PLATFORM    = nangate45

export USE_SURELOG = 1
export VERILOG_INCLUDE_DIRS = ./designs/src/$(DESIGN_NICKNAME)/prim ./designs/src/$(DESIGN_NICKNAME)/dv_utils
export VERILOG_FILES = ./designs/src/$(DESIGN_NICKNAME)/ibex_pkg.sv \
./designs/src/$(DESIGN_NICKNAME)/ibex_alu.sv \
./designs/src/$(DESIGN_NICKNAME)/ibex_compressed_decoder.sv \
./designs/src/$(DESIGN_NICKNAME)/ibex_controller.sv \
./designs/src/$(DESIGN_NICKNAME)/ibex_counter.sv \
./designs/src/$(DESIGN_NICKNAME)/ibex_cs_registers.sv \
./designs/src/$(DESIGN_NICKNAME)/ibex_decoder.sv \
./designs/src/$(DESIGN_NICKNAME)/ibex_ex_block.sv \
./designs/src/$(DESIGN_NICKNAME)/ibex_id_stage.sv \
./designs/src/$(DESIGN_NICKNAME)/ibex_if_stage.sv \
./designs/src/$(DESIGN_NICKNAME)/ibex_load_store_unit.sv \
./designs/src/$(DESIGN_NICKNAME)/ibex_multdiv_slow.sv \
./designs/src/$(DESIGN_NICKNAME)/ibex_multdiv_fast.sv \
./designs/src/$(DESIGN_NICKNAME)/ibex_prefetch_buffer.sv \
./designs/src/$(DESIGN_NICKNAME)/ibex_fetch_fifo.sv \
./designs/src/$(DESIGN_NICKNAME)/ibex_register_file_ff.sv \
./designs/src/$(DESIGN_NICKNAME)/ibex_core.sv 

export SDC_FILE      = ./designs/$(PLATFORM)/$(DESIGN_NICKNAME)/constraint.sdc

# These values must be multiples of placement site
# x=0.19 y=1.4
export DIE_AREA    = 0 0 300.01 299.6 
export CORE_AREA   = 10.07 11.2 289.94 289.8 

export PLACE_DENSITY_LB_ADDON = 0.20
