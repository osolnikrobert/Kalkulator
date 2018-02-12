#!/usr/bin/env python
# -*- coding: utf-8 -*-

secret = 10
guess = int(raw_input("Skrito število je: "))
if guess == secret:
    print "Bravo! Uganil si pravo število!"
else:
    print "Poskusi znova!"