import urllib.request
import bs4 as bs
from PyQt4.QtWebKit import QWebPage
from PyQt4.QtCore import QUrl
from PyQt4.QtGui import QApplication
import sys
name = driver.find_element_by_xpath(
    '/html/body/form/table[1]/tbody/tr[1]/td[4]/b')

elements = name.find_elements_by_tag_name("b")
print(elements)
print(elements.get_attribule('value'))
for ele in elements:
print(ele.get_attribute('value'))


print(next_url)

print(requests.get(next_url).text)

web_soup = BeautifulSoup(requests.get(next_url).text, 'html.parser')

print(web_soup.prettify())


class Client(QWebPage):

    def __init__(self, url):

        self.app = QApplication(sys.argv)
        QWebPage.__init__(self)
        self.loadFinished.connect(self.on_page_load)
        self.mainFrame().load(QUrl(url))
        self.app.exec_()

    def on_page_load(self):

        self.app.quit()

        url = 'http://202.63.105.184/results/jsp/SearchResult.jsp?degree=btech&examCode=1391&etype=r17&type=grade17'

        client_resp = Client(url)

        source = client_resp.mainFrame().toHtml()

        soup = BeautifulSoup(source, 'lxml')

# js_test = soup.find('p', class_='jstest')
# print(js_test.text)

# print(soup.prettify())

# for tag in soup.find_all('input'):
# print(tag)

        input_tag = soup.find('input', id="txtCaptcha")

# given_tag = soup.find('input', id="txtInput")
        print(input_tag)

        print(input_tag.value)

        print(given_tag.value)
