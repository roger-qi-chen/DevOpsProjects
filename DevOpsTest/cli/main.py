import importlib
import pkgutil

from cli.cligroup import cli
from click_repl import register_repl
from cli import commands


def _load_command_modules(parent_module):
    """
    Walks through module tree, starting from the parent, and loads all found modules.
    Thanks to loading all modules the @cli.command will be executed and commands will be registered in cli group
    """
    for importer, modname, is_pkg in pkgutil.iter_modules(parent_module.__path__, parent_module.__name__ + '.'):
        imported_module = importlib.import_module(modname)

        if is_pkg:
            _load_command_modules(parent_module=imported_module)

def main():
    _load_command_modules(commands)
    register_repl(cli)
    cli()


if __name__ == '__main__':
    main()
