from apscheduler.triggers.cron import CronTrigger

blocktime_rajaprovider = CronTrigger(
    year="*", month="*", day="*", hour="8", minute="0", second="0"
)
