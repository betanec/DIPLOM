def t(self):
        if self.token is None or self.expiration is None or self.expiration < datetime.now():
            loop = asyncio.get_event_loop()
            loop.run_until_complete(self. __get_smth_for_smth__())
        if self.expiration > datetime.now():
            return self.token
    
async def __get_smth_for_smth__(self):
        loop = asyncio.get_event_loop()
        future = loop.run_in_executor(None, functools.partial(requests self.base_url))
        resp = await future
