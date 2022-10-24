export DESIGN_NAME = ReuseExample
export DESIGN_NICKNAME = rohd_ex
export PLATFORM    = nangate45

export USE_SURELOG = 1
export VERILOG_FILES = ./designs/src/$(DESIGN_NICKNAME)/ReuseExample.v
export SDC_FILE      = ./designs/$(PLATFORM)/$(DESIGN_NICKNAME)/constraint.sdc
export ABC_AREA      = 1

# These values must be multiples of placement site
# x=0.19 y=1.4
export DIE_AREA    = 0 0 70.11 70 
export CORE_AREA   = 10.07 11.2 60.04 60.2 

export PLACE_DENSITY_LB_ADDON = 0.20
