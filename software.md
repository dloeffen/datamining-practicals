# Setting up the Python environment

Instructions regarding setting up a Python environment can be found [here](https://github.com/tueimage/essential-skills/blob/master/python-essentials.md)

Now create a new environment using:

		conda create --name datamining python=3.6

And go into this environment using:

		conda activate datamining

Lastly you want to install these packages:

		conda install matplotlib, jupyter, scikit-learn, scipy, pandas, tensorflow, spyder


If you want to contribute to the repository, consider installing nbdime for merging jupyter notebooks:
		conda install -c conda-forge nbdime 


