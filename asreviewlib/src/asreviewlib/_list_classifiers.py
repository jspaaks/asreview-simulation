from .classifiers import LogisticClassifier
from .classifiers import LstmBaseClassifier
from .classifiers import LstmPoolClassifier
from .classifiers import NaiveBayesClassifier
from .classifiers import NN2LayerClassifier
from .classifiers import RandomForestClassifier
from .classifiers import SvmClassifier
from importlib.metadata import entry_points as entrypoints


def list_classifiers():
    my_classifiers = {c.name: c for c in [
        LogisticClassifier,
        LstmBaseClassifier,
        LstmPoolClassifier,
        NaiveBayesClassifier,
        NN2LayerClassifier,
        RandomForestClassifier,
        SvmClassifier
    ]}
    other_classifiers = {e.name: e.load() for e in entrypoints(group="classifiers")}
    rv = dict()
    rv.update(my_classifiers)
    rv.update(other_classifiers)
    return rv
