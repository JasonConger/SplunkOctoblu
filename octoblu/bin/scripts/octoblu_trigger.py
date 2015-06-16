import gzip
import csv
import time
import re
import sys, os
import logging, logging.handlers
import splunk
import base64
import datetime
import json
from optparse import OptionParser
import urllib2
import splunk.entity as en
import logging, cherrypy
import logging.handlers

#dynamically load in any eggs in the app directory
SPLUNK_HOME = os.environ.get("SPLUNK_HOME")
EGG_DIR = SPLUNK_HOME + "/etc/apps/octoblu/bin/"

for filename in os.listdir(EGG_DIR):
	if filename.endswith(".egg"):
		sys.path.append(EGG_DIR + filename)

import requests

## Setup the logger
def setup_logger():
	logger = logging.getLogger('splunk.octoblu')
	SPLUNK_HOME = os.environ['SPLUNK_HOME']
	LOGGING_DEFAULT_CONFIG_FILE = os.path.join(SPLUNK_HOME, 'etc', 'log.cfg')
	LOGGING_LOCAL_CONFIG_FILE = os.path.join(SPLUNK_HOME, 'etc', 'log-local.cfg')
	LOGGING_STANZA_NAME = 'python'
	LOGGING_FILE_NAME = "octoblu.log"
	BASE_LOG_PATH = os.path.join('var', 'log', 'splunk')
	LOGGING_FORMAT = "%(asctime)s %(levelname)-s\t%(module)s:%(lineno)d - %(message)s"
	splunk_log_handler = logging.handlers.RotatingFileHandler(os.path.join(SPLUNK_HOME, BASE_LOG_PATH, LOGGING_FILE_NAME), mode='a')
	splunk_log_handler.setFormatter(logging.Formatter(LOGGING_FORMAT))
	logger.addHandler(splunk_log_handler)
	splunk.setupSplunkLogger(logger, LOGGING_DEFAULT_CONFIG_FILE, LOGGING_LOCAL_CONFIG_FILE, LOGGING_STANZA_NAME)
	return logger

logger = setup_logger()


def defineOptions():

	parser = OptionParser();

	#Global Variables
	global alert_level
	alert_level = ""
	global url
	url = ""

	time.sleep(2)
	try:
		str = sys.argv[8]
		logger.info(str)
		f1=gzip.open(str,'rb')
	except IOError as e:
		logger.error("I/O error({0}): {1}".format(e.errno, e.strerror))
		logger.error("Could not open raw results file. Make sure you have read access to the raw results folder at "+ sys.argv[8])
		logger.error("Failed to execute Alert Script")
	except:
		logger.error("Unexpected error:", sys.exc_info()[0])
	
	csv_file=csv.DictReader(f1, delimiter=',')

	#pick the first event only
	for line in csv_file:

		#Read the first line only
		if alert_level == "":
			logger.info("capturing alert_level from raw results")
			try:
				alert_level=line['alert_level']
				logger.info("alert_level = '%s'" % (alert_level))
			except KeyError:
				logger.error("alert_level  must be set as a returned field in the alert raw results or hardcoded in the octoblu_trigger.py file. Exiting python script.")
				raise SystemExit

		if url == "":
			logger.info("capturing url from raw results")
			try:
				url=line['url']
				logger.info("url = '%s'" % (url))
			except KeyError:
				logger.error("url  must be set as a returned field in the alert raw results or hardcoded in the octoblu_trigger.py file. Exiting python script.")
				raise SystemExit
		break

	# get tokens from octoblu.conf if you want to authenticate
	#oconf = splunk.clilib.cli_common.getConfStanza("octoblu", "default")
	#meshblu_auth_uuid = oconf['meshblu_auth_uuid']
	#meshblu_auth_token = oconf['meshblu_auth_token']

	parser.add_option("--url", dest="url", help="The url of the trigger", default=url)
	parser.add_option("--alert_level", dest="alert_level", help="alert_level", default=alert_level)
	#parser.add_option("--meshblu_auth_uuid", dest="meshblu_auth_uuid", help="The meshblu_auth_uuid", default=meshblu_auth_uuid)
	#parser.add_option("--meshblu_auth_token", dest="meshblu_auth_token", help="The meshblu_auth_token", default=meshblu_auth_token)


	(options, args) = parser.parse_args()
	
	
	return options

	f1.close()


def execute():

	data = {"alert_level" : options.alert_level}
	#data = json.dumps(data)

	headers = {'meshblu_auth_uuid' : options.meshblu_auth_uuid, 'meshblu_auth_token' : options.meshblu_auth_token}
	
	#Send the request only when url and alert_level are set
	if (options.url !="") and (options.alert_level !=""):
		
		try:
			logger.info("sending data to octoblu")
			r = requests.post(options.url, headers=headers, data=data)
		
		except urllib2.HTTPError, e:
			logger.error("Failed to send the request to Octoblu " + str(e.reason))
			raise SystemExit
		except urllib2.URLError, e:
			logger.error("Failed to send the request to Octoblu " + str(e.reason))
			raise SystemExit
		except httplib.HTTPException, e:
			logger.error("Failed to send the request to Octoblu " + str(e.reason))	
			raise SystemExit
		except:
			logger.error("Unexpected error:", sys.exc_info()[0])
	else:
		logger.error("url and alert_level must be set. Will not send request to Octoblu.")


if __name__ == '__main__':
	logger = setup_logger()
	#logger.info("Start of Octoblu Alert script - Alert Name = " + sys.argv[4])
	#logger.info("Trigger Reason: " + sys.argv[5])
	#logger.info("Script  Name " + sys.argv[0])
	#logger.info("Raw file " + sys.argv[8])
	#logger.info("Search: " + sys.argv[3])
	options = defineOptions();
	execute();

