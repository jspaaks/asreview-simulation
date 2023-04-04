import click
from asreviewlib.queriers import ClusterQuerier
from .._epilog import epilog


name = ClusterQuerier.name


@click.command(epilog=epilog,
               help="Use Cluster querier",
               name=f"q-{name}")
@click.option("-f", "--force", "force",
              help="Force setting the querier configuration, even if that me" +
              "ans overwriting a previous configuration.",
              is_flag=True)
@click.option("--cluster_size", "cluster_size",
              default=350,
              help="hyperparameter 'cluster_size'.",
              show_default=True,
              type=click.INT)
@click.option("--update_interval", "update_interval",
              default=200,
              help="hyperparameter 'update_interval'.",
              show_default=True,
              type=click.INT)
@click.pass_obj
def cluster_querier(obj, force, cluster_size, update_interval):
    if not force:
        assert obj.provided.querier is False, "Attempted reassignment of querier"
    obj.querier.model = name
    obj.querier.params = {
        "cluster_size": cluster_size,
        "update_interval": update_interval
    }
    obj.provided.querier = True
