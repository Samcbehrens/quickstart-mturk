import os
import setup
from flask import Flask, render_template, url_for, request, make_response
from boto.mturk.connection import MTurkConnection
from boto.mturk.question import ExternalQuestion
from boto.mturk.qualification import Qualifications, PercentAssignmentsApprovedRequirement, NumberHitsApprovedRequirement
from boto.mturk.price import Price

#Start Configuration Variables
AWS_ACCESS_KEY_ID = "AKIAIYP75WEXWYM5KA3A"
AWS_SECRET_ACCESS_KEY = "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"
DEV_ENVIROMENT_BOOLEAN = True
DEBUG = True
#End Configuration Variables

#This allows us to specify whether we are pushing to the sandbox or live site.
if DEV_ENVIROMENT_BOOLEAN:
    AMAZON_HOST = "https://workersandbox.mturk.com/mturk/externalSubmit"
else:
    AMAZON_HOST = "https://www.mturk.com/mturk/externalSubmit"

connection = MTurkConnection(aws_access_key_id=AWS_ACCESS_KEY_ID,
                             aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                             host=AMAZON_HOST)




#frame_height in pixels
frame_height = 800

#Here, I create two sample qualifications
qualifications = Qualifications()
qualifications.add(PercentAssignmentsApprovedRequirement(comparator="GreaterThan", integer_value="90"))
qualifications.add(NumberHitsApprovedRequirement(comparator="GreaterThan", integer_value="100"))

#This url will be the url of your application, with appropriate GET parameters
url = "google.com" 
questionform = ExternalQuestion(url, frame_height)
create_hit_result = connection.create_hit(
    title="Insert the title of your HIT",
    description="Insert your description here",
    keywords=["add", "some", "keywords"],
    #duration is in seconds
    duration = 60*60,
    #max_assignments will set the amount of independent copies of the task (turkers can only see one)
    max_assignments=15,
    question=questionform,
    reward=Price(amount=amount),
     #Determines information returned by method in API, not super important
    response_groups=('Minimal', 'HITDetail'), 
    qualifications=qualifications,
    )