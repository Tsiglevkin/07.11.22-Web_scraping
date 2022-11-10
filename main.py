from functions import get_article_date, get_article_header, get_actual_link, make_soup, check_article_body

KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'Wasteland', 'ViRush']

if __name__ == '__main__':
    url = 'https://habr.com/ru'
    soup = make_soup(url)

    articles = soup.findAll('article')
    for article in articles:
        href_class = 'tm-article-snippet__title-link'
        full_article_url = get_actual_link(article=article)  # ссылка на полную статью

        article_soup = make_soup(full_article_url)  # получаем суп из полной статьи.
        header_class = 'tm-article-snippet__title tm-article-snippet__title_h1'
        body_class = 'article-formatted-body article-formatted-body article-formatted-body_version-2'

        article_word_set = check_article_body(  # получаем множество из слов, взятых из тела статьи
            full_article_soup=article_soup,
            body_class=body_class,
        )

        # print(get_article_header(article=article_soup, article_title_class=header_class))  # для проверки,
        # на какой статье обвалиливается.
        for word in KEYWORDS:  # проверка вхождения требуемых слов в тело полной статьи
            if word.lower() in article_word_set:
                article_date = get_article_date(article=article_soup)
                header = get_article_header(article=article_soup, article_title_class=header_class)
                print(f'Дата: {article_date}. Название статьи - {header}, '
                      f'ссылка - {full_article_url}')


#  программа обрывается, т.к. иногда у body_class меняется версия с version-2 на version-1. Не знаю, как обойти...


