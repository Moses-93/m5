

class CurrencyRatesFormatter:
    """
    Клас для форматування даних про курси валют.
    """
    @staticmethod
    def format_rates(data: dict, target_currencies: list[str]) -> dict:
        """
        Форматує дані про курси валют.
        """
        result = {}
        exchange_date = data.get("date")
        if not exchange_date:
            return result

        rates = data.get("exchangeRate", [])
        result[exchange_date] = {}
        for currency in rates:
            if currency.get("currency") in target_currencies:
                result[exchange_date][currency["currency"]] = {
                    "sale": currency.get("saleRate"),
                    "purchase": currency.get("purchaseRate")
                }
        return result
    