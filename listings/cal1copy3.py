new_proxies = [i for i in [proxies_list[i:i+2] for i in range(0,len(proxies_list),2)]]
proxies = [{'IP': new_proxies[i][0], 'Port': new_proxies[i][1], 'Status': 'unknown'} for i in range(len(new_proxies))]
