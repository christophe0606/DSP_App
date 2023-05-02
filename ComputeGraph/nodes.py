from cmsisdsp.cg.scheduler import *
from cmsisdsp.cg.scheduler import GenericNode,GenericSink,GenericSource

##############################
#
# Define new types of Nodes 
#

# Converting a block of F32 samples to Q15
class F32TOQ15(GenericNode):
    def __init__(self,name,ioLength):
        GenericNode.__init__(self,name)
        self.addInput("i",CType(F32),ioLength)
        self.addOutput("o",CType(Q15),ioLength)

    @property
    def typeName(self):
        return "F32TOQ15"

# Converting a block of F32 samples to Q31
class F32TOQ31(GenericNode):
    def __init__(self,name,ioLength):
        GenericNode.__init__(self,name)
        self.addInput("i",CType(F32),ioLength)
        self.addOutput("o",CType(Q31),ioLength)

    @property
    def typeName(self):
        return "F32TOQ31"

# Converting a block of Q15 samples to F32
class Q15TOF32(GenericNode):
    def __init__(self,name,ioLength):
        GenericNode.__init__(self,name)
        self.addInput("i",CType(Q15),ioLength)
        self.addOutput("o",CType(F32),ioLength)

    @property
    def typeName(self):
        return "Q15TOF32"

# Converting a block of Q31 samples to F32
class Q31TOF32(GenericNode):
    def __init__(self,name,ioLength):
        GenericNode.__init__(self,name)
        self.addInput("i",CType(Q31),ioLength)
        self.addOutput("o",CType(F32),ioLength)

    @property
    def typeName(self):
        return "Q31TOF32"

# IIR node
class IIR(GenericNode):
    def __init__(self,name,theType,ioLength):
        GenericNode.__init__(self,name)
        self.addInput("i",theType,ioLength)
        self.addOutput("o",theType,ioLength)

    @property
    def typeName(self):
        return "IIR"

# FIR node
class FIR(GenericNode):
    def __init__(self,name,theType,ioLength):
        GenericNode.__init__(self,name)
        self.addInput("i",theType,ioLength)
        self.addOutput("o",theType,ioLength)

    @property
    def typeName(self):
        return "FIR"

# Output node (interface to timer interrupt)
class DAC(GenericSink):
    def __init__(self,name,inLength,dsp_context_variable="dsp_context"):
        GenericSink.__init__(self,name)
        self.addInput("i",CType(F32),inLength)
        self.addVariableArg(dsp_context_variable)

    @property
    def typeName(self):
        return "DAC"

# Input node (interface to timer interrupt)
class ADC(GenericSource):
    def __init__(self,name,outLength,dsp_context_variable="dsp_context"):
        GenericSource.__init__(self,name)
        self.addOutput("o",CType(F32),outLength)
        self.addVariableArg(dsp_context_variable)


    @property
    def typeName(self):
        return "ADC"

# Decision node : Comparison with a threshold
class Threshold(GenericNode):
    def __init__(self,name,theType,threshold_value=0x3600):
        GenericNode.__init__(self,name)
        self.addInput("i",theType,1)
        self.addOutput("o",theType,1)
        if isinstance(threshold_value, str):
           self.addVariableArg(threshold_value)
        else:
           self.addLiteralArg(threshold_value)


    @property
    def typeName(self):
        return "Threshold"

# Root mean square of a window of samples using
# CMSIS-DSP
class RMS(GenericNode):
    def __init__(self,name,theType,inLength):
        GenericNode.__init__(self,name)
        self.addInput("i",theType,inLength)
        self.addOutput("o",theType,1)

    @property
    def typeName(self):
        return "RMS"

# Interface with uVision logic analyzer (using global
# variable)
class LogicAnalyzer(GenericSink):
    def __init__(self,name,theType,c_global_variable=""):
        GenericSink.__init__(self,name)
        self.addInput("i",theType,1)
        self.addVariableArg("&"+c_global_variable);


    @property
    def typeName(self):
        return "LogicAnalyzer"
