import click
from asreviewlib.classifiers import LogisticClassifier


name = LogisticClassifier.name


@click.command(name=f"c-{name}", help="Use Logistic Regression classifier")
@click.option("-c", "c", default=1.0, type=float, help="hyperparameter 'C'.")
@click.option("-class_weight", "class_weight", default=1.0, type=float, help="hyperparameter 'class_weight'.")
@click.pass_obj
def logistic_classifier(obj, c, class_weight):
    assert obj.provided.classifier is False, "Attempted reassignment of classifier"
    obj.classifier.model = name
    obj.classifier.params = {
        "c": c,
        "class_weight": class_weight
    }
    obj.provided.classifier = True
