test = {   'name': 'q3_4',
    'points': 1,
    'suites': [   {   'cases': [   {   'code': '>>> test_dict = {"IBM": nyse["IBM"], \n'
                                               '...              "D": nyse["D"],\n'
                                               '...              "KO": nyse["KO"],\n'
                                               '...              "DIS": nyse["DIS"],\n'
                                               '...              "BA": nyse["BA"]};\n'
                                               '>>> import os;\n'
                                               '>>> from contextlib import redirect_stdout;\n'
                                               '>>> with open(os.devnull, "w") as f, redirect_stdout(f):\n'
                                               '...     test_w, test_l = main_function(test_dict, date_range, nyse_returns, 1);\n'
                                               '>>> assert len(test_w) == 16;\n'
                                               '>>> assert len(test_l) == 16\n',
                                       'hidden': False,
                                       'locked': False}],
                      'scored': True,
                      'setup': '',
                      'teardown': '',
                      'type': 'doctest'}]}
