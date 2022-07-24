import os

"""
Get environment variables for database connection.
It has default values for development environment.
"""
DATASOURCE_URL = "postgresql://%s:%s@%s:%s/%s" % (
        os.getenv("DATASOURCE_USER", "restaurant"),
        os.getenv("DATASOURCE_PASSWORD", "aaa"),
        os.getenv("DATASOURCE_URL", "localhost"),
        os.getenv("DATASOURCE_PORT", "5432"),
        os.getenv("DATASOURCE_DB", "restaurant"),
)

"""
Gets database connection url.
"""
def get_datasource_url():
        return DATASOURCE_URL