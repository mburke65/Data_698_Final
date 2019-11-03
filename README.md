# Data_698_Final

Justin Herman
Meaghan Burke
Vikas Sinha
Joseph Garcia 

## Detecing Media Bias in the 2020 Democratic Primary Cycle

This repository contains the accompanying scripts to our capstone project. all writeups are contained in the [Literature Review](https://github.com/mburke65/Data_698_Final/tree/master/Literature_Review), [Meeting_Notes](https://github.com/mburke65/Data_698_Final/tree/master/Meeting_Notes), [Paper](https://github.com/mburke65/Data_698_Final/tree/master/Paper), and [Proposal](https://github.com/mburke65/Data_698_Final/tree/master/Proposal) folders.  These folders contain individual contributions, for the final writeup please see [Rough draft ](http://google.comhttps://github.com/mburke65/Data_698_Final/blob/master/Paper/FinalPaper_vks.docx)

## Executable scripts

The scrapers folder contains the scraping scripts we created to automate the API request process.  These scripts require storing API keys in a config file for execution. There are several versions floating around inside the scraper folder as we attempted to split up some of the scraping requests to stay within query request limits.  The results from the API requests are stored as csv's in the [data_csvs folder](https://github.com/mburke65/Data_698_Final/tree/master/data_csvs). The [original scraper](Develop_automated_news_aggregator.ipynb) lives in the main folder and has explanations for the code.    

The next step was to develop a script to aggregate all the csv results, this was done in the [experimenting_with_data script](https://github.com/mburke65/Data_698_Final/blob/master/expermineting_with_data.ipynb),  The final product for this script is an aggregated csv file called [Vikas.csv](https://github.com/mburke65/Data_698_Final/tree/master/code).  This file lives in the code folder alongside our scripts which develop a [sentiment model](https://github.com/mburke65/Data_698_Final/blob/master/code/s1_analysis.py). The final step in the project is to feed the model from the s_1_analysis script into a script which applies the model to our dataset.  This is done in this [folder](https://github.com/mburke65/Data_698_Final/blob/master/code/naive_sent_analysis.ipynb).   


