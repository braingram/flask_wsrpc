#!/usr/bin/env python

import pizco

proxy = pizco.Proxy('ipc:///tmp/pizcojs_test_rep')
print(proxy.bar)
print(proxy.splat())
