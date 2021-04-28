# Data science is Software: #lifehacks for the Jupyer data scientist
----------

### Materials for the 1.5 hr talk: (Updated for ODSC East 2017)

[![ODSC 2017 Video](https://img.youtube.com/vi/HM56wCNxCnQ/0.jpg)](https://www.youtube.com/watch?v=HM56wCNxCnQwCNxCnQ)

 - [Slides](https://github.com/drivendata/data-science-is-software/blob/master/slides/Data%20Science%20is%20Software%20-%201hr%20lecture%20-%20Slides.pdf)
 - [Commandline Demo Script](https://github.com/drivendata/data-science-is-software/blob/master/slides/commandline_script.mdmdmdmd)
 - [Jupyter Notebook](https://github.com/drivendata/data-science-is-software/blob/master/notebooks/1-hr-lecture.ipynb)
 - [Example project that was created during the talk](https://github.com/pjbull/pumpspumps)


[!(Things to take away)](https://www.youtube.com/watch?v=HM56wCNxCnQwCNxCnQ)
    - [Data is immutable]
        - [put raw data in data/raw and leave it there. Never update those, only use pipeline to process them.]
        - [put processed data in data/processed. This is the final data which will be put in model.]
        - [if you have data from other sources, put them in data/external]
        - [if data is in the middle of processing, put them in data/interim]
    - [Repeatable project need to be isolated project]
        - [always create new environment for new project. The environment name need to be the same as project name]
        - [All codes that need to be used accross notebooks need to be refractored and put in src/...]
        - [When .py file need to be fixed put autoreload 2 to that modules. It will reload new iterations everytimes the cell run]
    - [Debugging]
        - [Explain code line by line out loud is effective for bug squashing]
        - [When encounter an error. Use %debug to see the error stack and locate the bug. Then we can use u to move up the stack trace and findout where the error happens.]
        - [Another greate way to save debugging time is to make tests. Starting with Pytest]
        - [Use %%prun to print out the running time for each function]
    - [Make tests with pytest]
        - [Create test file with prefix test_ in src/appropriate_things/]
        - [run pytest src/. pytest will find every files with prefix test_ in folder and run those. Assert is a great way to start testing]
    - [Coverage]
        - []



```
.
├── data
│   └── raw
│       ├── pumps_train_labels.csv
│       └── pumps_train_values.csv
├── LICENSE
├── notebooks
│   ├── labs
│   │   ├── 2.0-environment-lab.ipynb
│   │   ├── 2.0-environment-solution.ipynb
│   │   ├── 3.0-refactoring-lab.ipynb
│   │   ├── 3.0-refactoring-solution.ipynb
│   │   └── 4.0-testing-lab.ipynb
│   └── lectures
│       ├── 2.0-environment.ipynb
│       ├── 3.0-refactoring.ipynb
│       └── 4.0-testing.ipynb
├── README.md
├── requirements.txt
├── setup.cfg
└── src
    ├── features
    │   ├── build_features.py
    │   └── preprocess_solution.py
    ├── __init__.py
    ├── mcmc
    │   └── hamiltonian.py
    ├── model
    │   └── train_model_solution.py
    ├── tests
    │   ├── example.py
    │   ├── __init__.py
    │   ├── test_example.py
    │   └── test_lab4_solutions.py
    └── utils.py
```
