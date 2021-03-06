#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#

def _illegal(a, b, c):
    return a + b <= c or a + c <= b or b + c <= a

def triangle(a, b, c):
    # DELETE 'PASS' AND WRITE THIS CODE
    num_unique_sides = len({a,b,c})
    if _illegal(a, b, c):
        raise TriangleError()
    if num_unique_sides is 3:
        return 'scalene'
    elif num_unique_sides is 2:
        return 'isosceles'
    else:
        return 'equilateral'




# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
