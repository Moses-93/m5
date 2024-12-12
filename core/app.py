import asyncio
import json
from datetime import datetime, timedelta

from services import formatter, fetcher


class CurrencyRatesApp:
    """
    Основний клас для роботи з додатком.
    """
    def __init__(self, days: int):
        self.days = days
        self.fetcher = fetcher.CurrencyRatesFetcher()
        self.formatter = formatter.CurrencyRatesFormatter()

    async def run(self):
        """
        Основний метод для запуску програми.
        """
        tasks = []
        today = datetime.now()
        target_currencies = ["USD", "EUR"]
        
        await self.fetcher.init_session()
        for i in range(self.days):
            date = (today - timedelta(days=i)).strftime("%d.%m.%Y")
            tasks.append(self.fetcher.fetch_rates(date))

        responses = await asyncio.gather(*tasks)
        formatted_data = []

        for response in responses:
            if response:
                formatted_data.append(
                    self.formatter.format_rates(response, target_currencies)
                )

        print(json.dumps(formatted_data, indent=2, ensure_ascii=False))
        await self.fetcher.close_session()
