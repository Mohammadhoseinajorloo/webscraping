from newsscraper.scheduling.base import scheduler
from newsscraper.scheduling.blocktime.rajaprovider import blocktime_rajaprovider
from newsscraper.scheduling.blocktime.rajaprovider import blocktime_rajaprovider
from newsscraper.provider.rajanewsprovider import RajanewsProvider
from newsscraper.core.config import settings


rajanews = RajanewsProvider(settings.RAJA_URL)

scheduler.add_job()

