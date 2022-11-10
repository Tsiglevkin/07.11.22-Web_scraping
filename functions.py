import requests
from fake_headers import Headers
import bs4


def make_soup(some_url):
    fake_headers = Headers(os='win').generate()
    response = requests.get(some_url, headers=fake_headers)
    res = response.text
    return bs4.BeautifulSoup(res, features='html.parser')


def get_article_date(article):
    return article.find('time').attrs.get('title')


def get_article_header(article, article_title_class):
    return article.find(class_=article_title_class).find('span').text


def get_actual_link(article):
    url = 'https://habr.com/ru'
    full_text_link = article.find('h2').find('a').attrs.get('href')
    return f'{url}{full_text_link[3:]}'  # delete a part '/ru' from href


# def check_article_body_1(full_article_soup, body_class, title_class):  # это старая копия. Не используется.
#     res_set = set()
#     article_soup = full_article_soup.find(class_=body_class)
#     article_header = get_article_header(article=full_article_soup, article_title_class=title_class)
#     print(article_header)
#     for elem in article_soup:
#         paragraphs = elem.findAll('p')
#         for row in paragraphs:
#             temp_par_list = [row.text.split()]
#             for word_2 in temp_par_list[0]:
#                 new_word_2 = word_2.strip(',.«»!?#*').lower()
#                 res_set.add(new_word_2)
#     return res_set


def check_article_body(full_article_soup, body_class, title_class=None):
    res_set = set()
    article_soup = full_article_soup.find(class_=body_class)
    article_header = get_article_header(article=full_article_soup, article_title_class=title_class)
    # print(article_header)
    temp_list = article_soup.text.split()
    for word in temp_list:
        new_word = word.strip(',.«»!?#*').lower()
        res_set.add(new_word)

    return res_set
