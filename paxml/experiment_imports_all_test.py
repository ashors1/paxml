# coding=utf-8
# Copyright 2022 Google LLC.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Test experiment configurations import and construction."""

from absl import app
from absl.testing import absltest
from paxml import experiment_imports_test_helper
from paxml import experiment_registry


class Test(experiment_imports_test_helper.ExperimentImportsTestHelper):
  pass


def main(args):
  del args  # Unused.

  n = Test.create_test_methods_for_all_registered_experiments(
      experiment_registry, task_regexes=[""], exclude_regexes=[])
  assert n > 0, "No experiment registered!"

  absltest.main()


if __name__ == "__main__":
  app.run(main)
