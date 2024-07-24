from newsscraper.scheduling.blocktime.rajaprovider import blocktime_rajaprovider


def rajaprovider_job(scheduler, scrapefunc):
    return scheduler.add_job(scrapefunc, blocktime_rajaprovider, id='rajaprovider')
