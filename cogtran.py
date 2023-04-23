import openai
import requests
import json
from bs4 import BeautifulSoup
import os

OPENAI_API_KEY = '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'
openai.api_key = OPENAI_API_KEY

def extract_text(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    paragraphs = soup.find_all('p')
    text = ' '.join([p.get_text() for p in paragraphs])
    return text


def get_publication_info(text):
    response = openai.Completion.create(
        engine='text-davinci-002',
        prompt=f'''Analyze the article and provide the following items in a JSON:
        
        - publication's name, 
        - bias direction (left or right),
        - bias scale (1-10)
        
        Article: \n\n{text}''',
        max_tokens=300,
        n=1,
        stop=None,
        temperature=0.7,
    )

    return response.choices[0].text.strip()

def get_author_info(text):
    response = openai.Completion.create(
        engine='text-davinci-002',
         prompt=f'''Analyze the article and provide the following as JSON:
        
        - author's name (the human, not the publication),
        - author's bias direction (left or right),
        - author's bias scale (1-10)
        
        Article: \n\n{text}''',
        max_tokens=300,
        n=1,
        stop=None,
        temperature=0.7,
    )

    return response.choices[0].text.strip()

def get_article_info(text):
    response = openai.Completion.create(
        engine='text-davinci-002',
        prompt=f'''Analyze the article and provide the following items in a JSON:
        
        - article's name,
        - article's publication date,
        - article's bias direction,
        - article's bias scale (1-10)
        - a short 3-5 sentence summary of the article
        
        Article: \n\n{text}''',
        max_tokens=300,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()

def get_article_summary(text):
    response = openai.Completion.create(
        engine='text-davinci-002',
        prompt=f'''Analyze the article and provide the following items in a JSON:
        
        - shortSum: 3-5 sentence summary of the article,
        - quickSum: 1 sentence summary of the article
        
        Article: \n\n{text}''',
        max_tokens=300,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()


def get_article_translations(text):
    response = openai.Completion.create(
        engine='text-davinci-002',
        prompt=f'''
        Analyze the article and provide the following items in a JSON:
        
        {{
        - "genzSum": "a short summary using as many Gen Z slang words as possible",
        - "5yoSum": "a short summary that can be understood by a 5 year old (super simple words)"
        }}
        
        
        Article: \n\n{text}''',
        max_tokens=300,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()


def analyze_article(text):
    pub_info_text = get_publication_info(text)
    auth_info_text = get_author_info(text)
    article_info_text = get_article_info(text)
    # summary_text = get_article_summary(text)
    # translations_text = get_article_translations(text)

    print("Publication info text:", pub_info_text)
    print("Author info text:", auth_info_text)
    print("Article info text:", article_info_text)
    # print("Summary text:", summary_text)
    # print("Translations text:", translations_text)

    publication_info = json.loads(pub_info_text)
    author_info = json.loads(auth_info_text)
    article_info = json.loads(article_info_text)
    # summary = json.loads(summary_text)
    # translations = json.loads(translations_text)

    result = {
        "publication_info": publication_info,
        "author_info": author_info,
        "article_info": article_info,
        # "summary": summary,
        # "translations": translations
    }

    return result ##json.dumps(result, indent=2)

'''
def main():
    url = input("Enter the article URL: ")
    text = extract_text(url)
    analysis = analyze_article(text)
    print("Analysis:\n", json.dumps(analysis, indent=2))

if __name__ == '__main__':
    main()

'''