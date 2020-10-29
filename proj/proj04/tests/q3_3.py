test = {   'name': 'q3_3',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> test_ranks = Table().with_columns("stock", make_array("ABC", "DEF", "XYZ"), \n'
                                               '...                                   "excess_returns", make_array(3, 2, 1));\n'
                                               '>>> test_market_returns = make_array(2, 1, 2);\n'
                                               '>>> test_date_range = make_array(1,2,3);\n'
                                               '>>> test_dict = {"ABC": Table().with_columns("date_string", make_array(1,2,3), \n'
                                               '...                                          "return", make_array(2, 1, 2)), \n'
                                               '...              "XYZ": Table().with_columns("date_string", make_array(1,2,3), \n'
                                               '...                                          "return", make_array(2, 1, 3))};\n'
                                               '>>> test_w, test_l = track_portfolio(test_ranks, 1, 0, 2, test_date_range, test_market_returns, test_dict);\n'
                                               '>>> assert test_w == 1;\n'
                                               '>>> assert test_l == 2\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
