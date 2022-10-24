export DESIGN_NICKNAME = popcount
export DESIGN_NAME = popcount
export PLATFORM    = nangate45

export USE_SURELOG = 1
export VERILOG_INCLUDE_DIRS = ./designs/src/$(DESIGN_NICKNAME)/bsg_misc
export VERILOG_FILES = ./designs/src/$(DESIGN_NICKNAME)/popcount.v \
./designs/src/$(DESIGN_NICKNAME)/bsg_misc/bsg_popcount.v

export SDC_FILE      = ./designs/$(PLATFORM)/$(DESIGN_NICKNAME)/constraint.sdc

# These values must be multiples of placement site
# x=0.19 y=1.4
export DIE_AREA    = 0 0 300.01 299.6 
export CORE_AREA   = 10.07 11.2 289.94 289.8 

export PLACE_DENSITY_LB_ADDON = 0.20
