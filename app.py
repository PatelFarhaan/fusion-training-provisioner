import json
import time
import string
import random
import urllib.request
from selenium import webdriver
from mails.ebs_mail import ebs_email
from mails.fusion_mail import fusion_email
from mails.ebs_mail_existing import ebs_email_exist
from google_sheet.google import google_sheet_update
from mails.fusion_mail_existing import fusion_email_exist



######################################### SINGLES #######################################################
def oracle_workflow_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_172'][name^='jform[groups][]'][type='checkbox'][value='172']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_workflow_training = driver.find_element_by_xpath('//*[@id="1group_172"]')
        driver.execute_script("arguments[0].click();", oracle_workflow_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def obiee_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_131'][name^='jform[groups][]'][type='checkbox'][value='131']").get_attribute("checked")
    if not isChecked == 'true':
        obiee_training = driver.find_element_by_xpath('//*[@id="1group_131"]')
        driver.execute_script("arguments[0].click();", obiee_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_fusion_fundamentals_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_44'][name^='jform[groups][]'][type='checkbox'][value='44']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_fundamentals_training = driver.find_element_by_xpath('//*[@id="1group_44"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_fundamentals_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_286'][name^='jform[groups][]'][type='checkbox'][value='286']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_instance = driver.find_element_by_xpath('//*[@id="1group_286"]')
        driver.execute_script("arguments[0].click();", fusion_instance)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def fusion_hcm_core_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_35'][name^='jform[groups][]'][type='checkbox'][value='35']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_hcm_core_training = driver.find_element_by_xpath('//*[@id="1group_35"]')
        driver.execute_script("arguments[0].click();", fusion_hcm_core_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_286'][name^='jform[groups][]'][type='checkbox'][value='286']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_instance = driver.find_element_by_xpath('//*[@id="1group_286"]')
        driver.execute_script("arguments[0].click();", fusion_instance)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_fusion_talent_management_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_30'][name^='jform[groups][]'][type='checkbox'][value='30']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_talent_management_training = driver.find_element_by_xpath('//*[@id="1group_30"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_talent_management_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_286'][name^='jform[groups][]'][type='checkbox'][value='286']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_instance = driver.find_element_by_xpath('//*[@id="1group_286"]')
        driver.execute_script("arguments[0].click();", fusion_instance)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_fusion_benefits_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_64'][name^='jform[groups][]'][type='checkbox'][value='64']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_benefits_training_1 = driver.find_element_by_xpath('//*[@id="1group_64"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_benefits_training_1)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_283'][name^='jform[groups][]'][type='checkbox'][value='283']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_benefits_training_2 = driver.find_element_by_xpath('//*[@id="1group_283"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_benefits_training_2)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_286'][name^='jform[groups][]'][type='checkbox'][value='286']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_instance = driver.find_element_by_xpath('//*[@id="1group_286"]')
        driver.execute_script("arguments[0].click();", fusion_instance)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def fusion_payroll_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_239'][name^='jform[groups][]'][type='checkbox'][value='239']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_payroll_training = driver.find_element_by_xpath('//*[@id="1group_239"]')
        driver.execute_script("arguments[0].click();", fusion_payroll_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_286'][name^='jform[groups][]'][type='checkbox'][value='286']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_instance = driver.find_element_by_xpath('//*[@id="1group_286"]')
        driver.execute_script("arguments[0].click();", fusion_instance)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_fusion_fastformula_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_45'][name^='jform[groups][]'][type='checkbox'][value='45']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_fastformula = driver.find_element_by_xpath('//*[@id="1group_45"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_fastformula)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_286'][name^='jform[groups][]'][type='checkbox'][value='286']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_instance = driver.find_element_by_xpath('//*[@id="1group_286"]')
        driver.execute_script("arguments[0].click();", fusion_instance)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_fusion_compensation_workbench_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_29'][name^='jform[groups][]'][type='checkbox'][value='29']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_compensation_workbench = driver.find_element_by_xpath('//*[@id="1group_29"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_compensation_workbench)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_286'][name^='jform[groups][]'][type='checkbox'][value='286']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_instance = driver.find_element_by_xpath('//*[@id="1group_286"]')
        driver.execute_script("arguments[0].click();", fusion_instance)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_fusion_hcm_approval_management_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_240'][name^='jform[groups][]'][type='checkbox'][value='240']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_hcm_approval_management = driver.find_element_by_xpath('//*[@id="1group_240"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_hcm_approval_management)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_286'][name^='jform[groups][]'][type='checkbox'][value='286']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_instance = driver.find_element_by_xpath('//*[@id="1group_286"]')
        driver.execute_script("arguments[0].click();", fusion_instance)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_fusion_time_and_labour_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_241'][name^='jform[groups][]'][type='checkbox'][value='241']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_time_and_labour_training = driver.find_element_by_xpath('//*[@id="1group_241"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_time_and_labour_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_286'][name^='jform[groups][]'][type='checkbox'][value='286']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_instance = driver.find_element_by_xpath('//*[@id="1group_286"]')
        driver.execute_script("arguments[0].click();", fusion_instance)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def fusion_hcm_for_ebs_hcm_experts_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_245'][name^='jform[groups][]'][type='checkbox'][value='245']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_hcm_for_ebs_hcm_experts_training = driver.find_element_by_xpath('//*[@id="1group_245"]')
        driver.execute_script("arguments[0].click();", fusion_hcm_for_ebs_hcm_experts_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_286'][name^='jform[groups][]'][type='checkbox'][value='286']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_instance = driver.find_element_by_xpath('//*[@id="1group_286"]')
        driver.execute_script("arguments[0].click();", fusion_instance)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def fusion_procurement_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_39'][name^='jform[groups][]'][type='checkbox'][value='39']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_procurement_training = driver.find_element_by_xpath('//*[@id="1group_39"]')
        driver.execute_script("arguments[0].click();", fusion_procurement_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_286'][name^='jform[groups][]'][type='checkbox'][value='286']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_instance = driver.find_element_by_xpath('//*[@id="1group_286"]')
        driver.execute_script("arguments[0].click();", fusion_instance)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_fusion_hcm_technical_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_277'][name^='jform[groups][]'][type='checkbox'][value='277']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_hcm_technical_training = driver.find_element_by_xpath('//*[@id="1group_277"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_hcm_technical_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_286'][name^='jform[groups][]'][type='checkbox'][value='286']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_instance = driver.find_element_by_xpath('//*[@id="1group_286"]')
        driver.execute_script("arguments[0].click();", fusion_instance)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_fusion_financials_accounting_hub_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_259'][name^='jform[groups][]'][type='checkbox'][value='259']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_financials_accounting_hub_training_1 = driver.find_element_by_xpath('//*[@id="1group_259"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_financials_accounting_hub_training_1)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_46'][name^='jform[groups][]'][type='checkbox'][value='46']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_financials_accounting_hub_training_2 = driver.find_element_by_xpath('//*[@id="1group_46"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_financials_accounting_hub_training_2)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_286'][name^='jform[groups][]'][type='checkbox'][value='286']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_instance = driver.find_element_by_xpath('//*[@id="1group_286"]')
        driver.execute_script("arguments[0].click();", fusion_instance)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_fusion_procure_to_pay_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_62'][name^='jform[groups][]'][type='checkbox'][value='62']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_procure_to_pay_training = driver.find_element_by_xpath('//*[@id="1group_62"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_procure_to_pay_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_286'][name^='jform[groups][]'][type='checkbox'][value='286']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_instance = driver.find_element_by_xpath('//*[@id="1group_286"]')
        driver.execute_script("arguments[0].click();", fusion_instance)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def fusion_application_installation_and_patching_R9_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_115'][name^='jform[groups][]'][type='checkbox'][value='115']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_application_installation_and_patching_R9_training = driver.find_element_by_xpath('//*[@id="1group_115"]')
        driver.execute_script("arguments[0].click();", fusion_application_installation_and_patching_R9_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def development_in_fusion_applications_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_83'][name^='jform[groups][]'][type='checkbox'][value='83']").get_attribute("checked")
    if not isChecked == 'true':
        development_in_fusion_applications = driver.find_element_by_xpath('//*[@id="1group_83"]')
        driver.execute_script("arguments[0].click();", development_in_fusion_applications)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_fusion_financials_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_50'][name^='jform[groups][]'][type='checkbox'][value='50']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_financials_training = driver.find_element_by_xpath('//*[@id="1group_50"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_financials_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_286'][name^='jform[groups][]'][type='checkbox'][value='286']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_instance = driver.find_element_by_xpath('//*[@id="1group_286"]')
        driver.execute_script("arguments[0].click();", fusion_instance)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_BI_reproting_and_OTBI_training_in_fusion_apps_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_123'][name^='jform[groups][]'][type='checkbox'][value='123']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_BI_reproting_and_OTBI_training_in_fusion_apps_1 = driver.find_element_by_xpath('//*[@id="1group_123"]')
        driver.execute_script("arguments[0].click();", oracle_BI_reproting_and_OTBI_training_in_fusion_apps_1)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_135'][name^='jform[groups][]'][type='checkbox'][value='135']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_BI_reproting_and_OTBI_training_in_fusion_apps_2 = driver.find_element_by_xpath('//*[@id="1group_135"]')
        driver.execute_script("arguments[0].click();", oracle_BI_reproting_and_OTBI_training_in_fusion_apps_2)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_286'][name^='jform[groups][]'][type='checkbox'][value='286']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_instance = driver.find_element_by_xpath('//*[@id="1group_286"]')
        driver.execute_script("arguments[0].click();", fusion_instance)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_fusion_accounts_receivable_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_229'][name^='jform[groups][]'][type='checkbox'][value='229']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_accounts_receivable_training = driver.find_element_by_xpath('//*[@id="1group_229"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_accounts_receivable_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_286'][name^='jform[groups][]'][type='checkbox'][value='286']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_instance = driver.find_element_by_xpath('//*[@id="1group_286"]')
        driver.execute_script("arguments[0].click();", fusion_instance)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_fusion_financials_cloud_tax_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_256'][name^='jform[groups][]'][type='checkbox'][value='256']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_financials_cloud_tax_training = driver.find_element_by_xpath('//*[@id="1group_256"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_financials_cloud_tax_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_286'][name^='jform[groups][]'][type='checkbox'][value='286']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_instance = driver.find_element_by_xpath('//*[@id="1group_286"]')
        driver.execute_script("arguments[0].click();", fusion_instance)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_apps_DBA_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_145'][name^='jform[groups][]'][type='checkbox'][value='145']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_apps_DBA = driver.find_element_by_xpath('//*[@id="1group_145"]')
        driver.execute_script("arguments[0].click();", oracle_apps_DBA)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_EBS_R12_inventory_order_management_and_purchasing_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_49'][name^='jform[groups][]'][type='checkbox'][value='49']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_EBS_R12_inventory_order_management_and_purchasing_training = driver.find_element_by_xpath('//*[@id="1group_49"]')
        driver.execute_script("arguments[0].click();", oracle_EBS_R12_inventory_order_management_and_purchasing_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_R12_subledger_accounting_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_43'][name^='jform[groups][]'][type='checkbox'][value='43']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_R12_subledger_accounting_training = driver.find_element_by_xpath('//*[@id="1group_43"]')
        driver.execute_script("arguments[0].click();", oracle_R12_subledger_accounting_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_EBS_R12_functional_financial_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_117'][name^='jform[groups][]'][type='checkbox'][value='117']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_EBS_R12_functional_financial_training = driver.find_element_by_xpath('//*[@id="1group_117"]')
        driver.execute_script("arguments[0].click();", oracle_EBS_R12_functional_financial_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def OA_framework_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_41'][name^='jform[groups][]'][type='checkbox'][value='41']").get_attribute("checked")
    if not isChecked == 'true':
        OA_framework_training = driver.find_element_by_xpath('//*[@id="1group_41"]')
        driver.execute_script("arguments[0].click();", OA_framework_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def R12_advanced_global_intercompany_system_AGIS_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_48'][name^='jform[groups][]'][type='checkbox'][value='48']").get_attribute("checked")
    if not isChecked == 'true':
        R12_advanced_global_intercompany_system_AGIS_training = driver.find_element_by_xpath('//*[@id="1group_48"]')
        driver.execute_script("arguments[0].click();", R12_advanced_global_intercompany_system_AGIS_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_EBusiness_tax_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_128'][name^='jform[groups][]'][type='checkbox'][value='128']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_EBusiness_tax_training_1 = driver.find_element_by_xpath('//*[@id="1group_128"]')
        driver.execute_script("arguments[0].click();", oracle_EBusiness_tax_training_1)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_252'][name^='jform[groups][]'][type='checkbox'][value='252']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_EBusiness_tax_training_2 = driver.find_element_by_xpath('//*[@id="1group_252"]')
        driver.execute_script("arguments[0].click();", oracle_EBusiness_tax_training_2)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_demantra_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_65'][name^='jform[groups][]'][type='checkbox'][value='65']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_demantra_training = driver.find_element_by_xpath('//*[@id="1group_65"]')
        driver.execute_script("arguments[0].click();", oracle_demantra_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_R12_HRMS_payroll_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_144'][name^='jform[groups][]'][type='checkbox'][value='144']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_R12_HRMS_payroll_training = driver.find_element_by_xpath('//*[@id="1group_144"]')
        driver.execute_script("arguments[0].click();", oracle_R12_HRMS_payroll_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_implement_configurator_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_149'][name^='jform[groups][]'][type='checkbox'][value='149']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_implement_configurator_training = driver.find_element_by_xpath('//*[@id="1group_149"]')
        driver.execute_script("arguments[0].click();", oracle_implement_configurator_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_R12_project_accounting_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_138'][name^='jform[groups][]'][type='checkbox'][value='138']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_R12_project_accounting_training = driver.find_element_by_xpath('//*[@id="1group_138"]')
        driver.execute_script("arguments[0].click();", oracle_R12_project_accounting_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_R12_advance_supply_chain_planning_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_137'][name^='jform[groups][]'][type='checkbox'][value='137']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_R12_advance_supply_chain_planning_training = driver.find_element_by_xpath('//*[@id="1group_137"]')
        driver.execute_script("arguments[0].click();", oracle_R12_advance_supply_chain_planning_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_R12_financial_accounting_hub_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_136'][name^='jform[groups][]'][type='checkbox'][value='136']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_R12_financial_accounting_hub_training = driver.find_element_by_xpath('//*[@id="1group_136"]')
        driver.execute_script("arguments[0].click();", oracle_R12_financial_accounting_hub_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_business_intelligence_applications_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_131'][name^='jform[groups][]'][type='checkbox'][value='131']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_business_intelligence_applications_training = driver.find_element_by_xpath('//*[@id="1group_131"]')
        driver.execute_script("arguments[0].click();", oracle_business_intelligence_applications_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_business_intelligence_enterprise_edition_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_56'][name^='jform[groups][]'][type='checkbox'][value='56']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_business_intelligence_enterprise_edition_training = driver.find_element_by_xpath('//*[@id="1group_56"]')
        driver.execute_script("arguments[0].click();", oracle_business_intelligence_enterprise_edition_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_adf_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_76'][name^='jform[groups][]'][type='checkbox'][value='76']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_adf_training = driver.find_element_by_xpath('//*[@id="1group_76"]')
        driver.execute_script("arguments[0].click();", oracle_adf_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_business_process_management_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_130'][name^='jform[groups][]'][type='checkbox'][value='130']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_business_process_management_training = driver.find_element_by_xpath('//*[@id="1group_130"]')
        driver.execute_script("arguments[0].click();", oracle_business_process_management_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_soa_BPEL_mediator_OBS_development_training_1_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_40'][name^='jform[groups][]'][type='checkbox'][value='40']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_soa_BPEL_mediator_OBS_development_training_1 = driver.find_element_by_xpath('//*[@id="1group_40"]')
        driver.execute_script("arguments[0].click();", oracle_soa_BPEL_mediator_OBS_development_training_1)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_122'][name^='jform[groups][]'][type='checkbox'][value='122']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_soa_BPEL_mediator_OBS_development_training_12C = driver.find_element_by_xpath('//*[@id="1group_122"]')
        driver.execute_script("arguments[0].click();", oracle_soa_BPEL_mediator_OBS_development_training_12C)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_data_integrator_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_126'][name^='jform[groups][]'][type='checkbox'][value='126']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_data_integrator_training = driver.find_element_by_xpath('//*[@id="1group_126"]')
        driver.execute_script("arguments[0].click();", oracle_data_integrator_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_mobile_application_framework_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_113'][name^='jform[groups][]'][type='checkbox'][value='113']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_mobile_application_framework_training = driver.find_element_by_xpath('//*[@id="1group_113"]')
        driver.execute_script("arguments[0].click();", oracle_mobile_application_framework_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_java_xml_and_web_service_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_129'][name^='jform[groups][]'][type='checkbox'][value='129']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_java_xml_and_web_service_training = driver.find_element_by_xpath('//*[@id="1group_129"]')
        driver.execute_script("arguments[0].click();", oracle_java_xml_and_web_service_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_sql_and_plSQL_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_155'][name^='jform[groups][]'][type='checkbox'][value='155']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_sql_and_plSQL_training = driver.find_element_by_xpath('//*[@id="1group_155"]')
        driver.execute_script("arguments[0].click();", oracle_sql_and_plSQL_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def fusion_financials_integration_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_253'][name^='jform[groups][]'][type='checkbox'][value='253']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_financials_integration_training = driver.find_element_by_xpath('//*[@id="1group_253"]')
        driver.execute_script("arguments[0].click();", fusion_financials_integration_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_286'][name^='jform[groups][]'][type='checkbox'][value='286']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_instance = driver.find_element_by_xpath('//*[@id="1group_286"]')
        driver.execute_script("arguments[0].click();", fusion_instance)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def fusion_financials_security_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_268'][name^='jform[groups][]'][type='checkbox'][value='268']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_financials_security_training_1 = driver.find_element_by_xpath('//*[@id="1group_268"]')
        driver.execute_script("arguments[0].click();", fusion_financials_security_training_1)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_272'][name^='jform[groups][]'][type='checkbox'][value='272']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_financials_security_training_2 = driver.find_element_by_xpath('//*[@id="1group_272"]')
        driver.execute_script("arguments[0].click();", fusion_financials_security_training_2)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_286'][name^='jform[groups][]'][type='checkbox'][value='286']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_instance = driver.find_element_by_xpath('//*[@id="1group_286"]')
        driver.execute_script("arguments[0].click();", fusion_instance)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()



def fusion_financials_reporting_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_235'][name^='jform[groups][]'][type='checkbox'][value='235']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_financials_reporting_training = driver.find_element_by_xpath('//*[@id="1group_235"]')
        driver.execute_script("arguments[0].click();", fusion_financials_reporting_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_286'][name^='jform[groups][]'][type='checkbox'][value='286']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_instance = driver.find_element_by_xpath('//*[@id="1group_286"]')
        driver.execute_script("arguments[0].click();", fusion_instance)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def fusion_financials_approval_management_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_209'][name^='jform[groups][]'][type='checkbox'][value='209']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_financials_approval_management_training = driver.find_element_by_xpath('//*[@id="1group_209"]')
        driver.execute_script("arguments[0].click();", fusion_financials_approval_management_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_286'][name^='jform[groups][]'][type='checkbox'][value='286']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_instance = driver.find_element_by_xpath('//*[@id="1group_286"]')
        driver.execute_script("arguments[0].click();", fusion_instance)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_fusion_integration_cloud_Service_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_250'][name^='jform[groups][]'][type='checkbox'][value='250']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_integration_cloud_Service_training = driver.find_element_by_xpath('//*[@id="1group_250"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_integration_cloud_Service_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_sales_cloud_extensibility_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_204'][name^='jform[groups][]'][type='checkbox'][value='204']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_sales_cloud_extensibility_training = driver.find_element_by_xpath('//*[@id="1group_204"]')
        driver.execute_script("arguments[0].click();", oracle_sales_cloud_extensibility_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_286'][name^='jform[groups][]'][type='checkbox'][value='286']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_instance = driver.find_element_by_xpath('//*[@id="1group_286"]')
        driver.execute_script("arguments[0].click();", fusion_instance)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_fusion_account_payable_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_28'][name^='jform[groups][]'][type='checkbox'][value='28']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_account_payable_training = driver.find_element_by_xpath('//*[@id="1group_28"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_account_payable_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_286'][name^='jform[groups][]'][type='checkbox'][value='286']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_instance = driver.find_element_by_xpath('//*[@id="1group_286"]')
        driver.execute_script("arguments[0].click();", fusion_instance)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_fusion_general_ledger_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_231'][name^='jform[groups][]'][type='checkbox'][value='231']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_general_ledger_training = driver.find_element_by_xpath('//*[@id="1group_231"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_general_ledger_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_286'][name^='jform[groups][]'][type='checkbox'][value='286']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_instance = driver.find_element_by_xpath('//*[@id="1group_286"]')
        driver.execute_script("arguments[0].click();", fusion_instance)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def fusion_fixed_asset_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_220'][name^='jform[groups][]'][type='checkbox'][value='220']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_fixed_asset_training = driver.find_element_by_xpath('//*[@id="1group_220"]')
        driver.execute_script("arguments[0].click();", fusion_fixed_asset_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_286'][name^='jform[groups][]'][type='checkbox'][value='286']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_instance = driver.find_element_by_xpath('//*[@id="1group_286"]')
        driver.execute_script("arguments[0].click();", fusion_instance)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_fusion_project_portfolio_management_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_238'][name^='jform[groups][]'][type='checkbox'][value='238']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_project_portfolio_management_training = driver.find_element_by_xpath('//*[@id="1group_238"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_project_portfolio_management_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_286'][name^='jform[groups][]'][type='checkbox'][value='286']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_instance = driver.find_element_by_xpath('//*[@id="1group_286"]')
        driver.execute_script("arguments[0].click();", fusion_instance)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_business_suit_fundamentals_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_194'][name^='jform[groups][]'][type='checkbox'][value='194']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_business_suit_fundamentals_training = driver.find_element_by_xpath('//*[@id="1group_194"]')
        driver.execute_script("arguments[0].click();", oracle_business_suit_fundamentals_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_R12_iprocurement_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_212'][name^='jform[groups][]'][type='checkbox'][value='212']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_R12_iprocurement_training = driver.find_element_by_xpath('//*[@id="1group_212"]')
        driver.execute_script("arguments[0].click();", oracle_R12_iprocurement_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_ebs_R12_service_contract_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_206'][name^='jform[groups][]'][type='checkbox'][value='206']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_ebs_R12_service_contract_training = driver.find_element_by_xpath('//*[@id="1group_206"]')
        driver.execute_script("arguments[0].click();", oracle_ebs_R12_service_contract_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_ebs_R12_fixed_assets_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_216'][name^='jform[groups][]'][type='checkbox'][value='216']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_ebs_R12_fixed_assets_training = driver.find_element_by_xpath('//*[@id="1group_216"]')
        driver.execute_script("arguments[0].click();", oracle_ebs_R12_fixed_assets_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_transportation_management_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_219'][name^='jform[groups][]'][type='checkbox'][value='219']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_transportation_management_training = driver.find_element_by_xpath('//*[@id="1group_219"]')
        driver.execute_script("arguments[0].click();", oracle_transportation_management_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_demantra_ptp_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_263'][name^='jform[groups][]'][type='checkbox'][value='263']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_demantra_ptp_training = driver.find_element_by_xpath('//*[@id="1group_263"]')
        driver.execute_script("arguments[0].click();", oracle_demantra_ptp_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_identity_management_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_52'][name^='jform[groups][]'][type='checkbox'][value='52']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_identity_management_training = driver.find_element_by_xpath('//*[@id="1group_52"]')
        driver.execute_script("arguments[0].click();", oracle_identity_management_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_access_manager_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_73'][name^='jform[groups][]'][type='checkbox'][value='73']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_access_manager_training = driver.find_element_by_xpath('//*[@id="1group_73"]')
        driver.execute_script("arguments[0].click();", oracle_access_manager_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_weblogic_administrator_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_47'][name^='jform[groups][]'][type='checkbox'][value='47']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_weblogic_administrator_training = driver.find_element_by_xpath('//*[@id="1group_47"]')
        driver.execute_script("arguments[0].click();", oracle_weblogic_administrator_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_entitlement_server_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_159'][name^='jform[groups][]'][type='checkbox'][value='159']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_entitlement_server_training = driver.find_element_by_xpath('//*[@id="1group_159"]')
        driver.execute_script("arguments[0].click();", oracle_entitlement_server_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def fusion_middleware_12C_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_134'][name^='jform[groups][]'][type='checkbox'][value='134']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_middleware_12C_training = driver.find_element_by_xpath('//*[@id="1group_134"]')
        driver.execute_script("arguments[0].click();", fusion_middleware_12C_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_goldengate_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_66'][name^='jform[groups][]'][type='checkbox'][value='66']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_goldengate_training = driver.find_element_by_xpath('//*[@id="1group_66"]')
        driver.execute_script("arguments[0].click();", oracle_goldengate_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_database_12C_advanced_admininstration_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_171'][name^='jform[groups][]'][type='checkbox'][value='171']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_database_12C_advanced_admininstration_training = driver.find_element_by_xpath('//*[@id="1group_171"]')
        driver.execute_script("arguments[0].click();", oracle_database_12C_advanced_admininstration_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_data_guard_administration_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_177'][name^='jform[groups][]'][type='checkbox'][value='177']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_data_guard_administration_training = driver.find_element_by_xpath('//*[@id="1group_177"]')
        driver.execute_script("arguments[0].click();", oracle_data_guard_administration_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def r12_approval_management_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_156'][name^='jform[groups][]'][type='checkbox'][value='156']").get_attribute("checked")
    if not isChecked == 'true':
        r12_approval_management_training_1 = driver.find_element_by_xpath('//*[@id="1group_156"]')
        driver.execute_script("arguments[0].click();", r12_approval_management_training_1)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_230'][name^='jform[groups][]'][type='checkbox'][value='230']").get_attribute("checked")
    if not isChecked == 'true':
        r12_approval_management_training_2 = driver.find_element_by_xpath('//*[@id="1group_230"]')
        driver.execute_script("arguments[0].click();", r12_approval_management_training_2)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def ebusiness_suit_development_erp_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_153'][name^='jform[groups][]'][type='checkbox'][value='153']").get_attribute("checked")
    if not isChecked == 'true':
        ebusiness_suit_development_erp_training = driver.find_element_by_xpath('//*[@id="1group_153"]')
        driver.execute_script("arguments[0].click();", ebusiness_suit_development_erp_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def workflow_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_172'][name^='jform[groups][]'][type='checkbox'][value='172']").get_attribute("checked")
    if not isChecked == 'true':
        workflow_training = driver.find_element_by_xpath('//*[@id="1group_172"]')
        driver.execute_script("arguments[0].click();", workflow_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def bi_publisher_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_154'][name^='jform[groups][]'][type='checkbox'][value='154']").get_attribute("checked")
    if not isChecked == 'true':
        bi_publisher_training = driver.find_element_by_xpath('//*[@id="1group_154"]')
        driver.execute_script("arguments[0].click();", bi_publisher_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def ebs_techno_functional_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_243'][name^='jform[groups][]'][type='checkbox'][value='243']").get_attribute("checked")
    if not isChecked == 'true':
        ebs_techno_functional_training = driver.find_element_by_xpath('//*[@id="1group_243"]')
        driver.execute_script("arguments[0].click();", ebs_techno_functional_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def fusion_hcm_reporting_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_279'][name^='jform[groups][]'][type='checkbox'][value='279']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_hcm_reporting_training = driver.find_element_by_xpath('//*[@id="1group_279"]')
        driver.execute_script("arguments[0].click();", fusion_hcm_reporting_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_286'][name^='jform[groups][]'][type='checkbox'][value='286']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_instance = driver.find_element_by_xpath('//*[@id="1group_286"]')
        driver.execute_script("arguments[0].click();", fusion_instance)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_fusion_hcm_integration_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_19'][name^='jform[groups][]'][type='checkbox'][value='19']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_hcm_integration_training = driver.find_element_by_xpath('//*[@id="1group_19"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_hcm_integration_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_286'][name^='jform[groups][]'][type='checkbox'][value='286']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_instance = driver.find_element_by_xpath('//*[@id="1group_286"]')
        driver.execute_script("arguments[0].click();", fusion_instance)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def fusion_security_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_273'][name^='jform[groups][]'][type='checkbox'][value='273']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_security_training = driver.find_element_by_xpath('//*[@id="1group_273"]')
        driver.execute_script("arguments[0].click();", fusion_security_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_286'][name^='jform[groups][]'][type='checkbox'][value='286']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_instance = driver.find_element_by_xpath('//*[@id="1group_286"]')
        driver.execute_script("arguments[0].click();", fusion_instance)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_taleo_recruting_and_onboarding_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_181'][name^='jform[groups][]'][type='checkbox'][value='181']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_taleo_recruting_and_onboarding_training = driver.find_element_by_xpath('//*[@id="1group_181"]')
        driver.execute_script("arguments[0].click();", oracle_taleo_recruting_and_onboarding_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_taleo_tcc_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_202'][name^='jform[groups][]'][type='checkbox'][value='202']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_taleo_tcc_training = driver.find_element_by_xpath('//*[@id="1group_202"]')
        driver.execute_script("arguments[0].click();", oracle_taleo_tcc_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def oracle_taleo_integration_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_192'][name^='jform[groups][]'][type='checkbox'][value='192']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_taleo_integration_training = driver.find_element_by_xpath('//*[@id="1group_192"]')
        driver.execute_script("arguments[0].click();", oracle_taleo_integration_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def r1213_administration_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_201'][name^='jform[groups][]'][type='checkbox'][value='201']").get_attribute("checked")
    if not isChecked == 'true':
        r1213_administration_training = driver.find_element_by_xpath('//*[@id="1group_201"]')
        driver.execute_script("arguments[0].click();", r1213_administration_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def Siebel_openUI_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_54'][name^='jform[groups][]'][type='checkbox'][value='54']").get_attribute("checked")
    if not isChecked == 'true':
        Siebel_openUI_training = driver.find_element_by_xpath('//*[@id="1group_54"]')
        driver.execute_script("arguments[0].click();", Siebel_openUI_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def hyperion_financials_management_hfm_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_79'][name^='jform[groups][]'][type='checkbox'][value='79']").get_attribute("checked")
    if not isChecked == 'true':
        hyperion_financials_management_hfm_training = driver.find_element_by_xpath('//*[@id="1group_79"]')
        driver.execute_script("arguments[0].click();", hyperion_financials_management_hfm_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def hyperion_planning_training_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_63'][name^='jform[groups][]'][type='checkbox'][value='63']").get_attribute("checked")
    if not isChecked == 'true':
        hyperion_planning_training = driver.find_element_by_xpath('//*[@id="1group_63"]')
        driver.execute_script("arguments[0].click();", hyperion_planning_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def mastering_hyperion_calculation_manager_single():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_182'][name^='jform[groups][]'][type='checkbox'][value='182']").get_attribute("checked")
    if not isChecked == 'true':
        mastering_hyperion_calculation_manager = driver.find_element_by_xpath('//*[@id="1group_182"]')
        driver.execute_script("arguments[0].click();", mastering_hyperion_calculation_manager)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


################################################  PACKAGES  #################################################
def Fusion_HCM_Technical_Package():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_240'][name^='jform[groups][]'][type='checkbox'][value='240']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_hcm_approval_training = driver.find_element_by_xpath('//*[@id="1group_240"]')
        driver.execute_script("arguments[0].click();", fusion_hcm_approval_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_19'][name^='jform[groups][]'][type='checkbox'][value='19']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_hcm_integration = driver.find_element_by_xpath('//*[@id="1group_19"]')
        driver.execute_script("arguments[0].click();", fusion_hcm_integration)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_271'][name^='jform[groups][]'][type='checkbox'][value='271']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_instance = driver.find_element_by_xpath('//*[@id="1group_271"]')
        driver.execute_script("arguments[0].click();", fusion_instance)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def Hyperion_suit_training_package():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_79'][name^='jform[groups][]'][type='checkbox'][value='79']").get_attribute("checked")
    if not isChecked == 'true':
        hyperion_financials_management_hfm_training = driver.find_element_by_xpath('//*[@id="1group_79"]')
        driver.execute_script("arguments[0].click();", hyperion_financials_management_hfm_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_63'][name^='jform[groups][]'][type='checkbox'][value='63']").get_attribute("checked")
    if not isChecked == 'true':
        hyperion_planning_training = driver.find_element_by_xpath('//*[@id="1group_63"]')
        driver.execute_script("arguments[0].click();", hyperion_planning_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_182'][name^='jform[groups][]'][type='checkbox'][value='182']").get_attribute("checked")
    if not isChecked == 'true':
        mastering_hyperion_calculation_manager = driver.find_element_by_xpath('//*[@id="1group_182"]')
        driver.execute_script("arguments[0].click();", mastering_hyperion_calculation_manager)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def Fusion_middleware_administration_package():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_52'][name^='jform[groups][]'][type='checkbox'][value='52']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_identity_management_training = driver.find_element_by_xpath('//*[@id="1group_52"]')
        driver.execute_script("arguments[0].click();", oracle_identity_management_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_73'][name^='jform[groups][]'][type='checkbox'][value='73']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_access_manager_training = driver.find_element_by_xpath('//*[@id="1group_73"]')
        driver.execute_script("arguments[0].click();", oracle_access_manager_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_47'][name^='jform[groups][]'][type='checkbox'][value='47']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_weblogic_administrator_training = driver.find_element_by_xpath('//*[@id="1group_47"]')
        driver.execute_script("arguments[0].click();", oracle_weblogic_administrator_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_159'][name^='jform[groups][]'][type='checkbox'][value='159']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_entitlement_server_training = driver.find_element_by_xpath('//*[@id="1group_159"]')
        driver.execute_script("arguments[0].click();", oracle_entitlement_server_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_134'][name^='jform[groups][]'][type='checkbox'][value='134']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_middleware_12C_training = driver.find_element_by_xpath('//*[@id="1group_134"]')
        driver.execute_script("arguments[0].click();", fusion_middleware_12C_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_66'][name^='jform[groups][]'][type='checkbox'][value='66']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_goldengate_training = driver.find_element_by_xpath('//*[@id="1group_66"]')
        driver.execute_script("arguments[0].click();", oracle_goldengate_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_171'][name^='jform[groups][]'][type='checkbox'][value='171']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_database_12C_advanced_admininstration_training = driver.find_element_by_xpath('//*[@id="1group_171"]')
        driver.execute_script("arguments[0].click();", oracle_database_12C_advanced_admininstration_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_177'][name^='jform[groups][]'][type='checkbox'][value='177']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_data_guard_administration_training = driver.find_element_by_xpath('//*[@id="1group_177"]')
        driver.execute_script("arguments[0].click();", oracle_data_guard_administration_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_271'][name^='jform[groups][]'][type='checkbox'][value='271']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_instance = driver.find_element_by_xpath('//*[@id="1group_271"]')
        driver.execute_script("arguments[0].click();", fusion_instance)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def EBS_R12_Technical_Package():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_156'][name^='jform[groups][]'][type='checkbox'][value='156']").get_attribute("checked")
    if not isChecked == 'true':
        r12_approval_management_training_1 = driver.find_element_by_xpath('//*[@id="1group_156"]')
        driver.execute_script("arguments[0].click();", r12_approval_management_training_1)


    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_230'][name^='jform[groups][]'][type='checkbox'][value='230']").get_attribute("checked")
    if not isChecked == 'true':
        r12_approval_management_training_2 = driver.find_element_by_xpath('//*[@id="1group_230"]')
        driver.execute_script("arguments[0].click();", r12_approval_management_training_2)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_145'][name^='jform[groups][]'][type='checkbox'][value='145']").get_attribute("checked")
    if not isChecked == 'true':
        apps_dba_training = driver.find_element_by_xpath('//*[@id="1group_145"]')
        driver.execute_script("arguments[0].click();", apps_dba_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_41'][name^='jform[groups][]'][type='checkbox'][value='41']").get_attribute("checked")
    if not isChecked == 'true':
        oaf_training = driver.find_element_by_xpath('//*[@id="1group_41"]')
        driver.execute_script("arguments[0].click();", oaf_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_136'][name^='jform[groups][]'][type='checkbox'][value='136']").get_attribute("checked")
    if not isChecked == 'true':
        r12_financial_accounting_hub_training = driver.find_element_by_xpath('//*[@id="1group_136"]')
        driver.execute_script("arguments[0].click();", r12_financial_accounting_hub_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_153'][name^='jform[groups][]'][type='checkbox'][value='153']").get_attribute("checked")
    if not isChecked == 'true':
        ebusiness_suit_development_erp_training = driver.find_element_by_xpath('//*[@id="1group_153"]')
        driver.execute_script("arguments[0].click();", ebusiness_suit_development_erp_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_230'][name^='jform[groups][]'][type='checkbox'][value='230']").get_attribute("checked")
    if not isChecked == 'true':
        r1213_administration_training = driver.find_element_by_xpath('//*[@id="1group_230"]')
        driver.execute_script("arguments[0].click();", r1213_administration_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_172'][name^='jform[groups][]'][type='checkbox'][value='172']").get_attribute("checked")
    if not isChecked == 'true':
        workflow_training = driver.find_element_by_xpath('//*[@id="1group_172"]')
        driver.execute_script("arguments[0].click();", workflow_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_154'][name^='jform[groups][]'][type='checkbox'][value='154']").get_attribute("checked")
    if not isChecked == 'true':
        bi_publisher_training = driver.find_element_by_xpath('//*[@id="1group_154"]')
        driver.execute_script("arguments[0].click();", bi_publisher_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_243'][name^='jform[groups][]'][type='checkbox'][value='243']").get_attribute("checked")
    if not isChecked == 'true':
        ebs_techno_functional_training = driver.find_element_by_xpath('//*[@id="1group_243"]')
        driver.execute_script("arguments[0].click();", ebs_techno_functional_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_54'][name^='jform[groups][]'][type='checkbox'][value='54']").get_attribute("checked")
    if not isChecked == 'true':
        Siebel_openUI_training = driver.find_element_by_xpath('//*[@id="1group_54"]')
        driver.execute_script("arguments[0].click();", Siebel_openUI_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def Fusion_HCM_functional_package():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_44'][name^='jform[groups][]'][type='checkbox'][value='44']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_fundamentals_training = driver.find_element_by_xpath('//*[@id="1group_44"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_fundamentals_training)


    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_35'][name^='jform[groups][]'][type='checkbox'][value='35']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_hcm_core_training = driver.find_element_by_xpath('//*[@id="1group_35"]')
        driver.execute_script("arguments[0].click();", fusion_hcm_core_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_30'][name^='jform[groups][]'][type='checkbox'][value='30']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_talent_management_training = driver.find_element_by_xpath('//*[@id="1group_30"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_talent_management_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_64'][name^='jform[groups][]'][type='checkbox'][value='64']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_benefits_training_1 = driver.find_element_by_xpath('//*[@id="1group_64"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_benefits_training_1)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_283'][name^='jform[groups][]'][type='checkbox'][value='283']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_benefits_training_2 = driver.find_element_by_xpath('//*[@id="1group_283"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_benefits_training_2)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_239'][name^='jform[groups][]'][type='checkbox'][value='239']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_payroll_training = driver.find_element_by_xpath('//*[@id="1group_239"]')
        driver.execute_script("arguments[0].click();", fusion_payroll_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_45'][name^='jform[groups][]'][type='checkbox'][value='45']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_fastformula = driver.find_element_by_xpath('//*[@id="1group_45"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_fastformula)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_29'][name^='jform[groups][]'][type='checkbox'][value='29']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_compensation_workbench = driver.find_element_by_xpath('//*[@id="1group_29"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_compensation_workbench)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_240'][name^='jform[groups][]'][type='checkbox'][value='240']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_hcm_approval_management = driver.find_element_by_xpath('//*[@id="1group_240"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_hcm_approval_management)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_241'][name^='jform[groups][]'][type='checkbox'][value='241']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_time_and_labour_training = driver.find_element_by_xpath('//*[@id="1group_241"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_time_and_labour_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_245'][name^='jform[groups][]'][type='checkbox'][value='245']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_hcm_for_ebs_hcm_experts_training = driver.find_element_by_xpath('//*[@id="1group_245"]')
        driver.execute_script("arguments[0].click();", fusion_hcm_for_ebs_hcm_experts_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_271'][name^='jform[groups][]'][type='checkbox'][value='271']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_instance = driver.find_element_by_xpath('//*[@id="1group_271"]')
        driver.execute_script("arguments[0].click();", fusion_instance)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()



def R12_Fusion_Apps_Training():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_39'][name^='jform[groups][]'][type='checkbox'][value='39']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_procurement_training = driver.find_element_by_xpath('//*[@id="1group_39"]')
        driver.execute_script("arguments[0].click();", fusion_procurement_training)


    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_239'][name^='jform[groups][]'][type='checkbox'][value='239']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_payroll_training = driver.find_element_by_xpath('//*[@id="1group_239"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_payroll_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_29'][name^='jform[groups][]'][type='checkbox'][value='29']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_compensation_workbench_traning = driver.find_element_by_xpath('//*[@id="1group_29"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_compensation_workbench_traning)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_35'][name^='jform[groups][]'][type='checkbox'][value='35']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_hcm_core_training = driver.find_element_by_xpath('//*[@id="1group_35"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_hcm_core_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_277'][name^='jform[groups][]'][type='checkbox'][value='277']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_hcm_technical_training = driver.find_element_by_xpath('//*[@id="1group_277"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_hcm_technical_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_30'][name^='jform[groups][]'][type='checkbox'][value='30']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_talent_management_training = driver.find_element_by_xpath('//*[@id="1group_30"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_talent_management_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_259'][name^='jform[groups][]'][type='checkbox'][value='259']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_financials_accounting_hub_training_1 = driver.find_element_by_xpath('//*[@id="1group_259"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_financials_accounting_hub_training_1)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_46'][name^='jform[groups][]'][type='checkbox'][value='46']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_financials_accounting_hub_training_2 = driver.find_element_by_xpath('//*[@id="1group_46"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_financials_accounting_hub_training_2)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_62'][name^='jform[groups][]'][type='checkbox'][value='62']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_procure_to_pay_training = driver.find_element_by_xpath('//*[@id="1group_62"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_procure_to_pay_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_45'][name^='jform[groups][]'][type='checkbox'][value='45']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_fastformula_training = driver.find_element_by_xpath('//*[@id="1group_45"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_fastformula_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_44'][name^='jform[groups][]'][type='checkbox'][value='44']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_application_fundamental_training = driver.find_element_by_xpath('//*[@id="1group_44"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_application_fundamental_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_115'][name^='jform[groups][]'][type='checkbox'][value='115']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_application_installation_and_patching_R9_training = driver.find_element_by_xpath('//*[@id="1group_115"]')
        driver.execute_script("arguments[0].click();", fusion_application_installation_and_patching_R9_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_83'][name^='jform[groups][]'][type='checkbox'][value='83']").get_attribute("checked")
    if not isChecked == 'true':
        development_in_fusion_applications = driver.find_element_by_xpath('//*[@id="1group_83"]')
        driver.execute_script("arguments[0].click();", development_in_fusion_applications)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_50'][name^='jform[groups][]'][type='checkbox'][value='50']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_financials_training = driver.find_element_by_xpath('//*[@id="1group_50"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_financials_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_123'][name^='jform[groups][]'][type='checkbox'][value='123']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_BI_reproting_and_OTBI_training_in_fusion_apps_1 = driver.find_element_by_xpath('//*[@id="1group_123"]')
        driver.execute_script("arguments[0].click();", oracle_BI_reproting_and_OTBI_training_in_fusion_apps_1)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_135'][name^='jform[groups][]'][type='checkbox'][value='135']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_BI_reproting_and_OTBI_training_in_fusion_apps_2 = driver.find_element_by_xpath('//*[@id="1group_135"]')
        driver.execute_script("arguments[0].click();", oracle_BI_reproting_and_OTBI_training_in_fusion_apps_2)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_229'][name^='jform[groups][]'][type='checkbox'][value='229']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_accounts_receivable_training = driver.find_element_by_xpath('//*[@id="1group_229"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_accounts_receivable_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_256'][name^='jform[groups][]'][type='checkbox'][value='256']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_financials_cloud_tax_training = driver.find_element_by_xpath('//*[@id="1group_256"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_financials_cloud_tax_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_145'][name^='jform[groups][]'][type='checkbox'][value='145']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_apps_DBA = driver.find_element_by_xpath('//*[@id="1group_145"]')
        driver.execute_script("arguments[0].click();", oracle_apps_DBA)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_49'][name^='jform[groups][]'][type='checkbox'][value='49']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_EBS_R12_inventory_order_management_and_purchasing_training = driver.find_element_by_xpath(
            '//*[@id="1group_49"]')
        driver.execute_script("arguments[0].click();", oracle_EBS_R12_inventory_order_management_and_purchasing_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_43'][name^='jform[groups][]'][type='checkbox'][value='43']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_R12_subledger_accounting_training = driver.find_element_by_xpath('//*[@id="1group_43"]')
        driver.execute_script("arguments[0].click();", oracle_R12_subledger_accounting_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_117'][name^='jform[groups][]'][type='checkbox'][value='117']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_EBS_R12_functional_financial_training = driver.find_element_by_xpath('//*[@id="1group_117"]')
        driver.execute_script("arguments[0].click();", oracle_EBS_R12_functional_financial_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_41'][name^='jform[groups][]'][type='checkbox'][value='41']").get_attribute("checked")
    if not isChecked == 'true':
        OA_framework_training = driver.find_element_by_xpath('//*[@id="1group_41"]')
        driver.execute_script("arguments[0].click();", OA_framework_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_48'][name^='jform[groups][]'][type='checkbox'][value='48']").get_attribute("checked")
    if not isChecked == 'true':
        R12_advanced_global_intercompany_system_AGIS_training = driver.find_element_by_xpath('//*[@id="1group_48"]')
        driver.execute_script("arguments[0].click();", R12_advanced_global_intercompany_system_AGIS_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_128'][name^='jform[groups][]'][type='checkbox'][value='128']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_EBusiness_tax_training_1 = driver.find_element_by_xpath('//*[@id="1group_128"]')
        driver.execute_script("arguments[0].click();", oracle_EBusiness_tax_training_1)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_252'][name^='jform[groups][]'][type='checkbox'][value='252']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_EBusiness_tax_training_2 = driver.find_element_by_xpath('//*[@id="1group_252"]')
        driver.execute_script("arguments[0].click();", oracle_EBusiness_tax_training_2)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_65'][name^='jform[groups][]'][type='checkbox'][value='65']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_demantra_training = driver.find_element_by_xpath('//*[@id="1group_65"]')
        driver.execute_script("arguments[0].click();", oracle_demantra_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_144'][name^='jform[groups][]'][type='checkbox'][value='144']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_R12_HRMS_payroll_training = driver.find_element_by_xpath('//*[@id="1group_144"]')
        driver.execute_script("arguments[0].click();", oracle_R12_HRMS_payroll_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_149'][name^='jform[groups][]'][type='checkbox'][value='149']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_implement_configurator_training = driver.find_element_by_xpath('//*[@id="1group_149"]')
        driver.execute_script("arguments[0].click();", oracle_implement_configurator_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_138'][name^='jform[groups][]'][type='checkbox'][value='138']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_R12_project_accounting_training = driver.find_element_by_xpath('//*[@id="1group_138"]')
        driver.execute_script("arguments[0].click();", oracle_R12_project_accounting_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_137'][name^='jform[groups][]'][type='checkbox'][value='137']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_R12_advance_supply_chain_planning_training = driver.find_element_by_xpath('//*[@id="1group_137"]')
        driver.execute_script("arguments[0].click();", oracle_R12_advance_supply_chain_planning_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_136'][name^='jform[groups][]'][type='checkbox'][value='136']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_R12_financial_accounting_hub_training = driver.find_element_by_xpath('//*[@id="1group_136"]')
        driver.execute_script("arguments[0].click();", oracle_R12_financial_accounting_hub_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_271'][name^='jform[groups][]'][type='checkbox'][value='271']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_instance = driver.find_element_by_xpath('//*[@id="1group_271"]')
        driver.execute_script("arguments[0].click();", fusion_instance)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()



def Fusion_middleware_development_package():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_131'][name^='jform[groups][]'][type='checkbox'][value='131']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_business_intelligence_applications_training = driver.find_element_by_xpath('//*[@id="1group_131"]')
        driver.execute_script("arguments[0].click();", oracle_business_intelligence_applications_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_56'][name^='jform[groups][]'][type='checkbox'][value='56']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_business_intelligence_enterprise_edition_training = driver.find_element_by_xpath('//*[@id="1group_56"]')
        driver.execute_script("arguments[0].click();", oracle_business_intelligence_enterprise_edition_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_76'][name^='jform[groups][]'][type='checkbox'][value='76']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_adf_training = driver.find_element_by_xpath('//*[@id="1group_76"]')
        driver.execute_script("arguments[0].click();", oracle_adf_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_130'][name^='jform[groups][]'][type='checkbox'][value='130']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_business_process_management_training = driver.find_element_by_xpath('//*[@id="1group_130"]')
        driver.execute_script("arguments[0].click();", oracle_business_process_management_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_40'][name^='jform[groups][]'][type='checkbox'][value='40']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_soa_BPEL_mediator_OBS_development_training_1 = driver.find_element_by_xpath('//*[@id="1group_40"]')
        driver.execute_script("arguments[0].click();", oracle_soa_BPEL_mediator_OBS_development_training_1)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_122'][name^='jform[groups][]'][type='checkbox'][value='122']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_soa_BPEL_mediator_OBS_development_training_12C = driver.find_element_by_xpath('//*[@id="1group_122"]')
        driver.execute_script("arguments[0].click();", oracle_soa_BPEL_mediator_OBS_development_training_12C)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_126'][name^='jform[groups][]'][type='checkbox'][value='126']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_data_integrator_training = driver.find_element_by_xpath('//*[@id="1group_126"]')
        driver.execute_script("arguments[0].click();", oracle_data_integrator_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_113'][name^='jform[groups][]'][type='checkbox'][value='113']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_mobile_application_framework_training = driver.find_element_by_xpath('//*[@id="1group_113"]')
        driver.execute_script("arguments[0].click();", oracle_mobile_application_framework_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_129'][name^='jform[groups][]'][type='checkbox'][value='129']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_java_xml_and_web_service_training = driver.find_element_by_xpath('//*[@id="1group_129"]')
        driver.execute_script("arguments[0].click();", oracle_java_xml_and_web_service_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_155'][name^='jform[groups][]'][type='checkbox'][value='155']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_sql_and_plSQL_training = driver.find_element_by_xpath('//*[@id="1group_155"]')
        driver.execute_script("arguments[0].click();", oracle_sql_and_plSQL_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()



def Fusion_financials_technical_package():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_253'][name^='jform[groups][]'][type='checkbox'][value='253']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_financials_integration_training = driver.find_element_by_xpath('//*[@id="1group_253"]')
        driver.execute_script("arguments[0].click();", fusion_financials_integration_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_268'][name^='jform[groups][]'][type='checkbox'][value='268']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_financials_security_training_1 = driver.find_element_by_xpath('//*[@id="1group_268"]')
        driver.execute_script("arguments[0].click();", fusion_financials_security_training_1)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_272'][name^='jform[groups][]'][type='checkbox'][value='272']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_financials_security_training_2 = driver.find_element_by_xpath('//*[@id="1group_272"]')
        driver.execute_script("arguments[0].click();", fusion_financials_security_training_2)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_235'][name^='jform[groups][]'][type='checkbox'][value='235']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_financials_reporting_training = driver.find_element_by_xpath('//*[@id="1group_235"]')
        driver.execute_script("arguments[0].click();", fusion_financials_reporting_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_209'][name^='jform[groups][]'][type='checkbox'][value='209']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_financials_approval_management_training = driver.find_element_by_xpath('//*[@id="1group_209"]')
        driver.execute_script("arguments[0].click();", fusion_financials_approval_management_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_271'][name^='jform[groups][]'][type='checkbox'][value='271']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_instance = driver.find_element_by_xpath('//*[@id="1group_271"]')
        driver.execute_script("arguments[0].click();", fusion_instance)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()



def Fusion_cloud_common_technology_package():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_83'][name^='jform[groups][]'][type='checkbox'][value='83']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_application_development_training = driver.find_element_by_xpath('//*[@id="1group_83"]')
        driver.execute_script("arguments[0].click();", fusion_application_development_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_115'][name^='jform[groups][]'][type='checkbox'][value='115']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_application_installation_and_patching_r9_training = driver.find_element_by_xpath('//*[@id="1group_115"]')
        driver.execute_script("arguments[0].click();", fusion_application_installation_and_patching_r9_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_250'][name^='jform[groups][]'][type='checkbox'][value='250']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_integration_cloud_Service_training = driver.find_element_by_xpath('//*[@id="1group_250"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_integration_cloud_Service_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_204'][name^='jform[groups][]'][type='checkbox'][value='204']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_sales_cloud_extensibility_training = driver.find_element_by_xpath('//*[@id="1group_204"]')
        driver.execute_script("arguments[0].click();", oracle_sales_cloud_extensibility_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_271'][name^='jform[groups][]'][type='checkbox'][value='271']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_instance = driver.find_element_by_xpath('//*[@id="1group_271"]')
        driver.execute_script("arguments[0].click();", fusion_instance)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def Fusion_financials_functional_package():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_39'][name^='jform[groups][]'][type='checkbox'][value='39']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_procurement_training = driver.find_element_by_xpath('//*[@id="1group_39"]')
        driver.execute_script("arguments[0].click();", fusion_procurement_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_259'][name^='jform[groups][]'][type='checkbox'][value='259']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_financials_accounting_hub_training_1 = driver.find_element_by_xpath('//*[@id="1group_259"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_financials_accounting_hub_training_1)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_46'][name^='jform[groups][]'][type='checkbox'][value='46']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_financials_accounting_hub_training_2 = driver.find_element_by_xpath('//*[@id="1group_46"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_financials_accounting_hub_training_2)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_50'][name^='jform[groups][]'][type='checkbox'][value='50']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_financials_training = driver.find_element_by_xpath('//*[@id="1group_50"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_financials_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_229'][name^='jform[groups][]'][type='checkbox'][value='229']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_accounts_receivable_trainings = driver.find_element_by_xpath('//*[@id="1group_229"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_accounts_receivable_trainings)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_28'][name^='jform[groups][]'][type='checkbox'][value='28']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_account_payable_training = driver.find_element_by_xpath('//*[@id="1group_28"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_account_payable_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_231'][name^='jform[groups][]'][type='checkbox'][value='231']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_general_ledger_training = driver.find_element_by_xpath('//*[@id="1group_231"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_general_ledger_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_256'][name^='jform[groups][]'][type='checkbox'][value='256']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_tax_training = driver.find_element_by_xpath('//*[@id="1group_256"]')
        driver.execute_script("arguments[0].click();", fusion_tax_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_220'][name^='jform[groups][]'][type='checkbox'][value='220']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_fixed_asset_training = driver.find_element_by_xpath('//*[@id="1group_220"]')
        driver.execute_script("arguments[0].click();", fusion_fixed_asset_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_271'][name^='jform[groups][]'][type='checkbox'][value='271']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_instance = driver.find_element_by_xpath('//*[@id="1group_271"]')
        driver.execute_script("arguments[0].click();", fusion_instance)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def Fusion_trainings_package():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_39'][name^='jform[groups][]'][type='checkbox'][value='39']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_procurement_training = driver.find_element_by_xpath('//*[@id="1group_39"]')
        driver.execute_script("arguments[0].click();", fusion_procurement_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_239'][name^='jform[groups][]'][type='checkbox'][value='239']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_payroll_training = driver.find_element_by_xpath('//*[@id="1group_239"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_payroll_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_29'][name^='jform[groups][]'][type='checkbox'][value='29']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_compensation_workbench_traning = driver.find_element_by_xpath('//*[@id="1group_29"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_compensation_workbench_traning)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_35'][name^='jform[groups][]'][type='checkbox'][value='35']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_hcm_core_training = driver.find_element_by_xpath('//*[@id="1group_35"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_hcm_core_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_277'][name^='jform[groups][]'][type='checkbox'][value='277']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_hcm_technical_training = driver.find_element_by_xpath('//*[@id="1group_277"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_hcm_technical_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_30'][name^='jform[groups][]'][type='checkbox'][value='30']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_talent_management_training = driver.find_element_by_xpath('//*[@id="1group_30"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_talent_management_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_259'][name^='jform[groups][]'][type='checkbox'][value='259']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_financials_accounting_hub_training_1 = driver.find_element_by_xpath('//*[@id="1group_259"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_financials_accounting_hub_training_1)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_46'][name^='jform[groups][]'][type='checkbox'][value='46']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_financials_accounting_hub_training_2 = driver.find_element_by_xpath('//*[@id="1group_46"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_financials_accounting_hub_training_2)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_62'][name^='jform[groups][]'][type='checkbox'][value='62']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_procure_to_pay_training = driver.find_element_by_xpath('//*[@id="1group_62"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_procure_to_pay_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_45'][name^='jform[groups][]'][type='checkbox'][value='45']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_fastformula_training = driver.find_element_by_xpath('//*[@id="1group_45"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_fastformula_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_44'][name^='jform[groups][]'][type='checkbox'][value='44']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_application_fundamental_training = driver.find_element_by_xpath('//*[@id="1group_44"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_application_fundamental_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_115'][name^='jform[groups][]'][type='checkbox'][value='115']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_application_installation_and_patching_R9_training = driver.find_element_by_xpath('//*[@id="1group_115"]')
        driver.execute_script("arguments[0].click();", fusion_application_installation_and_patching_R9_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_83'][name^='jform[groups][]'][type='checkbox'][value='83']").get_attribute("checked")
    if not isChecked == 'true':
        development_in_fusion_applications = driver.find_element_by_xpath('//*[@id="1group_83"]')
        driver.execute_script("arguments[0].click();", development_in_fusion_applications)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_50'][name^='jform[groups][]'][type='checkbox'][value='50']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_financials_training = driver.find_element_by_xpath('//*[@id="1group_50"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_financials_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_123'][name^='jform[groups][]'][type='checkbox'][value='123']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_BI_reproting_and_OTBI_training_in_fusion_apps_1 = driver.find_element_by_xpath('//*[@id="1group_123"]')
        driver.execute_script("arguments[0].click();", oracle_BI_reproting_and_OTBI_training_in_fusion_apps_1)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_135'][name^='jform[groups][]'][type='checkbox'][value='135']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_BI_reproting_and_OTBI_training_in_fusion_apps_2 = driver.find_element_by_xpath('//*[@id="1group_135"]')
        driver.execute_script("arguments[0].click();", oracle_BI_reproting_and_OTBI_training_in_fusion_apps_2)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_229'][name^='jform[groups][]'][type='checkbox'][value='229']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_accounts_receivable_training = driver.find_element_by_xpath('//*[@id="1group_229"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_accounts_receivable_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_256'][name^='jform[groups][]'][type='checkbox'][value='256']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_financials_cloud_tax_training = driver.find_element_by_xpath('//*[@id="1group_256"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_financials_cloud_tax_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_238'][name^='jform[groups][]'][type='checkbox'][value='238']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_project_portfolio_management_training = driver.find_element_by_xpath('//*[@id="1group_238"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_project_portfolio_management_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_268'][name^='jform[groups][]'][type='checkbox'][value='268']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_financials_Security_training_1 = driver.find_element_by_xpath('//*[@id="1group_268"]')
        driver.execute_script("arguments[0].click();", fusion_financials_Security_training_1)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_272'][name^='jform[groups][]'][type='checkbox'][value='272']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_financials_Security_training_2 = driver.find_element_by_xpath('//*[@id="1group_272"]')
        driver.execute_script("arguments[0].click();", fusion_financials_Security_training_2)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_19'][name^='jform[groups][]'][type='checkbox'][value='19']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_integration_training = driver.find_element_by_xpath('//*[@id="1group_19"]')
        driver.execute_script("arguments[0].click();", fusion_integration_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_28'][name^='jform[groups][]'][type='checkbox'][value='28']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_account_payable_training = driver.find_element_by_xpath('//*[@id="1group_28"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_account_payable_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_231'][name^='jform[groups][]'][type='checkbox'][value='231']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_general_ledger_training = driver.find_element_by_xpath('//*[@id="1group_231"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_general_ledger_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_240'][name^='jform[groups][]'][type='checkbox'][value='240']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_hcm_approval_management = driver.find_element_by_xpath('//*[@id="1group_240"]')
        driver.execute_script("arguments[0].click();", fusion_hcm_approval_management)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_64'][name^='jform[groups][]'][type='checkbox'][value='64']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_benefits_training_1 = driver.find_element_by_xpath('//*[@id="1group_64"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_benefits_training_1)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_283'][name^='jform[groups][]'][type='checkbox'][value='283']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_benefits_training_2 = driver.find_element_by_xpath('//*[@id="1group_283"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_benefits_training_2)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_271'][name^='jform[groups][]'][type='checkbox'][value='271']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_instance = driver.find_element_by_xpath('//*[@id="1group_271"]')
        driver.execute_script("arguments[0].click();", fusion_instance)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def Oracle_EBS_R12_functional_package():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_49'][name^='jform[groups][]'][type='checkbox'][value='49']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_ebs_R12_inventory_order_management_and_purchasing_training = driver.find_element_by_xpath(
            '//*[@id="1group_49"]')
        driver.execute_script("arguments[0].click();",
                              oracle_ebs_R12_inventory_order_management_and_purchasing_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_43'][name^='jform[groups][]'][type='checkbox'][value='43']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_R12_subledger_accounting_training = driver.find_element_by_xpath('//*[@id="1group_43"]')
        driver.execute_script("arguments[0].click();", oracle_R12_subledger_accounting_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_117'][name^='jform[groups][]'][type='checkbox'][value='117']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_ebs_R12_functional_financials_training = driver.find_element_by_xpath('//*[@id="1group_117"]')
        driver.execute_script("arguments[0].click();", oracle_ebs_R12_functional_financials_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_48'][name^='jform[groups][]'][type='checkbox'][value='48']").get_attribute("checked")
    if not isChecked == 'true':
        R12_advance_global_intercompany_system_training = driver.find_element_by_xpath('//*[@id="1group_48"]')
        driver.execute_script("arguments[0].click();", R12_advance_global_intercompany_system_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_128'][name^='jform[groups][]'][type='checkbox'][value='128']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_EBusiness_tax_training_1 = driver.find_element_by_xpath('//*[@id="1group_128"]')
        driver.execute_script("arguments[0].click();", oracle_EBusiness_tax_training_1)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_252'][name^='jform[groups][]'][type='checkbox'][value='252']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_EBusiness_tax_training_2 = driver.find_element_by_xpath('//*[@id="1group_252"]')
        driver.execute_script("arguments[0].click();", oracle_EBusiness_tax_training_2)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_65'][name^='jform[groups][]'][type='checkbox'][value='65']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_demantra_training = driver.find_element_by_xpath('//*[@id="1group_65"]')
        driver.execute_script("arguments[0].click();", oracle_demantra_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_144'][name^='jform[groups][]'][type='checkbox'][value='144']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_R12_HRMS_payroll_training = driver.find_element_by_xpath('//*[@id="1group_144"]')
        driver.execute_script("arguments[0].click();", oracle_R12_HRMS_payroll_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_149'][name^='jform[groups][]'][type='checkbox'][value='149']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_impelment_configurator_training = driver.find_element_by_xpath('//*[@id="1group_149"]')
        driver.execute_script("arguments[0].click();", oracle_impelment_configurator_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_138'][name^='jform[groups][]'][type='checkbox'][value='138']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_R12_project_accounting_training = driver.find_element_by_xpath('//*[@id="1group_138"]')
        driver.execute_script("arguments[0].click();", oracle_R12_project_accounting_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_137'][name^='jform[groups][]'][type='checkbox'][value='137']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_R12_Advance_supply_chain_palnning_training = driver.find_element_by_xpath('//*[@id="1group_137"]')
        driver.execute_script("arguments[0].click();", oracle_R12_Advance_supply_chain_palnning_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_194'][name^='jform[groups][]'][type='checkbox'][value='194']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_business_suit_fundamentals_training = driver.find_element_by_xpath('//*[@id="1group_194"]')
        driver.execute_script("arguments[0].click();", oracle_business_suit_fundamentals_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_212'][name^='jform[groups][]'][type='checkbox'][value='212']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_R12_iprocurement_training = driver.find_element_by_xpath('//*[@id="1group_212"]')
        driver.execute_script("arguments[0].click();", oracle_R12_iprocurement_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_206'][name^='jform[groups][]'][type='checkbox'][value='206']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_ebs_R12_service_contract_training = driver.find_element_by_xpath('//*[@id="1group_206"]')
        driver.execute_script("arguments[0].click();", oracle_ebs_R12_service_contract_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_216'][name^='jform[groups][]'][type='checkbox'][value='216']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_ebs_R12_fixed_assets_training = driver.find_element_by_xpath('//*[@id="1group_216"]')
        driver.execute_script("arguments[0].click();", oracle_ebs_R12_fixed_assets_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_219'][name^='jform[groups][]'][type='checkbox'][value='219']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_transportation_management_training = driver.find_element_by_xpath('//*[@id="1group_219"]')
        driver.execute_script("arguments[0].click();", oracle_transportation_management_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_263'][name^='jform[groups][]'][type='checkbox'][value='263']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_demantra_ptp_training = driver.find_element_by_xpath('//*[@id="1group_263"]')
        driver.execute_script("arguments[0].click();", oracle_demantra_ptp_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def Fusion_HCM_Modules_Package():
    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_35'][name^='jform[groups][]'][type='checkbox'][value='35']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_hcm_core_training = driver.find_element_by_xpath('//*[@id="1group_35"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_hcm_core_training)


    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_30'][name^='jform[groups][]'][type='checkbox'][value='30']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_talent_management_training = driver.find_element_by_xpath('//*[@id="1group_30"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_talent_management_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_64'][name^='jform[groups][]'][type='checkbox'][value='64']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_benefit_training_1 = driver.find_element_by_xpath('//*[@id="1group_64"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_benefit_training_1)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_283'][name^='jform[groups][]'][type='checkbox'][value='283']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_benefit_training_2 = driver.find_element_by_xpath('//*[@id="1group_283"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_benefit_training_2)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_239'][name^='jform[groups][]'][type='checkbox'][value='239']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_payroll_training = driver.find_element_by_xpath('//*[@id="1group_239"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_payroll_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_45'][name^='jform[groups][]'][type='checkbox'][value='45']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_fast_formula = driver.find_element_by_xpath('//*[@id="1group_45"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_fast_formula)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_29'][name^='jform[groups][]'][type='checkbox'][value='29']").get_attribute("checked")
    if not isChecked == 'true':
        compensation_workbench = driver.find_element_by_xpath('//*[@id="1group_29"]')
        driver.execute_script("arguments[0].click();", compensation_workbench)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_240'][name^='jform[groups][]'][type='checkbox'][value='240']").get_attribute("checked")
    if not isChecked == 'true':
        hcm_approval_management = driver.find_element_by_xpath('//*[@id="1group_240"]')
        driver.execute_script("arguments[0].click();", hcm_approval_management)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_277'][name^='jform[groups][]'][type='checkbox'][value='277']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_hcm_technical_training = driver.find_element_by_xpath('//*[@id="1group_277"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_hcm_technical_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_19'][name^='jform[groups][]'][type='checkbox'][value='19']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_hcm_integration_training = driver.find_element_by_xpath('//*[@id="1group_19"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_hcm_integration_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_271'][name^='jform[groups][]'][type='checkbox'][value='271']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_instance = driver.find_element_by_xpath('//*[@id="1group_271"]')
        driver.execute_script("arguments[0].click();", fusion_instance)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def Fusion_HCM_and_Taleo_functional_and_technical_package():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_44'][name^='jform[groups][]'][type='checkbox'][value='44']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_hcm_fundamentals_training = driver.find_element_by_xpath('//*[@id="1group_44"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_hcm_fundamentals_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_35'][name^='jform[groups][]'][type='checkbox'][value='35']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_hcm_core_training = driver.find_element_by_xpath('//*[@id="1group_35"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_hcm_core_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_30'][name^='jform[groups][]'][type='checkbox'][value='30']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_talent_management_training = driver.find_element_by_xpath('//*[@id="1group_30"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_talent_management_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_64'][name^='jform[groups][]'][type='checkbox'][value='64']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_benefits_training_1 = driver.find_element_by_xpath('//*[@id="1group_64"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_benefits_training_1)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_283'][name^='jform[groups][]'][type='checkbox'][value='283']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_benefits_training_2 = driver.find_element_by_xpath('//*[@id="1group_283"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_benefits_training_2)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_239'][name^='jform[groups][]'][type='checkbox'][value='239']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_payroll_training = driver.find_element_by_xpath('//*[@id="1group_239"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_payroll_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_45'][name^='jform[groups][]'][type='checkbox'][value='45']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_fast_formula = driver.find_element_by_xpath('//*[@id="1group_45"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_fast_formula)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_29'][name^='jform[groups][]'][type='checkbox'][value='29']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_compensation_workbench = driver.find_element_by_xpath('//*[@id="1group_29"]')
        driver.execute_script("arguments[0].click();", fusion_compensation_workbench)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_240'][name^='jform[groups][]'][type='checkbox'][value='240']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_hcm_approval_management = driver.find_element_by_xpath('//*[@id="1group_240"]')
        driver.execute_script("arguments[0].click();", fusion_hcm_approval_management)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_241'][name^='jform[groups][]'][type='checkbox'][value='241']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_time_and_labour_training = driver.find_element_by_xpath('//*[@id="1group_241"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_time_and_labour_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_245'][name^='jform[groups][]'][type='checkbox'][value='245']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_hcm_for_ebs_hcm_expert_payroll_training = driver.find_element_by_xpath('//*[@id="1group_245"]')
        driver.execute_script("arguments[0].click();", fusion_hcm_for_ebs_hcm_expert_payroll_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_279'][name^='jform[groups][]'][type='checkbox'][value='279']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_hcm_reporting_training = driver.find_element_by_xpath('//*[@id="1group_279"]')
        driver.execute_script("arguments[0].click();", fusion_hcm_reporting_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_19'][name^='jform[groups][]'][type='checkbox'][value='19']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_hcm_integration_training = driver.find_element_by_xpath('//*[@id="1group_19"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_hcm_integration_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_273'][name^='jform[groups][]'][type='checkbox'][value='273']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_security_training = driver.find_element_by_xpath('//*[@id="1group_273"]')
        driver.execute_script("arguments[0].click();", fusion_security_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_181'][name^='jform[groups][]'][type='checkbox'][value='181']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_taleo_recruting_and_onboarding_training = driver.find_element_by_xpath('//*[@id="1group_181"]')
        driver.execute_script("arguments[0].click();", oracle_taleo_recruting_and_onboarding_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_202'][name^='jform[groups][]'][type='checkbox'][value='202']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_taleo_tcc_training = driver.find_element_by_xpath('//*[@id="1group_202"]')
        driver.execute_script("arguments[0].click();", oracle_taleo_tcc_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_192'][name^='jform[groups][]'][type='checkbox'][value='192']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_taleo_integration_training = driver.find_element_by_xpath('//*[@id="1group_192"]')
        driver.execute_script("arguments[0].click();", oracle_taleo_integration_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_277'][name^='jform[groups][]'][type='checkbox'][value='277']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_hcm_technical = driver.find_element_by_xpath('//*[@id="1group_277"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_hcm_technical)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_271'][name^='jform[groups][]'][type='checkbox'][value='271']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_instance = driver.find_element_by_xpath('//*[@id="1group_271"]')
        driver.execute_script("arguments[0].click();", fusion_instance)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def Fusion_Application_Training_Package():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_50'][name^='jform[groups][]'][type='checkbox'][value='50']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_financials = driver.find_element_by_xpath('//*[@id="1group_50"]')
        driver.execute_script("arguments[0].click();", fusion_financials)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_259'][name^='jform[groups][]'][type='checkbox'][value='259']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_accounting_hub_1 = driver.find_element_by_xpath('//*[@id="1group_259"]')
        driver.execute_script("arguments[0].click();", fusion_accounting_hub_1)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_46'][name^='jform[groups][]'][type='checkbox'][value='46']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_accounting_hub_2 = driver.find_element_by_xpath('//*[@id="1group_46"]')
        driver.execute_script("arguments[0].click();", fusion_accounting_hub_2)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_62'][name^='jform[groups][]'][type='checkbox'][value='62']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_procure_to_pay = driver.find_element_by_xpath('//*[@id="1group_62"]')
        driver.execute_script("arguments[0].click();", fusion_procure_to_pay)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_44'][name^='jform[groups][]'][type='checkbox'][value='44']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_application_fundamentals = driver.find_element_by_xpath('//*[@id="1group_44"]')
        driver.execute_script("arguments[0].click();", fusion_application_fundamentals)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_135'][name^='jform[groups][]'][type='checkbox'][value='135']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_BI_reporting = driver.find_element_by_xpath('//*[@id="1group_135"]')
        driver.execute_script("arguments[0].click();", oracle_BI_reporting)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_123'][name^='jform[groups][]'][type='checkbox'][value='123']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_OTBI = driver.find_element_by_xpath('//*[@id="1group_123"]')
        driver.execute_script("arguments[0].click();", oracle_OTBI)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_271'][name^='jform[groups][]'][type='checkbox'][value='271']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_instance = driver.find_element_by_xpath('//*[@id="1group_271"]')
        driver.execute_script("arguments[0].click();", fusion_instance)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def Fusion_Apps_Training_Package():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_39'][name^='jform[groups][]'][type='checkbox'][value='39']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_procurement_training = driver.find_element_by_xpath('//*[@id="1group_39"]')
        driver.execute_script("arguments[0].click();", fusion_procurement_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_239'][name^='jform[groups][]'][type='checkbox'][value='239']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_payroll_training = driver.find_element_by_xpath('//*[@id="1group_239"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_payroll_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_29'][name^='jform[groups][]'][type='checkbox'][value='29']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_compensation_workbench_training = driver.find_element_by_xpath('//*[@id="1group_29"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_compensation_workbench_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_35'][name^='jform[groups][]'][type='checkbox'][value='35']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_HCM_core_training = driver.find_element_by_xpath('//*[@id="1group_35"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_HCM_core_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_277'][name^='jform[groups][]'][type='checkbox'][value='277']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_HCM_technical_training = driver.find_element_by_xpath('//*[@id="1group_277"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_HCM_technical_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_30'][name^='jform[groups][]'][type='checkbox'][value='30']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_talent_management_training = driver.find_element_by_xpath('//*[@id="1group_30"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_talent_management_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_259'][name^='jform[groups][]'][type='checkbox'][value='259']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_financial_accounting_hub_training_1 = driver.find_element_by_xpath('//*[@id="1group_259"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_financial_accounting_hub_training_1)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_46'][name^='jform[groups][]'][type='checkbox'][value='46']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_financial_accounting_hub_training_2 = driver.find_element_by_xpath('//*[@id="1group_46"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_financial_accounting_hub_training_2)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_62'][name^='jform[groups][]'][type='checkbox'][value='62']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_procure_to_pay_training = driver.find_element_by_xpath('//*[@id="1group_62"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_procure_to_pay_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_45'][name^='jform[groups][]'][type='checkbox'][value='45']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_fastformula_training = driver.find_element_by_xpath('//*[@id="1group_45"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_fastformula_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_44'][name^='jform[groups][]'][type='checkbox'][value='44']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_applications_fundamental_training = driver.find_element_by_xpath('//*[@id="1group_44"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_applications_fundamental_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_115'][name^='jform[groups][]'][type='checkbox'][value='115']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_applications_installation_and_patching_R9_training = driver.find_element_by_xpath('//*[@id="1group_115"]')
        driver.execute_script("arguments[0].click();", fusion_applications_installation_and_patching_R9_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_83'][name^='jform[groups][]'][type='checkbox'][value='83']").get_attribute("checked")
    if not isChecked == 'true':
        development_in_fusion_applications = driver.find_element_by_xpath('//*[@id="1group_83"]')
        driver.execute_script("arguments[0].click();", development_in_fusion_applications)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_50'][name^='jform[groups][]'][type='checkbox'][value='50']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_financials_training = driver.find_element_by_xpath('//*[@id="1group_50"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_financials_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_123'][name^='jform[groups][]'][type='checkbox'][value='123']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_BI_reporting_and_OTBI_training_in_fusion_apps_1 = driver.find_element_by_xpath('//*[@id="1group_123"]')
        driver.execute_script("arguments[0].click();", oracle_BI_reporting_and_OTBI_training_in_fusion_apps_1)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_135'][name^='jform[groups][]'][type='checkbox'][value='135']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_BI_reporting_and_OTBI_training_in_fusion_apps_2 = driver.find_element_by_xpath('//*[@id="1group_135"]')
        driver.execute_script("arguments[0].click();", oracle_BI_reporting_and_OTBI_training_in_fusion_apps_2)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_229'][name^='jform[groups][]'][type='checkbox'][value='229']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_account_receivable_training = driver.find_element_by_xpath('//*[@id="1group_229"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_account_receivable_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_28'][name^='jform[groups][]'][type='checkbox'][value='28']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_account_payable_training = driver.find_element_by_xpath('//*[@id="1group_28"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_account_payable_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_231'][name^='jform[groups][]'][type='checkbox'][value='231']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_general_ledger_training = driver.find_element_by_xpath('//*[@id="1group_231"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_general_ledger_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_238'][name^='jform[groups][]'][type='checkbox'][value='238']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_project_portfolio_management_training = driver.find_element_by_xpath('//*[@id="1group_238"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_project_portfolio_management_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_268'][name^='jform[groups][]'][type='checkbox'][value='268']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_financials_security_training_1 = driver.find_element_by_xpath('//*[@id="1group_268"]')
        driver.execute_script("arguments[0].click();", fusion_financials_security_training_1)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_272'][name^='jform[groups][]'][type='checkbox'][value='272']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_financials_security_training_2 = driver.find_element_by_xpath('//*[@id="1group_272"]')
        driver.execute_script("arguments[0].click();", fusion_financials_security_training_2)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_235'][name^='jform[groups][]'][type='checkbox'][value='235']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_financials_reporting_training = driver.find_element_by_xpath('//*[@id="1group_235"]')
        driver.execute_script("arguments[0].click();", fusion_financials_reporting_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_64'][name^='jform[groups][]'][type='checkbox'][value='64']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_benefits_training_1 = driver.find_element_by_xpath('//*[@id="1group_64"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_benefits_training_1)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_283'][name^='jform[groups][]'][type='checkbox'][value='283']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_benefits_training_2 = driver.find_element_by_xpath('//*[@id="1group_283"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_benefits_training_2)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_271'][name^='jform[groups][]'][type='checkbox'][value='271']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_instance = driver.find_element_by_xpath('//*[@id="1group_271"]')
        driver.execute_script("arguments[0].click();", fusion_instance)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()


def Unlimited_Oracle_training_Package():

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_181'][name^='jform[groups][]'][type='checkbox'][value='181']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_taleo_recruting_and_onboarding_training = driver.find_element_by_xpath('//*[@id="1group_181"]')
        driver.execute_script("arguments[0].click();", oracle_taleo_recruting_and_onboarding_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_202'][name^='jform[groups][]'][type='checkbox'][value='202']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_taleo_tcc_training = driver.find_element_by_xpath('//*[@id="1group_202"]')
        driver.execute_script("arguments[0].click();", oracle_taleo_tcc_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_192'][name^='jform[groups][]'][type='checkbox'][value='192']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_taleo_integration_training = driver.find_element_by_xpath('//*[@id="1group_192"]')
        driver.execute_script("arguments[0].click();", oracle_taleo_integration_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_156'][name^='jform[groups][]'][type='checkbox'][value='156']").get_attribute("checked")
    if not isChecked == 'true':
        r12_approval_management_training_1 = driver.find_element_by_xpath('//*[@id="1group_156"]')
        driver.execute_script("arguments[0].click();", r12_approval_management_training_1)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_230'][name^='jform[groups][]'][type='checkbox'][value='230']").get_attribute("checked")
    if not isChecked == 'true':
        r12_approval_management_training_2 = driver.find_element_by_xpath('//*[@id="1group_230"]')
        driver.execute_script("arguments[0].click();", r12_approval_management_training_2)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_145'][name^='jform[groups][]'][type='checkbox'][value='145']").get_attribute("checked")
    if not isChecked == 'true':
        apps_dba_training = driver.find_element_by_xpath('//*[@id="1group_145"]')
        driver.execute_script("arguments[0].click();", apps_dba_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_41'][name^='jform[groups][]'][type='checkbox'][value='41']").get_attribute("checked")
    if not isChecked == 'true':
        oaf_training = driver.find_element_by_xpath('//*[@id="1group_41"]')
        driver.execute_script("arguments[0].click();", oaf_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_136'][name^='jform[groups][]'][type='checkbox'][value='136']").get_attribute("checked")
    if not isChecked == 'true':
        r12_financial_accounting_hub_training = driver.find_element_by_xpath('//*[@id="1group_136"]')
        driver.execute_script("arguments[0].click();", r12_financial_accounting_hub_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_153'][name^='jform[groups][]'][type='checkbox'][value='153']").get_attribute("checked")
    if not isChecked == 'true':
        ebusiness_suit_development_erp_training = driver.find_element_by_xpath('//*[@id="1group_153"]')
        driver.execute_script("arguments[0].click();", ebusiness_suit_development_erp_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_230'][name^='jform[groups][]'][type='checkbox'][value='230']").get_attribute("checked")
    if not isChecked == 'true':
        r1213_administration_training = driver.find_element_by_xpath('//*[@id="1group_230"]')
        driver.execute_script("arguments[0].click();", r1213_administration_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_172'][name^='jform[groups][]'][type='checkbox'][value='172']").get_attribute("checked")
    if not isChecked == 'true':
        workflow_training = driver.find_element_by_xpath('//*[@id="1group_172"]')
        driver.execute_script("arguments[0].click();", workflow_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_154'][name^='jform[groups][]'][type='checkbox'][value='154']").get_attribute("checked")
    if not isChecked == 'true':
        bi_publisher_training = driver.find_element_by_xpath('//*[@id="1group_154"]')
        driver.execute_script("arguments[0].click();", bi_publisher_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_243'][name^='jform[groups][]'][type='checkbox'][value='243']").get_attribute("checked")
    if not isChecked == 'true':
        ebs_techno_functional_training = driver.find_element_by_xpath('//*[@id="1group_243"]')
        driver.execute_script("arguments[0].click();", ebs_techno_functional_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_54'][name^='jform[groups][]'][type='checkbox'][value='54']").get_attribute("checked")
    if not isChecked == 'true':
        Siebel_openUI_training = driver.find_element_by_xpath('//*[@id="1group_54"]')
        driver.execute_script("arguments[0].click();", Siebel_openUI_training)

#################################################################################################################################

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_49'][name^='jform[groups][]'][type='checkbox'][value='49']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_ebs_R12_inventory_order_management_and_purchasing_training = driver.find_element_by_xpath(
            '//*[@id="1group_49"]')
        driver.execute_script("arguments[0].click();",
                              oracle_ebs_R12_inventory_order_management_and_purchasing_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_43'][name^='jform[groups][]'][type='checkbox'][value='43']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_R12_subledger_accounting_training = driver.find_element_by_xpath('//*[@id="1group_43"]')
        driver.execute_script("arguments[0].click();", oracle_R12_subledger_accounting_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_117'][name^='jform[groups][]'][type='checkbox'][value='117']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_ebs_R12_functional_financials_training = driver.find_element_by_xpath('//*[@id="1group_117"]')
        driver.execute_script("arguments[0].click();", oracle_ebs_R12_functional_financials_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_48'][name^='jform[groups][]'][type='checkbox'][value='48']").get_attribute("checked")
    if not isChecked == 'true':
        R12_advance_global_intercompany_system_training = driver.find_element_by_xpath('//*[@id="1group_48"]')
        driver.execute_script("arguments[0].click();", R12_advance_global_intercompany_system_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_128'][name^='jform[groups][]'][type='checkbox'][value='128']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_EBusiness_tax_training_1 = driver.find_element_by_xpath('//*[@id="1group_128"]')
        driver.execute_script("arguments[0].click();", oracle_EBusiness_tax_training_1)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_252'][name^='jform[groups][]'][type='checkbox'][value='252']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_EBusiness_tax_training_2 = driver.find_element_by_xpath('//*[@id="1group_252"]')
        driver.execute_script("arguments[0].click();", oracle_EBusiness_tax_training_2)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_65'][name^='jform[groups][]'][type='checkbox'][value='65']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_demantra_training = driver.find_element_by_xpath('//*[@id="1group_65"]')
        driver.execute_script("arguments[0].click();", oracle_demantra_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_144'][name^='jform[groups][]'][type='checkbox'][value='144']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_R12_HRMS_payroll_training = driver.find_element_by_xpath('//*[@id="1group_144"]')
        driver.execute_script("arguments[0].click();", oracle_R12_HRMS_payroll_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_149'][name^='jform[groups][]'][type='checkbox'][value='149']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_impelment_configurator_training = driver.find_element_by_xpath('//*[@id="1group_149"]')
        driver.execute_script("arguments[0].click();", oracle_impelment_configurator_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_138'][name^='jform[groups][]'][type='checkbox'][value='138']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_R12_project_accounting_training = driver.find_element_by_xpath('//*[@id="1group_138"]')
        driver.execute_script("arguments[0].click();", oracle_R12_project_accounting_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_137'][name^='jform[groups][]'][type='checkbox'][value='137']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_R12_Advance_supply_chain_palnning_training = driver.find_element_by_xpath('//*[@id="1group_137"]')
        driver.execute_script("arguments[0].click();", oracle_R12_Advance_supply_chain_palnning_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_194'][name^='jform[groups][]'][type='checkbox'][value='194']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_business_suit_fundamentals_training = driver.find_element_by_xpath('//*[@id="1group_194"]')
        driver.execute_script("arguments[0].click();", oracle_business_suit_fundamentals_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_212'][name^='jform[groups][]'][type='checkbox'][value='212']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_R12_iprocurement_training = driver.find_element_by_xpath('//*[@id="1group_212"]')
        driver.execute_script("arguments[0].click();", oracle_R12_iprocurement_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_206'][name^='jform[groups][]'][type='checkbox'][value='206']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_ebs_R12_service_contract_training = driver.find_element_by_xpath('//*[@id="1group_206"]')
        driver.execute_script("arguments[0].click();", oracle_ebs_R12_service_contract_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_216'][name^='jform[groups][]'][type='checkbox'][value='216']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_ebs_R12_fixed_assets_training = driver.find_element_by_xpath('//*[@id="1group_216"]')
        driver.execute_script("arguments[0].click();", oracle_ebs_R12_fixed_assets_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_219'][name^='jform[groups][]'][type='checkbox'][value='219']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_transportation_management_training = driver.find_element_by_xpath('//*[@id="1group_219"]')
        driver.execute_script("arguments[0].click();", oracle_transportation_management_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_263'][name^='jform[groups][]'][type='checkbox'][value='263']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_demantra_ptp_training = driver.find_element_by_xpath('//*[@id="1group_263"]')
        driver.execute_script("arguments[0].click();", oracle_demantra_ptp_training)

##############################################################################################################################

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_52'][name^='jform[groups][]'][type='checkbox'][value='52']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_identity_management_training = driver.find_element_by_xpath('//*[@id="1group_52"]')
        driver.execute_script("arguments[0].click();", oracle_identity_management_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_73'][name^='jform[groups][]'][type='checkbox'][value='73']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_access_manager_training = driver.find_element_by_xpath('//*[@id="1group_73"]')
        driver.execute_script("arguments[0].click();", oracle_access_manager_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_47'][name^='jform[groups][]'][type='checkbox'][value='47']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_weblogic_administrator_training = driver.find_element_by_xpath('//*[@id="1group_47"]')
        driver.execute_script("arguments[0].click();", oracle_weblogic_administrator_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_159'][name^='jform[groups][]'][type='checkbox'][value='159']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_entitlement_server_training = driver.find_element_by_xpath('//*[@id="1group_159"]')
        driver.execute_script("arguments[0].click();", oracle_entitlement_server_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_134'][name^='jform[groups][]'][type='checkbox'][value='134']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_middleware_12C_training = driver.find_element_by_xpath('//*[@id="1group_134"]')
        driver.execute_script("arguments[0].click();", fusion_middleware_12C_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_66'][name^='jform[groups][]'][type='checkbox'][value='66']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_goldengate_training = driver.find_element_by_xpath('//*[@id="1group_66"]')
        driver.execute_script("arguments[0].click();", oracle_goldengate_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_171'][name^='jform[groups][]'][type='checkbox'][value='171']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_database_12C_advanced_admininstration_training = driver.find_element_by_xpath('//*[@id="1group_171"]')
        driver.execute_script("arguments[0].click();", oracle_database_12C_advanced_admininstration_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_177'][name^='jform[groups][]'][type='checkbox'][value='177']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_data_guard_administration_training = driver.find_element_by_xpath('//*[@id="1group_177"]')
        driver.execute_script("arguments[0].click();", oracle_data_guard_administration_training)

##############################################################################################################################

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_131'][name^='jform[groups][]'][type='checkbox'][value='131']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_business_intelligence_applications_training = driver.find_element_by_xpath('//*[@id="1group_131"]')
        driver.execute_script("arguments[0].click();", oracle_business_intelligence_applications_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_56'][name^='jform[groups][]'][type='checkbox'][value='56']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_business_intelligence_enterprise_edition_training = driver.find_element_by_xpath('//*[@id="1group_56"]')
        driver.execute_script("arguments[0].click();", oracle_business_intelligence_enterprise_edition_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_76'][name^='jform[groups][]'][type='checkbox'][value='76']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_adf_training = driver.find_element_by_xpath('//*[@id="1group_76"]')
        driver.execute_script("arguments[0].click();", oracle_adf_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_130'][name^='jform[groups][]'][type='checkbox'][value='130']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_business_process_management_training = driver.find_element_by_xpath('//*[@id="1group_130"]')
        driver.execute_script("arguments[0].click();", oracle_business_process_management_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_40'][name^='jform[groups][]'][type='checkbox'][value='40']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_soa_BPEL_mediator_OBS_development_training_1 = driver.find_element_by_xpath('//*[@id="1group_40"]')
        driver.execute_script("arguments[0].click();", oracle_soa_BPEL_mediator_OBS_development_training_1)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_122'][name^='jform[groups][]'][type='checkbox'][value='122']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_soa_BPEL_mediator_OBS_development_training_12C = driver.find_element_by_xpath('//*[@id="1group_122"]')
        driver.execute_script("arguments[0].click();", oracle_soa_BPEL_mediator_OBS_development_training_12C)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_126'][name^='jform[groups][]'][type='checkbox'][value='126']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_data_integrator_training = driver.find_element_by_xpath('//*[@id="1group_126"]')
        driver.execute_script("arguments[0].click();", oracle_data_integrator_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_113'][name^='jform[groups][]'][type='checkbox'][value='113']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_mobile_application_framework_training = driver.find_element_by_xpath('//*[@id="1group_113"]')
        driver.execute_script("arguments[0].click();", oracle_mobile_application_framework_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_129'][name^='jform[groups][]'][type='checkbox'][value='129']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_java_xml_and_web_service_training = driver.find_element_by_xpath('//*[@id="1group_129"]')
        driver.execute_script("arguments[0].click();", oracle_java_xml_and_web_service_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_155'][name^='jform[groups][]'][type='checkbox'][value='155']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_sql_and_plSQL_training = driver.find_element_by_xpath('//*[@id="1group_155"]')
        driver.execute_script("arguments[0].click();", oracle_sql_and_plSQL_training)

##############################################################################################################################

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_39'][name^='jform[groups][]'][type='checkbox'][value='39']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_procurement_training = driver.find_element_by_xpath('//*[@id="1group_39"]')
        driver.execute_script("arguments[0].click();", fusion_procurement_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_259'][name^='jform[groups][]'][type='checkbox'][value='259']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_financials_accounting_hub_training_1 = driver.find_element_by_xpath('//*[@id="1group_259"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_financials_accounting_hub_training_1)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_46'][name^='jform[groups][]'][type='checkbox'][value='46']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_financials_accounting_hub_training_2 = driver.find_element_by_xpath('//*[@id="1group_46"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_financials_accounting_hub_training_2)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_50'][name^='jform[groups][]'][type='checkbox'][value='50']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_financials_training = driver.find_element_by_xpath('//*[@id="1group_50"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_financials_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_229'][name^='jform[groups][]'][type='checkbox'][value='229']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_accounts_receivable_trainings = driver.find_element_by_xpath('//*[@id="1group_229"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_accounts_receivable_trainings)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_28'][name^='jform[groups][]'][type='checkbox'][value='28']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_account_payable_training = driver.find_element_by_xpath('//*[@id="1group_28"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_account_payable_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_231'][name^='jform[groups][]'][type='checkbox'][value='231']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_general_ledger_training = driver.find_element_by_xpath('//*[@id="1group_231"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_general_ledger_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_256'][name^='jform[groups][]'][type='checkbox'][value='256']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_tax_training = driver.find_element_by_xpath('//*[@id="1group_256"]')
        driver.execute_script("arguments[0].click();", fusion_tax_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_220'][name^='jform[groups][]'][type='checkbox'][value='220']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_fixed_asset_training = driver.find_element_by_xpath('//*[@id="1group_220"]')
        driver.execute_script("arguments[0].click();", fusion_fixed_asset_training)

##############################################################################################################################

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_253'][name^='jform[groups][]'][type='checkbox'][value='253']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_financials_integration_training = driver.find_element_by_xpath('//*[@id="1group_253"]')
        driver.execute_script("arguments[0].click();", fusion_financials_integration_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_268'][name^='jform[groups][]'][type='checkbox'][value='268']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_financials_security_training_1 = driver.find_element_by_xpath('//*[@id="1group_268"]')
        driver.execute_script("arguments[0].click();", fusion_financials_security_training_1)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_272'][name^='jform[groups][]'][type='checkbox'][value='272']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_financials_security_training_2 = driver.find_element_by_xpath('//*[@id="1group_272"]')
        driver.execute_script("arguments[0].click();", fusion_financials_security_training_2)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_235'][name^='jform[groups][]'][type='checkbox'][value='235']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_financials_reporting_training = driver.find_element_by_xpath('//*[@id="1group_235"]')
        driver.execute_script("arguments[0].click();", fusion_financials_reporting_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_209'][name^='jform[groups][]'][type='checkbox'][value='209']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_financials_approval_management_training = driver.find_element_by_xpath('//*[@id="1group_209"]')
        driver.execute_script("arguments[0].click();", fusion_financials_approval_management_training)

##############################################################################################################################

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_79'][name^='jform[groups][]'][type='checkbox'][value='79']").get_attribute("checked")
    if not isChecked == 'true':
        hyperion_financials_management_hfm_training = driver.find_element_by_xpath('//*[@id="1group_79"]')
        driver.execute_script("arguments[0].click();", hyperion_financials_management_hfm_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_63'][name^='jform[groups][]'][type='checkbox'][value='63']").get_attribute("checked")
    if not isChecked == 'true':
        hyperion_planning_training = driver.find_element_by_xpath('//*[@id="1group_63"]')
        driver.execute_script("arguments[0].click();", hyperion_planning_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_182'][name^='jform[groups][]'][type='checkbox'][value='182']").get_attribute("checked")
    if not isChecked == 'true':
        mastering_hyperion_calculation_manager = driver.find_element_by_xpath('//*[@id="1group_182"]')
        driver.execute_script("arguments[0].click();", mastering_hyperion_calculation_manager)

##############################################################################################################################

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_44'][name^='jform[groups][]'][type='checkbox'][value='44']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_fundamentals_training = driver.find_element_by_xpath('//*[@id="1group_44"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_fundamentals_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_35'][name^='jform[groups][]'][type='checkbox'][value='35']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_hcm_core_training = driver.find_element_by_xpath('//*[@id="1group_35"]')
        driver.execute_script("arguments[0].click();", fusion_hcm_core_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_30'][name^='jform[groups][]'][type='checkbox'][value='30']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_talent_management_training = driver.find_element_by_xpath('//*[@id="1group_30"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_talent_management_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_64'][name^='jform[groups][]'][type='checkbox'][value='64']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_benefits_training_1 = driver.find_element_by_xpath('//*[@id="1group_64"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_benefits_training_1)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_283'][name^='jform[groups][]'][type='checkbox'][value='283']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_benefits_training_2 = driver.find_element_by_xpath('//*[@id="1group_283"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_benefits_training_2)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_239'][name^='jform[groups][]'][type='checkbox'][value='239']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_payroll_training = driver.find_element_by_xpath('//*[@id="1group_239"]')
        driver.execute_script("arguments[0].click();", fusion_payroll_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_45'][name^='jform[groups][]'][type='checkbox'][value='45']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_fastformula = driver.find_element_by_xpath('//*[@id="1group_45"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_fastformula)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_29'][name^='jform[groups][]'][type='checkbox'][value='29']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_compensation_workbench = driver.find_element_by_xpath('//*[@id="1group_29"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_compensation_workbench)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_240'][name^='jform[groups][]'][type='checkbox'][value='240']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_hcm_approval_management = driver.find_element_by_xpath('//*[@id="1group_240"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_hcm_approval_management)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_241'][name^='jform[groups][]'][type='checkbox'][value='241']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_time_and_labour_training = driver.find_element_by_xpath('//*[@id="1group_241"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_time_and_labour_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_245'][name^='jform[groups][]'][type='checkbox'][value='245']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_hcm_for_ebs_hcm_experts_training = driver.find_element_by_xpath('//*[@id="1group_245"]')
        driver.execute_script("arguments[0].click();", fusion_hcm_for_ebs_hcm_experts_training)

##############################################################################################################################

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_83'][name^='jform[groups][]'][type='checkbox'][value='83']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_application_development_training = driver.find_element_by_xpath('//*[@id="1group_83"]')
        driver.execute_script("arguments[0].click();", fusion_application_development_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_115'][name^='jform[groups][]'][type='checkbox'][value='115']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_application_installation_and_patching_r9_training = driver.find_element_by_xpath('//*[@id="1group_115"]')
        driver.execute_script("arguments[0].click();", fusion_application_installation_and_patching_r9_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_250'][name^='jform[groups][]'][type='checkbox'][value='250']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_fusion_integration_cloud_Service_training = driver.find_element_by_xpath('//*[@id="1group_250"]')
        driver.execute_script("arguments[0].click();", oracle_fusion_integration_cloud_Service_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_204'][name^='jform[groups][]'][type='checkbox'][value='204']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_sales_cloud_extensibility_training = driver.find_element_by_xpath('//*[@id="1group_204"]')
        driver.execute_script("arguments[0].click();", oracle_sales_cloud_extensibility_training)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_277'][name^='jform[groups][]'][type='checkbox'][value='277']").get_attribute("checked")
    if not isChecked == 'true':
        hcm_technical = driver.find_element_by_xpath('//*[@id="1group_277"]')
        driver.execute_script("arguments[0].click();", hcm_technical)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_62'][name^='jform[groups][]'][type='checkbox'][value='62']").get_attribute("checked")
    if not isChecked == 'true':
        procure_to_pay = driver.find_element_by_xpath('//*[@id="1group_62"]')
        driver.execute_script("arguments[0].click();", procure_to_pay)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_273'][name^='jform[groups][]'][type='checkbox'][value='273']").get_attribute("checked")
    if not isChecked == 'true':
        hcm_security = driver.find_element_by_xpath('//*[@id="1group_273"]')
        driver.execute_script("arguments[0].click();", hcm_security)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_279'][name^='jform[groups][]'][type='checkbox'][value='279']").get_attribute("checked")
    if not isChecked == 'true':
        hcm_reporting = driver.find_element_by_xpath('//*[@id="1group_279"]')
        driver.execute_script("arguments[0].click();", hcm_reporting)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_218'][name^='jform[groups][]'][type='checkbox'][value='218']").get_attribute("checked")
    if not isChecked == 'true':
        oracle_transportation_management = driver.find_element_by_xpath('//*[@id="1group_218"]')
        driver.execute_script("arguments[0].click();", oracle_transportation_management)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_135'][name^='jform[groups][]'][type='checkbox'][value='135']").get_attribute("checked")
    if not isChecked == 'true':
        BI_reporting = driver.find_element_by_xpath('//*[@id="1group_135"]')
        driver.execute_script("arguments[0].click();", BI_reporting)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_123'][name^='jform[groups][]'][type='checkbox'][value='123']").get_attribute("checked")
    if not isChecked == 'true':
        OTBI_reporting = driver.find_element_by_xpath('//*[@id="1group_123"]')
        driver.execute_script("arguments[0].click();", OTBI_reporting)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_238'][name^='jform[groups][]'][type='checkbox'][value='238']").get_attribute("checked")
    if not isChecked == 'true':
        ppm_cloud = driver.find_element_by_xpath('//*[@id="1group_238"]')
        driver.execute_script("arguments[0].click();", ppm_cloud)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_249'][name^='jform[groups][]'][type='checkbox'][value='249']").get_attribute("checked")
    if not isChecked == 'true':
        ebs_otl = driver.find_element_by_xpath('//*[@id="1group_249"]')
        driver.execute_script("arguments[0].click();", ebs_otl)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_254'][name^='jform[groups][]'][type='checkbox'][value='254']").get_attribute("checked")
    if not isChecked == 'true':
        ebs_fundamentals = driver.find_element_by_xpath('//*[@id="1group_254"]')
        driver.execute_script("arguments[0].click();", ebs_fundamentals)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_237'][name^='jform[groups][]'][type='checkbox'][value='237']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_scm = driver.find_element_by_xpath('//*[@id="1group_237"]')
        driver.execute_script("arguments[0].click();", fusion_scm)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_224'][name^='jform[groups][]'][type='checkbox'][value='224']").get_attribute("checked")
    if not isChecked == 'true':
        EBusiness_tax = driver.find_element_by_xpath('//*[@id="1group_224"]')
        driver.execute_script("arguments[0].click();", EBusiness_tax)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_161'][name^='jform[groups][]'][type='checkbox'][value='161']").get_attribute("checked")
    if not isChecked == 'true':
        support_ticket = driver.find_element_by_xpath('//*[@id="1group_161"]')
        driver.execute_script("arguments[0].click();", support_ticket)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_25'][name^='jform[groups][]'][type='checkbox'][value='25']").get_attribute("checked")
    if not isChecked == 'true':
        training_forum = driver.find_element_by_xpath('//*[@id="1group_25"]')
        driver.execute_script("arguments[0].click();", training_forum)

    isChecked = driver.find_element_by_css_selector(
        "input[id*='1group_271'][name^='jform[groups][]'][type='checkbox'][value='271']").get_attribute("checked")
    if not isChecked == 'true':
        fusion_instance = driver.find_element_by_xpath('//*[@id="1group_271"]')
        driver.execute_script("arguments[0].click();", fusion_instance)

    save_and_close = driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/div/div/div[1]/button').click()
    driver.quit()



def joomla(customer_email):
    driver.get('Link to website')

    email = driver.find_element_by_xpath('//*[@id="mod-login-username"]')
    email.send_keys('username')
    time.sleep(2)

    password = driver.find_element_by_xpath('//*[@id="mod-login-password"]')
    password.send_keys('password')
    time.sleep(2)

    submit = driver.find_element_by_xpath('//*[@id="form-login"]/fieldset/div[3]/div/div/button')
    submit.click()
    time.sleep(2)

    email = driver.find_element_by_xpath('//*[@id="mod-login-username"]')
    email.send_keys('username')
    time.sleep(2)

    password = driver.find_element_by_xpath('//*[@id="mod-login-password"]')
    password.send_keys('password')
    time.sleep(2)

    submit = driver.find_element_by_xpath('//*[@id="form-login"]/fieldset/div[3]/div/div/button')
    submit.click()
    time.sleep(2)

    users_click = driver.find_element_by_xpath('/html/body/nav/div/div/div/ul[1]/li[2]/a').click()
    time.sleep(2)

    manage_click = driver.find_element_by_xpath('/html/body/nav/div/div/div/ul[1]/li[2]/ul/li[1]/a').click()
    time.sleep(2)

    users_search = driver.find_element_by_xpath('//*[@id="filter_search"]')
    users_search.send_keys(customer_email)
    time.sleep(1)

    users_search_click = driver.find_element_by_xpath(
        '/html/body/div[2]/section/div/div/form/div[2]/div[1]/div[1]/div[1]/div[1]/button').click()
    time.sleep(2)

    try:
        isBlocked = driver.find_element_by_xpath('//*[@id="userList"]/tbody/tr/td[4]/a').get_attribute("data-original-title")
        if isBlocked == 'Unblock':
            unblock = driver.find_element_by_xpath('//*[@id="userList"]/tbody/tr/td[4]/a/span').click()
        time.sleep(2)

        found_user = driver.find_element_by_xpath(
            '/html/body/div[2]/section/div/div/form/div[2]/table/tbody/tr/td[2]/div[1]/a')
        found_user.click()
        time.sleep(2)

        login_name = driver.find_element_by_xpath('//*[@id="jform_username"]').get_attribute('value')
        time.sleep(2)

        existing_customer_username = driver.find_element_by_xpath('//*[@id="jform_username"]').get_attribute('value')

        assigned_users_groups = driver.find_element_by_xpath(
            '/html/body/div[2]/section/div/div/form/fieldset/ul/li[2]/a').click()
        time.sleep(2)
######################################################### SINGLE TRAININGS ##################################################
        if sku == 'Fusion Apps Foundation':
            sheet_package = 'oracle_fusion_fundamentals_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_fusion_fundamentals_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion HCM Core Functional':
            sheet_package = 'fusion_hcm_core_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            fusion_hcm_core_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion Talent Management':
            sheet_package = 'oracle_fusion_talent_management_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_fusion_talent_management_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion Benefits':
            sheet_package = 'oracle_fusion_benefits_training_1'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_fusion_benefits_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion Payroll':
            sheet_package = 'fusion_payroll_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            fusion_payroll_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle Fusion Fast Formula Training':
            sheet_package = 'oracle_fusion_fastformula'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_fusion_fastformula_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion Compensation Workbench':
            sheet_package = 'oracle_fusion_compensation_workbench'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_fusion_compensation_workbench_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle Fusion HCM Approval Management':
            sheet_package = 'oracle_fusion_hcm_approval_management'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_fusion_hcm_approval_management_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle Time & Labour (OTL)':
            sheet_package = 'oracle_fusion_time_and_labour_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_fusion_time_and_labour_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'EBS HCM Experts':
            sheet_package = 'fusion_hcm_for_ebs_hcm_experts_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            fusion_hcm_for_ebs_hcm_experts_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion Procurement':
            sheet_package = 'fusion_procurement_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORDpr0c'
            fusion_procurement_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion HCM technical Training':
            sheet_package = 'oracle_fusion_hcm_technical_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_fusion_hcm_technical_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion Accounting Hub':
            sheet_package = 'oracle_fusion_financials_accounting_hub_training_1'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_fusion_financials_accounting_hub_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion Procure to Pay':
            sheet_package = 'oracle_fusion_procure_to_pay_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_fusion_procure_to_pay_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion Applications Installation & Patching R9':
            sheet_package = 'fusion_application_installation_and_patching_R9_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            fusion_application_installation_and_patching_R9_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Development In Fusion Applications':
            sheet_package = 'development_in_fusion_applications'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            development_in_fusion_applications_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion Financials':
            sheet_package = 'oracle_fusion_financials_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_fusion_financials_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        # if sku == 'Oracle Fusion HCM Reporting Training':
        #     sheet_package = 'oracle_BI_reproting_and_OTBI_training_in_fusion_apps_1'
        #     isFusion = True
        #     isPackage = False
        #     single_training_password = 'REDACTED_TRAINING_PASSWORD'
        #     oracle_BI_reproting_and_OTBI_training_in_fusion_apps_single()
        #     fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
        #                        single_training_password)
        #     google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
        #                         sheet_package, isPackage)

        if sku == 'Fusion Account Receivables':
            sheet_package = 'oracle_fusion_accounts_receivable_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_fusion_accounts_receivable_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion e-biz Tax':
            sheet_package = 'oracle_fusion_financials_cloud_tax_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_fusion_financials_cloud_tax_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle Apps DBA Training':
            sheet_package = 'oracle_apps_DBA'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_apps_DBA_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle Inventory Order Management & Purchasing':
            sheet_package = 'oracle_EBS_R12_inventory_order_management_and_purchasing_training'
            isFusion = False
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_EBS_R12_inventory_order_management_and_purchasing_training_single()
            ebs_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle Subledger Accounting':
            sheet_package = 'oracle_R12_subledger_accounting_training'
            isFusion = False
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_R12_subledger_accounting_training_single()
            ebs_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle EBS Financials Functional R12':
            sheet_package = 'oracle_EBS_R12_functional_financial_training'
            isFusion = False
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_EBS_R12_functional_financial_training_single()
            ebs_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'OAF Training':
            sheet_package = 'OA_framework_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            OA_framework_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle R12 AGIS Training':
            sheet_package = 'R12_advanced_global_intercompany_system_AGIS_training'
            isFusion = False
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            R12_advanced_global_intercompany_system_AGIS_training_single()
            ebs_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'ORACLE E-BUSINESS TAX':
            sheet_package = 'oracle_EBusiness_tax_training_1'
            isFusion = False
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_EBusiness_tax_training_single()
            ebs_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle Demantra':
            sheet_package = 'oracle_demantra_training'
            isFusion = False
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_demantra_training_single()
            ebs_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'ORACLE R12 HRMS PAYROLL TRAINING':
            sheet_package = 'oracle_R12_HRMS_payroll_training'
            isFusion = False
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_R12_HRMS_payroll_training_single()
            ebs_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle Implement Configurator':
            sheet_package = 'oracle_implement_configurator_training'
            isFusion = False
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_implement_configurator_training_single()
            ebs_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle R12 Project Accounting':
            sheet_package = 'oracle_R12_project_accounting_training'
            isFusion = False
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_R12_project_accounting_training_single()
            ebs_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle R12 - Advanced Supply Chain Planning (ASCP) Fundamentals':
            sheet_package = 'oracle_R12_advance_supply_chain_planning_training'
            isFusion = False
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_R12_advance_supply_chain_planning_training_single()
            ebs_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle R12 Financials Accounting Hub Fundamentals':
            sheet_package = 'oracle_R12_financial_accounting_hub_training'
            isFusion = False
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_R12_financial_accounting_hub_training_single()
            ebs_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle Business Intelligence Applications Training':
            sheet_package = 'oracle_business_intelligence_applications_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_business_intelligence_applications_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        # if sku == 'oracle_business_intelligence_enterprise_edition_training':
        #     sheet_package = 'oracle_business_intelligence_enterprise_edition_training'
        #     isFusion = True
        #     isPackage = False
        #     single_training_password = 'REDACTED_TRAINING_PASSWORD'
        #     oracle_business_intelligence_enterprise_edition_training_single()
        #     fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
        #                        single_training_password)
        #     google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
        #                         sheet_package, isPackage)

        if sku == 'Oracle ADF Training':
            sheet_package = 'oracle_adf_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_adf_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle BPM - Business Process Management Training':
            sheet_package = 'oracle_business_process_management_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_business_process_management_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'SOA BPEL Mediator OSB 12c':
            sheet_package = 'oracle_soa_BPEL_mediator_OBS_development_training_1'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_soa_BPEL_mediator_OBS_development_training_1_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle Data Integrator ODI':
            sheet_package = 'oracle_data_integrator_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_data_integrator_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle MAF':
            sheet_package = 'oracle_mobile_application_framework_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_mobile_application_framework_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Java, XML and Webservices':
            sheet_package = 'oracle_java_xml_and_web_service_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_java_xml_and_web_service_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle SQL and PL/SQL Training':
            sheet_package = 'oracle_sql_and_plSQL_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_sql_and_plSQL_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Financial Integration':
            sheet_package = 'fusion_financials_integration_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            fusion_financials_integration_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion Security':
            sheet_package = 'fusion_financials_security_training_1'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            fusion_financials_security_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle Fusion Financials Reporting Training':
            sheet_package = 'fusion_financials_reporting_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            fusion_financials_reporting_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion Financials Approval':
            sheet_package = 'fusion_financials_approval_management_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            fusion_financials_approval_management_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Integration Cloud Service':
            sheet_package = 'oracle_fusion_integration_cloud_Service_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_fusion_integration_cloud_Service_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle Sales Cloud Extensibility':
            sheet_package = 'oracle_sales_cloud_extensibility_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_sales_cloud_extensibility_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion Account Payables':
            sheet_package = 'oracle_fusion_account_payable_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_fusion_account_payable_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion General Ledger':
            sheet_package = 'oracle_fusion_general_ledger_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_fusion_general_ledger_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        # if sku == 'fusion_fixed_asset_training':
        #     sheet_package = 'fusion_fixed_asset_training'
        #     isFusion = True
        #     isPackage = False
        #     single_training_password = 'REDACTED_TRAINING_PASSWORD'
        #     fusion_fixed_asset_training_single()
        #     fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
        #                        single_training_password)
        #     google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
        #                         sheet_package, isPackage)

        if sku == 'Oracle Fusion Project Portfolio Management':
            sheet_package = 'oracle_fusion_project_portfolio_management_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_fusion_project_portfolio_management_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle Ebusiness Suite Fundamentals':
            sheet_package = 'oracle_business_suit_fundamentals_training'
            isFusion = False
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_business_suit_fundamentals_training_single()
            ebs_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle R12 iProcurement':
            sheet_package = 'oracle_R12_iprocurement_training'
            isFusion = False
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_R12_iprocurement_training_single()
            ebs_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle Service Contract Fundamentals':
            sheet_package = 'oracle_ebs_R12_service_contract_training'
            isFusion = False
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_ebs_R12_service_contract_training_single()
            ebs_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        # if sku == 'oracle_ebs_R12_fixed_assets_training':
        #     sheet_package = 'oracle_ebs_R12_fixed_assets_training'
        #     isFusion = False
        #     isPackage = False
        #     single_training_password = 'REDACTED_TRAINING_PASSWORD'
        #     oracle_ebs_R12_fixed_assets_training_single()
        #     ebs_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
        #                        single_training_password)
        #     google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
        #                         sheet_package, isPackage)

        if sku == 'Oracle Transportation Management':
            sheet_package = 'oracle_transportation_management_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_transportation_management_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle Demantra : Predictive Trade Planning':
            sheet_package = 'oracle_demantra_ptp_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_demantra_ptp_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'IDM Foundation':
            sheet_package = 'oracle_identity_management_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_identity_management_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle Access Manager':
            sheet_package = 'oracle_access_manager_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_access_manager_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Weblogic Training':
            sheet_package = 'oracle_weblogic_administrator_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_weblogic_administrator_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle Entitlement Server Training':
            sheet_package = 'oracle_entitlement_server_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_entitlement_server_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle Fusion MiddleWare 12c Administration':
            sheet_package = 'fusion_middleware_12C_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            fusion_middleware_12C_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle GoldenGate':
            sheet_package = 'oracle_goldengate_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_goldengate_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle Database 12c: New Features for Administrators Ed2':
            sheet_package = 'oracle_database_12C_advanced_admininstration_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_database_12C_advanced_admininstration_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle Database : Data Guard Administration':
            sheet_package = 'oracle_data_guard_administration_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_data_guard_administration_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle R12 Approvals Management Engine (AME)':
            sheet_package = 'r12_approval_management_training_1'
            isFusion = False
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            r12_approval_management_training_single()
            ebs_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle ERP Development':
            sheet_package = 'ebusiness_suit_development_erp_training'
            isFusion = False
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            ebusiness_suit_development_erp_training_single()
            ebs_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        # if sku == 'Oracle Workflow Training':
        #     sheet_package = 'workflow_training'
        #     isFusion = False
        #     isPackage = False
        #     single_training_password = 'REDACTED_TRAINING_PASSWORD'
        #     workflow_training_single()
        #     ebs_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
        #                        single_training_password)
        #     google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
        #                         sheet_package, isPackage)

        if sku == 'Oracle BI Publisher':
            sheet_package = 'bi_publisher_training'
            isFusion = False
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            bi_publisher_training_single()
            ebs_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'EBS Techno-Functional Package':
            sheet_package = 'ebs_techno_functional_training'
            isFusion = False
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            ebs_techno_functional_training_single()
            ebs_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle Fusion HCM Reporting Training':
            sheet_package = 'fusion_hcm_reporting_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            fusion_hcm_reporting_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion Integration Training':
            sheet_package = 'oracle_fusion_hcm_integration_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_fusion_hcm_integration_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion HCM':
            sheet_package = 'fusion_security_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            fusion_security_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle Taleo Training':
            sheet_package = 'oracle_taleo_recruting_and_onboarding_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_taleo_recruting_and_onboarding_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Taleo Connect Client':
            sheet_package = 'oracle_taleo_tcc_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_taleo_tcc_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        # if sku == 'oracle_taleo_integration_training':
        #     sheet_package = 'oracle_taleo_integration_training'
        #     isFusion = True
        #     isPackage = False
        #     single_training_password = 'REDACTED_TRAINING_PASSWORD'
        #     oracle_taleo_integration_training_single()
        #     fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
        #                        single_training_password)
        #     google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
        #                         sheet_package, isPackage)

        # if sku == 'r1213_administration_training':
        #     sheet_package = 'r1213_administration_training'
        #     isFusion = False
        #     isPackage = False
        #     single_training_password = 'REDACTED_TRAINING_PASSWORD'
        #     r1213_administration_training_single()
        #     fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
        #                        single_training_password)
        #     google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
        #                         sheet_package, isPackage)

        if sku == 'Siebel open UI':
            sheet_package = 'Siebel_openUI_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            Siebel_openUI_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Hyperion Financial Management':
            sheet_package = 'hyperion_financials_management_hfm_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            hyperion_financials_management_hfm_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion Hyperion Planning':
            sheet_package = 'hyperion_planning_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            hyperion_planning_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Mastering Hyperion Calculation Manager with Essbase and Planning':
            sheet_package = 'mastering_hyperion_calculation_manager'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            mastering_hyperion_calculation_manager_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)



        if sku == 'OBIEE Training':
            sheet_package = 'OBIEE Training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            obiee_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)


        if sku == 'Oracle Workflow Training':
            sheet_package = 'Oracle Workflow Builder Training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_workflow_training_single()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)



############################################### PACKAGES ###########################################################

        if sku == 'Fusion Middleware Administration Package':
            sheet_package = 'Fusion Middleware administration Package'
            isFusion = True
            isPackage = True
            single_training_password = None
            Fusion_middleware_administration_package()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Hyperion Suite Training Package':
            sheet_package = 'Hyperion Suit Training Package'
            isFusion = True
            isPackage = True
            single_training_password = None
            Hyperion_suit_training_package()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion HCM Technical Package':
            sheet_package = 'HCM Technical Package'
            isFusion = True
            isPackage = True
            single_training_password = None
            Fusion_HCM_Technical_Package()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'EBS R12 Technical training Package':
            sheet_package = 'Oracle EBS R12 Technical Package'
            isFusion = True
            isPackage = True
            single_training_password = None
            EBS_R12_Technical_Package()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'FUsion HCM Modules PAckage':
            sheet_package = 'Fusion HCM Modules Training Package'
            isFusion = True
            isPackage = True
            single_training_password = None
            Fusion_HCM_Modules_Package()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'FUSION APPLICATIONS TRAINING':
            sheet_package = 'Fusion Applications Package'
            isFusion = True
            isPackage = True
            single_training_password = None
            Fusion_Application_Training_Package()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion Cloud Common Technology Package':
            sheet_package = 'Fusion Cloud Common Technology Package'
            isFusion = True
            isPackage = True
            single_training_password = None
            Fusion_cloud_common_technology_package()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion Financials Functional Package':
            sheet_package = 'Fusion Financials Functional Package'
            isFusion = True
            isPackage = True
            single_training_password = None
            Fusion_financials_functional_package()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion Financials Technical Package':
            sheet_package = 'Fusion Financials Technical Package'
            isFusion = True
            isPackage = True
            single_training_password = None
            Fusion_financials_technical_package()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion HCM and Taleo Functional & Technical Package':
            sheet_package = 'FUSION HCM AND TALEO FUNCTIONAL & TECHNICAL PACKAGE'
            isFusion = True
            isPackage = True
            single_training_password = None
            Fusion_HCM_and_Taleo_functional_and_technical_package()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion HCM trainings':
            sheet_package = 'Fusion HCM Modules Training Package'
            isFusion = True
            isPackage = True
            single_training_password = None
            Fusion_HCM_functional_package()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion Middleware Development Package':  #fusion access not given
            sheet_package = 'Fusion Middleware Development Training Package'
            isFusion = True
            isPackage = True
            single_training_password = None
            Fusion_middleware_development_package()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle EBS R12 Functional Package':
            sheet_package = 'Oracle EBS R12 Functional Package'
            isFusion = False
            isPackage = True
            single_training_password = None
            Oracle_EBS_R12_functional_package()
            ebs_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'R12 + Fusion Apps Training':  # Fusion+EBS
            sheet_package = 'Fusion + R12 Package'
            isFusion = 'Both'
            isPackage = True
            single_training_password = None
            R12_Fusion_Apps_Training()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Unlimited Oracle Training Package':# Fusion+EBS
            sheet_package = 'Unlimited Training Package'
            isFusion = 'Both'
            isPackage = True
            single_training_password = None
            Unlimited_Oracle_training_Package()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion Apps Training Package':
            sheet_package = 'Fusion Apps Training Package'
            isFusion = True
            isPackage = True
            single_training_password = None
            Fusion_Apps_Training_Package()
            fusion_email_exist(customer_name, existing_customer_username, customer_email, sku, isPackage,
                               single_training_password, isFusion)
            google_sheet_update(customer_name, existing_customer_username, None, isFusion, customer_email,
                                sheet_package, isPackage)


    except:

        new_user = driver.find_element_by_xpath('//*[@id="toolbar-new"]/button').click()
        time.sleep(2)

        new_customer_name = driver.find_element_by_xpath('//*[@id="jform_name"]').send_keys(customer_name)
        new_customer_username = driver.find_element_by_xpath('//*[@id="jform_username"]').send_keys(customer_username)
        new_customer_password = driver.find_element_by_xpath('//*[@id="jform_password"]').send_keys(random_password)
        conform_new_password = driver.find_element_by_xpath('//*[@id="jform_password2"]').send_keys(random_password)
        new_customer_email = driver.find_element_by_xpath('//*[@id="jform_email"]').send_keys(customer_email)


##############################################################  SINGLE TRAININGS #############################################################################

        if sku == 'Fusion Apps Foundation':
            sheet_package = 'oracle_fusion_fundamentals_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_fusion_fundamentals_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion HCM Core Functional':
            sheet_package = 'fusion_hcm_core_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            fusion_hcm_core_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion Talent Management':
            sheet_package = 'oracle_fusion_talent_management_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_fusion_talent_management_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion Benefits':
            sheet_package = 'oracle_fusion_benefits_training_1'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_fusion_benefits_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion Payroll':
            sheet_package = 'fusion_payroll_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            fusion_payroll_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle Fusion Fast Formula Training':
            sheet_package = 'oracle_fusion_fastformula'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_fusion_fastformula_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion Compensation Workbench':
            sheet_package = 'oracle_fusion_compensation_workbench'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_fusion_compensation_workbench_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle Fusion HCM Approval Management':
            sheet_package = 'oracle_fusion_hcm_approval_management'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_fusion_hcm_approval_management_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle Time & Labour (OTL)':
            sheet_package = 'oracle_fusion_time_and_labour_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_fusion_time_and_labour_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'EBS HCM Experts':
            sheet_package = 'fusion_hcm_for_ebs_hcm_experts_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            fusion_hcm_for_ebs_hcm_experts_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion Procurement':
            sheet_package = 'fusion_procurement_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORDpr0c'
            fusion_procurement_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion HCM technical Training':
            sheet_package = 'oracle_fusion_hcm_technical_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_fusion_hcm_technical_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion Accounting Hub':
            sheet_package = 'oracle_fusion_financials_accounting_hub_training_1'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_fusion_financials_accounting_hub_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion Procure to Pay':
            sheet_package = 'oracle_fusion_procure_to_pay_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_fusion_procure_to_pay_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion Applications Installation & Patching R9':
            sheet_package = 'fusion_application_installation_and_patching_R9_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            fusion_application_installation_and_patching_R9_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Development In Fusion Applications':
            sheet_package = 'development_in_fusion_applications'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            development_in_fusion_applications_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion Financials':
            sheet_package = 'oracle_fusion_financials_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_fusion_financials_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        # if sku == 'oracle_BI_reproting_and_OTBI_training_in_fusion_apps_1':
        #     sheet_package = 'oracle_BI_reproting_and_OTBI_training_in_fusion_apps_1'
        #     isFusion = True
        #     isPackage = False
        #     single_training_password = 'REDACTED_TRAINING_PASSWORD'
        #     oracle_BI_reproting_and_OTBI_training_in_fusion_apps_single()
        #     fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
        #                  single_training_password)
        #     google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
        #                         sheet_package, isPackage)

        if sku == 'Fusion Account Receivables':
            sheet_package = 'oracle_fusion_accounts_receivable_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_fusion_accounts_receivable_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion e-biz Tax':
            sheet_package = 'oracle_fusion_financials_cloud_tax_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_fusion_financials_cloud_tax_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle Apps DBA Training':
            sheet_package = 'oracle_apps_DBA'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_apps_DBA_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle Inventory Order Management & Purchasing':
            sheet_package = 'oracle_EBS_R12_inventory_order_management_and_purchasing_training'
            isFusion = False
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_EBS_R12_inventory_order_management_and_purchasing_training_single()
            ebs_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle Subledger Accounting':
            sheet_package = 'oracle_R12_subledger_accounting_training'
            isFusion = False
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_R12_subledger_accounting_training_single()
            ebs_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle EBS Financials Functional R12':
            sheet_package = 'oracle_EBS_R12_functional_financial_training'
            isFusion = False
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_EBS_R12_functional_financial_training_single()
            ebs_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'OAF Training':
            sheet_package = 'OA_framework_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            OA_framework_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle R12 AGIS Training':
            sheet_package = 'R12_advanced_global_intercompany_system_AGIS_training'
            isFusion = False
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            R12_advanced_global_intercompany_system_AGIS_training_single()
            ebs_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'ORACLE E-BUSINESS TAX':
            sheet_package = 'oracle_EBusiness_tax_training_1'
            isFusion = False
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_EBusiness_tax_training_single()
            ebs_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle Demantra':
            sheet_package = 'oracle_demantra_training'
            isFusion = False
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_demantra_training_single()
            ebs_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'ORACLE R12 HRMS PAYROLL TRAINING':
            sheet_package = 'oracle_R12_HRMS_payroll_training'
            isFusion = False
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_R12_HRMS_payroll_training_single()
            ebs_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle Implement Configurator':
            sheet_package = 'oracle_implement_configurator_training'
            isFusion = False
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_implement_configurator_training_single()
            ebs_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle R12 Project Accounting':
            sheet_package = 'oracle_R12_project_accounting_training'
            isFusion = False
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_R12_project_accounting_training_single()
            ebs_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle R12 - Advanced Supply Chain Planning (ASCP) Fundamentals':
            sheet_package = 'oracle_R12_advance_supply_chain_planning_training'
            isFusion = False
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_R12_advance_supply_chain_planning_training_single()
            ebs_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle R12 Financials Accounting Hub Fundamentals':
            sheet_package = 'oracle_R12_financial_accounting_hub_training'
            isFusion = False
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_R12_financial_accounting_hub_training_single()
            ebs_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle Business Intelligence Applications Training':
            sheet_package = 'oracle_business_intelligence_applications_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_business_intelligence_applications_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        # if sku == 'oracle_business_intelligence_enterprise_edition_training':
        #     sheet_package = 'oracle_business_intelligence_enterprise_edition_training'
        #     isFusion = True
        #     isPackage = False
        #     single_training_password = 'REDACTED_TRAINING_PASSWORD'
        #     oracle_business_intelligence_enterprise_edition_training_single()
        #     fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
        #                  single_training_password)
        #     google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
        #                         sheet_package, isPackage)

        if sku == 'Oracle ADF Training':
            sheet_package = 'oracle_adf_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_adf_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle BPM - Business Process Management Training':
            sheet_package = 'oracle_business_process_management_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_business_process_management_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'SOA BPEL Mediator OSB 12c':
            sheet_package = 'oracle_soa_BPEL_mediator_OBS_development_training_1'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_soa_BPEL_mediator_OBS_development_training_1_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle Data Integrator ODI':
            sheet_package = 'oracle_data_integrator_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_data_integrator_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle MAF':
            sheet_package = 'oracle_mobile_application_framework_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_mobile_application_framework_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Java, XML and Webservices':
            sheet_package = 'oracle_java_xml_and_web_service_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_java_xml_and_web_service_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle SQL and PL/SQL Training':
            sheet_package = 'oracle_sql_and_plSQL_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_sql_and_plSQL_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Financial Integration':
            sheet_package = 'fusion_financials_integration_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            fusion_financials_integration_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion Security':
            sheet_package = 'fusion_financials_security_training_1'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            fusion_financials_security_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle Fusion Financials Reporting Training':
            sheet_package = 'fusion_financials_reporting_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            fusion_financials_reporting_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion Financials Approval':
            sheet_package = 'fusion_financials_approval_management_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            fusion_financials_approval_management_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Integration Cloud Service':
            sheet_package = 'oracle_fusion_integration_cloud_Service_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_fusion_integration_cloud_Service_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle Sales Cloud Extensibility':
            sheet_package = 'oracle_sales_cloud_extensibility_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_sales_cloud_extensibility_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion Account Payables':
            sheet_package = 'oracle_fusion_account_payable_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_fusion_account_payable_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion General Ledger':
            sheet_package = 'oracle_fusion_general_ledger_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_fusion_general_ledger_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        # if sku == 'fusion_fixed_asset_training':
        #     sheet_package = 'fusion_fixed_asset_training'
        #     isFusion = True
        #     isPackage = False
        #     single_training_password = 'REDACTED_TRAINING_PASSWORD'
        #     fusion_fixed_asset_training_single()
        #     fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
        #                  single_training_password)
        #     google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
        #                         sheet_package, isPackage)

        if sku == 'Oracle Fusion Project Portfolio Management':
            sheet_package = 'oracle_fusion_project_portfolio_management_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_fusion_project_portfolio_management_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle Ebusiness Suite Fundamentals':
            sheet_package = 'oracle_business_suit_fundamentals_training'
            isFusion = False
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_business_suit_fundamentals_training_single()
            ebs_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle R12 iProcurement':
            sheet_package = 'oracle_R12_iprocurement_training'
            isFusion = False
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_R12_iprocurement_training_single()
            ebs_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle Service Contract Fundamentals':
            sheet_package = 'oracle_ebs_R12_service_contract_training'
            isFusion = False
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_ebs_R12_service_contract_training_single()
            ebs_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        # if sku == 'oracle_ebs_R12_fixed_assets_training':
        #     sheet_package = 'oracle_ebs_R12_fixed_assets_training'
        #     isFusion = False
        #     isPackage = False
        #     single_training_password = 'REDACTED_TRAINING_PASSWORD'
        #     oracle_ebs_R12_fixed_assets_training_single()
        #     ebs_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
        #                  single_training_password)
        #     google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
        #                         sheet_package, isPackage)

        if sku == 'Oracle Transportation Management':
            sheet_package = 'oracle_transportation_management_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_transportation_management_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle Demantra : Predictive Trade Planning':
            sheet_package = 'oracle_demantra_ptp_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_demantra_ptp_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'IDM Foundation':
            sheet_package = 'oracle_identity_management_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_identity_management_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle Access Manager':
            sheet_package = 'oracle_access_manager_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_access_manager_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Weblogic Training':
            sheet_package = 'oracle_weblogic_administrator_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_weblogic_administrator_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle Entitlement Server Training':
            sheet_package = 'oracle_entitlement_server_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_entitlement_server_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle Fusion MiddleWare 12c Administration':
            sheet_package = 'fusion_middleware_12C_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            fusion_middleware_12C_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle GoldenGate':
            sheet_package = 'oracle_goldengate_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_goldengate_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle Database 12c: New Features for Administrators Ed2':
            sheet_package = 'oracle_database_12C_advanced_admininstration_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_database_12C_advanced_admininstration_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle Database : Data Guard Administration':
            sheet_package = 'oracle_data_guard_administration_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_data_guard_administration_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle R12 Approvals Management Engine (AME)':
            sheet_package = 'r12_approval_management_training_1'
            isFusion = False
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            r12_approval_management_training_single()
            ebs_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle ERP Development':
            sheet_package = 'ebusiness_suit_development_erp_training'
            isFusion = False
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            ebusiness_suit_development_erp_training_single()
            ebs_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        # if sku == 'workflow_training':
        #     sheet_package = 'workflow_training'
        #     isFusion = False
        #     isPackage = False
        #     single_training_password = 'REDACTED_TRAINING_PASSWORD'
        #     workflow_training_single()
        #     ebs_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
        #                  single_training_password)
        #     google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
        #                         sheet_package, isPackage)

        if sku == 'Oracle BI Publisher':
            sheet_package = 'bi_publisher_training'
            isFusion = False
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            bi_publisher_training_single()
            ebs_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'EBS Techno-Functional Package':
            sheet_package = 'ebs_techno_functional_training'
            isFusion = False
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            ebs_techno_functional_training_single()
            ebs_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle Fusion HCM Reporting Training':
            sheet_package = 'fusion_hcm_reporting_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            fusion_hcm_reporting_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion Integration Training':
            sheet_package = 'oracle_fusion_hcm_integration_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_fusion_hcm_integration_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion HCM':
            sheet_package = 'fusion_security_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            fusion_security_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle Taleo Training':
            sheet_package = 'oracle_taleo_recruting_and_onboarding_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_taleo_recruting_and_onboarding_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Taleo Connect Client':
            sheet_package = 'oracle_taleo_tcc_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_taleo_tcc_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        # if sku == 'oracle_taleo_integration_training':
        #     sheet_package = 'oracle_taleo_integration_training'
        #     isFusion = True
        #     isPackage = False
        #     single_training_password = 'REDACTED_TRAINING_PASSWORD'
        #     oracle_taleo_integration_training_single()
        #     fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
        #                  single_training_password)
        #     google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
        #                         sheet_package, isPackage)

        # if sku == 'r1213_administration_training':
        #     sheet_package = 'r1213_administration_training'
        #     isFusion = False
        #     isPackage = False
        #     single_training_password = 'REDACTED_TRAINING_PASSWORD'
        #     r1213_administration_training_single()
        #     ebs_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
        #                  single_training_password)
        #     google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
        #                         sheet_package, isPackage)

        if sku == 'Siebel open UI':
            sheet_package = 'Siebel_openUI_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            Siebel_openUI_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Hyperion Financial Management':
            sheet_package = 'hyperion_financials_management_hfm_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            hyperion_financials_management_hfm_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion Hyperion Planning':
            sheet_package = 'hyperion_planning_training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            hyperion_planning_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Mastering Hyperion Calculation Manager with Essbase and Planning':
            sheet_package = 'mastering_hyperion_calculation_manager'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            mastering_hyperion_calculation_manager_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)


        if sku == 'OBIEE Training':
            sheet_package = 'OBIEE Training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            obiee_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle Workflow Training':
            sheet_package = 'Oracle Workflow Builder Training'
            isFusion = True
            isPackage = False
            single_training_password = 'REDACTED_TRAINING_PASSWORD'
            oracle_workflow_training_single()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

####################################################################### PACKAGES ###################################################################################

        if sku == 'FUsion HCM Modules PAckage':
            sheet_package = 'Fusion HCM Modules Training Package'
            isFusion = True
            isPackage = True
            single_training_password = None
            Fusion_HCM_Modules_Package()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Hyperion Suite Training Package':
            sheet_package = 'Hyperion Suit Training Package'
            isFusion = True
            isPackage = True
            single_training_password = None
            Hyperion_suit_training_package()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion HCM Technical Package':
            sheet_package = 'HCM Technical Package'
            isFusion = True
            isPackage = True
            single_training_password = None
            Fusion_HCM_Technical_Package()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'EBS R12 Technical training Package':
            sheet_package = 'Oracle EBS R12 Technical Package'
            isFusion = True
            isPackage = True
            single_training_password = None
            EBS_R12_Technical_Package()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion Middleware Administration Package':
            sheet_package = 'Fusion Middleware administration Package'
            isFusion = True
            isPackage = True
            single_training_password = None
            Fusion_middleware_administration_package()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'FUSION APPLICATIONS TRAINING':
            sheet_package = 'Fusion Applications Package'
            isFusion = True
            isPackage = True
            single_training_password = None
            Fusion_Application_Training_Package()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion Apps Training Package':
            sheet_package = 'Fusion Apps Training Package'
            isFusion = True
            isPackage = True
            single_training_password = None
            Fusion_Apps_Training_Package()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion Cloud Common Technology Package':
            sheet_package = 'Fusion Cloud Common Technology Package'
            isFusion = True
            isPackage = True
            single_training_password = None
            Fusion_cloud_common_technology_package()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion Financials Functional Package':
            sheet_package = 'Fusion Financials Functional Package'
            isFusion = True
            isPackage = True
            single_training_password = None
            Fusion_financials_functional_package()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion Financials Technical Package':
            sheet_package = 'Fusion Financials Technical Package'
            isFusion = True
            isPackage = True
            single_training_password = None
            Fusion_financials_technical_package()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion HCM and Taleo Functional & Technical Package':
            sheet_package = 'FUSION HCM AND TALEO FUNCTIONAL & TECHNICAL PACKAGE'
            isFusion = True
            isPackage = True
            single_training_password = None
            Fusion_HCM_and_Taleo_functional_and_technical_package()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion HCM trainings':
            sheet_package = 'Fusion HCM Modules Training Package'
            isFusion = True
            isPackage = True
            single_training_password = None
            Fusion_HCM_functional_package()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Fusion Middleware Development Package':
            sheet_package = 'Fusion Middleware Development Training Package'
            isFusion = True
            isPackage = True
            single_training_password = None
            Fusion_middleware_development_package()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Oracle EBS R12 Functional Package':
            sheet_package = 'Oracle EBS R12 Functional Package'
            isFusion = False
            isPackage = True
            single_training_password = None
            Oracle_EBS_R12_functional_package()
            ebs_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'R12 + Fusion Apps Training':
            sheet_package = 'Fusion + R12 Package'
            isFusion = 'Both'
            isPackage = True
            single_training_password = None
            R12_Fusion_Apps_Training()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

        if sku == 'Unlimited Oracle Training Package':
            sheet_package = 'Unlimited Training Package'
            isFusion = 'Both'
            isPackage = True
            single_training_password = None
            Unlimited_Oracle_training_Package()
            fusion_email(customer_name, customer_username, random_password, customer_email, sku, isPackage,
                         single_training_password, isFusion)
            google_sheet_update(customer_name, customer_username, random_password, isFusion, customer_email,
                                sheet_package, isPackage)

#############################################################################################################################################################

order_id = input("Enter the Order ID : ")
response = urllib.request.urlopen(
    'ecwid link for retrieving order details={number}'.format(number=order_id))
data = json.loads(response.read())

number = data['orders'][0]['number']
payment_status = data['orders'][0]['paymentStatus']
customer_name = data['orders'][0]['customerName']
customer_email = data['orders'][0]['customerEmail']
sku = data['orders'][0]['items'][0]['sku']
value = data['orders'][0]['items'][0]['options'][0]['value']

if payment_status == 'ACCEPTED':

    random_String = ''.join(random.choices(string.ascii_uppercase + string.ascii_lowercase, k=4))
    random_password = ''.join(random.choices(string.ascii_lowercase + string.ascii_uppercase, k=8))
    first_name = customer_name.split()[0]
    customer_username = "sp_{name1}_{name2}".format(name1=first_name, name2=random_String)

    options = webdriver.ChromeOptions()
    options.add_argument('--disable-extentions')
    options.add_argument('--enable-popup-blocking')
    options.add_argument('--hide-scrollbars')
    options.add_argument('--disable-gpu')
    options.add_argument("--log-level=3")
    options.add_argument("--start-maximized")
    options.add_argument('--headless')


    driver = webdriver.Chrome(executable_path='/mnt/d/Users/hp/Python/Scripts/chromedriver.exe',
                              chrome_options=options)
    joomla(customer_email)

else:
    print ("Payment Status NOT Accepted")