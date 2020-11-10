test = {   'name': 'q1_1',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> assert model.data.xnames == ["const", "x1"];\n'
                                               '>>> assert model.data.exog.shape == (30000, 2);\n'
                                               '>>> assert (model.endog == defaults.column("bill_sep05")).all();\n'
                                               '>>> assert len(results.fittedvalues) == 30000;\n'
                                               '>>> assert len(y_hat) == 30000\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
