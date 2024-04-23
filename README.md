Script for plotting the output of easyVmaf (https://github.com/gdavila/easyVmaf)

Initial code from https://github.com/master-of-zen/Plot_Vmaf

Further code from https://github.com/PhilippeR/Pra_Plot_Vmaf

Requirements:
easyVmaf for doing VMAF measures
ffmpeg for extracting frames
Python3 with numpy, matplotlib, Pillow

This version improves on :

- Being agnostic for the distinctive field for 4k and hd in the EasyVmaf output.
- Using the Mean and Harmonic mean values from the EasyVmaf JSON output instead of recalculating.
- Introducing .50 and .99 percentile in the histogram.
- Creating a a more useful grid on the plots, so it's easier to read the JND of 5 VMAF points.
- Focussing on Harmonic Mean instead of Mean values as indicator in the plots.
- Option to export frames with a VMAF score below the 0.01 percentile as TIFF files.
  NOTE: Please use the TIFF export conciously and with care.  Using this on a large video file can cause a multitude of TIFFs being exported.

## Usage

```bash
python plot_vmaf_improved.py [-h] [-o OUTPUT] [-p] vmaf_file1 vmaf_file2 ..... vmaf_fileX 
```

## Example

```bash
python plot_vmaf_improved.py vmaf.json -o plot.svg
```

## Options

```
-o --output ["file"] name and format of the temporal VMAF graph (default plot.png)
-p  generate percentile graph 
-f  export frames with vmaf below 0.01 percentile to TIFF
```

## References

##### About Harmonic Mean

According Zhi Li (https://netflixtechblog.com/vmaf-the-journey-continues-44b51ee9ed12) and Jan Ozer (https://streaminglearningcenter.com/blogs/compute-vmaf-using-ffmpeg-on-windows.html) , harmonic mean makes more sense than arithmetic mean.

##### About percentile

https://blog.twitter.com/engineering/en_us/topics/infrastructure/2020/introducing-vmaf-percentiles-for-video-quality-measurements
