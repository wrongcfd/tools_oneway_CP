# tools_oneway_CP

# **1. Generate coordinates needed in OF**

 **step1**. `hill2D.py`: generate hill coords file.

 **step2**. `scriptfor_OF_onestep.py` : read hill coords file from hill2D.py, then generate file coords for in sampleDictCoord OF_bottom. 
note: hill_extended.pc is used to double-check the coords.

 **step3**. Copy sampleDictCoord OF_bottom to sampleDict and run OpenFOAM. Then copy the postprocessing files to the ReverseOF.py folder.
 
 # **2. Convert OF results to GASCANS**
 
**step1**. `ReverseOF.py`: generate files for LBM
 
 
