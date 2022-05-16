some_req = Request('https://www.example/.org/', proxies = proxies[random.randint(len(proxies))], timeout=5,verify=False)
some_req.add_header('User-Agent', ua.random)
some_doc = urlopen(some_req).read().decode('utf8')
