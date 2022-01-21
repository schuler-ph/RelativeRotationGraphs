# RelativeRotationGraphs
## Disclaimer
RRG Research is the company that holds the intellectual property, copyrights© and the international Registered TradeMark® for Relative Rotation Graphs® or RRGs® as they are commonly known. My application is just a simple and approximate recreation of the concept, as the original formulas for calculating Rs-Ratio and Rs-Momentum are kept secret.

## Short description
Relative Rotation Graphs are a method to compare different stocks or etfs against a common benchmark, rate the relative performance and categorize them in the following four quadrants:

* Leading
* Weakening
* Lagging
* Improving

The plan is to invest in the stocks, which are in the process of transitioning from improving to leading and sell them when they start to fall towards weakening.

## Comparison

### Original from Optuma.com: https://www.optuma.com/relative-rotation-graphs/
![RRG_example](https://cdn1.optuma.com/wp-content/uploads/Relative-Rotation-Graph-GIF.gif)

### My Result:
![gif3](https://user-images.githubusercontent.com/38164738/150478622-18b44a25-62e2-49b0-bb98-4b0f46d18975.gif)

## Installation
```
git clone https://github.com/schuler-ph/RelativeRotationGraphs.git
cd RelativeRotationGraphs
pip install -r requirements.txt
```

* Imageio => Gif-Creator
* Matplotlib => Plots
* Requests => Fetch from Alphavantage.co

## Run
### config.json
* symbols: The symbols, which will be fetched from Alphavantage.co in *update_database.py*.
* compare_to: The benchmark symbol, all symbols will be compared to in *process_data.py*. This will also be fetched in *update_database.py*.
* rs_ratio_avg and rs_momentum_avg: These are the moving averages for rs_ratio and rs_momentum which have produced the best results and represented the data from RRG Online and Stockcharts.com the best.
* tail_length: The tail length on the plot in weeks (default = 10).
* plot_symbols: Which stocks to plot.
* history_range: How many plots should be created in weeks (default = 10).
* filename: The filename used to create the plots and gifs (default = "plot").
* remove_files_after_gif: Defines, if the plot files should be removed, after being used in a gif creation (default = True).
* gif_frame_time_delay: The time between each frame in the gif in seconds (default = 0.2).

### apikey.txt
You will have to get your own Api-Key from Alphavantage.co and save it to a file called *apikey.txt* in the root repository folder.

### rrg_db.py
In this file you will find the database manager, which saves the fetched data to a MySQL database and is generally in charge for all database operations. Update the *__init__* function with your own user credentials and database.

### update_database.py
This file will fetch the data from Alphavantage.co from the TIME_SERIES_WEEKLY function. It will fetch all the symbols defined in the config *symybols* and *compare_to* and save them to the MySQL database.

### process_data.py
This fills the database with the needed data for the plot (price_relative, rs_ratio, rs_ratio_avg, rs_momentum, rs_momentum avg)

### plot.py
Creates a matplotlib scatter plot with the four sectors.

### create_gif.py
Uses imageio to generate a gif with **all** the files provided in the src/plots/ folder.
