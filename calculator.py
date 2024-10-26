import importlib

def load_plugin(plugin_name, func_name, arg):
    """Loads and executes a function from a plugin."""
    try:
        # Dynamically import the plugin module
        plugin = importlib.import_module(f'plugins.{plugin_name}')
        # Get the function from the plugin
        func = getattr(plugin, func_name)
        # Call the function with the argument
        return func(arg)
    except (ModuleNotFoundError, AttributeError) as e:
        print(f"Error loading plugin: {e}")
        return None

# Example usage within REPL
if __name__ == "__main__":
    print(load_plugin('square', 'square', 5))  # Should print 25

