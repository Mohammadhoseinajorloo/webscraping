from newsscraper.provider.asriranprovider import AsriranProvider
from newsscraper.provider.rajanewsprovider import RajanewsProvider
from newsscraper.core.config import settings


def run(massage="wellcome to web scraping app :)"):
    print(massage)

    raja = RajanewsProvider(settings.RAJA_URL)
    asriran = AsriranProvider(settings.ASRIRAN_URL)

    print(f"start scrape {settings.RAJA_URL} ...")
    rajanews = raja.scrape()
    print(f"end scraping {settings.RAJA_URL}.")
    print(f"start scrape {settings.ASRIRAN_URL}...")
    asrirannews = asriran.scrape()
    print(f"end scraping {settings.ASRIRAN_URL}.")


if __name__ == "__main__":
    run()
