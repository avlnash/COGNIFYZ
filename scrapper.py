import requests
from bs4 import BeautifulSoup
import pandas as pd
def extract_news_from_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = []
    summaries = []
    article_links = []
    articles = soup.find_all('li', class_='news_list_li')
    for article in articles:
        headline = article.find('h2', class_='news_title').get_text().strip() if article.find('h2',
                                                                                              class_='news_title') else 'No headline'
        summary = article.find('div', class_='news_desc').get_text().strip() if article.find('div',
                                                                                             class_='news_desc') else 'No summary'
        link_tag = article.find('a')
        link = link_tag['href'] if link_tag else 'No link'
        headlines.append(headline)
        summaries.append(summary)
        article_links.append(link)
    return headlines, summaries, article_links
all_headlines = []
all_summaries = []
all_links = []
for page in range(1, 6):
    url = f'https://www.sakshi.com/tags/Andhra-Pradesh?page={page}'
    headlines, summaries, links = extract_news_from_page(url)
    all_headlines.extend(headlines)
    all_summaries.extend(summaries)
    all_links.extend(links)
df = pd.DataFrame({
    'Headline': all_headlines,
    'Summary': all_summaries,
    'Link': all_links
})
df.to_csv('sakshi_news.csv', index=False, encoding='utf-8-sig')
print("Scraping complete! News information saved to 'sakshi_news.csv'.")