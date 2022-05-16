class WSManager:
    def __init__(self, base_url):
        self.base_url = base_url
    def get_urls(self, level):
        urls = []
        try:
            links_1 = []
            start_link = self.base_url
            links_1.append(start_link)
            for i in links_1:
                response = requests.get(i)
                soup = BeautifulSoup(response.content, "html.parser", parse_only=SoupStrainer(['a', 'img']))
                full_list = [link['href'] for link in soup if link.get('href')] + [img['src'] for img in soup if img.get('src')]
                full_list = list(set(full_list))
                for url in full_list:
                    if not url.startswith('https:/'):
                        if url.startswith('/'):
                            if url.find('.org') == -1:
                                url = start_link + url[1:]
                                full_list.append(url)
                            elif url.find('.org'):
                                url = 'https:' + url
                                full_list.append(url)
                        elif url.startswith('//'):
                            url = start_link + url[2:]
                            full_list.append(url)
                        else:
                            pass
                    elif url.startswith('https:/'):
                        full_list.append(url)
                        urls.append(full_list)
                self.get_urls(level - 1)
                links_1 = full_list
                links_1 = list(set(links_1))
                return links_1
        except MemoryError as e:
            print(e)

        return urls
