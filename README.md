## L2-news-simplifier (Final course project for L2326 - Machine learning for statistical NLP: Advanced) - Anni Nieminen

This repository holds my code (two Jupyter notebooks), data, and report for the final course project of LT2326.

Note that due to memory issues, the fine-tuned models are not available in this repository. Also note that the data (D-wikipedia dataset) used for the fine-tuning in Notebook 1 is compressed in this repository.
Both the models as well as extracted data (as well as all the files that are have been uploaded in this repository) can be found on the mltgpu at: 

```bash
/home/gusniemian@GU.GU.SE/L2-Swe-news-simplifier-L2326
```

## Notebook 1: `task-fine-tuning.ipynb`

This notebook holds the code for fine-tuning the base model (mT5-small) for the task.
The resulting fine-tuned model is named:

```bash
final-task-fine-tuned-model-40k-traindata
```

and it is available at:

```bash
/home/gusniemian@GU.GU.SE/L2-Swe-news-simplifier-L2326/final-task-fine-tuned-model-40k-traindata 
```

## Notebook 2: `language-fine-tuning.ipynb`

This notebook holds the code for the second fine-tuning of the model. Meaning that this code fine-tunes the model that 
is saved in task-fine-tuning.ipynb.
The resulting fine-tuned model is named:

```bash
final-language-fine-tuned-model
```

and it is available at: 

```bash
/home/gusniemian@GU.GU.SE/L2-Swe-news-simplifier-L2326/final-language-fine-tuned-model
```

## Data for notebook 2: `data.json`

Holds the 50 Swedish news article pairs used for the fine-tuning in notebook 2.

## Project report : `Advanced Machine Learning final project report.pdf`

My project report discussing project background, methodolody, data, results, and limitations.




