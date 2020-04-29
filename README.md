# PandS_Project

## Programming and Scripting Problem Sheet 2020

- Introduction
- Technologies
- How to Use
- Research 
- Methodology
- Analysis 
- Improvements
- Conclusion 
- References (Course Video)

## Introduction

This repository contains my attempt at the final project for the Programming & Scripting module year 2020. The project was broken down into smaller programs which are all included in the repository, along with their logfile that demosntrate how they were developed 

The objective of this project was to research the Iris data set and use python to perform analysis of it. We were to complie a program in python and present our reseach, methodology and findings. The project should be conducted in stages and we should discuss the work done at each stage.

The program was required to perform a few tasks:
1. Output a summary of the variables to a single text file
2. Save a histogram of each variable to .png
3. Output a scatter plot of each variable

## Technologies

Here I will detail the different programs, languages and libraries used through the project

### Visual Studio Code 

This was the text editor I used through the project.

### Terminal 

As I operate on a MAC, Terminal was the command line interface I used 

### Python

Python was the language used to compile the program and the version was 3.7.4

### Ipython 

I used Ipython to test lines of code before incorporating them into the main programs. Ipython was extremely useful for trail and error and I made use of %logstart to track my work 

### Matplotlib

### Pandas 

### Seaborn

## How to Use 

To run this programs, you will first need to ensure you can access the Command Line Interface on your device. Then you should:
- Download the file "Analysis.py" to your machine.
- Go to the Command Line Interface on your machine 
- Use 'cd' to navigating to the folder that contains "Analysis.py".
- Run the program by typing "python Analysis.py" to the Command Line Interface and hitting enter.

## Research 

## Methodology

After research, I began work on the program itself. I decided to break the program into separate, more mangable programs and once they were working, I would merging them together into one project. 

### Reading in the Data Set 

The fist step I needed to take was to find a suitable data set to work with. I chose to go with a CSV file instead of JSON or Txt as it would make it easier to differentiate the variables. I found a reliable file on Kaggle; (https://www.kaggle.com/arshid/iris-flower-dataset). I went with this as it was a "Tidy" data set. A "Tidy" data set is defined as a data set arranged such that each varaialbe is a column and each observtion is a row.

Reading in the file was stragiht forward, I used the Pandas .read function

### Summary 

The first aspect of the program I decided to tackle was outputing a summary of the variables of the data set to a text file. The individual file for this aspect of the program can be found in the repository named "summary,py" and "summary_log.py" is the relevant log file.

Using Pandas describe() function, it was relatively similar to generate the summary. What was difficult was outputting this summary to a text file. After some trial and error, I realised I should pass the summary to a variable and then output that variable to the text file. At first this wouldnt work either until i realised the variable needed to be a string. 

Another apsect I struggled with was trying to nicely format the summary in the text. Unfortunatly, I was able to find out how to format text when writing to a file. 

### Histogram

The next aspect of the program I undertook was saving a histogram of each variable to .png. The individual file for this aspect of the program can be found in the repository named "hist.py" and "hist_log.py" & "hist_improve_log.py" are the relevant log files.

Generating these histograms proved to be the most difficult and time consuming single aspect of the program. 

### Scatter Plot

Simple

I wanted to output just scatter plots ( without the histograms that are included) as I had already created histograms, but couldn't find a sutable plot type in the seaborn documentation. 

### Joining everything together 

## Conclusion

I spent too much time on reasearch and investigate way beyond the scope of this module. 

I relied on Ipython for trail and error and worked a lot locally before uploading my first. Due to this my commit history is qutie recent and appears as though i have not been working consistently 
