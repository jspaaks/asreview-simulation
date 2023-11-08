import json
import pytest
from click.testing import CliRunner
from asreview_simulation._private.cli import cli


@pytest.mark.sam_random
@pytest.mark.fex_tfidf
@pytest.mark.cls_logistic
@pytest.mark.qry_max
@pytest.mark.bal_double
@pytest.mark.stp_rel
def test_logistic_classifier_default_parameterization():
    runner = CliRunner()
    args = [
        "cls-logistic",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    classifier = json.loads(result.output)["cls"]
    assert classifier["abbr"] == "cls-logistic"
    params = classifier["params"].keys()
    expected_pairs = [
        ("c", 1.0),
        ("class_weight", 1.0),
    ]
    assert len(params) == len(expected_pairs), "Unexpected number of parameters"
    for param, expected_value in expected_pairs:
        assert param in params, f"Expected key '{param}' to be present in parameterization of classifier."
        actual_value = classifier["params"][param]
        assert type(actual_value) == type(expected_value), f"Unexpected type for key '{param}'"
        assert actual_value == expected_value, f"Expected key '{param}' to have value '{expected_value}'."