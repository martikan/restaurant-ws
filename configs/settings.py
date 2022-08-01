import os


# Get environment variables for database connection.
# It has default values for development environment.
DATASOURCE_URL = "postgresql+asyncpg://%s:%s@%s:%s/%s" % (
        os.getenv("DATASOURCE_USER", "restaurant"),
        os.getenv("DATASOURCE_PASSWORD", "aaa"),
        os.getenv("DATASOURCE_URL", "localhost"),
        os.getenv("DATASOURCE_PORT", "5432"),
        os.getenv("DATASOURCE_DB", "restaurant"),
)

def get_datasource_url():
        """Gets database connection url.
        * localhost connection is the default one.
        """
        
        return DATASOURCE_URL

def get_profile():
        """Get profile.
        * prod - For production
        * dev  - For development. [It is the default]
        """
        
        return os.getenv("PROFILE", "dev") # False means it's in development mode.

def is_development():
        """Return True if it's in development mode.
        """
        
        return "dev" == get_profile()
        