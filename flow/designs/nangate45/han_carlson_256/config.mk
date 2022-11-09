export DESIGN_NICKNAME = han_carlson_256
export DESIGN_NAME = Adder
export PLATFORM    = nangate45

export VERILOG_FILES = ./designs/src/$(DESIGN_NICKNAME)/Adder.sv
export SDC_FILE      = ./designs/$(PLATFORM)/$(DESIGN_NICKNAME)/constraint.sdc

# These values must be multiples of placement site
# x=0.19 y=1.4
export DIE_AREA    = 0 0 190 70
export CORE_AREA   = 9.5 11.2 180.5 58.8
export PLACE_PINS_ARGS = -exclude left:* -exclude right:*

export PLACE_DENSITY_LB_ADDON = 0.20
