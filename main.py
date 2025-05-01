from datetime import datetime

def define_env(env):
    """Define variables and macros."""
    # Existing variable for the current year
    env.variables['current_year'] = datetime.now().year