1. There are 2 jupyter notebooks (.ipynb files) in the code folder :

	Exploratory_DA.ipynb was used for data exploration.
   	Train.ipynb was used for training.
   
   Both notebooks were run on Kaggle (an online platform). The required data was directly downloaded from the google drive on to the
   working directories of the notebook on Kaggle. Preferably, the notebooks should be run on Kaggle. However, if the notebooks are run
   on a local computer or some other online platform, the only change required is changing the directory from "/kaggle/working" to 
   "/home/user/" (for example, if the notebook is run a Linux operated computer), wherever the "kaggle/working" directory is explicitly 
   mentioned in the code.
   

2. The inference.py script should be run using command/terminal. Note that the working directory should be changed to the location of this
   python file before executing the following command.

	python inference.py --dir '/home/user/pictures' --model 'home/user/model.hdf5'

   where '/home/user/pictures' is the directory containing pictures that are required to be classified. The pictures must in any one of these
   formats - .jpg or .png or .jpeg only.
   
   And where 'home/user/model.hdf5' is the path of the trained model.

   The result csv file will be available in the pictures directory ('/home/user/pictures') after the script's run is complete.

3. Before running the inference file, make sure that Python 3.0 or any higher version is installed. Also make sure to install the libraries
   listed in the requirements.txt file. If the latest Anaconda Distribution is installed, then the requirements will automatically be taken 
   care of.

4. The Results folder contains the plots obtained while training (training loss & validation loss, training f1 score & validation f1 score), 	as well as results on the test set (confusion matrix, and a csv file containing the food lable wise statistics). It also contains the
   plots generated during data exploraion (label count) and during training (neural network schematic).  

5. A 6 page report exists in the form of report.pdf file.


	
