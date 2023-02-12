# -*- coding: utf-8 -*-

import pytest


total_count = 0


def pytest_addoption(parser):
    group = parser.getgroup('linewrapper')
    group.addoption(
        '--output-length',
        action='store',
        dest='output_length',
        type=int,
        default=300,
        help='Max line length before wrapping'
    )


@pytest.hookimpl(hookwrapper=True)
def pytest_report_teststatus(report, config):
    global total_count
    yield
    if report.when == "call":
        total_count += 1
        if total_count > config.option.output_length:
            total_count = 0
            print()
