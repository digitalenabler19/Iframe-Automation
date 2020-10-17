#Author:Prasad Katankot, 13-Oct-2020
from selenium import webdriver
import json
import logging
import sys
import os 



def setup_log(name, logPath):
	try:
	    filename = logPath+"\\log_{}.log".format(name)
	    
	    logger = logging.getLogger(name)  
	    logger.setLevel(logging.DEBUG)
	    log_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
	   
	    log_handler = logging.FileHandler(filename)
	    log_handler.setLevel(logging.DEBUG)
	    log_handler.setFormatter(log_format)
	    logger.addHandler(log_handler)
	    return logger
	except Exception as inst:
	     exc_type, exc_obj, exc_tb = sys.exc_info()
	     print(type(inst))
	     print(inst.args)
	     print(inst)
	     print(exc_tb.tb_lineno)


def iframe(dict_val):
	try:
		logger = setup_log("iframe",dict_val["logPath"])
		logger.info(type(dict_val))
		logger.info(dict_val)
		logger.info(dict_val["iframe"])
		logger.info("start")
		identifier=eval(dict_val['iframe'])['identifier']
		logger.info(identifier)
		findmethod=eval(dict_val['iframe'])['findmethod']
		logger.info(findmethod)
		# val=eval(dict_val['field1'])['value']
		# logger.info(val)
		dir_path = os.path.dirname(os.path.realpath(__file__))
		logger.info(dir_path)
		driver = webdriver.Chrome(dir_path+"/chromedriver")
		#driver = webdriver.Chrome("D:/chromedriver")
		if dict_val["URL"] is not None:
			driver.get(dict_val["URL"])
		else:
			raise Exception("Target URL not found")
		#iframeElement = driver.find_element_by_id('loginframe')
		if None not in (findmethod,identifier):
			iframeElement=getElement(findmethod, identifier,driver)
			if (iframeElement is not None):
				driver.switch_to.frame(iframeElement)
				for key,val in dict_val.items():
					logger.info(key)
					if key != "iframe" and key != "logPath":
						keyval=eval(val)
						identifier=keyval["identifier"]
						logger.info(identifier)
						findmethod=keyval['findmethod']
						logger.info(findmethod)
						fldvalue=keyval['value']
						logger.info(fldvalue)
						if None not in (findmethod,identifier,fldvalue):
							fld=getElement(findmethod, identifier,driver)
							if fld is not None:
								logger.info(setElement(findmethod, identifier,fldvalue,driver))
	except Exception as inst:
		     exc_type, exc_obj, exc_tb = sys.exc_info()
		     logger.info(type(inst))
		     logger.info(inst.args)
		     logger.info(inst)
		     logger.info(exc_tb.tb_lineno)

def getElement(findmethod, identifier,driver):
	try:
		iframeElement=None
		if (findmethod=="find_element_by_id"):
			iframeElement = driver.find_element_by_id(identifier)
		elif(findmethod=="find_element_by_xpath"):
			iframeElement = driver.find_element_by_xpath(identifier)
		elif(findmethod=="find_element_by_name"):
			iframeElement = driver.find_element_by_name(identifier)
		return iframeElement
	except Exception as inst:
		     exc_type, exc_obj, exc_tb = sys.exc_info()
		     logger.info(type(inst))
		     logger.info(inst.args)
		     logger.info(inst)
		     logger.info(exc_tb.tb_lineno)

def setElement(findmethod, identifier,value,driver):
	try:
		setStatus=None
		if (findmethod=="find_element_by_id"):
			setStatus = driver.find_element_by_id(identifier).send_keys(value)
		elif(findmethod=="find_element_by_xpath"):
			setStatus = driver.find_element_by_xpath(identifier).send_keys(value)
		elif(findmethod=="find_element_by_name"):
			setStatus = driver.find_element_by_name(identifier).send_keys(value)
		return setStatus
	except Exception as inst:
		     exc_type, exc_obj, exc_tb = sys.exc_info()
		     logger.info(type(inst))
		     logger.info(inst.args)
		     logger.info(inst)
		     logger.info(exc_tb.tb_lineno)


