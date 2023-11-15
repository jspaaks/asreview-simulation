import click
from asreview.models.feature_extraction import EmbeddingLSTM
from asreview_simulation._private.cli.cli_epilog import epilog
from asreview_simulation._private.lib.fex.fex_embedding_lstm_config import get_fex_embedding_lstm_config


default_params = get_fex_embedding_lstm_config().params
name = f"fex-{EmbeddingLSTM.name}"


@click.command(
    epilog=epilog,
    help="Configure the simulation to use Embedding LSTM extractor",
    name=name,
    short_help="Embedding LSTM extractor",
)
@click.option(
    "--embedding",
    "embedding",
    default=default_params["embedding"],
    help="File path of embedding matrix.",
    type=click.Path(exists=True),
)
@click.option(
    "--fill",
    "fill",
    default=default_params["fill"],
    help="What to do when a sequence is too short. \"loop\": loop the sequence; \"append-zeros\": pad rig"
    + "ht side with zeros; \"prepend-zeros\": pad left side with zeros",
    show_default=True,
    type=click.Choice(["loop", "append-zeros", "prepend-zeros"]),
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the querier configuration, even if that me" + "ans overwriting a previous configuration.",
    is_flag=True,
)
@click.option(
    "--max_sequence_length",
    "max_sequence_length",
    default=default_params["max_sequence_length"],
    help="Maximum length of the sequence. Longer gets truncated, according to the value of --truncating. Shorte"
    + "r sequences get either looped or padded with zeros, according to the value of --fill.",
    show_default=True,
    type=click.INT,
)
@click.option(
    "--num_words",
    "num_words",
    default=default_params["num_words"],
    help="Maximum number of unique words to be processed.",
    show_default=True,
    type=click.INT,
)
@click.option(
    "--split_ta",
    "split_ta",
    default=default_params["split_ta"],
    help="Include this flag to split ta.",
    is_flag=True,
)
@click.option(
    "--truncating",
    "truncating",
    default=default_params["truncating"],
    help="Which side should be truncated.",
    show_default=True,
    type=click.Choice(["pre", "post"]),
)
@click.option(
    "--use_keywords",
    "use_keywords",
    default=default_params["use_keywords"],
    help="Include this flag to use keywords.",
    is_flag=True,
)
@click.pass_obj
def fex_embedding_lstm_subcommand(
    obj,
    embedding,
    force,
    loop_sequence,
    max_sequence_length,
    num_words,
    padding,
    split_ta,
    truncating,
    use_keywords,
):
    if not force:
        assert obj.provided.fex is False, (
            "Attempted reassignment of extractor. Use the --force flag "
            + "if you mean to overwrite the extractor configuration from previous steps. "
        )
    obj.models.fex.abbr = name
    obj.models.fex.params = {
        "embedding": embedding,
        "loop_sequence": loop_sequence,
        "max_sequence_length": max_sequence_length,
        "num_words": num_words,
        "padding": padding,
        "split_ta": split_ta,
        "truncating": truncating,
        "use_keywords": use_keywords,
    }
    obj.provided.fex = True