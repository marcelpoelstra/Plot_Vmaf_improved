#!/usr/bin/env python3

#import sys
import argparse 
import os
import numpy as np
import matplotlib.pyplot as plt
import json
from math import log10
from statistics import mean, harmonic_mean
from os.path import basename



def read_json(file):
    with open(file, 'r') as f:
        fl = json.load(f)
        return fl


def plot_percentile_vmaf(vmafs,vmaf_file_names):
    plt.figure(2)
    fig, ax = plt.subplots()
    
    # Create datapoints
    i=0
    x = [1,5,25,50,75,99]
    ymin=100
    
    # Calculate required plot height based on the number of VMAF files
    plot_height = 5 + len(vmafs) * 0.5
    fig.set_size_inches(6, plot_height)
    
    for vmaf in vmafs:
        perc_1 = round(np.percentile(vmaf, 1), 2)
        perc_5 = round(np.percentile(vmaf, 5), 2)
        perc_25 = round(np.percentile(vmaf, 25), 2)
# create .50 percentile
        perc_50 = round(np.percentile(vmaf, 50), 2)
        perc_75 = round(np.percentile(vmaf, 75), 2)
# create .99 percentile
        perc_99 = round(np.percentile(vmaf, 99), 2)
        if ymin>perc_1:
            ymin=perc_1
        hmean=round(harmonic_mean(vmaf),2)
        amean=round(mean(vmaf),2)    
        y=[perc_1,perc_5,perc_25,perc_50,perc_75,perc_99]
        plotName=basename(vmaf_file_names[i])
        plt.plot(x, y,'-*', label=f'File: {plotName}\n'
                                f'Mean: {amean} - HMean:{hmean}\n'  
                                f'1%: {perc_1} 5%: {perc_5} 25%: {perc_25}  50%: {perc_50} 75%: {perc_75} 99%: {perc_99}', linewidth=0.7)
        i=i+1
    
    # make x-axis 10 points
    ax.set_xticks(np.arange(0, 100, 5))
    ax.set_xticklabels(np.arange(0, 100, 5))
    #ax.set_xlabel('PERCENTILE')
    ax.set_ylim([ymin,100])
    ax.set_ylabel('VMAF')
    ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True, shadow=True, fontsize='x-small')
    ax.grid(True)    
    plt.tight_layout()
    plt.margins(0)

    # Save
    fileName, fileExtension = os.path.splitext(args.output)
    plt.savefig(fileName+"_histo"+fileExtension, dpi=500)

def plot_multi_vmaf(vmafs, vmaf_file_names):
    plt.figure(1)

    # Create datapoints
    i = 0
    ymin = 100

    # Initialize the lists inside the function
    ameans = []
    hmeans = []

    # Move the for loop and if statement inside the function
    for f in args.vmaf_file:
        jsn = read_json(f)

        # Fetch mean and harmonic mean from JSON file
        pooled_metrics = jsn.get('pooled_metrics', {})
        if 'vmaf_hd' in pooled_metrics:
            ameans.append(pooled_metrics['vmaf_hd']['mean'])
            hmeans.append(pooled_metrics['vmaf_hd']['harmonic_mean'])
        elif 'vmaf_4k' in pooled_metrics:
            ameans.append(pooled_metrics['vmaf_4k']['mean'])
            hmeans.append(pooled_metrics['vmaf_4k']['harmonic_mean'])
        else:
            raise ValueError(f"Neither 'vmaf_hd' nor 'vmaf_4k' found in pooled_metrics for file {f}")

    for vmaf in vmafs:
        x = [x for x in range(len(vmaf))]
        plot_size = len(vmaf)

        # Use mean and harmonic mean values from JSON file
        hmean = round(hmeans[i], 2)
        amean = round(ameans[i], 2)



        perc_1 = round(np.percentile(vmaf, 1), 3)
        perc_25 = round(np.percentile(vmaf, 25), 3)
# add .50 percentile
        perc_50 = round(np.percentile(vmaf, 50), 3)
        perc_75 = round(np.percentile(vmaf, 75), 3)
# add .99 percentile
        perc_99 = round(np.percentile(vmaf, 99), 3)
        if ymin > perc_1:
            ymin = perc_1
        plotName = basename(vmaf_file_names[i])
        plt.plot(x, vmaf, label=f'File: {plotName}\n'
                                f'Frames: {len(vmaf)} Mean:{amean} - Harmonic Mean:{hmean}\n'
                                f'1%: {perc_1}  25%: {perc_25}  50%: {perc_50}, 75%: {perc_75}, 99%: {perc_99}', linewidth=0.7)
        plt.plot([1, plot_size], [amean, amean], ':')
        plt.annotate(f'Mean: {amean}', xy=(0, amean))
        i = i + 1

    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.1), fancybox=True, shadow=True, fontsize='x-small')
    #plt.xlabel('FRAMES')
    # make Y axis 10 points grid
    plt.yticks(np.arange(0, 100, 5))
    plt.ylim(int(ymin), 100)
    plt.tight_layout()
    plt.margins(0)

    # Save
    plt.savefig(args.output, dpi=500)

def plot_vmaf(vmafs):
    # Create datapoints
    x = [x for x in range(len(vmafs))]
    mean = round(sum(vmafs) / len(vmafs), 3)
    plot_size = len(vmafs)
    perc_1 = round(np.percentile(vmafs, 1), 3)
    perc_25 = round(np.percentile(vmafs, 25), 3)
    perc_50 = round(np.percentile(vmafs, 50), 3)
    perc_75 = round(np.percentile(vmafs, 75), 3)
    perc_99 = round(np.percentile(vmafs, 99), 3)

    # Plot
    figure_width = 3 + round((4 * log10(plot_size)))
    plt.figure(figsize=(figure_width, 5))
    # create x axis 10 points grid
    [plt.axhline(i, color='grey', linewidth=0.4) for i in range(0, 100, 5)]
    [plt.axhline(i, color='black', linewidth=0.6) for i in range(0, 100, 10)]
    plt.plot(x, vmafs, label=f'Frames: {len(vmafs)} Mean:{mean}\n'
                                f'1%: {perc_1}  25%: {perc_25}  75%: {perc_75} 99%: {perc_99}', linewidth=0.7)

    plt.plot([1, plot_size], [perc_1, perc_1], '-', color='red')
    plt.annotate(f'1%: {perc_1}', xy=(0, perc_1), color='red')

    plt.plot([1, plot_size], [perc_25, perc_25], ':', color='orange')
    plt.annotate(f'25%: {perc_25}', xy=(0, perc_25), color='orange')

    plt.plot([1, plot_size], [perc_75, perc_75], ':', color='blue')
# add .50 and .99 percentile
    plt.annotate(f'75%: {perc_75}', xy=(0, perc_75), color='blue')
# add .50 and .99 percentile 
    plt.plot([1, plot_size], [perc_99, perc_99], ':', color='green')
    plt.annotate(f'99%: {perc_99}', xy=(0, perc_99), color='green')

    plt.plot([1, plot_size], [mean, mean], ':', color='black')
    plt.annotate(f'Mean: {mean}', xy=(0, mean), color='black')
    plt.ylabel('VMAF')
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05), fancybox=True, shadow=True)
    plt.ylim(int(perc_1), 100)
    plt.tight_layout()
    plt.margins(0)

    # Save
    plt.savefig(args.output, dpi=500)

def main():
    vmafs = []
    vmaf_file_names = []
    for f in args.vmaf_file:
        jsn = read_json(f)
        temp_vmafs = []
# be agnostic for different hd and 4k fields
        for x in jsn['frames']:
            if 'vmaf_hd' in x['metrics']:
                temp_vmafs.append(x['metrics']['vmaf_hd'])
            elif 'vmaf_4k' in x['metrics']:
                temp_vmafs.append(x['metrics']['vmaf_4k'])
            else:
                raise ValueError(f"Neither 'vmaf_hd' nor 'vmaf_4k' found in metrics for file {f}")
        vmafs.append(temp_vmafs)
        vmaf_file_names.append(f)

    if len(vmafs) == 1:
        plot_vmaf(vmafs[0])
    else:
        plot_multi_vmaf(vmafs, vmaf_file_names)

    if args.percent:
        plot_percentile_vmaf(vmafs, vmaf_file_names)

def parse_arguments():
    parser = argparse.ArgumentParser(description='Plot vmaf to graph')
    parser.add_argument('vmaf_file', type=str,nargs='+', help='Vmaf log file')
    parser.add_argument('-o','--output', dest='output', type=str, default='./output/plot.png', help='Graph output filename (default plot.png)')
    parser.add_argument('-p','--percent', help='Plot percentile', action='store_true')

    return(parser.parse_args())

if __name__ == "__main__":
    args = parse_arguments()
    main()