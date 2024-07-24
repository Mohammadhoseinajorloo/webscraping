from newsscraper.provider.asriranprovider import AsriranProvider
from newsscraper.provider.rajanewsprovider import RajanewsProvider
from newsscraper.core.config import settings
from newsscraper.scheduling.scheduler import scheduler
from newsscraper.scheduling.jobs.rajaprovider import rajaprovider_job
from newsscraper.scheduling.jobs.asriranprovider import asriranprovider_job


def rajascraper(url):
    raja = RajanewsProvider(url)
    return raja.scrape


def asriranscraper(url):
    asri = AsriranProvider(url)
    return asri.scrape


def scheduling(scrapers):
    rajaprovider_job(scheduler, scrapers[0])
    asriranprovider_job(scheduler, scrapers[1])


def run(massage="Welcome to NewsScraper!"):
    print(massage)
    rajaprovider = rajascraper(settings.RAJA_URL)
    asriranprovider = asriranscraper(settings.ASRIRAN_URL)
    scheduling([rajaprovider, asriranprovider])
    try:
        print("Schedule Started ...")
        scheduler.start()
    except (KeyboardInterrupt, SystemExit):
        print("Schedule Stopped ...")
        pass


if __name__ == '__main__':
    run()
