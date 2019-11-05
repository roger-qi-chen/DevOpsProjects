import click
import logging.config
from click import Context
from click.decorators import pass_context
from click.globals import get_current_context

from cli.log_config import get_log_config

_CLI_CONTEXT_KEY = '__cli_context'


class CliContext:
    def __init__(self, debug_mode: bool):
        self.debug_mode = debug_mode


def get_cli_context() -> CliContext:
    click_ctx = get_current_context()
    cli_context = click_ctx.obj.get(_CLI_CONTEXT_KEY)

    if cli_context is None:
        raise Exception('Context was not initialized yet!')

    return cli_context


def init_logging(log_level: str):
    logging.config.dictConfig(get_log_config(log_level))


@click.group()
@click.option('--log-level', default='debug', envvar='CLI_LOG_LEVEL', type=click.Choice([
    'off', 'debug', 'info', 'warning', 'error', 'critical'
]))
@click.option('--force-color', is_flag=True, help='Force use of colored output')
@pass_context
def cli(ctx: Context, force_color: bool, log_level: str):
    log_level_upper = log_level.upper()

    init_logging(log_level=log_level_upper)

    if force_color:
        ctx.color = True

    ctx.obj = {
        _CLI_CONTEXT_KEY: CliContext(
            debug_mode=(log_level == 'debug')
        )
    }


if __name__ == '__main__':
    raise Exception("Sorry, you should run the 'main' instead of this module.")
