export PLATFORM               = intel16

export DESIGN_NICKNAME        = full_adder
export DESIGN_NAME            = full_adder

export VERILOG_FILES         = $(sort $(wildcard ./designs/src/$(DESIGN_NICKNAME)/*.v))
export SDC_FILE              = ./designs/$(PLATFORM)/$(DESIGN_NICKNAME)/constraint.sdc

# x=0.108 y=0.63
export DIE_AREA    = 0 0 21.60 12.6
export CORE_AREA    = 0 0 21.60 12.6

export PLACE_DENSITY_LB_ADDON  = 0.20

export ENABLE_DPO = 0
