import json
import pytest
from click.testing import CliRunner
from asreview_simulation._private.cli.cli import cli


@pytest.mark.sam_random
@pytest.mark.fex_tfidf
@pytest.mark.cls_nb
@pytest.mark.qry_max
@pytest.mark.bal_double
@pytest.mark.stp_rel
def test_max_querier_default_parameterization():
    runner = CliRunner()
    args = [
        "qry-max",
        "print-settings",
    ]
    result = runner.invoke(cli, args)
    querier = json.loads(result.output)["querier"]
    assert querier["abbr"] == "max"
    params = querier["params"].keys()
    expected_pairs = [
        ("n_instances", 1),
    ]
    assert len(params) == len(expected_pairs), "Unexpected number of parameters"
    for param, expected_value in expected_pairs:
        assert param in params, f"Expected key '{param}' to be present in parameterization of querier."
        assert querier["params"][param] == expected_value, f"Expected key '{param}' to have value '{expected_value}'."
