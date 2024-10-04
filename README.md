## L2-news-simplifier (Final course project for L2326 - Machine learning for statistical NLP: Advanced)

# Preliminary plan:
-Manually collect around 50 regular news article - simplified news article pairs that discuss the same topic into a json file.
-Fine-tune T5 model from HuggingFace or Swedish GPT

# Already risen problems / challenges:
-SweDN dataset summaries are otherwise good, but they are not necessarily simplified language. They mainly seem to offer a consise version of the article, using still words that are most likely challenging for L2-Swedish learners.

-Will 50 data pairs be enough for the model?

-The news articles in 8sidor often have this 'base' information at the start of the article, which is obviously not the case in the regular news articles. Will the model to be able to generalize enough with so few samples?
