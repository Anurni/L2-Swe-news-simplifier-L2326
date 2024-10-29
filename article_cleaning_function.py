def clean_article_text(text):
    cleaned_text = ' '.join(text.split())
    return cleaned_text

copied_article = """

"""

cleaned_article = clean_article_text(copied_article)
print(cleaned_article)
