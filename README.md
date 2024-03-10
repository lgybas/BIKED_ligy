# BIKED_ligy
 
Data Analysis and Machine Learning of BIKED-dataset

The data and inspiration comes from this repository https://github.com/Lyleregenwetter/BIKED
And further information can be found here: http://decode.mit.edu/projects/biked/

I am very grateful for the author to share his work and make it accessible to everyone under the MIT Licence.

The author explored three tasks: 
1. classification of bicycle types
2. identification which features are best in predicting which type
3. exploration of the design space for new bicycles

My changes (for 1.) are that I am
* Using Pipelines and changing the preprocessing
* Using RandomizedSearch to find best parameters for algorithms
* Using CrossValidation (instead of shuffling)

Key results (for 1.) are:
* Classification accuracy can be raised to above 75 % on the testset when using only numerical columns of the reduced.csv
* The processed.csv data-set contains 555 columns of the OneHot-Encoded column "SIZE".
* A presentation for a non-technical audience can be found [here](Final_Presentation - WBS Coding School.pdf)

Have fun exploring!

