export DESIGN_NICKNAME = latch_based_reg_file
export DESIGN_NAME = latch_based_reg_file
export PLATFORM    = nangate45



export VERILOG_FILES = ./designs/src/$(DESIGN_NICKNAME)/latch_based_reg_file.v


export SDC_FILE      = ./designs/$(PLATFORM)/$(DESIGN_NICKNAME)/constraint.sdc

# These values must be multiples of placement site
# x=0.19 y=1.4
export DIE_AREA    = 0 0 300.01 299.6 
export CORE_AREA   = 10.07 11.2 289.94 289.8 

export PLACE_DENSITY_LB_ADDON = 0.20
