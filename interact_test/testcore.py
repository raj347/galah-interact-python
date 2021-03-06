# Copyright (c) 2013 Galah Group LLC
# Copyright (c) 2013 Other contributers as noted in the CONTRIBUTERS file
#
# This file is part of galah-interact-python.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
#
# You may obtain a copy of the License at
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import operator

def test_cases_one_of(
        testcase_object, test_cases, test_func, comparator = operator.eq):
    for case, expected in test_cases:
        result = test_func(case)
        for i in expected:
            if comparator(result, i):
                break
        else:
            test_case_object.fail(
                "Expected one of %s, got %s for case %s." %
                    (repr(expected), repr(result), repr(case))
            )

def test_cases(testcase_object, test_cases, test_func, assertion = None):
    if assertion is None:
        assertion = testcase_object.assertEqual

    for case, expected in test_cases:
        assertion(test_func(case), expected)
