#!/usr/bin/env python
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.
"""Configuration for the bot."""

import os


class DefaultConfig:
    """Configuration for the bot."""

    PORT = 3978
    """
    APP_ID = os.environ.get("MicrosoftAppId", "dbd267a0-1141-4087-8cf2-a77bd477d6bc")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "b5319493-ba5e-4ed1-bace-0252c23ef634")
    LUIS_APP_ID = os.environ.get("LuisAppId", "077e5fce-c99c-4e89-909f-dd6bd6807e85")
    LUIS_API_KEY = os.environ.get("LuisAPIKey", "033c3af6d53b49c7afa2cbe5637d578c")
    LUIS_API_HOST_NAME = os.environ.get("LuisAPIHostName", "p10evinstance.cognitiveservices.azure.com/")
    APPINSIGHTS_INSTRUMENTATION_KEY = os.environ.get("AppInsightsInstrumentationKey", "50159b95-fcaf-41cd-8359-66926b01bfe3")
   """
   
    APP_ID = "dbd267a0-1141-4087-8cf2-a77bd477d6bc"
    APP_PASSWORD =  "b5319493-ba5e-4ed1-bace-0252c23ef634"
    LUIS_APP_ID = "077e5fce-c99c-4e89-909f-dd6bd6807e85"
    LUIS_API_KEY = "033c3af6d53b49c7afa2cbe5637d578c"
    LUIS_API_HOST_NAME = "p10evinstance.cognitiveservices.azure.com/"
    APPINSIGHTS_INSTRUMENTATION_KEY = "50159b95-fcaf-41cd-8359-66926b01bfe3"
   
    




