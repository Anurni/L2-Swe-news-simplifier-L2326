## L2-news-simplifier (Final course project for L2326 - Machine learning for statistical NLP: Advanced)

# Preliminary plan:

- Collect 50 news article - pairs in json
- preprocess and tokenize the data
- split data
-Fine-tune T5 model from HuggingFace or Swedish GPT? Possible to compare the performance
- evaluate the performance (qualitative metrics)

# Already risen problems / challenges:
-SweDN dataset summaries are otherwise good, but they are not necessarily simplified language. They mainly seem to offer a consise version of the article, using still words that are most likely challenging for L2-Swedish learners.

-The news articles in 8sidor often have this 'base' information at the start of the article, which is obviously not the case in the regular news articles. Will the model to be able to generalize enough with so few samples?
