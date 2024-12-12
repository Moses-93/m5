import asyncio
import sys

from core.app import CurrencyRatesApp


async def main():
    """
    Точка входу програми.
    """
    if len(sys.argv) != 2:
        print("Usage: python main.py <days>")
        print("<days> should be an integer between 1 and 10.")
        sys.exit(1)

    try:
        days = int(sys.argv[1])
        if days < 1 or days > 10:
            raise ValueError("Days must be between 1 and 10.")
        app = CurrencyRatesApp(days)
        await app.run()
    except ValueError as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    asyncio.run(main())