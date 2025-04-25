from datetime import datetime

def define_env(env):
    """Define variables and macros."""
    env.variables['current_year'] = datetime.now().year