import logging
import sentry_sdk

from sentry_sdk.integrations.fastapi import FastApiIntegration
from sentry_sdk.integrations.logging import LoggingIntegration

from app.config import Settings

sentry_config = Settings.sentry


def setup_sentry():

    if Settings.env == "production":
        print("init sentry")
        sentry_logging = LoggingIntegration(
            level=logging.INFO,
            event_level=logging.WARNING,
        )
        sentry_sdk.init(
            dsn=sentry_config.dsn,
            integrations=[
                FastApiIntegration(),
                sentry_logging,
            ],
            traces_sample_rate=0.01,
        )
