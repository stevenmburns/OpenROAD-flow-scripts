export DESIGN_NICKNAME = popcount
export DESIGN_NAME = popcount
export PLATFORM    = intel16

# Enable SystemVerilog frontend
export USE_SURELOG = 1
export VERILOG_INCLUDE_DIRS = ./designs/src/$(DESIGN_NICKNAME)/bsg_misc
export VERILOG_FILES = ./designs/src/$(DESIGN_NICKNAME)/popcount.v \
./designs/src/$(DESIGN_NICKNAME)/bsg_misc/bsg_popcount.v

export SDC_FILE      = ./designs/$(PLATFORM)/$(DESIGN_NICKNAME)/constraint.sdc

export CORE_UTILIZATION       =  20
export CORE_ASPECT_RATIO      = 1
export CORE_MARGIN            = 2
export PLACE_DENSITY_LB_ADDON  = 0.20

export ENABLE_DPO = 0
