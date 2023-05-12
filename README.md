# Python Code to Plot New Jersey GPS Data on a Map

This Python code reads GPS data from an Excel file, converts the coordinates from the New Jersey State Plane coordinate system to the global WGS84 system, and then plots the data on a map. The data points are colored based on categories.

## Requirements

Before running the code, make sure you have the following requirements:

### Python

You need Python installed on your computer. You can download it from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

### Pip (Python Package Installer)

Pip is the package installer for Python. It comes pre-installed with Python versions 3.4 and above. If you don't have pip installed, you can install it using the following guide: [https://pip.pypa.io/en/stable/installation/](https://pip.pypa.io/en/stable/installation/)

### Libraries

The code uses several Python libraries. You can install them using pip, which is a package manager for Python. Open your terminal (or Command Prompt on Windows) and type the following commands:

```bash
pip install pandas
pip install matplotlib
pip install geopandas
pip install contextily
pip install pyproj
pip install openpyxl
```

Please note, if you have multiple Python versions installed on your computer, you might need to use pip3 instead of pip.

### Data
You need to have your data in an Excel file. The code expects the file to be named 'GPSdata.xlsx' and located in the same directory as the Python script. The Excel file should have at least four columns: easting, northing, elevation, and category. The easting and northing should be in the New Jersey State Plane coordinate system (US Survey Feet).

How to Run the Code
Once you have Python and the necessary libraries installed, and you have your data in the correct format, you can run the code.

If you are running the code from a terminal, navigate to the directory containing the Python script and type:

```bash
python GPSdata.py
```

If you are running the code from an Integrated Development Environment (IDE) like PyCharm or a notebook interface like Jupyter Notebook, you can simply open the script in the IDE or notebook and run it from there.

## Code Explanation

The code does the following:

1. Loads the data from the Excel file.
2. Defines the coordinate systems for the New Jersey State Plane (EPSG:3424) and WGS84 (EPSG:4326).
3. Converts the coordinates from the State Plane to WGS84 using the `Transformer` class from the `pyproj` library.
4. Creates a GeoDataFrame (a data structure from the GeoPandas library that is used for handling spatial data) using the `geopandas.GeoDataFrame` function. The GeoDataFrame is created from the original DataFrame and the converted latitude and longitude.
5. Plots the data on a map, coloring the data points based on the 'category' column in the data. It uses the `plot` function from `matplotlib` library to create the plot. The `column='category'` argument is used to color the points based on the category, and `legend=True` argument is used to include a legend in the plot.
6. Sets the labels for the x and y axes as "Longitude" and "Latitude" using the `set_xlabel` and `set_ylabel` functions from `matplotlib`.
7. Zooms into the area where the data points are using the `set_xlim` and `set_ylim` functions from `matplotlib`. These functions limit the x and y axis extents of the plot to the minimum and maximum longitude and latitude of the data, with a small margin added for better visualization.
8. Adds a basemap (a map background) from OpenStreetMap using the `add_basemap` function from `contextily` library. This function adds the basemap to the plot using the specified CRS (Coordinate Reference System).
9. Displays the plot using the `show` function from `matplotlib`.

## Author

**Erfan Amini**\
_Davidson Lab, Stevens Institute of Technology_

