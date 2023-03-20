# ---WIP--- 


Simple script for vmaf plotting.
Initial code from https://github.com/master-of-zen/Plot_Vmaf
Further code from https://github.com/PhilippeR/Pra_Plot_Vmaf
To be used with https://github.com/gdavila/easyVmaf

This version improves on :

- Being agnostic for the destinctive field for 4k and hd in the EasyVmaf output.
- Introducing .99 percentile in the histogram
- Creating a 5 point grid on the plots, being in line with the JND of 5 points with VMAF measures


## Usage
```bash
python plot_vmaf.py [-h] [-o OUTPUT] [-p] vmaf_file1 vmaf_file2 ..... vmaf_fileX 
```

## Example
```bash
python plot_vmaf.py vmaf.json -o plot.svg
```

## Options
```
-o --output ["file"] name and format of the temporal VMAF graph (default plot.png)
-p  generate percentile graph 
```

## Requirements
Python 3
Matplotlib
Numpy

## References 
##### About Harmonic Mean
According Zhi Li (https://netflixtechblog.com/vmaf-the-journey-continues-44b51ee9ed12) and Jan Ozer (https://streaminglearningcenter.com/blogs/compute-vmaf-using-ffmpeg-on-windows.html) , harmonic mean makes more sense than arithmetic mean.

##### About percentile
https://blog.twitter.com/engineering/en_us/topics/infrastructure/2020/introducing-vmaf-percentiles-for-video-quality-measurements
