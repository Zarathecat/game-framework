#!/usr/bin/env python

# Copyright 2017 Zara Zaimeche

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from character import *
from colours import *

dude = Character()
dude.name = 'Dude'
dude.colour = BRIGHTBLUE
dude.catchphrase = "I'm a dudely dude!"
dude.location = [10, 40]
dude.size = 3

heroine = Character()
heroine.name = 'Magical Pixie'
heroine.colour = RED
heroine.catchphrase = """Gonna defeat the villains, for I am mystical!"""
heroine.location = [30, 10]
heroine.size = 2

tiger = Character()
tiger.name = 'Tiger Jackson'
tiger.colour = ORANGE
tiger.catchphrase = "Grr, I am a tiger. Grr grr grr."
tiger.location = [20, 30]
tiger.size = 1

charas = [dude, heroine, tiger]
