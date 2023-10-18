import hyperopt


def get_pyll_bal_double():
    return {
        "abbr": "double",
        "params": {
            "a": hyperopt.hp.lognormal("a", 0, 1),
            "alpha": hyperopt.hp.uniform("alpha", 0, 2),
            "b": hyperopt.hp.uniform("b", 0, 1),
            "beta": hyperopt.hp.uniform("beta", 0, 2),
        }
    }
