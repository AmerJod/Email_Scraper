import unittest
import emails_scraper
from _tests.fexture import file_1, file_2, file_3

# Expected results
expected_emails_1 = "product@hackerrank.com, hackers@hackerrank.com, interviewstreet@hackerrank.com, info [at] legalist [dot] com, christian @ legalist . com, benjamin/at/legalist/dot/com"
expected_emails_2 = "mpotts@ngs.org, jbmccorm@ngs.org, ngsline@customersvc.com, ngsdigital@customersvc.com, givinginfo@ngs.org, askngs@nationalgeographic.com, genographic@ngs.org, genographicespanol@ngs.org, apps@ngs.org, feedback@natgeotv.com, online at nationalgeographicexpeditions.com, ngsforum@nationalgeographic.com, maps@ngs.org, stock@ngs.org, ngassignment@ngs.org, newsdesk@nationalgeographic.com, pressroom@ngs.org, speakers@ngs.org, topo@ngs.org, traveler@ngs.org"
expected_emails_3 = "mpotts@ngs.org, jbmccorm@ngs.org, ngsline@customersvc.com, ngsdigital@customersvc.com, givinginfo@ngs.org, askngs@nationalgeographic.com, genographic@ngs.org, genographicespanol@ngs.org, apps@ngs.org, feedback@natgeotv.com, online at nationalgeographicexpeditions.com, ngsforum@nationalgeographic.com, maps@ngs.org, stock@ngs.org, ngassignment@ngs.org, newsdesk@nationalgeographic.com, pressroom@ngs.org, speakers@ngs.org, topo@ngs.org, traveler@ngs.org"


class EmailFinderTest(unittest.TestCase):
    def test_get_emails(self):
        print("** get_emails method - Test 3 scenarios **")
        # test a actual data
        emails = emails_scraper.get_emails(file_1.data)
        self.assertEqual(emails, expected_emails_1)

        # test a actual data
        emails = emails_scraper.get_emails(file_2.data)
        self.assertEqual(emails, expected_emails_2)

        # test a clean data
        emails = emails_scraper.get_emails(file_3.data)
        self.assertEqual(emails, expected_emails_3)


if __name__ == "__main__":
    unittest.main()
