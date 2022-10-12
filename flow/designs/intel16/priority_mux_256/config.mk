export PLATFORM               = intel16

export DESIGN_NICKNAME        = priority_mux_256
export DESIGN_NAME            = priority_mux

export VERILOG_FILES         = $(sort $(wildcard ./designs/src/$(DESIGN_NICKNAME)/*.v))
export SDC_FILE              = ./designs/$(PLATFORM)/$(DESIGN_NICKNAME)/constraint.sdc

export CORE_UTILIZATION       =  20
export CORE_ASPECT_RATIO      = 10
export CORE_MARGIN            = 2
export PLACE_DENSITY_LB_ADDON  = 0.20

export ENABLE_DPO = 0
