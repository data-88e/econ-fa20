test = {   'name': 'q3_2',
    'points': 1,
    'suites': [   {   'cases': [   {'code': '>>> result = rank_stocks(nyse, 0, 12, date_range, nyse_returns);\n>>> assert type(result) == type(Table())\n', 'hidden': False, 'locked': False},
                                   {   'code': '>>> result = rank_stocks(nyse, 0, 12, date_range, nyse_returns);\n'
                                               '>>> assert result.column("excess_returns").item(0) > result.column("excess_returns").item(-1)\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
