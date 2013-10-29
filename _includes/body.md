﻿In current biomedical research, fluorescence correlation spectroscopy (FCS) is  applied
to characterize molecular dynamic processes in vitro and in living cells.  Commercial
FCS setups only permit data analysis that is limited to  a specific instrument by
the use of in-house file formats or a  finite number of implemented correlation
model functions. PyCorrFit is a general-purpose FCS evaluation software that,
amongst other formats, supports the established Zeiss ConfoCor3 ~.fcs  file format.
PyCorrFit comes with several built-in model functions, covering a wide range of
applications in standard confocal FCS. In addition, it contains equations dealing
with different excitation geometries like total internal reflection (TIR). For more
information, visit the official homepage at

[http://pycorrfit.craban.de](http://pycorrfit.craban.de).


#### Supported Operating Systems:
- Windows XP/7 (binary and source code)  
- Ubuntu Linux 12.04 (binary and source code) 
- MacOSx 10.6+ (binary and source code) 
- Any other system with a Python 2.7 installation (source code only) 

#### Supported Filetypes:
- ALV-6000 correlator files (.ALV) (single and multiple runs / tested in autocorrelation mode) 
- Confocor3 files (.fcs)
- Correlator.com (.SIN): Those are files usually created by e.g. Flex02-01D correlators.
- PyCorrFit (.csv): This is a simple .csv file format.        

#### Fitting:
- Least squares fit using the Levenberg-Marquard algorithm
- Weighted fitting with standard deviation
- Parameter error estimation 
- Large set of pre-defined model functions 
- Import of user-defined model functions 

#### Tools and Features:
- Averaging of curves
- Background correction
- Batch processing
- Curve selection
- Global fitting (shared parameters)
- Parameter simulation
- Session management

#### Verbosity:
- Includes python shell access
- Documented and structured source code
- Information window shows all parameters of a measurement
- Update helper checks for new program version

#### Screenshots:


<table>

    <tr>
      <td  valign="top">Desktop</td>
      <td>[
        ![](./images/Screenshot_Desktop.png) ](./images/Screenshot_Desktop.png)</td>
    </tr>

    <tr>
      <td  valign="top">Main 
 window</td>
      <td>[
          ![](./images/Screenshot_Main.png) ](./images/Screenshot_Main.png)</td>
    </tr>

    <tr>
      <td  valign="top">Background 
correction</td>
      <td>[
          ![](./images/Screenshot_Background_correction.png) ](./images/Screenshot_Background_correction.png)</td>
    </tr>

    <tr>
      <td  valign="top">Graphics 
 output 
 (matplotlib)</td>
      <td>[
          ![](./images/Screenshot_Graphics_output.png) ](./images/Screenshot_Graphics_output.png)</td>
    </tr>

    <tr>
      <td  valign="top">Curve 
 selection</td>
      <td>[
          ![](./images/Screenshot_Select_curves.png) ](./images/Screenshot_Select_curves.png)</td>
    </tr>

    <tr>
      <td  valign="top">Trace 
 view</td>
      <td>[
          ![](./images/Screenshot_Trace_view.png) ](./images/Screenshot_Trace_view.png)</td>
    </tr>

</table>