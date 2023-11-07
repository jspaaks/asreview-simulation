import click
from asreview.models.classifiers import SVMClassifier
from asreview_simulation._private.cli.epilog import epilog


name = f"cls-{SVMClassifier.name}"


@click.command(
    epilog=epilog,
    help="Configure the simulation to use Support Vector Machine classifier.",
    name=name,
    short_help="Support Vector Machine classifier",
)
@click.option(
    "--c",
    "c",
    default=15.4,
    help="C value of the SVM model.",
    show_default=True,
    type=click.FLOAT,
)
@click.option(
    "--class_weight",
    "class_weight",
    default=0.249,
    help="Class weight of the inclusions.",
    show_default=True,
    type=click.FLOAT,
)
@click.option(
    "-f",
    "--force",
    "force",
    help="Force setting the querier configuration, even if that me" + "ans overwriting a previous configuration.",
    is_flag=True,
)
@click.option(
    "--gamma",
    "gamma",
    default="auto",
    help="Gamma value of the SVM model.",
    show_default=True,
    type=click.Choice(["auto", "scale"]),
)
@click.option(
    "--kernel",
    "kernel",
    default="linear",
    help="Kernel type of the SVM model.",
    show_default=True,
    type=click.Choice(["linear", "rbf", "poly", "sigmoid"]),
)
@click.pass_obj
def cls_svm(obj, c, class_weight, gamma, force, kernel):
    if not force:
        assert obj.provided.classifier is False, (
            "Attempted reassignment of classifier. Use the --force flag "
            + "if you mean to overwrite the classifier configuration from previous steps. "
        )
    obj.models.classifier.abbr = name
    obj.models.classifier.params = {
        "c": c,
        "class_weight": class_weight,
        "gamma": gamma,
        "kernel": kernel,
    }
    obj.provided.classifier = True
