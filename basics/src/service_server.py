#!/usr/bin/env python

import rospy

from rosbook_basics.srv import WordCount,WordCountResponse


def count_words(request):
    return WordCountResponse(len(request.words.split()))
    #return [len(request.words.split())] #To return multiple args as a tuple or list
    #return {'count': len(request.words.split())} #To return a dictionary where the keys are the args' names (given as strings)


rospy.init_node('service_server')

service = rospy.Service('word_count', WordCount, count_words)

rospy.spin()

