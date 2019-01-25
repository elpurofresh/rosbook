#!/usr/bin/env python

import rospy

from rosbook_basics.srv import WordCount

import sys


rospy.init_node('service_client')

# We have to wait for the service to be running (advertised by ROS), otherwise
# the call will fail with an exception.
rospy.wait_for_service('word_count')

# We need to specify the name of the service ('word_count') and its type (WordCount).
word_counter = rospy.ServiceProxy('word_count', WordCount)

words = ' '.join(sys.argv[1:])

word_count = word_counter(words)

print words, '->', word_count.count

