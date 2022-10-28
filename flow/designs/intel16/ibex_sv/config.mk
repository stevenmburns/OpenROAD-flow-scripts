export DESIGN_NICKNAME        = ibex_sv
export DESIGN_NAME            = ibex_core
export PLATFORM               = intel16

export USE_SURELOG = 1
export VERILOG_INCLUDE_DIRS = ./designs/src/$(DESIGN_NICKNAME) ./designs/src/$(DESIGN_NICKNAME)/prim ./designs/src/$(DESIGN_NICKNAME)/dv_utils
export VERILOG_FILES = \
./designs/src/ibex_sv/prim/prim_flop_macros.sv \
./designs/src/ibex_sv/ibex_pkg.sv \
./designs/src/ibex_sv/ibex_pmp.sv \
./designs/src/ibex_sv/ibex_register_file_ff.sv \
./designs/src/ibex_sv/ibex_alu.sv \
./designs/src/ibex_sv/ibex_branch_predict.sv \
./designs/src/ibex_sv/ibex_compressed_decoder.sv \
./designs/src/ibex_sv/ibex_controller.sv \
./designs/src/ibex_sv/ibex_counter.sv \
./designs/src/ibex_sv/ibex_csr.sv \
./designs/src/ibex_sv/ibex_cs_registers.sv \
./designs/src/ibex_sv/ibex_decoder.sv \
./designs/src/ibex_sv/ibex_ex_block.sv \
./designs/src/ibex_sv/ibex_fetch_fifo.sv \
./designs/src/ibex_sv/ibex_icache.sv \
./designs/src/ibex_sv/ibex_id_stage.sv \
./designs/src/ibex_sv/ibex_if_stage.sv \
./designs/src/ibex_sv/ibex_load_store_unit.sv \
./designs/src/ibex_sv/ibex_multdiv_fast.sv \
./designs/src/ibex_sv/ibex_multdiv_slow.sv \
./designs/src/ibex_sv/ibex_prefetch_buffer.sv \
./designs/src/ibex_sv/ibex_wb_stage.sv \
./designs/src/ibex_sv/ibex_core.sv


export SDC_FILE      = ./designs/$(PLATFORM)/$(DESIGN_NICKNAME)/constraint.sdc

export CORE_UTILIZATION       = 28 
export CORE_ASPECT_RATIO      = 1
export CORE_MARGIN            = 2
export PLACE_DENSITY_LB_ADDON  = 0.20

export ENABLE_DPO = 0
