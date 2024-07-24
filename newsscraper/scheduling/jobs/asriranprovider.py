from newsscraper.scheduling.blocktime.asriranprovider import blocktime_asriranprovider


def asriranprovider_job(scheduler, scrapefunc):
    return scheduler.add_job(scrapefunc, blocktime_asriranprovider, id='asriranprovider')
