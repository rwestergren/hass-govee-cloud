"""Constants for the Govee Cloud integration."""

DOMAIN = "govee_cloud"

# API endpoints
API_BASE_URL = "https://app2.govee.com"
LOGIN_ENDPOINT = f"{API_BASE_URL}/account/rest/account/v2/login"
DEVICES_ENDPOINT = f"{API_BASE_URL}/bff-app/v1/device/list"

# Device types
THERMOMETER_SKU = "H5111"

# Configuration keys
CONF_EMAIL = "email"
CONF_PASSWORD = "password"

# Update interval
UPDATE_INTERVAL = 300  # 5 minutes
