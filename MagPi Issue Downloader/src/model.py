from email.mime import base
from bs4 import BeautifulSoup
import requests

def getLatestIssue(baseUrl):
    # sends request to get the website
    x = requests.get(baseUrl + "/issues")

    # extracts html code and reduces code to just latest issue section
    soup = BeautifulSoup(x.text, 'lxml')
    latestIssue = soup.select('section[class="c-latest-issue"]')
    #(str(latestIssue[0]))

    # gets the download intermediary page link for the issue
    latestIssueSoup = BeautifulSoup(str(latestIssue[0]), 'lxml')
    latestIssueDownloadLink = latestIssueSoup.select_one('a[class="c-issue-actions__link c-link u-text-bold"]')
    downloadSoup = BeautifulSoup(str(latestIssueDownloadLink), 'lxml')
    #print(downloadSoup.a["href"])
    issue_url = baseUrl + downloadSoup.a["href"] + "/download"
    print(issue_url)

    issueNumber = get_latest_issue_number(baseUrl)

    # goes to the actual download
    downloadPage = requests.get(str(issue_url))
    downloadPageSoup = BeautifulSoup(downloadPage.text, 'lxml')
    #print(downloadPageSoup.prettify())
    issueDownloadText = downloadPageSoup.select_one('a[class="c-link"]')
    print(issueDownloadText)
    #print("Download Issue Text", issueDownloadText)
    downloadIssueSoup = BeautifulSoup(str(issueDownloadText), 'lxml')
    #print(downloadIssueSoup.a["href"])
    #print(downloadIssueSoup.prettify())
    issue_download_url = baseUrl + downloadIssueSoup.a["href"]

    issuePDF = requests.get(issue_download_url, stream=True)
    with open(f"E:\Books\MagPi Issues\wireframe Issue {str(issueNumber)}.pdf", "wb") as pdf:
        for chunk in issuePDF.iter_content(chunk_size=1024):  
            # writing one chunk at a time to pdf file
            if chunk:
                pdf.write(chunk)

def downloadAllIssues():
    issueNumber = get_latest_issue_number()

def get_latest_issue_number(baseurl):
    # sends request to get the website
    x = requests.get(f"{baseurl}/issues")

    # extracts html code and reduces code to just latest issue section
    soup = BeautifulSoup(x.text, 'lxml')
    latestIssue = soup.select('section[class="c-latest-issue"]')
    # print(str(latestIssue[0]))

    # gets the download intermediary page link for the issue
    latestIssueSoup = BeautifulSoup(str(latestIssue[0]), 'lxml')
    # print(latestIssueSoup)

    # gets the number of the Issue
    latestIssueBreakdown = BeautifulSoup(str(latestIssueSoup.select_one('a[href]')), 'lxml')
    issueLink = latestIssueBreakdown.a["href"]
    issueNumber = int(issueLink[8:])
    return issueNumber

getLatestIssue("https://wireframe.raspberrypi.com")