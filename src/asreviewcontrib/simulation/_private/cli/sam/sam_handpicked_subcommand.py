import click
from asreviewcontrib.simulation._private.cli.cli_epilog import epilog
from asreviewcontrib.simulation._private.cli.cli_msgs import dont_reassign_sam_msg
from asreviewcontrib.simulation._private.lib.config import OneModelConfig
from asreviewcontrib.simulation._private.lib.sam.sam_handpicked_params import get_sam_handpicked_params


default_params = get_sam_handpicked_params()
abbr = "sam-handpicked"


@click.command(
    epilog=epilog,
    help="Configure the simulation to use Handpicked prior sampler. IDS: a comma separated string",
    name=abbr,
    short_help="Handpicked prior sampler",
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the 'sam' configuration, even if that means overwriting a previous configuration.",
    is_flag=True,
)
@click.option(
    "--records",
    "records",
    default=default_params["records"],
    help="Comma-separated string of integers, where each integer is the identifier for a record as used in the data.",
    type=click.STRING,
)
@click.option(
    "--rows",
    "rows",
    default=default_params["rows"],
    help="Comma-separated string of integers, where each integer is the row number of a record in the data.",
    type=click.STRING,
)
@click.pass_obj
def sam_handpicked_subcommand(obj, force, records, rows):
    if not force:
        assert obj.provided.sam is False, dont_reassign_sam_msg

    assert not (rows is None and records is None), "Need to define either --rows or --records."
    assert not (rows is not None and records is not None), "Need to define one of --rows or --records, not both."

    if rows is not None:
        try:
            ids = [int(elem.strip()) for elem in rows.split(",")]
        except ValueError as e:
            click.echo("\nProblem parsing row numbers.\n")
            raise e
        params = {
            "records": None,
            "rows": ids,
        }
        obj.config.sam = OneModelConfig(abbr=abbr, params=params)
        obj.provided.sam = True

    if records is not None:
        try:
            ids = [int(elem.strip()) for elem in records.split(",")]
        except ValueError as e:
            click.echo("\nProblem parsing record numbers.\n")
            raise e
        params = {
            "records": ids,
            "rows": None,
        }
        obj.config.sam = OneModelConfig(abbr=abbr, params=params)
        obj.provided.sam = True