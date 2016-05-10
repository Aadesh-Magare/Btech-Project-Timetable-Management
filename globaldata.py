# Timetable Management Software - Semi Automated Approach to Timetable Design.
# Copyright (C) 2016  Aadesh Magare - aadeshmagare01@gmail.com, Abhijit A M - abhijit13@gmail.com, Sourabh Limbore - limboresourabh@gmail.com

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

#!/usr/bin/python
header1 = ''
header2 = ''
header3 = ''

clipboard = ''
selection_left = None
selection_right = None
#globals to store all objects
all_teachers = []
all_venues = []
all_classes = []

subjects = {}

days_per_week = 7
lectures_per_day = 10
daily_max = 5
daily_min = 0
class_max = 25
start_time = 0
weekly_max = 20
weekly_min = 0
venueCapacity = 80
classCapacity = 80

rowLabels = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
colLabels = []
# colLabels = ['9-10','10-11', '11-12', '12-1', '1-2', '2-3', '3-4', '4-5', '5-6', '6-7']

teacher_fullnames = []
teacher_shortnames = ['ADD NEW']
teacher_weeklymax = []
teacher_dailymax = []

venue_fullnames = []
venue_shortnames = ['ADD NEW']
venue_capacity = []

class_fullnames = []
class_shortnames = ['ADD NEW']
class_capacity = []

subject_fullnames = []
subject_shortnames = ['ADD NEW']
subject_credits = []

teacher_class_map = {}
class_teacher_map = {}
teacher_subject_map = {}
subject_teacher_map = {}
venue_class_map = {}
class_venue_map = {}
subject_class_map = {}
class_subject_map = {}