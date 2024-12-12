import aiohttp

class CurrencyRatesFetcher:
    """
    Клас для отримання курсів валют від ПриватБанку.
    """
    BASE_URL = "https://api.privatbank.ua/p24api/exchange_rates?json&date={date}"

    def __init__(self):
        self.session = None

    async def init_session(self):
        """Ініціалізація сесії aiohttp."""
        self.session = aiohttp.ClientSession()

    async def fetch_rates(self, date: str) -> dict:
        """
        Отримує дані про курси валют для заданої дати.
        """
        if not self.session:
            raise RuntimeError("Session is not initialized. Call 'init_session' before fetching data.")

        url = self.BASE_URL.format(date=date)
        try:
            async with self.session.get(url) as response:
                if response.status == 200:
                    return await response.json()
                else:
                    raise ValueError(f"Failed to fetch data. Status code: {response.status}")
        except Exception as e:
            print(f"Error fetching data for {date}: {e}")
            return {}

    async def close_session(self):
        """
        Закриває сесію aiohttp.
        """
        if self.session:
            await self.session.close()
            