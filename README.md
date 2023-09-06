# Penguin-Predictor
>*"You did everything penguinly possible."- Happy Feet*


This project will load the dataset, clean and prepare data, implement several supervised learning models, and pick the best model for the given dataset.

# Dataset information
This project is based on a <a href="https://www.kaggle.com/datasets/parulpandey/palmer-archipelago-antarctica-penguin-data"></a>Kaggle dataset about 2020 Palmer Archipelago (Antarctica) penguins.

This data was originally published in:<br>
<a href="https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0090081">Gorman KB, Williams TD, Fraser WR (2014) Ecological Sexual Dimorphism and Environmental Variability within a Community of Antarctic Penguins (Genus Pygoscelis). PLoS ONE 9(3): e90081. doi:10.1371/journal.pone.009008</a>

The data folder contains one cvs file: <em>penguins_size.csv</em> 

Variables:
<ul>
 <li>species: penguin species (Chinstrap, Adélie, or Gentoo)</li>
 <li>culmen_length_mm: culmen length (mm)</li>
 <li>culmen_depth_mm: culmen depth (mm)</li>
 <li>flipper_length_mm: flipper length (mm)</li>
 <li>body_mass_g: body mass (g)</li>
 <li>island: island name (Dream, Torgersen, or Biscoe) in the Palmer Archipelago (Antarctica)</li>
 <li>sex: penguin sex</li>
</ul>

# Video Walkthrough

Here's a walkthrough of model deployed on a simple flask website:

<img src='https://github.com/gabrielaliera/Penguin-Predictor/blob/main/walkthrough.gif' title='Video Demo' width='1200' heigth="1200" alt='Video Demo' />
GIF created with <a href="https://www.cockos.com/licecap/">LICEcap.</a> 


# Data Visualizations
<p align="center">
  <img align="center" src="https://github.com/gabrielaliera/Penguin-Predictor/blob/main/README/data.PNG">
</p>

# Train and Model Selection
<p align="center">
  <img align="center" src="https://github.com/gabrielaliera/Penguin-Predictor/blob/main/README/training.gif">
</p>


# Tech/Framework
<ul>
  <li><a href="https://www.python.org/">Python</a></li>
  <li><a href="https://jupyter.org/">Jupyter Notebooks</a></li>
  <li><a href="https://www.kaggle.com/">Kaggle</a></li>
  <li><a href="https://numpy.org/">NumPy</a></li>
  <li><a href="https://pandas.pydata.org/">Pandas</a></li>
  <li><a href="https://matplotlib.org/">Matplotlib</a></li>
  <li><a href="https://seaborn.pydata.org/">Seaborn</a></li>
  <li><a href="https://scipy.org/">SciPy</a></li>
  <li><a href="https://www.statsmodels.org/stable/index.html">Statsmodel</a></li>
  
</ul>

## Installation

Make sure you have python3 and pip installed

Create and activate virtual environment using virtualenv
```bash
$ python -m venv venv
$ source venv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies!

```bash
pip install flask
pip install numpy
pip install -U scikit-learn
```

## Usage

Create a .env file using the example.env template (make a copy using the variables inside of the template)

Start flask development server
```bash
$ export FLASK_ENV=development
$ flask run
```

You should get a response like this in the terminal:
```
❯ flask run
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

You'll now be able to access the website at `localhost:5000` or `127.0.0.1:5000` in the browser! 


# Contributors
  <ul>
  <li>Gabriela Liera</li>
  </ul>

# Notes
View the <a href="https://github.com/gabrielaliera/Penguin-Predictor/blob/main/Penguin.ipynb">data preparation, data visualizatin, and model selection.</a> 
