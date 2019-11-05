from cli.cligroup import cli


@cli.group(name='creds')
def creds_cli():
    """ Manages stored credentials """
    pass
