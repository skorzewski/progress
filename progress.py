#!/usr/bin/env python3
# -*- coding:utf-8 -*-

import sys


class Progress(object):
    """Progress bar"""

    def __init__(self, total, bar_len=50):
        self.total = total
        self.bar_len = bar_len
        self.done = 0
        self.percentage = 0
        self.fraction = 0

    def _update(self):
        percentage = self.done * 100 / self.total
        fraction = self.done * self.bar_len / self.total
        if percentage > self.percentage or fraction > self.fraction:
            self.percentage = percentage
            self.fraction = fraction
            return True
        return False

    def update(self):
        self.done += 1
        if self._update():
            bar = (self.fraction * '#' + (self.bar_len - self.fraction) * ' ')
            sys.stdout.write('\r[{}] {:>3}%'.format(bar, self.percentage))
            sys.stdout.flush()

    def finish(self):
        print()
