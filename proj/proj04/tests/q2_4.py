test = {   'name': 'q2_4',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> test_dict = {"ABC": Table().with_columns("date_string", np.array([dt.date(2020, 1, 1), \n'
                                               '...                                                            dt.date(2020, 1, 2), \n'
                                               '...                                                            dt.date(2020, 1, 3)]), \n'
                                               '...                                          "return", np.array([1.0, 1.1, 1.2])), \n'
                                               '...              "DEF": Table().with_columns("date_string", np.array([dt.date(2020, 1, 1), \n'
                                               '...                                                            dt.date(2020, 1, 2), \n'
                                               '...                                                            dt.date(2020, 1, 4)]), \n'
                                               '...                                          "return", np.array([1.0, 1.2, 1.3]))};\n'
                                               '>>> test_dates = np.array([dt.date(2020, 1, 1), dt.date(2020, 1, 2), dt.date(2020, 1, 3), dt.date(2020, 1, 4)]);\n'
                                               '>>> test_rets = [1, 1.15, 1.2, 1.3];\n'
                                               '>>> for date, ret in zip(test_dates, test_rets):\n'
                                               '...     assert np.isclose(market_return(test_dict, date), ret)\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
